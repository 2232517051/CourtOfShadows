[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet("Structural", "Narrative")]
    [string]$Gate,
    [string]$ProjectRoot,
    [string]$RunRoot,
    [ValidateSet("Batch", "Final")]
    [string]$NarrativePhase = "Final",
    [ValidateRange(30, 1800)]
    [int]$ToolTimeoutSeconds = 300,
    [ValidateRange(300, 1800)]
    [int]$RenPyTimeoutSeconds = 300
)

$projectRootWasSpecified = $PSBoundParameters.ContainsKey('ProjectRoot')
$runRootWasSpecified = $PSBoundParameters.ContainsKey('RunRoot')

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Add-WinterGateNativeTypes {
    if ($null -ne ("WinterGate.Native" -as [type])) {
        return
    }
    $nativeSource = @'
using System;
using System.Collections;
using System.Collections.Generic;
using System.ComponentModel;
using System.Diagnostics;
using System.Globalization;
using System.IO;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading;
using Microsoft.Win32.SafeHandles;

namespace WinterGate
{
    public enum PathKind
    {
        File,
        Directory
    }

    public sealed class PathIdentity
    {
        public string FinalPath;
        public uint VolumeSerialNumber;
        public ulong FileIndex;
        public FileAttributes Attributes;
    }

    public sealed class BoundedProcessResult
    {
        public bool ProcessStarted;
        public int? ProcessId;
        public DateTime? StartedUtc;
        public DateTime? EndedUtc;
        public long? ElapsedMilliseconds;
        public int? ExitCode;
        public bool TimedOut;
        public bool TreeDrained;
        public bool HadLiveDescendantsAfterRootExit;
        public string StartError;
        public bool OutputEvidenceValid;
        public string OutputEvidenceError;
    }

    [Serializable]
    public sealed class WinterGatePathIdentityException : Exception
    {
        public int NativeErrorCode { get; private set; }

        public WinterGatePathIdentityException(string message)
            : base(message)
        {
        }

        public WinterGatePathIdentityException(
            string message,
            int nativeErrorCode,
            Exception innerException)
            : base(message, innerException)
        {
            NativeErrorCode = nativeErrorCode;
        }

        private WinterGatePathIdentityException(
            System.Runtime.Serialization.SerializationInfo info,
            System.Runtime.Serialization.StreamingContext context)
            : base(info, context)
        {
            NativeErrorCode = info.GetInt32("NativeErrorCode");
        }

        public override void GetObjectData(
            System.Runtime.Serialization.SerializationInfo info,
            System.Runtime.Serialization.StreamingContext context)
        {
            if (info == null)
            {
                throw new ArgumentNullException("info");
            }
            info.AddValue("NativeErrorCode", NativeErrorCode);
            base.GetObjectData(info, context);
        }
    }

    public static partial class Native
    {
        private const uint FILE_READ_DATA = 0x00000001;
        private const uint FILE_SHARE_READ = 0x00000001;
        private const uint FILE_SHARE_WRITE = 0x00000002;
        private const uint OPEN_EXISTING = 3;
        private const uint FILE_FLAG_BACKUP_SEMANTICS = 0x02000000;
        private const uint FILE_FLAG_OPEN_REPARSE_POINT = 0x00200000;
        private const int ERROR_FILE_NOT_FOUND = 2;
        private const int ERROR_PATH_NOT_FOUND = 3;

        internal sealed class HeldPathChain : IDisposable
        {
            internal readonly List<SafeFileHandle> Handles =
                new List<SafeFileHandle>();
            internal PathIdentity LeafIdentity;

            public void Dispose()
            {
                for (int index = Handles.Count - 1; index >= 0; index--)
                {
                    Handles[index].Dispose();
                }
                Handles.Clear();
            }
        }

        internal sealed class StepDependencyFile : IDisposable
        {
            internal readonly string RequestedPath;
            internal readonly PathIdentity CreationIdentity;
            internal HeldPathChain PathChain;
            internal IntPtr ReadHandle;

            internal StepDependencyFile(
                string requestedPath,
                PathIdentity creationIdentity,
                HeldPathChain pathChain,
                IntPtr readHandle)
            {
                RequestedPath = requestedPath;
                CreationIdentity = creationIdentity;
                PathChain = pathChain;
                ReadHandle = readHandle;
            }

            public void Dispose()
            {
                CloseOwnedHandle(ref ReadHandle);
                if (PathChain != null)
                {
                    PathChain.Dispose();
                    PathChain = null;
                }
            }
        }

        public sealed class StepDependencyLease : IDisposable
        {
            private readonly object synchronization = new object();
            private StepDependencyFile executable;
            private StepDependencyFile[] requiredFiles;
            private bool disposed;

            public string ExecutablePath { get; private set; }
            public string FirstMissingRequiredFilePath { get; private set; }

            internal StepDependencyLease(
                StepDependencyFile executable,
                StepDependencyFile[] requiredFiles,
                string firstMissingRequiredFilePath)
            {
                this.executable = executable;
                this.requiredFiles = requiredFiles;
                ExecutablePath = executable.CreationIdentity.FinalPath;
                FirstMissingRequiredFilePath = firstMissingRequiredFilePath;
            }

            ~StepDependencyLease()
            {
                Dispose(false);
            }

            public void AssertStable()
            {
                lock (synchronization)
                {
                    RequireOpen();
                    AssertStepDependencyFileStable(executable);
                    for (int index = 0; index < requiredFiles.Length; index++)
                    {
                        AssertStepDependencyFileStable(requiredFiles[index]);
                    }
                }
            }

            public void Dispose()
            {
                Dispose(true);
                GC.SuppressFinalize(this);
            }

            private void Dispose(bool disposing)
            {
                lock (synchronization)
                {
                    if (disposed)
                    {
                        return;
                    }
                    disposed = true;
                    for (int index = requiredFiles.Length - 1; index >= 0; index--)
                    {
                        requiredFiles[index].Dispose();
                    }
                    requiredFiles = new StepDependencyFile[0];
                    if (executable != null)
                    {
                        executable.Dispose();
                        executable = null;
                    }
                }
            }

            private void RequireOpen()
            {
                if (disposed)
                {
                    throw new ObjectDisposedException("StepDependencyLease");
                }
            }
        }

        [StructLayout(LayoutKind.Sequential)]
        private struct FILETIME
        {
            public uint LowDateTime;
            public uint HighDateTime;
        }

        [StructLayout(LayoutKind.Sequential)]
        private struct BY_HANDLE_FILE_INFORMATION
        {
            public uint FileAttributes;
            public FILETIME CreationTime;
            public FILETIME LastAccessTime;
            public FILETIME LastWriteTime;
            public uint VolumeSerialNumber;
            public uint FileSizeHigh;
            public uint FileSizeLow;
            public uint NumberOfLinks;
            public uint FileIndexHigh;
            public uint FileIndexLow;
        }

        [DllImport("kernel32.dll", CharSet = CharSet.Unicode, SetLastError = true)]
        private static extern SafeFileHandle CreateFileW(
            string fileName,
            uint desiredAccess,
            uint shareMode,
            IntPtr securityAttributes,
            uint creationDisposition,
            uint flagsAndAttributes,
            IntPtr templateFile);

        [DllImport("kernel32.dll", SetLastError = true)]
        [return: MarshalAs(UnmanagedType.Bool)]
        private static extern bool GetFileInformationByHandle(
            SafeFileHandle file,
            out BY_HANDLE_FILE_INFORMATION information);

        [DllImport("kernel32.dll", CharSet = CharSet.Unicode, SetLastError = true)]
        private static extern uint GetFinalPathNameByHandleW(
            SafeFileHandle file,
            StringBuilder path,
            uint pathLength,
            uint flags);

        [DllImport("kernel32.dll", CharSet = CharSet.Unicode, SetLastError = true)]
        [return: MarshalAs(UnmanagedType.Bool)]
        private static extern bool CreateDirectoryW(
            string path,
            IntPtr securityAttributes);

        public static PathIdentity GetPathIdentity(
            string path,
            PathKind expectedKind,
            bool rejectAnyReparseComponent)
        {
            string fullPath = RequireAbsoluteNonDevicePath(path);
            using (HeldPathChain chain = OpenExistingPathChain(
                fullPath,
                expectedKind,
                rejectAnyReparseComponent))
            {
                return chain.LeafIdentity;
            }
        }

        public static PathIdentity TryGetPathIdentity(
            string path,
            PathKind expectedKind,
            bool rejectAnyReparseComponent)
        {
            try
            {
                return GetPathIdentity(
                    path,
                    expectedKind,
                    rejectAnyReparseComponent);
            }
            catch (WinterGatePathIdentityException exception)
            {
                if (exception.NativeErrorCode == ERROR_FILE_NOT_FOUND ||
                    exception.NativeErrorCode == ERROR_PATH_NOT_FOUND)
                {
                    return null;
                }
                throw;
            }
        }

        public static void CreateDirectoryExclusive(
            string path,
            PathIdentity expectedParentIdentity)
        {
            string fullPath = RequireAbsoluteNonDevicePath(path);
            string parentPath = Path.GetDirectoryName(fullPath);
            string leafName = Path.GetFileName(fullPath);
            if (String.IsNullOrEmpty(parentPath) || String.IsNullOrEmpty(leafName))
            {
                throw new WinterGatePathIdentityException(
                    "path identity: exclusive directory needs a parent and leaf: " +
                    fullPath);
            }
            if (expectedParentIdentity == null)
            {
                throw new WinterGatePathIdentityException(
                    "path identity: exclusive directory expected parent is absent: " +
                    fullPath);
            }

            using (HeldPathChain parent = OpenExistingPathChain(
                parentPath,
                PathKind.Directory,
                true))
            {
                if (!SameStablePath(parent.LeafIdentity, expectedParentIdentity))
                {
                    throw new WinterGatePathIdentityException(
                        "path identity: exclusive directory parent changed after " +
                        "validation: " + parentPath);
                }
                string canonicalChild = Path.Combine(
                    parent.LeafIdentity.FinalPath,
                    leafName);
                if (!String.Equals(
                    NormalizeComparableFinalPath(canonicalChild),
                    fullPath,
                    StringComparison.OrdinalIgnoreCase))
                {
                    throw new WinterGatePathIdentityException(
                        "path identity: exclusive directory parent final path " +
                        "does not match the requested path: " + fullPath);
                }
                if (!CreateDirectoryW(canonicalChild, IntPtr.Zero))
                {
                    int error = Marshal.GetLastWin32Error();
                    throw NativePathError(
                        "create directory exclusively",
                        canonicalChild,
                        error);
                }

                SafeFileHandle childHandle = OpenPathHandle(
                    canonicalChild,
                    true);
                parent.Handles.Add(childHandle);
                PathIdentity childIdentity = ReadPathIdentityFromHandle(
                    childHandle,
                    PathKind.Directory,
                    true,
                    canonicalChild);
                if (!String.Equals(
                    NormalizeComparableFinalPath(canonicalChild),
                    childIdentity.FinalPath,
                    StringComparison.OrdinalIgnoreCase))
                {
                    throw new WinterGatePathIdentityException(
                        "path identity: exclusively created directory resolved " +
                        "outside its verified parent: " + canonicalChild);
                }
            }
        }

        public static bool SameObject(PathIdentity left, PathIdentity right)
        {
            return left != null &&
                right != null &&
                left.VolumeSerialNumber == right.VolumeSerialNumber &&
                left.FileIndex == right.FileIndex;
        }

        public static bool SameStablePath(PathIdentity left, PathIdentity right)
        {
            return SameObject(left, right) &&
                String.Equals(
                    NormalizeComparableFinalPath(left.FinalPath),
                    NormalizeComparableFinalPath(right.FinalPath),
                    StringComparison.OrdinalIgnoreCase);
        }

        internal static PathIdentity GetPathIdentityFromOpenHandle(
            IntPtr handle,
            PathKind expectedKind)
        {
            if (handle == IntPtr.Zero || handle == new IntPtr(-1))
            {
                throw new WinterGatePathIdentityException(
                    "path identity: invalid open handle");
            }

            using (SafeFileHandle borrowed = new SafeFileHandle(handle, false))
            {
                return ReadPathIdentityFromHandle(
                    borrowed,
                    expectedKind,
                    true,
                    "<open handle>");
            }
        }

// BEGIN PROCESS ENGINE
// BEGIN LOOP 3.1-A SHARED NATIVE DECLARATIONS
    private const uint GenericRead = 0x80000000;
    private const uint GenericWrite = 0x40000000;
    private const uint DeleteAccess = 0x00010000;
    private const uint SynchronizeAccess = 0x00100000;
    private const uint ProcessQueryLimitedInformation = 0x00001000;
    private const uint FileReadAttributes = 0x00000080;
    private const uint FileShareRead = 0x00000001;
    private const uint FileShareWrite = 0x00000002;
    private const uint FileShareDelete = 0x00000004;
    private const uint DuplicateSameAccess = 0x00000002;
    private const uint CreateNew = 1;
    private const uint OpenExisting = 3;
    private const uint FileAttributeNormal = 0x00000080;
    private const uint FileFlagOpenReparsePoint = 0x00200000;
    private const uint FileFlagBackupSemantics = 0x02000000;
    private const uint StartfUseStdHandles = 0x00000100;
    private const uint CreateSuspended = 0x00000004;
    private const uint CreateUnicodeEnvironment = 0x00000400;
    private const uint CreateNoWindow = 0x08000000;
    private const uint ExtendedStartupInfoPresent = 0x00080000;
    private const uint JobObjectLimitKillOnJobClose = 0x00002000;
    private const int JobObjectBasicAccountingInformation = 1;
    private const int JobObjectBasicProcessIdList = 3;
    private const int JobObjectExtendedLimitInformation = 9;
    private const int FileRenameInfo = 3;
    private const int ErrorFileNotFound = 2;
    private const int ErrorPathNotFound = 3;
    private const int ErrorMoreData = 234;
    private const int ErrorInvalidParameter = 87;
    private const int ErrorAlreadyExists = 183;
    private const long ProcThreadAttributeHandleList = 0x00020002;
    private const uint WaitObject0 = 0x00000000;
    private const uint WaitTimeout = 0x00000102;
    private const uint WaitFailed = 0xFFFFFFFF;
    private const uint StillActive = 259;
    private const uint ResumeFailed = 0xFFFFFFFF;
    private const uint ForcedExitCode = 0x0000DEAD;
    private const int CleanupTimeoutMilliseconds = 10000;
    private const int CleanupPollMilliseconds = 25;
    private const int MaximumJsonDepth = 64;
    private const int MaximumJsonDocumentCharacters = 1048576;
    private const int MaximumJsonNumberTokenLength = 128;

    private static readonly IntPtr InvalidHandleValue = new IntPtr(-1);
    private const string GateJobEnvironmentVariable = "WINTER_GATE_JOB_NAME";
    private const string StructuredOutputHandleEnvironmentVariable =
        "WINTER_GATE_STRUCTURED_OUTPUT_HANDLE";
    private const string StructuredOutputMarkerPrefix =
        "WINTER_GATE_RESERVED_V1:";

    public sealed class StructuredOutputSnapshot
    {
        public bool HasContent;
        public string Text;
    }

    public sealed class StructuredOutputReservation : IDisposable
    {
        private readonly object synchronization = new object();
        private IntPtr ownerHandle;
        private IntPtr evidenceDirectoryGuard;
        private bool writerIssued;
        private bool frozen;
        private bool disposed;
        private StructuredOutputSnapshot snapshot;
        internal readonly string FixedPath;
        internal readonly PathIdentity CreationIdentity;
        internal readonly PathIdentity EvidenceDirectoryIdentity;
        internal readonly byte[] MarkerBytes;

        internal StructuredOutputReservation(
            string fixedPath,
            IntPtr ownerHandle,
            IntPtr evidenceDirectoryGuard,
            PathIdentity creationIdentity,
            PathIdentity evidenceDirectoryIdentity,
            byte[] markerBytes)
        {
            FixedPath = fixedPath;
            this.ownerHandle = ownerHandle;
            this.evidenceDirectoryGuard = evidenceDirectoryGuard;
            CreationIdentity = creationIdentity;
            EvidenceDirectoryIdentity = evidenceDirectoryIdentity;
            MarkerBytes = markerBytes;
        }

        internal IntPtr DuplicateInheritableWriterHandle()
        {
            lock (synchronization)
            {
                RequireOpen();
                if (writerIssued || frozen)
                {
                    throw new InvalidOperationException(
                        "The structured output writer was already issued or frozen.");
                }
                IntPtr currentProcess = GetCurrentProcess();
                IntPtr duplicate;
                if (!DuplicateHandle(
                    currentProcess,
                    ownerHandle,
                    currentProcess,
                    out duplicate,
                    0,
                    true,
                    DuplicateSameAccess))
                {
                    throw new IOException(
                        LastError("DuplicateHandle(structured output writer)"));
                }
                writerIssued = true;
                return duplicate;
            }
        }

        internal StructuredOutputSnapshot Freeze(int maximumBytes)
        {
            lock (synchronization)
            {
                RequireOpen();
                if (snapshot != null)
                {
                    return snapshot;
                }
                if (!writerIssued)
                {
                    throw new InvalidOperationException(
                        "The structured output writer was not issued.");
                }
                snapshot = FreezeStructuredOutputCore(this, maximumBytes);
                frozen = true;
                return snapshot;
            }
        }

        public void Dispose()
        {
            ReleaseHandles();
            GC.SuppressFinalize(this);
        }

        ~StructuredOutputReservation()
        {
            ReleaseHandles();
        }

        private void RequireOpen()
        {
            if (disposed || ownerHandle == IntPtr.Zero ||
                evidenceDirectoryGuard == IntPtr.Zero)
            {
                throw new ObjectDisposedException(
                    "StructuredOutputReservation");
            }
        }

        private void ReleaseHandles()
        {
            lock (synchronization)
            {
                if (disposed)
                {
                    return;
                }
                disposed = true;
                CloseOwnedHandle(ref ownerHandle);
                CloseOwnedHandle(ref evidenceDirectoryGuard);
            }
        }

        internal IntPtr OwnerHandle
        {
            get { RequireOpen(); return ownerHandle; }
        }

        internal IntPtr EvidenceDirectoryGuard
        {
            get { RequireOpen(); return evidenceDirectoryGuard; }
        }
    }

    [StructLayout(LayoutKind.Sequential)]
    private struct SecurityAttributes
    {
        internal int Length;
        internal IntPtr SecurityDescriptor;
        internal int InheritHandle;
    }

    [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Unicode)]
    private struct StartupInfo
    {
        internal int Size;
        internal string Reserved;
        internal string Desktop;
        internal string Title;
        internal int X;
        internal int Y;
        internal int XSize;
        internal int YSize;
        internal int XCountChars;
        internal int YCountChars;
        internal int FillAttribute;
        internal int Flags;
        internal short ShowWindow;
        internal short Reserved2Size;
        internal IntPtr Reserved2;
        internal IntPtr StdInput;
        internal IntPtr StdOutput;
        internal IntPtr StdError;
    }

    [StructLayout(LayoutKind.Sequential)]
    private struct StartupInfoEx
    {
        internal StartupInfo StartupInfo;
        internal IntPtr AttributeList;
    }

    [StructLayout(LayoutKind.Sequential)]
    private struct ProcessInformation
    {
        internal IntPtr Process;
        internal IntPtr Thread;
        internal uint ProcessId;
        internal uint ThreadId;
    }

    [StructLayout(LayoutKind.Sequential)]
    private struct JobObjectBasicLimitInformation
    {
        internal long PerProcessUserTimeLimit;
        internal long PerJobUserTimeLimit;
        internal uint LimitFlags;
        internal UIntPtr MinimumWorkingSetSize;
        internal UIntPtr MaximumWorkingSetSize;
        internal uint ActiveProcessLimit;
        internal UIntPtr Affinity;
        internal uint PriorityClass;
        internal uint SchedulingClass;
    }

    [StructLayout(LayoutKind.Sequential)]
    private struct IoCounters
    {
        internal ulong ReadOperationCount;
        internal ulong WriteOperationCount;
        internal ulong OtherOperationCount;
        internal ulong ReadTransferCount;
        internal ulong WriteTransferCount;
        internal ulong OtherTransferCount;
    }

    [StructLayout(LayoutKind.Sequential)]
    private struct JobObjectExtendedLimitInformationData
    {
        internal JobObjectBasicLimitInformation BasicLimitInformation;
        internal IoCounters IoInfo;
        internal UIntPtr ProcessMemoryLimit;
        internal UIntPtr JobMemoryLimit;
        internal UIntPtr PeakProcessMemoryUsed;
        internal UIntPtr PeakJobMemoryUsed;
    }

    [StructLayout(LayoutKind.Sequential)]
    private struct JobObjectBasicAccountingInformationData
    {
        internal long TotalUserTime;
        internal long TotalKernelTime;
        internal long ThisPeriodTotalUserTime;
        internal long ThisPeriodTotalKernelTime;
        internal uint TotalPageFaultCount;
        internal uint TotalProcesses;
        internal uint ActiveProcesses;
        internal uint TotalTerminatedProcesses;
    }

    [DllImport("kernel32.dll", CharSet = CharSet.Unicode, SetLastError = true)]
    private static extern IntPtr CreateFileW(
        string fileName,
        uint desiredAccess,
        uint shareMode,
        ref SecurityAttributes securityAttributes,
        uint creationDisposition,
        uint flagsAndAttributes,
        IntPtr templateFile);

    [DllImport("kernel32.dll", SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool WriteFile(
        IntPtr file,
        IntPtr buffer,
        uint bytesToWrite,
        out uint bytesWritten,
        IntPtr overlapped);

    [DllImport("kernel32.dll", SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool FlushFileBuffers(IntPtr file);

    [DllImport("kernel32.dll", SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool SetFileInformationByHandle(
        IntPtr file,
        int informationClass,
        IntPtr information,
        uint bufferSize);

    [DllImport("kernel32.dll", CharSet = CharSet.Unicode, SetLastError = true)]
    private static extern IntPtr CreateJobObjectW(IntPtr jobAttributes, string name);

    [DllImport("kernel32.dll", SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool SetInformationJobObject(
        IntPtr job,
        int informationClass,
        ref JobObjectExtendedLimitInformationData information,
        int informationLength);

    [DllImport("kernel32.dll", SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool QueryInformationJobObject(
        IntPtr job,
        int informationClass,
        out JobObjectBasicAccountingInformationData information,
        int informationLength,
        IntPtr returnLength);

    [DllImport(
        "kernel32.dll",
        EntryPoint = "QueryInformationJobObject",
        SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool QueryInformationJobObjectBuffer(
        IntPtr job,
        int informationClass,
        IntPtr information,
        int informationLength,
        IntPtr returnLength);

    [DllImport("kernel32.dll", SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool InitializeProcThreadAttributeList(
        IntPtr attributeList,
        int attributeCount,
        int flags,
        ref IntPtr size);

    [DllImport("kernel32.dll", SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool UpdateProcThreadAttribute(
        IntPtr attributeList,
        uint flags,
        IntPtr attribute,
        IntPtr value,
        IntPtr size,
        IntPtr previousValue,
        IntPtr returnSize);

    [DllImport("kernel32.dll")]
    private static extern void DeleteProcThreadAttributeList(IntPtr attributeList);

    [DllImport("kernel32.dll", CharSet = CharSet.Unicode, SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool CreateProcessW(
        string applicationName,
        StringBuilder commandLine,
        IntPtr processAttributes,
        IntPtr threadAttributes,
        [MarshalAs(UnmanagedType.Bool)] bool inheritHandles,
        uint creationFlags,
        IntPtr environment,
        string currentDirectory,
        ref StartupInfoEx startupInfo,
        out ProcessInformation processInformation);

    [DllImport("kernel32.dll", SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool AssignProcessToJobObject(IntPtr job, IntPtr process);

    [DllImport("kernel32.dll", SetLastError = true)]
    private static extern uint ResumeThread(IntPtr thread);

    [DllImport("kernel32.dll", SetLastError = true)]
    private static extern uint WaitForSingleObject(IntPtr handle, uint milliseconds);

    [DllImport("kernel32.dll", SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool TerminateJobObject(IntPtr job, uint exitCode);

    [DllImport("kernel32.dll", SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool TerminateProcess(IntPtr process, uint exitCode);

    [DllImport("kernel32.dll", SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool GetExitCodeProcess(IntPtr process, out uint exitCode);

    [DllImport("kernel32.dll")]
    private static extern IntPtr GetCurrentProcess();

    [DllImport("kernel32.dll", SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool DuplicateHandle(
        IntPtr sourceProcess,
        IntPtr sourceHandle,
        IntPtr targetProcess,
        out IntPtr targetHandle,
        uint desiredAccess,
        [MarshalAs(UnmanagedType.Bool)] bool inheritHandle,
        uint options);

    [DllImport("kernel32.dll", SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool CloseHandle(IntPtr handle);

    [DllImport("kernel32.dll", SetLastError = true)]
    private static extern IntPtr OpenProcess(
        uint desiredAccess,
        [MarshalAs(UnmanagedType.Bool)] bool inheritHandle,
        uint processId);

// END LOOP 3.1-A SHARED NATIVE DECLARATIONS

// BEGIN LOOP 3.1-B READABLE PUBLIC API
    public static PathIdentity GetReadableFileIdentity(string path)
    {
        return GetReadableFileIdentityCore(path, false);
    }

    public static PathIdentity TryGetReadableFileIdentity(string path)
    {
        return GetReadableFileIdentityCore(path, true);
    }

    public static StepDependencyLease AcquireStepDependencyLease(
        string executable,
        string[] requiredFiles)
    {
        if (requiredFiles == null)
        {
            throw new ArgumentNullException("requiredFiles");
        }
        StepDependencyFile executableFile = null;
        List<StepDependencyFile> acquiredRequiredFiles =
            new List<StepDependencyFile>();
        try
        {
            executableFile = AcquireStepDependencyFile(executable, false);
            string firstMissingRequiredFilePath = null;
            for (int index = 0; index < requiredFiles.Length; index++)
            {
                StepDependencyFile required = AcquireStepDependencyFile(
                    requiredFiles[index],
                    true);
                if (required == null)
                {
                    if (firstMissingRequiredFilePath == null)
                    {
                        firstMissingRequiredFilePath = requiredFiles[index];
                    }
                    continue;
                }
                acquiredRequiredFiles.Add(required);
            }
            StepDependencyLease lease = new StepDependencyLease(
                executableFile,
                acquiredRequiredFiles.ToArray(),
                firstMissingRequiredFilePath);
            executableFile = null;
            acquiredRequiredFiles.Clear();
            return lease;
        }
        finally
        {
            for (int index = acquiredRequiredFiles.Count - 1; index >= 0; index--)
            {
                acquiredRequiredFiles[index].Dispose();
            }
            if (executableFile != null)
            {
                executableFile.Dispose();
            }
        }
    }

    public static string ReadVerifiedUtf8TextFile(
        string path,
        PathIdentity expectedIdentity,
        int maximumBytes)
    {
        if (expectedIdentity == null)
        {
            throw new ArgumentNullException("expectedIdentity");
        }
        if (maximumBytes < 1)
        {
            throw new ArgumentOutOfRangeException("maximumBytes");
        }
        RequirePlainAbsoluteFilePath(path, "path");
        PathIdentity chainIdentity = GetPathIdentity(
            path,
            PathKind.File,
            true);
        if (!SameStablePath(expectedIdentity, chainIdentity))
        {
            throw new WinterGatePathIdentityException(
                "path identity: verified UTF-8 input changed before open: " +
                path);
        }
        SecurityAttributes nonInheritable = NewSecurityAttributes(false);
        IntPtr fileHandle = CreateFileW(
            chainIdentity.FinalPath,
            GenericRead,
            FileShareRead,
            ref nonInheritable,
            OpenExisting,
            FileAttributeNormal | FileFlagOpenReparsePoint |
                FileFlagBackupSemantics,
            IntPtr.Zero);
        if (fileHandle == InvalidHandleValue)
        {
            throw JsonPathIdentityError(
                "CreateFileW(verified UTF-8 read)",
                path,
                Marshal.GetLastWin32Error());
        }
        try
        {
            PathIdentity currentIdentity = GetPathIdentityFromOpenHandle(
                fileHandle,
                PathKind.File);
            if ((currentIdentity.Attributes & FileAttributes.ReparsePoint) != 0 ||
                !SameStablePath(chainIdentity, currentIdentity) ||
                !SameStablePath(expectedIdentity, currentIdentity))
            {
                throw new WinterGatePathIdentityException(
                    "path identity: verified UTF-8 input changed: " + path);
            }

            using (SafeFileHandle safeHandle = new SafeFileHandle(
                fileHandle,
                true))
            {
                fileHandle = IntPtr.Zero;
                using (FileStream stream = new FileStream(
                    safeHandle,
                    FileAccess.Read))
                {
                    if (stream.Length > maximumBytes)
                    {
                        throw new InvalidDataException(
                            "Verified UTF-8 input exceeds its size limit: " + path);
                    }
                    using (StreamReader reader = new StreamReader(
                        stream,
                        new UTF8Encoding(false, true),
                        false,
                        4096,
                        true))
                    {
                        return reader.ReadToEnd();
                    }
                }
            }
        }
        finally
        {
            CloseOwnedHandle(ref fileHandle);
        }
    }

    public static void ValidateStrictJson(string json)
    {
        if (json == null)
        {
            throw new ArgumentNullException("json");
        }
        new StrictJsonParser(
            json,
            MaximumJsonDepth,
            MaximumJsonDocumentCharacters,
            MaximumJsonNumberTokenLength).Validate();
    }

    public static StructuredOutputReservation ReserveStructuredOutput(
        string path,
        PathIdentity expectedEvidenceDirectoryIdentity)
    {
        ValidateJsonPath(path, expectedEvidenceDirectoryIdentity);
        SecurityAttributes nonInheritable = NewSecurityAttributes(false);
        IntPtr evidenceDirectoryGuard = InvalidHandleValue;
        IntPtr ownerHandle = InvalidHandleValue;
        try
        {
            PathIdentity guardedEvidenceIdentity = OpenVerifiedEvidenceGuard(
                expectedEvidenceDirectoryIdentity,
                path,
                ref evidenceDirectoryGuard);
            ownerHandle = CreateFileW(
                path,
                GenericRead | GenericWrite,
                0,
                ref nonInheritable,
                CreateNew,
                FileAttributeNormal | FileFlagOpenReparsePoint,
                IntPtr.Zero);
            if (ownerHandle == InvalidHandleValue)
            {
                throw JsonPathIdentityError(
                    "CreateFileW(structured output reservation)",
                    path,
                    Marshal.GetLastWin32Error());
            }
            RequireDirectEvidenceChild(
                ownerHandle,
                path,
                guardedEvidenceIdentity,
                "structured output reservation");
            PathIdentity creationIdentity = GetPathIdentityFromOpenHandle(
                ownerHandle,
                PathKind.File);
            if ((creationIdentity.Attributes & FileAttributes.ReparsePoint) != 0)
            {
                throw new WinterGatePathIdentityException(
                    "path identity: structured output reservation is a " +
                    "reparse point: " + path);
            }
            byte[] markerBytes = Encoding.ASCII.GetBytes(
                StructuredOutputMarkerPrefix + Guid.NewGuid().ToString("N"));
            WriteAllAndFlush(
                ownerHandle,
                markerBytes,
                "structured output reservation marker");
            StructuredOutputReservation reservation =
                new StructuredOutputReservation(
                    path,
                    ownerHandle,
                    evidenceDirectoryGuard,
                    creationIdentity,
                    guardedEvidenceIdentity,
                    markerBytes);
            ownerHandle = IntPtr.Zero;
            evidenceDirectoryGuard = IntPtr.Zero;
            return reservation;
        }
        finally
        {
            CloseOwnedHandle(ref ownerHandle);
            CloseOwnedHandle(ref evidenceDirectoryGuard);
        }
    }

    public static StructuredOutputSnapshot FreezeStructuredOutput(
        StructuredOutputReservation reservation,
        int maximumBytes)
    {
        if (reservation == null)
        {
            throw new ArgumentNullException("reservation");
        }
        if (maximumBytes < 1)
        {
            throw new ArgumentOutOfRangeException("maximumBytes");
        }
        return reservation.Freeze(maximumBytes);
    }

// END LOOP 3.1-B READABLE PUBLIC API

// BEGIN LOOP 3.2-A JSON WRITER PUBLIC API
    public static string WriteOwnedSummaryUtf8Json(
        string path,
        string normalJson,
        string collisionFailureJson,
        PathIdentity expectedEvidenceDirectoryIdentity)
    {
        ValidateJsonPath(path, expectedEvidenceDirectoryIdentity);
        if (!String.Equals(
            Path.GetFileName(path),
            "gate-summary.json",
            StringComparison.Ordinal))
        {
            throw new ArgumentException(
                "The owned summary publisher only accepts gate-summary.json.",
                "path");
        }

        byte[] normalUtf8Bytes = EncodeUtf8Json(normalJson);
        byte[] collisionUtf8Bytes = EncodeUtf8Json(collisionFailureJson);
        string evidenceDirectory =
            expectedEvidenceDirectoryIdentity.FinalPath;
        string nonce = Guid.NewGuid().ToString("N");
        string stagingPath = Path.Combine(
            evidenceDirectory,
            "gate-summary.pending." + nonce + ".json");
        string quarantinePath = Path.Combine(
            evidenceDirectory,
            "gate-summary.unowned." + nonce + ".json");
        SecurityAttributes nonInheritable = NewSecurityAttributes(false);
        IntPtr evidenceDirectoryGuard = InvalidHandleValue;
        IntPtr stagingHandle = InvalidHandleValue;
        IntPtr existingHandle = InvalidHandleValue;
        IntPtr quarantineVerification = InvalidHandleValue;
        IntPtr finalVerification = InvalidHandleValue;
        bool quarantinedExistingSummary = false;
        try
        {
            PathIdentity guardedEvidenceIdentity = OpenVerifiedEvidenceGuard(
                expectedEvidenceDirectoryIdentity,
                path,
                ref evidenceDirectoryGuard);

            stagingHandle = CreateFileW(
                stagingPath,
                GenericWrite | DeleteAccess,
                FileShareRead | FileShareWrite,
                ref nonInheritable,
                CreateNew,
                FileAttributeNormal | FileFlagOpenReparsePoint,
                IntPtr.Zero);
            if (stagingHandle == InvalidHandleValue)
            {
                throw new IOException(
                    LastError("CreateFileW(summary staging create-new)"));
            }
            RequireDirectEvidenceChild(
                stagingHandle,
                stagingPath,
                guardedEvidenceIdentity,
                "summary staging");
            PathIdentity stagingBeforeRename = GetPathIdentityFromOpenHandle(
                stagingHandle,
                PathKind.File);
            existingHandle = CreateFileW(
                path,
                FileReadAttributes | DeleteAccess,
                FileShareRead | FileShareWrite,
                ref nonInheritable,
                OpenExisting,
                FileAttributeNormal | FileFlagOpenReparsePoint,
                IntPtr.Zero);
            if (existingHandle == InvalidHandleValue)
            {
                int error = Marshal.GetLastWin32Error();
                if (error != ErrorFileNotFound)
                {
                    throw JsonPathIdentityError(
                        "CreateFileW(existing unowned summary)",
                        path,
                        error);
                }
            }
            else
            {
                RequireDirectEvidenceChild(
                    existingHandle,
                    path,
                    guardedEvidenceIdentity,
                    "existing unowned summary");
                PathIdentity existingBeforeRename =
                    GetPathIdentityFromOpenHandle(
                        existingHandle,
                        PathKind.File);
                if ((existingBeforeRename.Attributes &
                        FileAttributes.ReparsePoint) != 0)
                {
                    throw new WinterGatePathIdentityException(
                        "path identity: existing gate-summary.json is a " +
                        "reparse point.");
                }
                RenameOpenFileNoReplace(
                    existingHandle,
                    quarantinePath,
                    expectedEvidenceDirectoryIdentity,
                    "quarantine unowned summary");
                PathIdentity existingAfterRename =
                    GetPathIdentityFromOpenHandle(
                        existingHandle,
                        PathKind.File);
                if (!SameObject(existingBeforeRename, existingAfterRename))
                {
                    throw new WinterGatePathIdentityException(
                        "path identity: unowned summary object changed during " +
                        "quarantine.");
                }
                quarantineVerification = OpenPlainDirectEvidenceFile(
                    quarantinePath,
                    guardedEvidenceIdentity,
                    nonInheritable,
                    "quarantined unowned summary");
                PathIdentity quarantineIdentity =
                    GetPathIdentityFromOpenHandle(
                        quarantineVerification,
                        PathKind.File);
                if (!SameObject(existingBeforeRename, quarantineIdentity) ||
                    !SameStablePath(existingAfterRename, quarantineIdentity))
                {
                    throw new WinterGatePathIdentityException(
                        "path identity: quarantined summary verification failed.");
                }
                quarantinedExistingSummary = true;
            }

            WriteAllAndFlush(
                stagingHandle,
                quarantinedExistingSummary
                    ? collisionUtf8Bytes
                    : normalUtf8Bytes,
                "summary staging");

            RenameOpenFileNoReplace(
                stagingHandle,
                path,
                expectedEvidenceDirectoryIdentity,
                "publish owned summary");
            PathIdentity stagingAfterRename = GetPathIdentityFromOpenHandle(
                stagingHandle,
                PathKind.File);
            if (!SameObject(stagingBeforeRename, stagingAfterRename))
            {
                throw new WinterGatePathIdentityException(
                    "path identity: summary staging object changed during publish.");
            }
            finalVerification = OpenPlainDirectEvidenceFile(
                path,
                guardedEvidenceIdentity,
                nonInheritable,
                "published owned summary");
            PathIdentity finalIdentity = GetPathIdentityFromOpenHandle(
                finalVerification,
                PathKind.File);
            if (!SameObject(stagingBeforeRename, finalIdentity) ||
                !SameStablePath(stagingAfterRename, finalIdentity))
            {
                throw new WinterGatePathIdentityException(
                    "path identity: published summary verification failed.");
            }
            return quarantinedExistingSummary
                ? "evidence/" + Path.GetFileName(quarantinePath)
                : null;
        }
        finally
        {
            CloseOwnedHandle(ref finalVerification);
            CloseOwnedHandle(ref quarantineVerification);
            CloseOwnedHandle(ref existingHandle);
            CloseOwnedHandle(ref stagingHandle);
            CloseOwnedHandle(ref evidenceDirectoryGuard);
        }
    }

    public static void WriteUtf8JsonCreateNew(
        string path,
        string json,
        PathIdentity expectedEvidenceDirectoryIdentity)
    {
        ValidateJsonPath(path, expectedEvidenceDirectoryIdentity);
        byte[] utf8Bytes = EncodeUtf8Json(json);
        SecurityAttributes nonInheritable = NewSecurityAttributes(false);
        IntPtr evidenceDirectoryGuard = InvalidHandleValue;
        IntPtr jsonHandle = InvalidHandleValue;
        try
        {
            PathIdentity guardedEvidenceIdentity = OpenVerifiedEvidenceGuard(
                expectedEvidenceDirectoryIdentity,
                path,
                ref evidenceDirectoryGuard);
            jsonHandle = CreateFileW(
                path,
                GenericWrite,
                0,
                ref nonInheritable,
                CreateNew,
                FileAttributeNormal,
                IntPtr.Zero);
            if (jsonHandle == InvalidHandleValue)
            {
                throw new IOException(LastError("CreateFileW(JSON create-new)"));
            }
            RequireDirectEvidenceChild(
                jsonHandle,
                path,
                guardedEvidenceIdentity,
                "JSON evidence");
            WriteAllAndFlush(jsonHandle, utf8Bytes, "JSON");
        }
        finally
        {
            CloseOwnedHandle(ref jsonHandle);
            CloseOwnedHandle(ref evidenceDirectoryGuard);
        }
    }

// END LOOP 3.2-A JSON WRITER PUBLIC API
// BEGIN LOOP 3.3-A PROCESS PUBLIC API AND LAUNCH BUILDERS
    public static BoundedProcessResult RunProcessTree(
        StepDependencyLease dependencyLease,
        string[] arguments,
        string workingDirectory,
        string stdoutPath,
        string stderrPath,
        int timeoutMilliseconds,
        PathIdentity expectedEvidenceDirectoryIdentity,
        StructuredOutputReservation structuredOutputReservation)
    {
        if (dependencyLease == null)
        {
            throw new ArgumentNullException("dependencyLease");
        }
        dependencyLease.AssertStable();
        string executable = dependencyLease.ExecutablePath;
        ValidateProcessArguments(
            executable,
            arguments,
            workingDirectory,
            stdoutPath,
            stderrPath,
            timeoutMilliseconds,
            expectedEvidenceDirectoryIdentity);

        BoundedProcessResult result = new BoundedProcessResult();
        result.ProcessStarted = false;
        result.ProcessId = null;
        result.StartedUtc = null;
        result.EndedUtc = null;
        result.ElapsedMilliseconds = null;
        result.ExitCode = null;
        result.TimedOut = false;
        result.TreeDrained = true;
        result.HadLiveDescendantsAfterRootExit = false;
        result.StartError = null;
        result.OutputEvidenceValid = false;
        result.OutputEvidenceError = null;

        IntPtr stdoutHandle = InvalidHandleValue;
        IntPtr stderrHandle = InvalidHandleValue;
        IntPtr stdinHandle = InvalidHandleValue;
        IntPtr evidenceDirectoryGuard = InvalidHandleValue;
        IntPtr jobHandle = IntPtr.Zero;
        IntPtr environmentBlock = IntPtr.Zero;
        IntPtr attributeList = IntPtr.Zero;
        IntPtr inheritedHandleArray = IntPtr.Zero;
        IntPtr structuredOutputChildHandle = IntPtr.Zero;
        bool attributeListInitialized = false;
        ProcessInformation processInformation = new ProcessInformation();
        bool processCreated = false;
        bool processAssigned = false;
        Stopwatch processClock = null;
        PathIdentity stdoutCreationIdentity = null;
        PathIdentity stderrCreationIdentity = null;
        PathIdentity outputEvidenceDirectoryIdentity = null;

        try
        {
            SecurityAttributes inheritable = new SecurityAttributes();
            inheritable.Length = Marshal.SizeOf(typeof(SecurityAttributes));
            inheritable.SecurityDescriptor = IntPtr.Zero;
            inheritable.InheritHandle = 1;

            SecurityAttributes nonInheritable = new SecurityAttributes();
            nonInheritable.Length = Marshal.SizeOf(typeof(SecurityAttributes));
            nonInheritable.SecurityDescriptor = IntPtr.Zero;
            nonInheritable.InheritHandle = 0;

            evidenceDirectoryGuard = CreateFileW(
                expectedEvidenceDirectoryIdentity.FinalPath,
                FileReadAttributes,
                FileShareRead | FileShareWrite,
                ref nonInheritable,
                OpenExisting,
                FileFlagBackupSemantics | FileFlagOpenReparsePoint,
                IntPtr.Zero);
            if (evidenceDirectoryGuard == InvalidHandleValue)
            {
                return RecordStartFailure(
                    result,
                    LastError("CreateFileW(evidence-directory-guard)"));
            }
            PathIdentity guardedEvidenceIdentity =
                GetPathIdentityFromOpenHandle(
                    evidenceDirectoryGuard,
                    PathKind.Directory);
            outputEvidenceDirectoryIdentity = guardedEvidenceIdentity;
            if ((guardedEvidenceIdentity.Attributes & FileAttributes.ReparsePoint) != 0 ||
                !SameStablePath(
                    expectedEvidenceDirectoryIdentity,
                    guardedEvidenceIdentity))
            {
                return RecordStartFailure(
                    result,
                    "Evidence directory identity changed before output creation.");
            }

            stdoutHandle = CreateFileW(
                stdoutPath,
                GenericWrite,
                FileShareRead | FileShareWrite | FileShareDelete,
                ref inheritable,
                CreateNew,
                FileAttributeNormal,
                IntPtr.Zero);
            if (stdoutHandle == InvalidHandleValue)
            {
                return RecordStartFailure(result, LastError("CreateFileW(stdout)"));
            }
            RequireDirectEvidenceChild(
                stdoutHandle,
                stdoutPath,
                guardedEvidenceIdentity,
                "stdout");
            stdoutCreationIdentity = GetPathIdentityFromOpenHandle(
                stdoutHandle,
                PathKind.File);

            stderrHandle = CreateFileW(
                stderrPath,
                GenericWrite,
                FileShareRead | FileShareWrite | FileShareDelete,
                ref inheritable,
                CreateNew,
                FileAttributeNormal,
                IntPtr.Zero);
            if (stderrHandle == InvalidHandleValue)
            {
                return RecordStartFailure(result, LastError("CreateFileW(stderr)"));
            }
            RequireDirectEvidenceChild(
                stderrHandle,
                stderrPath,
                guardedEvidenceIdentity,
                "stderr");
            stderrCreationIdentity = GetPathIdentityFromOpenHandle(
                stderrHandle,
                PathKind.File);

            stdinHandle = CreateFileW(
                "NUL",
                GenericRead,
                FileShareRead | FileShareWrite | FileShareDelete,
                ref inheritable,
                OpenExisting,
                FileAttributeNormal,
                IntPtr.Zero);
            if (stdinHandle == InvalidHandleValue)
            {
                return RecordStartFailure(result, LastError("CreateFileW(NUL)"));
            }

            string jobName = @"Local\WinterGate-" +
                Guid.NewGuid().ToString("N");
            jobHandle = CreateJobObjectW(IntPtr.Zero, jobName);
            if (jobHandle == IntPtr.Zero)
            {
                return RecordStartFailure(result, LastError("CreateJobObjectW"));
            }
            int createJobError = Marshal.GetLastWin32Error();
            if (createJobError == ErrorAlreadyExists)
            {
                return RecordStartFailure(
                    result,
                    "CreateJobObjectW unexpectedly opened an existing named Job.");
            }

            JobObjectExtendedLimitInformationData limits =
                new JobObjectExtendedLimitInformationData();
            limits.BasicLimitInformation.LimitFlags = JobObjectLimitKillOnJobClose;
            if (!SetInformationJobObject(
                jobHandle,
                JobObjectExtendedLimitInformation,
                ref limits,
                Marshal.SizeOf(typeof(JobObjectExtendedLimitInformationData))))
            {
                return RecordStartFailure(result, LastError("SetInformationJobObject"));
            }

            IntPtr attributeListSize = IntPtr.Zero;
            InitializeProcThreadAttributeList(
                IntPtr.Zero,
                1,
                0,
                ref attributeListSize);
            if (attributeListSize == IntPtr.Zero)
            {
                return RecordStartFailure(
                    result,
                    LastError("InitializeProcThreadAttributeList(size)"));
            }

            attributeList = Marshal.AllocHGlobal(attributeListSize);
            if (!InitializeProcThreadAttributeList(
                attributeList,
                1,
                0,
                ref attributeListSize))
            {
                return RecordStartFailure(
                    result,
                    LastError("InitializeProcThreadAttributeList"));
            }
            attributeListInitialized = true;

            if (structuredOutputReservation != null)
            {
                structuredOutputChildHandle =
                    structuredOutputReservation.DuplicateInheritableWriterHandle();
            }
            int inheritedHandleCount =
                structuredOutputReservation == null ? 3 : 4;
            int inheritedHandleBytes = checked(
                IntPtr.Size * inheritedHandleCount);
            inheritedHandleArray = Marshal.AllocHGlobal(inheritedHandleBytes);
            Marshal.WriteIntPtr(inheritedHandleArray, 0, stdinHandle);
            Marshal.WriteIntPtr(inheritedHandleArray, IntPtr.Size, stdoutHandle);
            Marshal.WriteIntPtr(inheritedHandleArray, IntPtr.Size * 2, stderrHandle);
            if (structuredOutputReservation != null)
            {
                Marshal.WriteIntPtr(
                    inheritedHandleArray,
                    IntPtr.Size * 3, structuredOutputChildHandle);
            }

            if (!UpdateProcThreadAttribute(
                attributeList,
                0,
                new IntPtr(ProcThreadAttributeHandleList),
                inheritedHandleArray,
                new IntPtr(inheritedHandleBytes),
                IntPtr.Zero,
                IntPtr.Zero))
            {
                return RecordStartFailure(
                    result,
                    LastError("UpdateProcThreadAttribute(handle-list)"));
            }

            StartupInfoEx startup = new StartupInfoEx();
            startup.StartupInfo.Size = Marshal.SizeOf(typeof(StartupInfoEx));
            startup.StartupInfo.Flags = (int)StartfUseStdHandles;
            startup.StartupInfo.StdInput = stdinHandle;
            startup.StartupInfo.StdOutput = stdoutHandle;
            startup.StartupInfo.StdError = stderrHandle;
            startup.AttributeList = attributeList;

            environmentBlock = BuildChildEnvironmentBlock(
                jobName,
                structuredOutputChildHandle);
            dependencyLease.AssertStable();
            StringBuilder commandLine = new StringBuilder(
                BuildWindowsCommandLine(executable, arguments));
            DateTime processStartUtc = DateTime.UtcNow;
            if (!CreateProcessW(
                executable,
                commandLine,
                IntPtr.Zero,
                IntPtr.Zero,
                true,
                CreateSuspended | CreateUnicodeEnvironment |
                    CreateNoWindow | ExtendedStartupInfoPresent,
                environmentBlock,
                workingDirectory,
                ref startup,
                out processInformation))
            {
                return RecordStartFailure(result, LastError("CreateProcessW"));
            }

            processCreated = true;
            Marshal.FreeHGlobal(environmentBlock);
            environmentBlock = IntPtr.Zero;
            processClock = Stopwatch.StartNew();
            result.ProcessStarted = true;
            result.ProcessId = unchecked((int)processInformation.ProcessId);
            result.StartedUtc = processStartUtc;
            result.TreeDrained = false;

            if (!AssignProcessToJobObject(jobHandle, processInformation.Process))
            {
                AddEngineError(result, LastError("AssignProcessToJobObject"));
                result.TreeDrained = StopRecordedTree(
                    jobHandle,
                    processInformation.Process,
                    false,
                    result);
                CaptureStartedProcessCompletion(
                    processInformation.Process,
                    processClock,
                    result);
                return result;
            }
            processAssigned = true;

            // The output-name race is now closed: both files are verified open,
            // the child is still suspended, and its Job assignment is complete.
            // Release the no-delete directory guard immediately before resume so
            // the deterministic child-swap test can rename the evidence directory
            // after the child starts. The already-open stdout/stderr handles keep
            // pointing at the original directory object.
            CloseOwnedHandle(ref evidenceDirectoryGuard);

            uint previousSuspendCount = ResumeThread(processInformation.Thread);
            if (previousSuspendCount == ResumeFailed)
            {
                AddEngineError(result, LastError("ResumeThread"));
                result.TreeDrained = StopRecordedTree(
                    jobHandle,
                    processInformation.Process,
                    true,
                    result);
                CaptureStartedProcessCompletion(
                    processInformation.Process,
                    processClock,
                    result);
                return result;
            }

            CloseOwnedHandle(ref processInformation.Thread);
            ReleaseProcessStartResources(
                ref stdinHandle,
                ref structuredOutputChildHandle,
                ref attributeList,
                ref attributeListInitialized,
                ref inheritedHandleArray);

            uint waitResult = WaitForSingleObject(
                processInformation.Process,
                checked((uint)timeoutMilliseconds));
            if (waitResult == WaitTimeout)
            {
                result.TimedOut = true;
                result.TreeDrained = StopRecordedTree(
                    jobHandle,
                    processInformation.Process,
                    processAssigned,
                    result);
            }
            else if (waitResult == WaitFailed)
            {
                AddEngineError(result, LastError("WaitForSingleObject(root)"));
                result.TreeDrained = StopRecordedTree(
                    jobHandle,
                    processInformation.Process,
                    processAssigned,
                    result);
            }
            else if (waitResult != WaitObject0)
            {
                AddEngineError(
                    result,
                    "WaitForSingleObject(root) returned unexpected status 0x" +
                    waitResult.ToString("X8", CultureInfo.InvariantCulture));
                result.TreeDrained = StopRecordedTree(
                    jobHandle,
                    processInformation.Process,
                    processAssigned,
                    result);
            }
            else
            {
                bool hadDescendant;
                if (!ObserveRootAccountingExit(
                    jobHandle,
                    processInformation.ProcessId,
                    result,
                    out hadDescendant))
                {
                    result.TreeDrained = StopRecordedTree(
                        jobHandle,
                        processInformation.Process,
                        processAssigned,
                        result);
                }
                else if (hadDescendant)
                {
                    result.HadLiveDescendantsAfterRootExit = true;
                    result.TreeDrained = StopRecordedTree(
                        jobHandle,
                        processInformation.Process,
                        processAssigned,
                        result);
                }
                else
                {
                    result.TreeDrained = true;
                }
            }

            CaptureStartedProcessCompletion(
                processInformation.Process,
                processClock,
                result);
            return result;
        }
        catch (Exception exception)
        {
            AddEngineError(
                result,
                exception.GetType().FullName + ": " + exception.Message);
            if (processCreated)
            {
                result.TreeDrained = StopRecordedTree(
                    jobHandle,
                    processInformation.Process,
                    processAssigned,
                    result);
                CaptureStartedProcessCompletion(
                    processInformation.Process,
                    processClock,
                    result);
            }
            return result;
        }
        finally
        {
            CloseOwnedHandle(ref processInformation.Thread);
            if ((!processCreated || result.TreeDrained) &&
                stdoutCreationIdentity != null &&
                stderrCreationIdentity != null)
            {
                ValidateOutputEvidenceBeforeClose(
                    result,
                    stdoutHandle,
                    stdoutPath,
                    stdoutCreationIdentity,
                    stderrHandle,
                    stderrPath,
                    stderrCreationIdentity,
                    outputEvidenceDirectoryIdentity);
            }
            ReleaseLaunchResources(
                ref stdoutHandle,
                ref stderrHandle,
                ref stdinHandle,
                ref structuredOutputChildHandle,
                ref attributeList,
                ref attributeListInitialized,
                ref inheritedHandleArray);
            CloseOwnedHandle(ref processInformation.Process);
            CloseOwnedHandle(ref jobHandle);
            CloseOwnedHandle(ref evidenceDirectoryGuard);
            if (environmentBlock != IntPtr.Zero)
            {
                Marshal.FreeHGlobal(environmentBlock);
                environmentBlock = IntPtr.Zero;
            }
        }
    }

    internal static string EncodeWindowsCommandLineArgument(string argument)
    {
        if (argument == null)
        {
            throw new ArgumentNullException("argument");
        }

        bool needsQuotes = argument.Length == 0;
        for (int index = 0; index < argument.Length && !needsQuotes; index++)
        {
            char value = argument[index];
            needsQuotes = value == '"' || char.IsWhiteSpace(value);
        }
        if (!needsQuotes)
        {
            return argument;
        }

        StringBuilder encoded = new StringBuilder(argument.Length + 2);
        encoded.Append('"');
        int pendingBackslashes = 0;
        for (int index = 0; index < argument.Length; index++)
        {
            char value = argument[index];
            if (value == '\\')
            {
                pendingBackslashes++;
                continue;
            }

            if (value == '"')
            {
                encoded.Append('\\', checked(pendingBackslashes * 2 + 1));
                encoded.Append('"');
                pendingBackslashes = 0;
                continue;
            }

            encoded.Append('\\', pendingBackslashes);
            pendingBackslashes = 0;
            encoded.Append(value);
        }

        encoded.Append('\\', checked(pendingBackslashes * 2));
        encoded.Append('"');
        return encoded.ToString();
    }

    private static string BuildWindowsCommandLine(
        string executable,
        string[] arguments)
    {
        StringBuilder commandLine = new StringBuilder();
        commandLine.Append(EncodeWindowsCommandLineArgument(executable));
        for (int index = 0; index < arguments.Length; index++)
        {
            commandLine.Append(' ');
            commandLine.Append(
                EncodeWindowsCommandLineArgument(arguments[index]));
        }

        if (commandLine.Length > 32766)
        {
            throw new ArgumentException(
                "The encoded process command line exceeds 32766 characters.",
                "arguments");
        }
        return commandLine.ToString();
    }

    private static IntPtr BuildChildEnvironmentBlock(
        string jobName,
        IntPtr structuredOutputChildHandle)
    {
        if (String.IsNullOrWhiteSpace(jobName))
        {
            throw new ArgumentException("Named Job identity is required.", "jobName");
        }
        SortedDictionary<string, string> environment =
            new SortedDictionary<string, string>(
                StringComparer.OrdinalIgnoreCase);
        foreach (DictionaryEntry entry in Environment.GetEnvironmentVariables())
        {
            string key = Convert.ToString(
                entry.Key,
                CultureInfo.InvariantCulture);
            string value = Convert.ToString(
                entry.Value,
                CultureInfo.InvariantCulture);
            if (!String.Equals(
                key,
                GateJobEnvironmentVariable,
                StringComparison.OrdinalIgnoreCase) &&
                !String.Equals(
                key,
                StructuredOutputHandleEnvironmentVariable,
                StringComparison.OrdinalIgnoreCase))
            {
                environment[key] = value;
            }
        }
        environment[GateJobEnvironmentVariable] = jobName;
        if (structuredOutputChildHandle != IntPtr.Zero &&
            structuredOutputChildHandle != InvalidHandleValue)
        {
            environment[StructuredOutputHandleEnvironmentVariable] =
                structuredOutputChildHandle.ToInt64().ToString(
                    CultureInfo.InvariantCulture);
        }

        StringBuilder block = new StringBuilder();
        foreach (KeyValuePair<string, string> entry in environment)
        {
            block.Append(entry.Key);
            block.Append('=');
            block.Append(entry.Value);
            block.Append('\0');
        }
        block.Append('\0');
        byte[] bytes = Encoding.Unicode.GetBytes(block.ToString());
        IntPtr nativeBlock = Marshal.AllocHGlobal(bytes.Length);
        try
        {
            Marshal.Copy(bytes, 0, nativeBlock, bytes.Length);
            return nativeBlock;
        }
        catch
        {
            Marshal.FreeHGlobal(nativeBlock);
            throw;
        }
    }

// END LOOP 3.3-A PROCESS PUBLIC API AND LAUNCH BUILDERS

// BEGIN LOOP 3.1-C READABLE HELPERS
    private static StructuredOutputSnapshot FreezeStructuredOutputCore(
        StructuredOutputReservation reservation,
        int maximumBytes)
    {
        PathIdentity currentEvidenceIdentity = GetPathIdentityFromOpenHandle(
            reservation.EvidenceDirectoryGuard,
            PathKind.Directory);
        if ((currentEvidenceIdentity.Attributes &
                FileAttributes.ReparsePoint) != 0 ||
            !SameStablePath(
                reservation.EvidenceDirectoryIdentity,
                currentEvidenceIdentity))
        {
            throw new WinterGatePathIdentityException(
                "path identity: structured output evidence directory changed.");
        }

        PathIdentity currentOpenIdentity = GetPathIdentityFromOpenHandle(
            reservation.OwnerHandle,
            PathKind.File);
        if ((currentOpenIdentity.Attributes & FileAttributes.ReparsePoint) != 0 ||
            !SameStablePath(
                reservation.CreationIdentity,
                currentOpenIdentity))
        {
            throw new WinterGatePathIdentityException(
                "path identity: structured output owner handle changed.");
        }
        RequireDirectEvidenceChild(
            reservation.OwnerHandle,
            reservation.FixedPath,
            currentEvidenceIdentity,
            "frozen structured output");

        byte[] content;
        using (SafeFileHandle borrowed = new SafeFileHandle(
            reservation.OwnerHandle,
            false))
        using (FileStream stream = new FileStream(
            borrowed,
            FileAccess.ReadWrite))
        {
            if (stream.Length > maximumBytes)
            {
                throw new InvalidDataException(
                    "Structured JSON exceeds its size limit: " +
                    reservation.FixedPath);
            }
            content = new byte[checked((int)stream.Length)];
            stream.Position = 0;
            int totalRead = 0;
            while (totalRead < content.Length)
            {
                int read = stream.Read(
                    content,
                    totalRead,
                    content.Length - totalRead);
                if (read == 0)
                {
                    throw new EndOfStreamException(
                        "Structured JSON ended before its reported length.");
                }
                totalRead += read;
            }
        }

        PathIdentity afterReadIdentity = GetPathIdentityFromOpenHandle(
            reservation.OwnerHandle,
            PathKind.File);
        if (!SameStablePath(
            reservation.CreationIdentity,
            afterReadIdentity))
        {
            throw new WinterGatePathIdentityException(
                "path identity: structured output changed during freeze.");
        }

        StructuredOutputSnapshot result = new StructuredOutputSnapshot();
        if (ByteArraysEqual(content, reservation.MarkerBytes))
        {
            result.HasContent = false;
            result.Text = null;
            return result;
        }
        result.HasContent = true;
        result.Text = new UTF8Encoding(false, true).GetString(content);
        return result;
    }

    private static bool ByteArraysEqual(byte[] left, byte[] right)
    {
        if (left == null || right == null || left.Length != right.Length)
        {
            return false;
        }
        for (int index = 0; index < left.Length; index++)
        {
            if (left[index] != right[index])
            {
                return false;
            }
        }
        return true;
    }

    private sealed class StrictJsonParser
    {
        private readonly string text;
        private readonly int maximumDepth;
        private readonly int maximumDocumentCharacters;
        private readonly int maximumNumberTokenLength;
        private int offset;

        internal StrictJsonParser(
            string text,
            int maximumDepth,
            int maximumDocumentCharacters,
            int maximumNumberTokenLength)
        {
            this.text = text;
            this.maximumDepth = maximumDepth;
            this.maximumDocumentCharacters = maximumDocumentCharacters;
            this.maximumNumberTokenLength = maximumNumberTokenLength;
        }

        internal void Validate()
        {
            if (text.Length > maximumDocumentCharacters)
            {
                ThrowInvalid(
                    "document_too_long",
                    maximumDocumentCharacters);
            }
            SkipWhitespace();
            ParseValue(0);
            SkipWhitespace();
            if (offset != text.Length)
            {
                ThrowInvalid("trailing_content");
            }
        }

        private void ParseValue(int containerDepth)
        {
            if (offset >= text.Length)
            {
                ThrowInvalid("expected_value");
            }
            char current = text[offset];
            if (current == '{')
            {
                RequireContainerDepth(containerDepth);
                ParseObject(containerDepth + 1);
                return;
            }
            if (current == '[')
            {
                RequireContainerDepth(containerDepth);
                ParseArray(containerDepth + 1);
                return;
            }
            if (current == '"')
            {
                ParseString();
                return;
            }
            if (current == '-' || IsDigit(current))
            {
                ParseNumber();
                return;
            }
            if (current == 't')
            {
                ParseLiteral("true");
                return;
            }
            if (current == 'f')
            {
                ParseLiteral("false");
                return;
            }
            if (current == 'n')
            {
                ParseLiteral("null");
                return;
            }
            ThrowInvalid("expected_value");
        }

        private void ParseObject(int containerDepth)
        {
            Expect('{');
            SkipWhitespace();
            if (Consume('}'))
            {
                return;
            }
            SortedSet<string> propertyNames = new SortedSet<string>(
                StringComparer.Ordinal);
            while (true)
            {
                if (offset >= text.Length || text[offset] != '"')
                {
                    ThrowInvalid("object_property_name");
                }
                int propertyOffset = offset;
                string propertyName = ParseString();
                if (!propertyNames.Add(propertyName))
                {
                    ThrowInvalid("duplicate_property", propertyOffset);
                }
                SkipWhitespace();
                Expect(':');
                SkipWhitespace();
                ParseValue(containerDepth);
                SkipWhitespace();
                if (Consume('}'))
                {
                    return;
                }
                Expect(',');
                SkipWhitespace();
            }
        }

        private void ParseArray(int containerDepth)
        {
            Expect('[');
            SkipWhitespace();
            if (Consume(']'))
            {
                return;
            }
            while (true)
            {
                ParseValue(containerDepth);
                SkipWhitespace();
                if (Consume(']'))
                {
                    return;
                }
                Expect(',');
                SkipWhitespace();
            }
        }

        private string ParseString()
        {
            Expect('"');
            StringBuilder decoded = new StringBuilder();
            while (offset < text.Length)
            {
                int characterOffset = offset;
                char current = text[offset++];
                if (current == '"')
                {
                    return decoded.ToString();
                }
                if (current == '\\')
                {
                    ParseEscape(decoded, characterOffset);
                    continue;
                }
                if (current <= '\u001f')
                {
                    ThrowInvalid("unescaped_control", characterOffset);
                }
                if (Char.IsHighSurrogate(current))
                {
                    if (offset >= text.Length ||
                        !Char.IsLowSurrogate(text[offset]))
                    {
                        ThrowInvalid(
                            "unpaired_high_surrogate",
                            characterOffset);
                    }
                    decoded.Append(current);
                    decoded.Append(text[offset++]);
                    continue;
                }
                if (Char.IsLowSurrogate(current))
                {
                    ThrowInvalid(
                        "unpaired_low_surrogate",
                        characterOffset);
                }
                decoded.Append(current);
            }
            ThrowInvalid("unterminated_string");
            return null;
        }

        private void ParseEscape(StringBuilder decoded, int escapeOffset)
        {
            if (offset >= text.Length)
            {
                ThrowInvalid("unterminated_escape", escapeOffset);
            }
            int escapedOffset = offset;
            char escaped = text[offset++];
            switch (escaped)
            {
                case '"': decoded.Append('"'); return;
                case '\\': decoded.Append('\\'); return;
                case '/': decoded.Append('/'); return;
                case 'b': decoded.Append('\b'); return;
                case 'f': decoded.Append('\f'); return;
                case 'n': decoded.Append('\n'); return;
                case 'r': decoded.Append('\r'); return;
                case 't': decoded.Append('\t'); return;
                case 'u':
                    int codeUnit = ParseHexCodeUnit();
                    if (codeUnit >= 0xd800 && codeUnit <= 0xdbff)
                    {
                        if (offset + 6 > text.Length ||
                            text[offset] != '\\' ||
                            text[offset + 1] != 'u')
                        {
                            ThrowInvalid(
                                "escaped_high_surrogate_requires_low",
                                escapeOffset);
                        }
                        int lowEscapeOffset = offset;
                        offset += 2;
                        int low = ParseHexCodeUnit();
                        if (low < 0xdc00 || low > 0xdfff)
                        {
                            ThrowInvalid(
                                "escaped_high_surrogate_requires_low",
                                lowEscapeOffset);
                        }
                        decoded.Append((char)codeUnit);
                        decoded.Append((char)low);
                        return;
                    }
                    if (codeUnit >= 0xdc00 && codeUnit <= 0xdfff)
                    {
                        ThrowInvalid(
                            "unpaired_escaped_low_surrogate",
                            escapeOffset);
                    }
                    decoded.Append((char)codeUnit);
                    return;
                default:
                    ThrowInvalid("unknown_escape", escapedOffset);
                    return;
            }
        }

        private int ParseHexCodeUnit()
        {
            if (offset + 4 > text.Length)
            {
                ThrowInvalid("incomplete_unicode_escape");
            }
            int value = 0;
            for (int index = 0; index < 4; index++)
            {
                int digitOffset = offset;
                char digit = text[offset++];
                int nibble;
                if (digit >= '0' && digit <= '9')
                {
                    nibble = digit - '0';
                }
                else if (digit >= 'a' && digit <= 'f')
                {
                    nibble = digit - 'a' + 10;
                }
                else if (digit >= 'A' && digit <= 'F')
                {
                    nibble = digit - 'A' + 10;
                }
                else
                {
                    ThrowInvalid("invalid_unicode_hex", digitOffset);
                    return 0;
                }
                value = (value << 4) | nibble;
            }
            return value;
        }

        private void ParseNumber()
        {
            int numberStart = offset;
            if (Consume('-'))
            {
                RequireNumberLength(numberStart);
            }
            if (offset >= text.Length)
            {
                ThrowInvalid("incomplete_number");
            }
            if (Consume('0'))
            {
                RequireNumberLength(numberStart);
                if (offset < text.Length && IsDigit(text[offset]))
                {
                    ThrowInvalid("leading_zero");
                }
            }
            else
            {
                if (offset >= text.Length ||
                    text[offset] < '1' || text[offset] > '9')
                {
                    ThrowInvalid("invalid_integer");
                }
                ConsumeDigits(numberStart);
            }
            if (Consume('.'))
            {
                RequireNumberLength(numberStart);
                if (offset >= text.Length || !IsDigit(text[offset]))
                {
                    ThrowInvalid("fraction_digit_required");
                }
                ConsumeDigits(numberStart);
            }
            if (offset < text.Length &&
                (text[offset] == 'e' || text[offset] == 'E'))
            {
                offset++;
                RequireNumberLength(numberStart);
                if (offset < text.Length &&
                    (text[offset] == '+' || text[offset] == '-'))
                {
                    offset++;
                    RequireNumberLength(numberStart);
                }
                if (offset >= text.Length || !IsDigit(text[offset]))
                {
                    ThrowInvalid("exponent_digit_required");
                }
                ConsumeDigits(numberStart);
            }
        }

        private void ConsumeDigits(int numberStart)
        {
            while (offset < text.Length && IsDigit(text[offset]))
            {
                offset++;
                RequireNumberLength(numberStart);
            }
        }

        private void RequireNumberLength(int numberStart)
        {
            if (offset - numberStart > maximumNumberTokenLength)
            {
                ThrowInvalid(
                    "number_too_long",
                    numberStart + maximumNumberTokenLength);
            }
        }

        private static bool IsDigit(char value)
        {
            return value >= '0' && value <= '9';
        }

        private void ParseLiteral(string literal)
        {
            for (int index = 0; index < literal.Length; index++)
            {
                int literalOffset = offset + index;
                if (literalOffset >= text.Length ||
                    text[literalOffset] != literal[index])
                {
                    ThrowInvalid("invalid_literal", literalOffset);
                }
            }
            offset += literal.Length;
        }

        private void RequireContainerDepth(int containerDepth)
        {
            if (containerDepth >= maximumDepth)
            {
                ThrowInvalid("maximum_depth");
            }
        }

        private void SkipWhitespace()
        {
            while (offset < text.Length)
            {
                char current = text[offset];
                if (current != ' ' && current != '\t' &&
                    current != '\r' && current != '\n')
                {
                    return;
                }
                offset++;
            }
        }

        private bool Consume(char expected)
        {
            if (offset < text.Length && text[offset] == expected)
            {
                offset++;
                return true;
            }
            return false;
        }

        private void Expect(char expected)
        {
            if (!Consume(expected))
            {
                ThrowInvalid("expected_token");
            }
        }

        private void ThrowInvalid(string reason)
        {
            ThrowInvalid(reason, offset);
        }

        private void ThrowInvalid(string reason, int failureOffset)
        {
            throw new FormatException(
                "strict_json:" + reason +
                " at UTF-16 offset " +
                failureOffset.ToString(CultureInfo.InvariantCulture) +
                ".");
        }
    }

    private static SecurityAttributes NewSecurityAttributes(bool inheritable)
    {
        SecurityAttributes attributes = new SecurityAttributes();
        attributes.Length = Marshal.SizeOf(typeof(SecurityAttributes));
        attributes.SecurityDescriptor = IntPtr.Zero;
        attributes.InheritHandle = inheritable ? 1 : 0;
        return attributes;
    }

    private static void RequirePlainAbsoluteFilePath(
        string path,
        string parameterName)
    {
        if (String.IsNullOrWhiteSpace(path) ||
            !Path.IsPathRooted(path) ||
            path.StartsWith(@"\\?\", StringComparison.OrdinalIgnoreCase) ||
            path.StartsWith(@"\\.\", StringComparison.OrdinalIgnoreCase))
        {
            throw new ArgumentException(
                parameterName + " must be an absolute, non-device path.",
                parameterName);
        }
        string fullPath = Path.GetFullPath(path);
        string leaf = Path.GetFileName(fullPath);
        if (!String.Equals(path, fullPath, StringComparison.OrdinalIgnoreCase) ||
            String.IsNullOrEmpty(leaf) ||
            leaf == "." ||
            leaf == ".." ||
            leaf.IndexOfAny(Path.GetInvalidFileNameChars()) >= 0 ||
            !String.Equals(
                leaf.TrimEnd(' ', '.'),
                leaf,
                StringComparison.Ordinal))
        {
            throw new ArgumentException(
                parameterName + " must end in one plain file-name component.",
                parameterName);
        }
    }

    private static StepDependencyFile AcquireStepDependencyFile(
        string path,
        bool missingReturnsNull)
    {
        RequirePlainAbsoluteFilePath(path, "path");
        PathIdentity initialIdentity = missingReturnsNull
            ? TryGetPathIdentity(path, PathKind.File, true)
            : GetPathIdentity(path, PathKind.File, true);
        if (initialIdentity == null)
        {
            return null;
        }

        HeldPathChain pathChain = null;
        IntPtr readHandle = InvalidHandleValue;
        try
        {
            pathChain = OpenExistingPathChain(
                initialIdentity.FinalPath,
                PathKind.File,
                true);
            if (!SameStablePath(initialIdentity, pathChain.LeafIdentity))
            {
                throw new WinterGatePathIdentityException(
                    "path identity: step dependency changed while its path " +
                    "chain was retained: " + path);
            }
            SecurityAttributes nonInheritable = NewSecurityAttributes(false);
            readHandle = CreateFileW(
                pathChain.LeafIdentity.FinalPath,
                GenericRead,
                FileShareRead,
                ref nonInheritable,
                OpenExisting,
                FileAttributeNormal | FileFlagOpenReparsePoint |
                    FileFlagBackupSemantics,
                IntPtr.Zero);
            if (readHandle == InvalidHandleValue)
            {
                throw JsonPathIdentityError(
                    "CreateFileW(step dependency lease)",
                    path,
                    Marshal.GetLastWin32Error());
            }
            PathIdentity creationIdentity = GetPathIdentityFromOpenHandle(
                readHandle,
                PathKind.File);
            if ((creationIdentity.Attributes & FileAttributes.ReparsePoint) != 0 ||
                !SameStablePath(pathChain.LeafIdentity, creationIdentity))
            {
                throw new WinterGatePathIdentityException(
                    "path identity: step dependency changed while its read " +
                    "lease was acquired: " + path);
            }
            StepDependencyFile result = new StepDependencyFile(
                path,
                creationIdentity,
                pathChain,
                readHandle);
            pathChain = null;
            readHandle = IntPtr.Zero;
            return result;
        }
        finally
        {
            CloseOwnedHandle(ref readHandle);
            if (pathChain != null)
            {
                pathChain.Dispose();
            }
        }
    }

    private static void AssertStepDependencyFileStable(
        StepDependencyFile dependency)
    {
        PathIdentity openIdentity = GetPathIdentityFromOpenHandle(
            dependency.ReadHandle,
            PathKind.File);
        if (!SameStablePath(dependency.CreationIdentity, openIdentity) ||
            !SameStablePath(
                dependency.CreationIdentity,
                dependency.PathChain.LeafIdentity))
        {
            throw new WinterGatePathIdentityException(
                "path identity: retained step dependency changed: " +
                dependency.RequestedPath);
        }
        PathIdentity currentIdentity = GetReadableFileIdentityCore(
            dependency.RequestedPath,
            false);
        if (!SameStablePath(dependency.CreationIdentity, currentIdentity))
        {
            throw new WinterGatePathIdentityException(
                "path identity: retained step dependency path changed: " +
                dependency.RequestedPath);
        }
    }

    private static PathIdentity GetReadableFileIdentityCore(
        string path,
        bool missingReturnsNull)
    {
        RequirePlainAbsoluteFilePath(path, "path");
        PathIdentity chainIdentity = missingReturnsNull
            ? TryGetPathIdentity(path, PathKind.File, true)
            : GetPathIdentity(path, PathKind.File, true);
        if (chainIdentity == null)
        {
            return null;
        }
        SecurityAttributes nonInheritable = NewSecurityAttributes(false);
        IntPtr fileHandle = CreateFileW(
            chainIdentity.FinalPath,
            GenericRead,
            FileShareRead | FileShareWrite,
            ref nonInheritable,
            OpenExisting,
            FileAttributeNormal | FileFlagOpenReparsePoint |
                FileFlagBackupSemantics,
            IntPtr.Zero);
        if (fileHandle == InvalidHandleValue)
        {
            int error = Marshal.GetLastWin32Error();
            if (missingReturnsNull &&
                (error == ErrorFileNotFound || error == ErrorPathNotFound))
            {
                return null;
            }
            throw JsonPathIdentityError(
                "CreateFileW(readable identity)",
                path,
                error);
        }
        try
        {
            PathIdentity identity = GetPathIdentityFromOpenHandle(
                fileHandle,
                PathKind.File);
            if ((identity.Attributes & FileAttributes.ReparsePoint) != 0 ||
                !SameStablePath(chainIdentity, identity))
            {
                throw new WinterGatePathIdentityException(
                    "path identity: readable file or ancestor changed: " + path);
            }
            return identity;
        }
        finally
        {
            CloseOwnedHandle(ref fileHandle);
        }
    }

// END LOOP 3.1-C READABLE HELPERS

// BEGIN LOOP 3.2-B JSON WRITER HELPERS
    private static void ValidateJsonPath(
        string path,
        PathIdentity expectedEvidenceDirectoryIdentity)
    {
        if (expectedEvidenceDirectoryIdentity == null ||
            String.IsNullOrWhiteSpace(expectedEvidenceDirectoryIdentity.FinalPath))
        {
            throw new ArgumentNullException(
                "expectedEvidenceDirectoryIdentity");
        }
        RequirePlainAbsoluteFilePath(path, "path");
        RequireLexicalDirectChild(
            path,
            expectedEvidenceDirectoryIdentity.FinalPath,
            "path");
    }

    private static IntPtr OpenPlainDirectEvidenceFile(
        string path,
        PathIdentity guardedEvidenceIdentity,
        SecurityAttributes nonInheritable,
        string label)
    {
        IntPtr handle = CreateFileW(
            path,
            FileReadAttributes,
            FileShareRead | FileShareWrite | FileShareDelete,
            ref nonInheritable,
            OpenExisting,
            FileAttributeNormal | FileFlagOpenReparsePoint,
            IntPtr.Zero);
        if (handle == InvalidHandleValue)
        {
            throw JsonPathIdentityError(
                "CreateFileW(" + label + ")",
                path,
                Marshal.GetLastWin32Error());
        }
        try
        {
            RequireDirectEvidenceChild(
                handle,
                path,
                guardedEvidenceIdentity,
                label);
            PathIdentity identity = GetPathIdentityFromOpenHandle(
                handle,
                PathKind.File);
            if ((identity.Attributes & FileAttributes.ReparsePoint) != 0)
            {
                throw new WinterGatePathIdentityException(
                    "path identity: " + label + " is a reparse point: " + path);
            }
            return handle;
        }
        catch
        {
            CloseOwnedHandle(ref handle);
            throw;
        }
    }

    private static void RenameOpenFileNoReplace(
        IntPtr sourceHandle,
        string absoluteTargetPath,
        PathIdentity expectedEvidenceDirectoryIdentity,
        string operation)
    {
        ValidateJsonPath(
            absoluteTargetPath,
            expectedEvidenceDirectoryIdentity);
        byte[] targetBytes = Encoding.Unicode.GetBytes(absoluteTargetPath);
        int rootDirectoryOffset = IntPtr.Size == 8 ? 8 : 4;
        int fileNameLengthOffset = IntPtr.Size == 8 ? 16 : 8;
        int fileNameOffset = IntPtr.Size == 8 ? 20 : 12;
        IntPtr information = Marshal.AllocHGlobal(
            checked(fileNameOffset + targetBytes.Length + 2));
        try
        {
            for (int index = 0;
                 index < fileNameOffset + targetBytes.Length + 2;
                 index++)
            {
                Marshal.WriteByte(information, index, 0);
            }
            Marshal.WriteByte(information, 0, 0);
            Marshal.WriteIntPtr(
                information,
                rootDirectoryOffset,
                IntPtr.Zero);
            Marshal.WriteInt32(
                information,
                fileNameLengthOffset,
                targetBytes.Length);
            Marshal.Copy(
                targetBytes,
                0,
                IntPtr.Add(information, fileNameOffset),
                targetBytes.Length);
            if (!SetFileInformationByHandle(
                sourceHandle,
                FileRenameInfo,
                information,
                checked((uint)(fileNameOffset + targetBytes.Length + 2))))
            {
                throw new IOException(
                    LastError("SetFileInformationByHandle(" + operation + ")"));
            }
        }
        finally
        {
            Marshal.FreeHGlobal(information);
        }
    }

    private static PathIdentity OpenVerifiedEvidenceGuard(
        PathIdentity expectedEvidenceDirectoryIdentity,
        string requestedPath,
        ref IntPtr evidenceDirectoryGuard)
    {
        SecurityAttributes nonInheritable = NewSecurityAttributes(false);
        evidenceDirectoryGuard = CreateFileW(
            expectedEvidenceDirectoryIdentity.FinalPath,
            FileReadAttributes,
            FileShareRead | FileShareWrite,
            ref nonInheritable,
            OpenExisting,
            FileFlagBackupSemantics | FileFlagOpenReparsePoint,
            IntPtr.Zero);
        if (evidenceDirectoryGuard == InvalidHandleValue)
        {
            int error = Marshal.GetLastWin32Error();
            throw JsonPathIdentityError(
                "CreateFileW(JSON evidence-directory guard)",
                expectedEvidenceDirectoryIdentity.FinalPath,
                error);
        }
        PathIdentity guardedEvidenceIdentity = GetPathIdentityFromOpenHandle(
            evidenceDirectoryGuard,
            PathKind.Directory);
        if ((guardedEvidenceIdentity.Attributes & FileAttributes.ReparsePoint) != 0 ||
            !SameStablePath(
                expectedEvidenceDirectoryIdentity,
                guardedEvidenceIdentity))
        {
            throw new WinterGatePathIdentityException(
                "path identity: evidence directory changed before JSON access: " +
                requestedPath);
        }
        return guardedEvidenceIdentity;
    }

    private static byte[] EncodeUtf8Json(string json)
    {
        if (json == null)
        {
            throw new ArgumentNullException("json");
        }
        return new UTF8Encoding(false, true).GetBytes(
            json + Environment.NewLine);
    }

    private static void WriteAllAndFlush(
        IntPtr fileHandle,
        byte[] bytes,
        string operation)
    {
        GCHandle pinnedBytes = default(GCHandle);
        bool bytesArePinned = false;
        try
        {
            if (bytes.Length != 0)
            {
                pinnedBytes = GCHandle.Alloc(bytes, GCHandleType.Pinned);
                bytesArePinned = true;
                int offset = 0;
                while (offset < bytes.Length)
                {
                    uint written;
                    if (!WriteFile(
                        fileHandle,
                        IntPtr.Add(pinnedBytes.AddrOfPinnedObject(), offset),
                        checked((uint)(bytes.Length - offset)),
                        out written,
                        IntPtr.Zero))
                    {
                        throw new IOException(
                            LastError("WriteFile(" + operation + ")"));
                    }
                    if (written == 0)
                    {
                        throw new IOException(
                            "WriteFile(" + operation +
                            ") made no forward progress.");
                    }
                    offset = checked(offset + checked((int)written));
                }
            }
            if (!FlushFileBuffers(fileHandle))
            {
                throw new IOException(
                    LastError("FlushFileBuffers(" + operation + ")"));
            }
        }
        finally
        {
            if (bytesArePinned)
            {
                pinnedBytes.Free();
            }
        }
    }

// END LOOP 3.2-B JSON WRITER HELPERS
// BEGIN LOOP 3.3-B PROCESS ARGUMENT VALIDATION
    private static void ValidateProcessArguments(
        string executable,
        string[] arguments,
        string workingDirectory,
        string stdoutPath,
        string stderrPath,
        int timeoutMilliseconds,
        PathIdentity expectedEvidenceDirectoryIdentity)
    {
        if (String.IsNullOrWhiteSpace(executable))
        {
            throw new ArgumentException("Executable is required.", "executable");
        }
        if (arguments == null)
        {
            throw new ArgumentNullException("arguments");
        }
        for (int index = 0; index < arguments.Length; index++)
        {
            if (arguments[index] == null)
            {
                throw new ArgumentException(
                    "Process arguments cannot contain null.",
                    "arguments");
            }
        }
        if (String.IsNullOrWhiteSpace(workingDirectory))
        {
            throw new ArgumentException(
                "Working directory is required.",
                "workingDirectory");
        }
        if (expectedEvidenceDirectoryIdentity == null ||
            String.IsNullOrWhiteSpace(expectedEvidenceDirectoryIdentity.FinalPath))
        {
            throw new ArgumentNullException(
                "expectedEvidenceDirectoryIdentity");
        }
        if (String.IsNullOrWhiteSpace(stdoutPath))
        {
            throw new ArgumentException("stdoutPath is required.", "stdoutPath");
        }
        if (String.IsNullOrWhiteSpace(stderrPath))
        {
            throw new ArgumentException("stderrPath is required.", "stderrPath");
        }
        if (String.Equals(stdoutPath, stderrPath, StringComparison.OrdinalIgnoreCase))
        {
            throw new ArgumentException(
                "stdoutPath and stderrPath must differ.",
                "stderrPath");
        }
        if (timeoutMilliseconds <= 0)
        {
            throw new ArgumentOutOfRangeException(
                "timeoutMilliseconds",
                "Process timeout must be positive.");
        }

        RequireLexicalDirectChild(
            stdoutPath,
            expectedEvidenceDirectoryIdentity.FinalPath,
            "stdoutPath");
        RequireLexicalDirectChild(
            stderrPath,
            expectedEvidenceDirectoryIdentity.FinalPath,
            "stderrPath");

        BuildWindowsCommandLine(executable, arguments);
    }

// END LOOP 3.3-B PROCESS ARGUMENT VALIDATION

// BEGIN LOOP 3.2-C JSON DIRECT-CHILD HELPERS
    private static void RequireLexicalDirectChild(
        string candidate,
        string expectedParent,
        string parameterName)
    {
        if (!Path.IsPathRooted(candidate) ||
            candidate.StartsWith(@"\\?\", StringComparison.OrdinalIgnoreCase) ||
            candidate.StartsWith(@"\\.\", StringComparison.OrdinalIgnoreCase))
        {
            throw new ArgumentException(
                parameterName +
                " must be an absolute, non-device path.",
                parameterName);
        }
        string fullCandidate = Path.GetFullPath(candidate);
        string actualParent = Path.GetDirectoryName(fullCandidate);
        string leaf = Path.GetFileName(fullCandidate);
        if (!String.Equals(
                candidate,
                fullCandidate,
                StringComparison.OrdinalIgnoreCase) ||
            String.IsNullOrEmpty(actualParent) ||
            String.IsNullOrEmpty(leaf) ||
            leaf == "." ||
            leaf == ".." ||
            leaf.IndexOfAny(Path.GetInvalidFileNameChars()) >= 0 ||
            !String.Equals(
                leaf.TrimEnd(' ', '.'),
                leaf,
                StringComparison.Ordinal) ||
            !String.Equals(
                actualParent.TrimEnd(Path.DirectorySeparatorChar),
                Path.GetFullPath(expectedParent).TrimEnd(Path.DirectorySeparatorChar),
                StringComparison.OrdinalIgnoreCase))
        {
            throw new ArgumentException(
                parameterName +
                " must name a direct child of the pinned evidence directory.",
                parameterName);
        }
    }

    private static void RequireDirectEvidenceChild(
        IntPtr fileHandle,
        string requestedPath,
        PathIdentity expectedParent,
        string streamName)
    {
        PathIdentity openedFile = GetPathIdentityFromOpenHandle(
            fileHandle,
            PathKind.File);
        string openedParent = Path.GetDirectoryName(openedFile.FinalPath);
        string openedLeaf = Path.GetFileName(openedFile.FinalPath);
        string requestedLeaf = Path.GetFileName(Path.GetFullPath(requestedPath));
        if (String.IsNullOrEmpty(openedParent) ||
            !String.Equals(
                openedParent.TrimEnd(Path.DirectorySeparatorChar),
                expectedParent.FinalPath.TrimEnd(Path.DirectorySeparatorChar),
                StringComparison.OrdinalIgnoreCase) ||
            !String.Equals(
                openedLeaf,
                requestedLeaf,
                StringComparison.OrdinalIgnoreCase))
        {
            throw new WinterGatePathIdentityException(
                "path identity: " + streamName +
                " handle did not open inside the pinned evidence directory.");
        }
    }

// END LOOP 3.2-C JSON DIRECT-CHILD HELPERS
// BEGIN LOOP 3.3-C PROCESS FAILURE AND DRAIN HELPERS
    private static BoundedProcessResult RecordStartFailure(
        BoundedProcessResult result,
        string error)
    {
        AddEngineError(result, error);
        result.ProcessStarted = false;
        result.ProcessId = null;
        result.StartedUtc = null;
        result.EndedUtc = null;
        result.ElapsedMilliseconds = null;
        result.ExitCode = null;
        result.TimedOut = false;
        result.TreeDrained = true;
        result.HadLiveDescendantsAfterRootExit = false;
        return result;
    }

    private static bool StopRecordedTree(
        IntPtr job,
        IntPtr process,
        bool processAssigned,
        BoundedProcessResult result)
    {
        if (processAssigned &&
            job != IntPtr.Zero &&
            !TerminateJobObject(job, ForcedExitCode))
        {
            AddEngineError(result, LastError("TerminateJobObject"));
        }

        uint initialProcessState = WaitForSingleObject(process, 0);
        if (initialProcessState != WaitObject0)
        {
            if (!TerminateProcess(process, ForcedExitCode))
            {
                int terminateError = Marshal.GetLastWin32Error();
                if (WaitForSingleObject(process, 0) != WaitObject0)
                {
                    AddEngineError(
                        result,
                        Win32Error("TerminateProcess", terminateError));
                }
            }
        }

        uint rootWait = WaitForSingleObject(
            process,
            CleanupTimeoutMilliseconds);
        bool rootGone = rootWait == WaitObject0;
        if (!rootGone)
        {
            if (rootWait == WaitFailed)
            {
                AddEngineError(
                    result,
                    LastError("WaitForSingleObject(cleanup-root)"));
            }
            else
            {
                AddEngineError(
                    result,
                    "Recorded root process did not exit within cleanup bound.");
            }
        }

        bool jobDrained = DrainJob(job, result);
        return rootGone && jobDrained;
    }

    private static bool DrainJob(
        IntPtr job,
        BoundedProcessResult result)
    {
        Stopwatch cleanupClock = Stopwatch.StartNew();
        while (true)
        {
            uint activeProcesses;
            if (!TryGetActiveProcessCount(job, out activeProcesses, result))
            {
                return false;
            }
            if (activeProcesses == 0)
            {
                return true;
            }
            if (cleanupClock.ElapsedMilliseconds >= CleanupTimeoutMilliseconds)
            {
                AddEngineError(
                    result,
                    "Job Object still had " +
                    activeProcesses.ToString(CultureInfo.InvariantCulture) +
                    " active process(es) after cleanup bound.");
                return false;
            }
            Thread.Sleep(CleanupPollMilliseconds);
        }
    }

    private static bool TryGetActiveProcessCount(
        IntPtr job,
        out uint activeProcesses,
        BoundedProcessResult result)
    {
        activeProcesses = 0;
        if (job == IntPtr.Zero)
        {
            AddEngineError(result, "Job Object handle is unavailable.");
            return false;
        }

        JobObjectBasicAccountingInformationData accounting =
            new JobObjectBasicAccountingInformationData();
        if (!QueryInformationJobObject(
            job,
            JobObjectBasicAccountingInformation,
            out accounting,
            Marshal.SizeOf(typeof(JobObjectBasicAccountingInformationData)),
            IntPtr.Zero))
        {
            AddEngineError(
                result,
                LastError("QueryInformationJobObject"));
            return false;
        }
        activeProcesses = accounting.ActiveProcesses;
        return true;
    }

// END LOOP 3.3-C PROCESS FAILURE AND DRAIN HELPERS

// BEGIN LOOP 3.5-A AUTHORITATIVE JOB-ZERO REPLACEMENT
    private static bool ObserveRootAccountingExit(
        IntPtr job,
        uint rootProcessId,
        BoundedProcessResult result,
        out bool hadDescendant)
    {
        hadDescendant = false;
        Stopwatch accountingClock = Stopwatch.StartNew();
        while (true)
        {
            ulong[] processIds;
            if (!TryGetJobProcessIds(job, result, out processIds))
            {
                return false;
            }

            bool rootStillListed = false;
            for (int index = 0; index < processIds.Length; index++)
            {
                if (processIds[index] == rootProcessId)
                {
                    rootStillListed = true;
                }
                else
                {
                    bool isRunning;
                    if (!TryIsProcessRunning(processIds[index], result, out isRunning))
                    {
                        return false;
                    }
                    if (isRunning)
                    {
                        hadDescendant = true;
                        return true;
                    }
                }
            }

            if (!rootStillListed)
            {
                uint activeProcesses;
                if (!TryGetActiveProcessCount(
                    job,
                    out activeProcesses,
                    result))
                {
                    return false;
                }
                if (activeProcesses == 0)
                {
                    return true;
                }
                if (accountingClock.ElapsedMilliseconds >= CleanupTimeoutMilliseconds)
                {
                    AddEngineError(
                        result,
                        "Job Object accounting remained active without a running " +
                        "process ID after the accounting bound.");
                    return false;
                }
                Thread.Sleep(CleanupPollMilliseconds);
                continue;
            }
            if (accountingClock.ElapsedMilliseconds >= CleanupTimeoutMilliseconds)
            {
                AddEngineError(
                    result,
                    "Signaled root process remained in the Job Object process list " +
                    "after the accounting bound.");
                return false;
            }
            Thread.Sleep(CleanupPollMilliseconds);
        }
    }

// END LOOP 3.5-A AUTHORITATIVE JOB-ZERO REPLACEMENT

// BEGIN LOOP 3.3-D PROCESS OBSERVATION AND RELEASE HELPERS
    private static bool TryGetJobProcessIds(
        IntPtr job,
        BoundedProcessResult result,
        out ulong[] processIds)
    {
        processIds = new ulong[0];
        int capacity = 16;
        while (capacity <= 65536)
        {
            int byteCount = checked(8 + capacity * IntPtr.Size);
            IntPtr buffer = Marshal.AllocHGlobal(byteCount);
            try
            {
                for (int offset = 0; offset < byteCount; offset += 4)
                {
                    Marshal.WriteInt32(buffer, offset, 0);
                }
                if (QueryInformationJobObjectBuffer(
                    job,
                    JobObjectBasicProcessIdList,
                    buffer,
                    byteCount,
                    IntPtr.Zero))
                {
                    int count = Marshal.ReadInt32(buffer, 4);
                    if (count < 0 || count > capacity)
                    {
                        AddEngineError(
                            result,
                            "Job Object returned an invalid process-ID count.");
                        return false;
                    }
                    processIds = new ulong[count];
                    for (int index = 0; index < count; index++)
                    {
                        int offset = 8 + index * IntPtr.Size;
                        processIds[index] = IntPtr.Size == 8
                            ? unchecked((ulong)Marshal.ReadInt64(buffer, offset))
                            : unchecked((uint)Marshal.ReadInt32(buffer, offset));
                    }
                    return true;
                }

                int error = Marshal.GetLastWin32Error();
                if (error != ErrorMoreData)
                {
                    AddEngineError(
                        result,
                        Win32Error("QueryInformationJobObject(process-list)", error));
                    return false;
                }
                int assigned = Marshal.ReadInt32(buffer, 0);
                capacity = Math.Max(capacity * 2, assigned);
            }
            finally
            {
                Marshal.FreeHGlobal(buffer);
            }
        }

        AddEngineError(
            result,
            "Job Object process list exceeded the bounded capacity.");
        return false;
    }

    private static bool TryIsProcessRunning(
        ulong processId,
        BoundedProcessResult result,
        out bool isRunning)
    {
        isRunning = false;
        if (processId > UInt32.MaxValue)
        {
            AddEngineError(result, "Job Object returned an invalid process ID.");
            return false;
        }
        IntPtr process = OpenProcess(
            SynchronizeAccess | ProcessQueryLimitedInformation,
            false,
            unchecked((uint)processId));
        if (process == IntPtr.Zero)
        {
            int error = Marshal.GetLastWin32Error();
            if (error == ErrorInvalidParameter)
            {
                return true;
            }
            AddEngineError(
                result,
                Win32Error("OpenProcess(job-descendant)", error));
            return false;
        }
        try
        {
            uint wait = WaitForSingleObject(process, 0);
            if (wait == WaitObject0)
            {
                return true;
            }
            if (wait == WaitTimeout)
            {
                uint exitCode;
                if (!GetExitCodeProcess(process, out exitCode))
                {
                    AddEngineError(
                        result,
                        LastError("GetExitCodeProcess(job-descendant)"));
                    return false;
                }
                if (exitCode != StillActive)
                {
                    return true;
                }
                isRunning = true;
                return true;
            }
            AddEngineError(
                result,
                wait == WaitFailed
                    ? LastError("WaitForSingleObject(job-descendant)")
                    : "Unexpected Job descendant wait status 0x" +
                        wait.ToString("X8", CultureInfo.InvariantCulture));
            return false;
        }
        finally
        {
            CloseHandle(process);
        }
    }

    private static void CaptureStartedProcessCompletion(
        IntPtr process,
        Stopwatch processClock,
        BoundedProcessResult result)
    {
        result.EndedUtc = DateTime.UtcNow;
        result.ElapsedMilliseconds =
            processClock == null ? 0L : processClock.ElapsedMilliseconds;
        result.ExitCode = -1;

        uint nativeExitCode;
        if (!GetExitCodeProcess(process, out nativeExitCode))
        {
            AddEngineError(result, LastError("GetExitCodeProcess"));
            return;
        }
        result.ExitCode = unchecked((int)nativeExitCode);
    }

    private static void ValidateOutputEvidenceBeforeClose(
        BoundedProcessResult result,
        IntPtr stdoutHandle,
        string stdoutPath,
        PathIdentity stdoutCreationIdentity,
        IntPtr stderrHandle,
        string stderrPath,
        PathIdentity stderrCreationIdentity,
        PathIdentity expectedEvidenceDirectoryIdentity)
    {
        List<string> errors = new List<string>();
        ValidateOutputEvidenceStream(
            "stdout",
            stdoutHandle,
            stdoutPath,
            stdoutCreationIdentity,
            expectedEvidenceDirectoryIdentity,
            errors);
        ValidateOutputEvidenceStream(
            "stderr",
            stderrHandle,
            stderrPath,
            stderrCreationIdentity,
            expectedEvidenceDirectoryIdentity,
            errors);
        result.OutputEvidenceValid = errors.Count == 0;
        result.OutputEvidenceError = errors.Count == 0
            ? null
            : String.Join(" | ", errors.ToArray());
    }

    private static void ValidateOutputEvidenceStream(
        string label,
        IntPtr openHandle,
        string fixedPath,
        PathIdentity creationIdentity,
        PathIdentity expectedEvidenceDirectoryIdentity,
        List<string> errors)
    {
        try
        {
            PathIdentity currentOpenIdentity =
                GetPathIdentityFromOpenHandle(openHandle, PathKind.File);
            if (!SameStablePath(creationIdentity, currentOpenIdentity))
            {
                errors.Add(
                    label + " open-handle identity changed after process drain.");
            }
        }
        catch (Exception exception)
        {
            errors.Add(
                label + " open-handle identity validation failed: " +
                exception.GetType().FullName + ": " + exception.Message);
        }

        try
        {
            SecurityAttributes nonInheritable = NewSecurityAttributes(false);
            IntPtr currentFixedHandle = CreateFileW(
                fixedPath,
                FileReadAttributes,
                FileShareRead | FileShareWrite | FileShareDelete,
                ref nonInheritable,
                OpenExisting,
                FileAttributeNormal | FileFlagOpenReparsePoint,
                IntPtr.Zero);
            if (currentFixedHandle == InvalidHandleValue)
            {
                throw JsonPathIdentityError(
                    "CreateFileW(" + label + " fixed-leaf reopen)",
                    fixedPath,
                    Marshal.GetLastWin32Error());
            }
            try
            {
                RequireDirectEvidenceChild(
                    currentFixedHandle,
                    fixedPath,
                    expectedEvidenceDirectoryIdentity,
                    label + " fixed leaf");
                PathIdentity currentFixedIdentity =
                    GetPathIdentityFromOpenHandle(
                        currentFixedHandle,
                        PathKind.File);
                if (!SameStablePath(creationIdentity, currentFixedIdentity))
                {
                    errors.Add(
                        label +
                        " fixed-leaf identity changed after process drain.");
                }
            }
            finally
            {
                CloseOwnedHandle(ref currentFixedHandle);
            }
        }
        catch (Exception exception)
        {
            errors.Add(
                label + " fixed-leaf identity validation failed: " +
                exception.GetType().FullName + ": " + exception.Message);
        }
    }

    private static void ReleaseProcessStartResources(
        ref IntPtr stdinHandle,
        ref IntPtr structuredOutputChildHandle,
        ref IntPtr attributeList,
        ref bool attributeListInitialized,
        ref IntPtr inheritedHandleArray)
    {
        if (attributeListInitialized && attributeList != IntPtr.Zero)
        {
            DeleteProcThreadAttributeList(attributeList);
            attributeListInitialized = false;
        }
        if (attributeList != IntPtr.Zero)
        {
            Marshal.FreeHGlobal(attributeList);
            attributeList = IntPtr.Zero;
        }
        if (inheritedHandleArray != IntPtr.Zero)
        {
            Marshal.FreeHGlobal(inheritedHandleArray);
            inheritedHandleArray = IntPtr.Zero;
        }
        CloseOwnedHandle(ref stdinHandle);
        CloseOwnedHandle(ref structuredOutputChildHandle);
    }

    private static void ReleaseLaunchResources(
        ref IntPtr stdoutHandle,
        ref IntPtr stderrHandle,
        ref IntPtr stdinHandle,
        ref IntPtr structuredOutputChildHandle,
        ref IntPtr attributeList,
        ref bool attributeListInitialized,
        ref IntPtr inheritedHandleArray)
    {
        ReleaseProcessStartResources(
            ref stdinHandle,
            ref structuredOutputChildHandle,
            ref attributeList,
            ref attributeListInitialized,
            ref inheritedHandleArray);
        CloseOwnedHandle(ref stdoutHandle);
        CloseOwnedHandle(ref stderrHandle);
    }

// END LOOP 3.3-D PROCESS OBSERVATION AND RELEASE HELPERS

// BEGIN LOOP 3.1-D SHARED HANDLE AND ERROR HELPERS
    private static void CloseOwnedHandle(ref IntPtr handle)
    {
        if (handle != IntPtr.Zero && handle != InvalidHandleValue)
        {
            CloseHandle(handle);
        }
        handle = IntPtr.Zero;
    }

    private static void AddEngineError(
        BoundedProcessResult result,
        string error)
    {
        if (String.IsNullOrEmpty(error))
        {
            return;
        }
        if (String.IsNullOrEmpty(result.StartError))
        {
            result.StartError = error;
        }
        else
        {
            result.StartError = result.StartError + " | " + error;
        }
    }

    private static string LastError(string operation)
    {
        return Win32Error(operation, Marshal.GetLastWin32Error());
    }

    private static WinterGatePathIdentityException JsonPathIdentityError(
        string operation,
        string path,
        int error)
    {
        Win32Exception inner = new Win32Exception(error);
        return new WinterGatePathIdentityException(
            "path identity: " + operation + " failed for '" + path +
            "' with Win32 error " +
            error.ToString(CultureInfo.InvariantCulture) + ": " +
            inner.Message,
            error,
            inner);
    }

    private static string Win32Error(string operation, int error)
    {
        return operation + " failed with Win32 error " +
            error.ToString(CultureInfo.InvariantCulture) + ": " +
            new Win32Exception(error).Message;
    }
// END LOOP 3.1-D SHARED HANDLE AND ERROR HELPERS
// END PROCESS ENGINE

        private static string RequireAbsoluteNonDevicePath(string path)
        {
            if (String.IsNullOrWhiteSpace(path))
            {
                throw new WinterGatePathIdentityException(
                    "path identity: path is empty");
            }
            if (path.StartsWith(@"\\?\", StringComparison.OrdinalIgnoreCase) ||
                path.StartsWith(@"\\.\", StringComparison.OrdinalIgnoreCase))
            {
                throw new WinterGatePathIdentityException(
                    "path identity: device paths are not accepted: " + path);
            }
            if (IsDirectorySeparator(path[0]) &&
                !(path.Length >= 2 && path[0] == '\\' && path[1] == '\\'))
            {
                throw new WinterGatePathIdentityException(
                    "path identity: current-drive-rooted paths are not accepted: " +
                    path);
            }
            if (path.Length >= 2 &&
                path[1] == ':' &&
                (path.Length == 2 || !IsDirectorySeparator(path[2])))
            {
                throw new WinterGatePathIdentityException(
                    "path identity: drive-relative paths are not accepted: " + path);
            }
            if (!Path.IsPathRooted(path))
            {
                throw new WinterGatePathIdentityException(
                    "path identity: absolute path required: " + path);
            }

            try
            {
                string fullPath = Path.GetFullPath(path);
                if (fullPath.StartsWith(@"\\?\", StringComparison.OrdinalIgnoreCase) ||
                    fullPath.StartsWith(@"\\.\", StringComparison.OrdinalIgnoreCase))
                {
                    throw new WinterGatePathIdentityException(
                        "path identity: device paths are not accepted: " + path);
                }
                return TrimEndingSeparatorsExceptRoot(fullPath);
            }
            catch (WinterGatePathIdentityException)
            {
                throw;
            }
            catch (Exception exception)
            {
                throw new WinterGatePathIdentityException(
                    "path identity: invalid absolute path: " + path,
                    0,
                    exception);
            }
        }

        private static List<string> BuildComponentPaths(string fullPath)
        {
            string root = Path.GetPathRoot(fullPath);
            if (String.IsNullOrEmpty(root))
            {
                throw new WinterGatePathIdentityException(
                    "path identity: path has no root: " + fullPath);
            }

            List<string> paths = new List<string>();
            string current = root;
            paths.Add(current);
            string remainder = fullPath.Substring(root.Length);
            string[] parts = remainder.Split(
                new[] { Path.DirectorySeparatorChar, Path.AltDirectorySeparatorChar },
                StringSplitOptions.RemoveEmptyEntries);
            foreach (string part in parts)
            {
                current = Path.Combine(current, part);
                paths.Add(current);
            }
            return paths;
        }

        private static HeldPathChain OpenExistingPathChain(
            string fullPath,
            PathKind expectedLeafKind,
            bool rejectAnyReparseComponent)
        {
            List<string> components = BuildComponentPaths(fullPath);
            HeldPathChain chain = new HeldPathChain();
            PathIdentity currentIdentity = null;
            try
            {
                for (int index = 0; index < components.Count; index++)
                {
                    bool isLeaf = index == components.Count - 1;
                    string component;
                    if (index == 0)
                    {
                        component = components[0];
                    }
                    else
                    {
                        string leafName = Path.GetFileName(components[index]);
                        component = Path.Combine(
                            currentIdentity.FinalPath,
                            leafName);
                    }

                    SafeFileHandle handle = OpenPathHandle(
                        component,
                        rejectAnyReparseComponent);
                    chain.Handles.Add(handle);
                    PathKind componentKind =
                        isLeaf ? expectedLeafKind : PathKind.Directory;
                    PathIdentity openedIdentity = ReadPathIdentityFromHandle(
                        handle,
                        componentKind,
                        rejectAnyReparseComponent,
                        component);
                    if (index > 0 &&
                        !String.Equals(
                            NormalizeComparableFinalPath(component),
                            openedIdentity.FinalPath,
                            StringComparison.OrdinalIgnoreCase))
                    {
                        throw new WinterGatePathIdentityException(
                            "path identity: component final path changed while " +
                            "resolving: " + component);
                    }
                    currentIdentity = openedIdentity;
                }

                if (currentIdentity == null)
                {
                    throw new WinterGatePathIdentityException(
                        "path identity: no leaf object was resolved: " + fullPath);
                }
                chain.LeafIdentity = currentIdentity;
                return chain;
            }
            catch
            {
                chain.Dispose();
                throw;
            }
        }

        private static SafeFileHandle OpenPathHandle(
            string path,
            bool rejectReparse)
        {
            uint flags = FILE_FLAG_BACKUP_SEMANTICS;
            if (rejectReparse)
            {
                flags |= FILE_FLAG_OPEN_REPARSE_POINT;
            }
            SafeFileHandle handle = CreateFileW(
                path,
                FILE_READ_DATA,
                FILE_SHARE_READ | FILE_SHARE_WRITE,
                IntPtr.Zero,
                OPEN_EXISTING,
                flags,
                IntPtr.Zero);
            if (handle.IsInvalid)
            {
                int error = Marshal.GetLastWin32Error();
                handle.Dispose();
                throw NativePathError("open", path, error);
            }
            return handle;
        }

        private static PathIdentity ReadPathIdentityFromHandle(
            SafeFileHandle handle,
            PathKind expectedKind,
            bool rejectReparse,
            string displayPath)
        {
            BY_HANDLE_FILE_INFORMATION information;
            if (!GetFileInformationByHandle(handle, out information))
            {
                int error = Marshal.GetLastWin32Error();
                throw NativePathError("inspect", displayPath, error);
            }
            FileAttributes attributes =
                (FileAttributes)information.FileAttributes;
            if (rejectReparse &&
                (attributes & FileAttributes.ReparsePoint) != 0)
            {
                throw new WinterGatePathIdentityException(
                    "path identity: reparse component rejected: " + displayPath);
            }
            bool isDirectory =
                (attributes & FileAttributes.Directory) != 0;
            bool expectedDirectory = expectedKind == PathKind.Directory;
            if (isDirectory != expectedDirectory)
            {
                throw new WinterGatePathIdentityException(
                    "path identity: expected " +
                    expectedKind.ToString().ToLowerInvariant() +
                    ": " + displayPath);
            }
            return new PathIdentity
            {
                FinalPath = GetNormalizedFinalPath(handle, displayPath),
                VolumeSerialNumber = information.VolumeSerialNumber,
                FileIndex =
                    ((ulong)information.FileIndexHigh << 32) |
                    information.FileIndexLow,
                Attributes = attributes
            };
        }

        private static string GetNormalizedFinalPath(
            SafeFileHandle handle,
            string displayPath)
        {
            int capacity = 512;
            while (true)
            {
                StringBuilder buffer = new StringBuilder(capacity);
                uint written = GetFinalPathNameByHandleW(
                    handle,
                    buffer,
                    (uint)buffer.Capacity,
                    0);
                if (written == 0)
                {
                    int error = Marshal.GetLastWin32Error();
                    throw NativePathError("resolve final path", displayPath, error);
                }
                if (written < buffer.Capacity)
                {
                    return NormalizeComparableFinalPath(buffer.ToString());
                }
                if (written > Int32.MaxValue - 1)
                {
                    throw new WinterGatePathIdentityException(
                        "path identity: final path is too long: " + displayPath);
                }
                capacity = checked((int)written + 1);
            }
        }

        private static string NormalizeComparableFinalPath(string path)
        {
            if (String.IsNullOrEmpty(path))
            {
                return path;
            }

            string normalized;
            if (path.StartsWith(@"\\?\UNC\", StringComparison.OrdinalIgnoreCase))
            {
                normalized = @"\\" + path.Substring(8);
            }
            else if (path.StartsWith(@"\\?\", StringComparison.OrdinalIgnoreCase))
            {
                normalized = path.Substring(4);
            }
            else
            {
                normalized = path;
            }
            normalized = Path.GetFullPath(normalized);
            return TrimEndingSeparatorsExceptRoot(normalized);
        }

        private static string TrimEndingSeparatorsExceptRoot(string path)
        {
            string root = Path.GetPathRoot(path);
            int minimum = String.IsNullOrEmpty(root) ? 0 : root.Length;
            int end = path.Length;
            while (end > minimum && IsDirectorySeparator(path[end - 1]))
            {
                end--;
            }
            return end == path.Length ? path : path.Substring(0, end);
        }

        private static bool IsDirectorySeparator(char value)
        {
            return value == Path.DirectorySeparatorChar ||
                value == Path.AltDirectorySeparatorChar;
        }

        private static WinterGatePathIdentityException NativePathError(
            string operation,
            string path,
            int nativeErrorCode)
        {
            Win32Exception native = new Win32Exception(nativeErrorCode);
            return new WinterGatePathIdentityException(
                "path identity: could not " + operation + " '" + path +
                "': " + native.Message + " (" + nativeErrorCode + ")",
                nativeErrorCode,
                native);
        }
    }
}
'@
    Add-Type -TypeDefinition $nativeSource -Language CSharp -ErrorAction Stop
}

function Throw-GatePathIdentityError {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [string]$Message,
        [Parameter(Position = 1)]
        [System.Exception]$InnerException
    )

    $fullMessage = "path identity: $Message"
    if ($null -eq $InnerException) {
        throw [WinterGate.WinterGatePathIdentityException]::new($fullMessage)
    }
    throw [WinterGate.WinterGatePathIdentityException]::new(
        $fullMessage,
        0,
        $InnerException
    )
}

function Assert-WinterGateHostIdentity {
    [CmdletBinding()]
    param()

    if ($PSVersionTable.PSEdition -ne 'Desktop' -or
        $PSVersionTable.PSVersion.Major -ne 5) {
        Throw-GatePathIdentityError `
            'gate host is not Windows PowerShell Desktop 5.1'
    }

    $trustedPath = Join-Path `
        ([Environment]::SystemDirectory) `
        'WindowsPowerShell\v1.0\powershell.exe'
    try {
        $currentPath = [System.Diagnostics.Process]::GetCurrentProcess().MainModule.FileName
        $trustedIdentity = [WinterGate.Native]::GetPathIdentity(
            $trustedPath,
            [WinterGate.PathKind]::File,
            $true
        )
        $currentIdentity = [WinterGate.Native]::GetPathIdentity(
            $currentPath,
            [WinterGate.PathKind]::File,
            $true
        )
    }
    catch [WinterGate.WinterGatePathIdentityException] {
        throw
    }
    catch {
        Throw-GatePathIdentityError `
            'could not resolve the trusted gate host identity' `
            $_.Exception
    }

    if (-not [WinterGate.Native]::SameObject(
        $currentIdentity,
        $trustedIdentity
    )) {
        Throw-GatePathIdentityError `
            'gate host is not the trusted System-directory PowerShell object'
    }
    return $trustedIdentity
}

function Get-NormalizedAbsolutePlainPath {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [string]$Path,
        [Parameter(Mandatory = $true, Position = 1)]
        [string]$Label
    )

    if ([string]::IsNullOrWhiteSpace($Path)) {
        Throw-GatePathIdentityError "$Label is empty"
    }
    if ($Path.StartsWith('\\?\', [System.StringComparison]::OrdinalIgnoreCase) -or
        $Path.StartsWith('\\.\', [System.StringComparison]::OrdinalIgnoreCase)) {
        Throw-GatePathIdentityError "$Label must not use a device path: $Path"
    }
    if (($Path.StartsWith('\', [System.StringComparison]::Ordinal) -and
         -not $Path.StartsWith('\\', [System.StringComparison]::Ordinal)) -or
        $Path.StartsWith('/', [System.StringComparison]::Ordinal)) {
        Throw-GatePathIdentityError `
            "$Label must not be rooted on the current drive: $Path"
    }
    if ($Path -match '^[A-Za-z]:(?![\\/])') {
        Throw-GatePathIdentityError "$Label must not be drive-relative: $Path"
    }
    if (-not [System.IO.Path]::IsPathRooted($Path)) {
        Throw-GatePathIdentityError "$Label must be absolute: $Path"
    }

    try {
        $fullPath = [System.IO.Path]::GetFullPath($Path)
        $root = [System.IO.Path]::GetPathRoot($fullPath)
    }
    catch {
        Throw-GatePathIdentityError "$Label is invalid: $Path" $_.Exception
    }
    if ([string]::IsNullOrEmpty($root)) {
        Throw-GatePathIdentityError "$Label has no root: $Path"
    }

    $rawRoot = [System.IO.Path]::GetPathRoot($Path)
    $rawRemainder = $Path.Substring($rawRoot.Length)
    if ($rawRemainder -match '[\\/]{2,}') {
        Throw-GatePathIdentityError "$Label contains an empty component: $Path"
    }
    $invalid = [System.IO.Path]::GetInvalidFileNameChars()
    foreach ($component in $rawRemainder.Split(
        [char[]]@('\', '/'),
        [System.StringSplitOptions]::RemoveEmptyEntries)) {
        if ($component -eq '.' -or $component -eq '..') {
            Throw-GatePathIdentityError "$Label contains a dot component: $Path"
        }
        if ($component.IndexOfAny($invalid) -ge 0 -or
            [System.Management.Automation.WildcardPattern]::ContainsWildcardCharacters(
                $component)) {
            Throw-GatePathIdentityError "$Label contains an invalid component: $Path"
        }
        if ($component.TrimEnd([char[]]@(' ', '.')) -ne $component) {
            Throw-GatePathIdentityError "$Label contains an aliased trailing character: $Path"
        }
    }

    if ($fullPath.Length -gt $root.Length) {
        $fullPath = $fullPath.TrimEnd([char[]]@('\', '/'))
    }
    return $fullPath
}

function Assert-PlainChildName {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [string]$LeafName,
        [Parameter(Mandatory = $true, Position = 1)]
        [string]$Label
    )

    if ([string]::IsNullOrWhiteSpace($LeafName) -or
        $LeafName -eq '.' -or
        $LeafName -eq '..' -or
        $LeafName.IndexOfAny([char[]]@('\', '/')) -ge 0 -or
        $LeafName.IndexOfAny([System.IO.Path]::GetInvalidFileNameChars()) -ge 0 -or
        [System.Management.Automation.WildcardPattern]::ContainsWildcardCharacters(
            $LeafName) -or
        $LeafName.TrimEnd([char[]]@(' ', '.')) -ne $LeafName) {
        Throw-GatePathIdentityError "$Label is not one plain path component: $LeafName"
    }
}

function Get-UnwrappedException {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [System.Exception]$Exception
    )

    $current = $Exception
    while ($null -ne $current.InnerException -and
        ($current -is [System.Management.Automation.MethodInvocationException] -or
         $current -is [System.Reflection.TargetInvocationException])) {
        $current = $current.InnerException
    }
    return $current
}

function Assert-GatePathState {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [WinterGate.PathIdentity]$ExpectedIdentity,
        [Parameter(Mandatory = $true, Position = 1)]
        [string]$Label
    )

    $expectedKind = [WinterGate.PathKind]::File
    if (($ExpectedIdentity.Attributes -band
        [System.IO.FileAttributes]::Directory) -ne 0) {
        $expectedKind = [WinterGate.PathKind]::Directory
    }
    try {
        $actual = [WinterGate.Native]::GetPathIdentity(
            $ExpectedIdentity.FinalPath,
            $expectedKind,
            $true
        )
    }
    catch {
        $unwrapped = Get-UnwrappedException $_.Exception
        if ($unwrapped -is [WinterGate.WinterGatePathIdentityException]) {
            throw $unwrapped
        }
        Throw-GatePathIdentityError "$Label could not be reopened" $unwrapped
    }
    if (-not [WinterGate.Native]::SameStablePath(
        $ExpectedIdentity,
        $actual)) {
        Throw-GatePathIdentityError "$Label changed after validation"
    }
    return $actual
}

function Test-SameOrChildFinalPath {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [object]$Candidate,
        [Parameter(Mandatory = $true, Position = 1)]
        [object]$Base
    )

    foreach ($record in @($Candidate, $Base)) {
        if ($null -eq $record -or
            $null -eq $record.PSObject.Properties['FinalPath'] -or
            $null -eq $record.PSObject.Properties['VolumeSerialNumber']) {
            Throw-GatePathIdentityError `
                'containment comparison requires a complete path identity or plan'
        }
    }
    if ([uint32]$Candidate.VolumeSerialNumber -ne
        [uint32]$Base.VolumeSerialNumber) {
        return $false
    }
    if ([string]::Equals(
        [string]$Candidate.FinalPath,
        [string]$Base.FinalPath,
        [System.StringComparison]::OrdinalIgnoreCase)) {
        return $true
    }
    $prefix = [string]$Base.FinalPath
    if (-not $prefix.EndsWith('\', [System.StringComparison]::Ordinal)) {
        $prefix += '\'
    }
    return ([string]$Candidate.FinalPath).StartsWith(
        $prefix,
        [System.StringComparison]::OrdinalIgnoreCase
    )
}

function Get-ProspectiveDirectoryPlan {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [string]$Path,
        [Parameter(Mandatory = $true, Position = 1)]
        [string]$Label,
        [switch]$RequireMissing
    )

    $fullPath = Get-NormalizedAbsolutePlainPath $Path $Label
    try {
        $existing = [WinterGate.Native]::TryGetPathIdentity(
            $fullPath,
            [WinterGate.PathKind]::Directory,
            $true
        )
    }
    catch {
        $unwrapped = Get-UnwrappedException $_.Exception
        if ($unwrapped -is [WinterGate.WinterGatePathIdentityException]) {
            throw $unwrapped
        }
        Throw-GatePathIdentityError "$Label could not be inspected" $unwrapped
    }
    if ($null -ne $existing) {
        if ($RequireMissing) {
            Throw-GatePathIdentityError "$Label already exists: $fullPath"
        }
        return [pscustomobject][ordered]@{
            ExistingIdentity = $existing
            MissingComponents = [string[]]@()
            FinalPath = $existing.FinalPath
            VolumeSerialNumber = $existing.VolumeSerialNumber
        }
    }

    $missing = New-Object 'System.Collections.Generic.List[string]'
    $probe = $fullPath
    while ($null -eq $existing) {
        $leaf = [System.IO.Path]::GetFileName($probe)
        Assert-PlainChildName $leaf "$Label unresolved component"
        $missing.Insert(0, $leaf)
        $parent = [System.IO.Path]::GetDirectoryName($probe)
        if ([string]::IsNullOrEmpty($parent) -or $parent -eq $probe) {
            Throw-GatePathIdentityError "$Label has no existing ancestor: $fullPath"
        }
        $probe = $parent
        try {
            $existing = [WinterGate.Native]::TryGetPathIdentity(
                $probe,
                [WinterGate.PathKind]::Directory,
                $true
            )
        }
        catch {
            $unwrapped = Get-UnwrappedException $_.Exception
            if ($unwrapped -is [WinterGate.WinterGatePathIdentityException]) {
                throw $unwrapped
            }
            Throw-GatePathIdentityError "$Label ancestor could not be inspected" $unwrapped
        }
    }

    $projected = $existing.FinalPath
    foreach ($component in $missing) {
        $projected = [System.IO.Path]::Combine($projected, $component)
    }
    return [pscustomobject][ordered]@{
        ExistingIdentity = $existing
        MissingComponents = [string[]]$missing.ToArray()
        FinalPath = $projected
        VolumeSerialNumber = $existing.VolumeSerialNumber
    }
}

function Resolve-GateProject {
    [CmdletBinding()]
    param(
        [AllowNull()]
        [string]$ProjectRoot,
        [bool]$WasSpecified
    )

    if ($WasSpecified -and [string]::IsNullOrWhiteSpace($ProjectRoot)) {
        Throw-GatePathIdentityError 'ProjectRoot was supplied without a path'
    }
    if (-not $WasSpecified) {
        $ProjectRoot = [System.IO.Path]::GetFullPath(
            [System.IO.Path]::Combine($PSScriptRoot, '..')
        )
    }
    $normalized = Get-NormalizedAbsolutePlainPath $ProjectRoot 'ProjectRoot'
    try {
        return [WinterGate.Native]::GetPathIdentity(
            $normalized,
            [WinterGate.PathKind]::Directory,
            $true
        )
    }
    catch {
        $unwrapped = Get-UnwrappedException $_.Exception
        if ($unwrapped -is [WinterGate.WinterGatePathIdentityException]) {
            throw $unwrapped
        }
        Throw-GatePathIdentityError 'ProjectRoot could not be resolved' $unwrapped
    }
}

function Get-CurrentProtectedPlayerSaveRootInput {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [ValidateSet('KnownApplicationData', 'ProcessApplicationData')]
        [string]$SourceKind
    )

    if ($SourceKind -eq 'KnownApplicationData') {
        try {
            $path = [System.Environment]::GetFolderPath(
                [System.Environment+SpecialFolder]::ApplicationData
            )
        }
        catch {
            Throw-GatePathIdentityError `
                'Windows known ApplicationData folder could not be resolved' `
                $_.Exception
        }
        if ([string]::IsNullOrWhiteSpace($path)) {
            Throw-GatePathIdentityError `
                'Windows known ApplicationData folder is unavailable'
        }
        return [pscustomobject][ordered]@{
            Label = 'Windows known ApplicationData folder'
            Path = $path
        }
    }

    if ([string]::IsNullOrWhiteSpace($env:APPDATA)) {
        Throw-GatePathIdentityError 'process APPDATA folder is unavailable'
    }
    return [pscustomobject][ordered]@{
        Label = 'process APPDATA folder'
        Path = $env:APPDATA
    }
}

function Get-ProtectedPlayerSaveRoots {
    [CmdletBinding()]
    param()

    $sourceKinds = [string[]]@(
        'KnownApplicationData',
        'ProcessApplicationData'
    )
    $roots = New-Object 'System.Collections.Generic.List[object]'
    foreach ($sourceKind in $sourceKinds) {
        $inputRoot = Get-CurrentProtectedPlayerSaveRootInput $sourceKind
        $normalized = Get-NormalizedAbsolutePlainPath `
            $inputRoot.Path `
            $inputRoot.Label
        try {
            $identity = [WinterGate.Native]::GetPathIdentity(
                $normalized,
                [WinterGate.PathKind]::Directory,
                $true
            )
        }
        catch {
            $unwrapped = Get-UnwrappedException $_.Exception
            if ($inputRoot.Label -eq 'Windows known ApplicationData folder') {
                Throw-GatePathIdentityError `
                    'Windows known ApplicationData folder could not be resolved' `
                    $unwrapped
            }
            Throw-GatePathIdentityError `
                'process APPDATA folder could not be resolved' `
                $unwrapped
        }
        [void]$roots.Add([pscustomobject][ordered]@{
            SourceKind = $sourceKind
            ConfiguredPath = $normalized
            Identity = $identity
        })
    }
    return [object[]]$roots.ToArray()
}

function Assert-ProtectedPlayerSaveState {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [AllowEmptyCollection()]
        [object[]]$ProtectedRoots,
        [Parameter(Mandatory = $true, Position = 1)]
        [object]$RunLocation
    )

    if ($ProtectedRoots.Count -ne 2) {
        Throw-GatePathIdentityError `
            'protected player-save roots are incomplete'
    }
    foreach ($root in $ProtectedRoots) {
        $inputRoot = Get-CurrentProtectedPlayerSaveRootInput $root.SourceKind
        $normalized = Get-NormalizedAbsolutePlainPath `
            $inputRoot.Path `
            $inputRoot.Label
        if (-not [string]::Equals(
            $normalized,
            [string]$root.ConfiguredPath,
            [System.StringComparison]::OrdinalIgnoreCase)) {
            Throw-GatePathIdentityError `
                "$($inputRoot.Label) path changed after validation"
        }
        try {
            $currentIdentity = [WinterGate.Native]::GetPathIdentity(
                $normalized,
                [WinterGate.PathKind]::Directory,
                $true
            )
        }
        catch {
            $unwrapped = Get-UnwrappedException $_.Exception
            if ($unwrapped -is [WinterGate.WinterGatePathIdentityException]) {
                throw $unwrapped
            }
            Throw-GatePathIdentityError `
                "$($inputRoot.Label) could not be revalidated" `
                $unwrapped
        }
        if (-not [WinterGate.Native]::SameStablePath(
            $root.Identity,
            $currentIdentity)) {
            Throw-GatePathIdentityError `
                "$($inputRoot.Label) changed after validation"
        }
        $protectedPath = [System.IO.Path]::Combine(
            $currentIdentity.FinalPath,
            'RenPy',
            'CourtOfShadows-save'
        )
        $savePlan = Get-ProspectiveDirectoryPlan `
            $protectedPath `
            'protected player-save root'
        if (Test-SameOrChildFinalPath $RunLocation $savePlan) {
            Throw-GatePathIdentityError `
                'RunRoot must be outside the player-save root'
        }
    }
}

function New-VerifiedChildDirectory {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [WinterGate.PathIdentity]$ParentIdentity,
        [Parameter(Mandatory = $true, Position = 1)]
        [string]$LeafName
    )

    Assert-PlainChildName $LeafName 'child directory name'
    $parentBefore = Assert-GatePathState $ParentIdentity 'parent directory'
    $childPath = [System.IO.Path]::Combine(
        $parentBefore.FinalPath,
        $LeafName
    )
    try {
        $existing = [WinterGate.Native]::TryGetPathIdentity(
            $childPath,
            [WinterGate.PathKind]::Directory,
            $true
        )
        if ($null -ne $existing) {
            Throw-GatePathIdentityError "child directory appeared concurrently: $childPath"
        }
        [WinterGate.Native]::CreateDirectoryExclusive(
            $childPath,
            $parentBefore
        )
        $parentAfter = Assert-GatePathState $ParentIdentity 'parent directory'
        $child = [WinterGate.Native]::GetPathIdentity(
            $childPath,
            [WinterGate.PathKind]::Directory,
            $true
        )
    }
    catch {
        $unwrapped = Get-UnwrappedException $_.Exception
        if ($unwrapped -is [WinterGate.WinterGatePathIdentityException]) {
            throw $unwrapped
        }
        Throw-GatePathIdentityError "child directory could not be created: $childPath" $unwrapped
    }

    $resolvedParentPath = [System.IO.Path]::GetDirectoryName($child.FinalPath)
    if ($child.VolumeSerialNumber -ne $parentAfter.VolumeSerialNumber -or
        -not [string]::Equals(
            $resolvedParentPath,
            $parentAfter.FinalPath,
            [System.StringComparison]::OrdinalIgnoreCase)) {
        Throw-GatePathIdentityError "child escaped its verified parent: $childPath"
    }
    return $child
}

function New-VerifiedRunRoot {
    [CmdletBinding()]
    param(
        [AllowNull()]
        [string]$Candidate,
        [Parameter(Mandatory = $true)]
        [bool]$CandidateWasSpecified,
        [Parameter(Mandatory = $true)]
        [WinterGate.PathIdentity]$ProjectIdentity,
        [AllowEmptyCollection()]
        [object[]]$ProtectedSaveRoots = @()
    )

    $verifiedProject = Assert-GatePathState $ProjectIdentity 'ProjectRoot'
    if ($CandidateWasSpecified -and [string]::IsNullOrWhiteSpace($Candidate)) {
        Throw-GatePathIdentityError 'RunRoot was supplied without a path'
    }
    if (-not $CandidateWasSpecified) {
        $Candidate = [System.IO.Path]::Combine(
            [System.IO.Path]::GetTempPath(),
            [System.Guid]::NewGuid().ToString('N').ToLowerInvariant()
        )
    }

    $runPlan = Get-ProspectiveDirectoryPlan $Candidate 'RunRoot' -RequireMissing
    if (Test-SameOrChildFinalPath $runPlan $verifiedProject) {
        Throw-GatePathIdentityError 'RunRoot must be outside ProjectRoot'
    }

    Assert-ProtectedPlayerSaveState $ProtectedSaveRoots $runPlan

    $current = $runPlan.ExistingIdentity
    foreach ($component in $runPlan.MissingComponents) {
        Assert-ProtectedPlayerSaveState $ProtectedSaveRoots $runPlan
        $current = New-VerifiedChildDirectory $current $component
        Assert-ProtectedPlayerSaveState $ProtectedSaveRoots $runPlan
    }
    $runIdentity = $current
    if ($runIdentity.VolumeSerialNumber -ne $runPlan.VolumeSerialNumber -or
        -not [string]::Equals(
            $runIdentity.FinalPath,
            $runPlan.FinalPath,
            [System.StringComparison]::OrdinalIgnoreCase)) {
        Throw-GatePathIdentityError 'RunRoot resolved somewhere other than its planned final path'
    }

    $verifiedProject = Assert-GatePathState $ProjectIdentity 'ProjectRoot'
    if (Test-SameOrChildFinalPath $runIdentity $verifiedProject) {
        Throw-GatePathIdentityError 'created RunRoot is inside ProjectRoot'
    }
    Assert-ProtectedPlayerSaveState $ProtectedSaveRoots $runIdentity

    $evidenceIdentity = New-VerifiedChildDirectory $runIdentity 'evidence'
    Assert-ProtectedPlayerSaveState $ProtectedSaveRoots $runIdentity
    $runIdentity = Assert-GatePathState $runIdentity 'RunRoot'
    Assert-ProtectedPlayerSaveState $ProtectedSaveRoots $runIdentity
    $savedirsIdentity = New-VerifiedChildDirectory $runIdentity 'savedirs'
    Assert-ProtectedPlayerSaveState $ProtectedSaveRoots $runIdentity
    $runIdentity = Assert-GatePathState $runIdentity 'RunRoot'
    [void](Assert-GatePathState $evidenceIdentity 'evidence directory')
    [void](Assert-GatePathState $savedirsIdentity 'savedirs directory')
    Assert-ProtectedPlayerSaveState $ProtectedSaveRoots $runIdentity

    return [pscustomobject][ordered]@{
        Identity = $runIdentity
        EvidenceIdentity = $evidenceIdentity
        SavedirsIdentity = $savedirsIdentity
    }
}

function New-VerifiedGateChildDirectory {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [WinterGate.PathIdentity]$ParentIdentity,
        [Parameter(Mandatory = $true, Position = 1)]
        [string]$LeafName
    )

    Assert-ProtectedPlayerSaveState `
        $script:ProtectedSaveRoots `
        $script:RunRootIdentity
    $child = New-VerifiedChildDirectory $ParentIdentity $LeafName
    Assert-ProtectedPlayerSaveState `
        $script:ProtectedSaveRoots `
        $script:RunRootIdentity
    return $child
}

# BEGIN LOOP 3.3-P1 HOST AND PROJECT FILE HELPERS
function Resolve-PythonExecutable {
    $command = Get-Command python.exe -CommandType Application -ErrorAction Stop |
        Select-Object -First 1
    if ($null -eq $command -or [string]::IsNullOrWhiteSpace($command.Source)) {
        throw 'python.exe did not resolve to an application.'
    }
    [WinterGate.Native]::GetReadableFileIdentity(
        [IO.Path]::GetFullPath($command.Source))
}

function Get-ExpectedProjectFilePath {
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [string]$ResolvedProjectRoot,
        [Parameter(Mandatory = $true, Position = 1)]
        [string]$RelativePath
    )
    if ([string]::IsNullOrWhiteSpace($RelativePath) -or
        [IO.Path]::IsPathRooted($RelativePath) -or
        $RelativePath.StartsWith('\\?\') -or
        $RelativePath.StartsWith('\\.\') -or
        $RelativePath.IndexOfAny([IO.Path]::GetInvalidPathChars()) -ge 0 -or
        [Management.Automation.WildcardPattern]::ContainsWildcardCharacters(
            $RelativePath)) {
        throw "Invalid fixed project-relative path: $RelativePath"
    }
    foreach ($component in $RelativePath.Split(@('\', '/'))) {
        if ([string]::IsNullOrWhiteSpace($component) -or
            $component -eq '.' -or $component -eq '..') {
            throw "Invalid fixed project-relative component: $RelativePath"
        }
    }
    $candidate = [IO.Path]::GetFullPath(
        [IO.Path]::Combine($ResolvedProjectRoot, $RelativePath))
    $prefix = $ResolvedProjectRoot.TrimEnd('\') + '\'
    if (-not $candidate.StartsWith(
        $prefix, [StringComparison]::OrdinalIgnoreCase)) {
        throw "Fixed project path escaped ProjectRoot: $RelativePath"
    }
    $candidate
}

# END LOOP 3.3-P1 HOST AND PROJECT FILE HELPERS

# BEGIN LOOP 3.4-P1 FINAL GIT IDENTITY LAYER
function Remove-GitTerminalNewline {
    param(
        [Parameter(Mandatory = $true)][string]$Text,
        [Parameter(Mandatory = $true)][string]$Label
    )
    $value = if ($Text.EndsWith("`r`n", [StringComparison]::Ordinal)) {
        $Text.Substring(0, $Text.Length - 2)
    } elseif ($Text.EndsWith("`n", [StringComparison]::Ordinal)) {
        $Text.Substring(0, $Text.Length - 1)
    } else { $Text }
    if ($value.IndexOf("`r") -ge 0 -or $value.IndexOf("`n") -ge 0 -or
        [string]::IsNullOrWhiteSpace($value)) {
        throw "$Label must contain exactly one non-empty line."
    }
    $value
}

function Read-VerifiedGateText {
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [Parameter(Mandatory = $true)]$Identity,
        [Parameter(Mandatory = $true)][int]$MaximumBytes
    )
    [WinterGate.Native]::ReadVerifiedUtf8TextFile(
        [IO.Path]::GetFullPath($Path),
        $Identity,
        $MaximumBytes)
}

function Resolve-GitMetadataPath {
    param(
        [Parameter(Mandatory = $true)][string]$BaseDirectory,
        [Parameter(Mandatory = $true)][string]$Value,
        [Parameter(Mandatory = $true)][string]$Label
    )
    if ([string]::IsNullOrWhiteSpace($Value) -or
        $Value.StartsWith('\\?\') -or
        $Value.StartsWith('\\.\')) {
        throw "$Label contains an unsafe path."
    }
    if ([IO.Path]::IsPathRooted($Value)) {
        $driveAbsolute = $Value -match '^[A-Za-z]:[\\/]'
        $uncAbsolute = $Value -match '^\\\\[^\\/]+[\\/][^\\/]+[\\/]'
        if (-not $driveAbsolute -and -not $uncAbsolute) {
            throw "$Label must not use a drive-relative or root-relative path."
        }
        return [IO.Path]::GetFullPath($Value)
    }
    [IO.Path]::GetFullPath([IO.Path]::Combine($BaseDirectory, $Value))
}

function Resolve-GitMetadataDirectory {
    $dotGitPath = [IO.Path]::Combine(
        $script:ProjectIdentity.FinalPath,
        '.git')
    try {
        $attributes = [IO.File]::GetAttributes($dotGitPath)
    }
    catch [IO.FileNotFoundException] { return $null }
    catch [IO.DirectoryNotFoundException] { return $null }
    if (($attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
        throw 'Project .git metadata entry must not be a reparse point.'
    }

    $metadataFiles = New-Object 'System.Collections.Generic.List[object]'
    if (($attributes -band [IO.FileAttributes]::Directory) -ne 0) {
        $gitDirectoryIdentity = [WinterGate.Native]::GetPathIdentity(
            $dotGitPath,
            [WinterGate.PathKind]::Directory,
            $true)
    } else {
        $gitFileIdentity = [WinterGate.Native]::GetReadableFileIdentity(
            $dotGitPath)
        [void]$metadataFiles.Add($gitFileIdentity)
        $gitFileText = Read-VerifiedGateText -Path $dotGitPath -Identity $gitFileIdentity -MaximumBytes 65536
        $gitFileLine = Remove-GitTerminalNewline -Text $gitFileText -Label 'Project .git file'
        if ($gitFileLine -cnotmatch '^gitdir: (.+)$') {
            throw 'Project .git file has an invalid gitdir record.'
        }
        $gitDirectoryPath = Resolve-GitMetadataPath -BaseDirectory ([IO.Path]::GetDirectoryName($dotGitPath)) -Value $Matches[1] -Label 'Project .git gitdir'
        $gitDirectoryIdentity = [WinterGate.Native]::GetPathIdentity(
            $gitDirectoryPath,
            [WinterGate.PathKind]::Directory,
            $true)
    }

    $commonDirectoryIdentity = $gitDirectoryIdentity
    $commonFilePath = [IO.Path]::Combine(
        $gitDirectoryIdentity.FinalPath,
        'commondir')
    $commonFileIdentity =
        [WinterGate.Native]::TryGetReadableFileIdentity($commonFilePath)
    if ($null -ne $commonFileIdentity) {
        [void]$metadataFiles.Add($commonFileIdentity)
        $commonText = Read-VerifiedGateText -Path $commonFilePath -Identity $commonFileIdentity -MaximumBytes 65536
        $commonLine = Remove-GitTerminalNewline -Text $commonText -Label 'Git commondir file'
        $commonPath = Resolve-GitMetadataPath -BaseDirectory $gitDirectoryIdentity.FinalPath -Value $commonLine -Label 'Git commondir'
        $commonDirectoryIdentity = [WinterGate.Native]::GetPathIdentity(
            $commonPath,
            [WinterGate.PathKind]::Directory,
            $true)
    }
    [pscustomobject][ordered]@{
        GitDirectoryIdentity = $gitDirectoryIdentity
        CommonDirectoryIdentity = $commonDirectoryIdentity
        MetadataFileIdentities = [object[]]$metadataFiles.ToArray()
    }
}

function Get-SafeGitReferencePath {
    param(
        [Parameter(Mandatory = $true)][string]$GitDirectory,
        [Parameter(Mandatory = $true)][string]$ReferenceName
    )
    if ($ReferenceName -cnotmatch '^refs/[A-Za-z0-9][A-Za-z0-9._/-]*$' -or
        $ReferenceName.Contains('//') -or
        $ReferenceName.Contains('..') -or
        $ReferenceName.Contains('@{') -or
        $ReferenceName.EndsWith('/') -or
        $ReferenceName.EndsWith('.') -or
        $ReferenceName.EndsWith('.lock', [StringComparison]::OrdinalIgnoreCase)) {
        throw "Git HEAD contains an unsafe reference: $ReferenceName"
    }
    $relative = $ReferenceName.Replace('/', '\')
    $candidate = [IO.Path]::GetFullPath(
        [IO.Path]::Combine($GitDirectory, $relative))
    $prefix = $GitDirectory.TrimEnd('\') + '\'
    if (-not $candidate.StartsWith(
        $prefix,
        [StringComparison]::OrdinalIgnoreCase)) {
        throw "Git reference escaped its metadata directory: $ReferenceName"
    }
    $candidate
}

function ConvertTo-GitObjectId {
    param(
        [Parameter(Mandatory = $true)][string]$Text,
        [Parameter(Mandatory = $true)][string]$Label
    )
    $value = Remove-GitTerminalNewline -Text $Text -Label $Label
    if ($value -cnotmatch '^[0-9a-f]{40}([0-9a-f]{24})?$') {
        throw "$Label is not a lowercase Git object id."
    }
    $value
}

function Test-GitPerWorktreeReference {
    param([Parameter(Mandatory = $true)][string]$ReferenceName)
    $ReferenceName.StartsWith('refs/bisect/', [StringComparison]::Ordinal) -or
        $ReferenceName.StartsWith('refs/rewritten/', [StringComparison]::Ordinal) -or
        $ReferenceName.StartsWith('refs/worktree/', [StringComparison]::Ordinal)
}

function Read-GitLooseReference {
    param(
        [Parameter(Mandatory = $true)]$Metadata,
        [Parameter(Mandatory = $true)][string]$ReferenceName
    )
    $perWorktree = Test-GitPerWorktreeReference $ReferenceName
    $directory = if ($perWorktree) {
        $Metadata.GitDirectoryIdentity.FinalPath
    } else {
        $Metadata.CommonDirectoryIdentity.FinalPath
    }
    $path = Get-SafeGitReferencePath $directory $ReferenceName
    $identity = [WinterGate.Native]::TryGetReadableFileIdentity($path)
    if ($null -ne $identity) {
        $text = Read-VerifiedGateText -Path $path -Identity $identity -MaximumBytes 65536
        return [pscustomobject][ordered]@{
            Commit = ConvertTo-GitObjectId -Text $text -Label "Git loose reference '$ReferenceName'"
            Identity = $identity
        }
    }
    $null
}

function Read-GitPackedReference {
    param(
        [Parameter(Mandatory = $true)]$Metadata,
        [Parameter(Mandatory = $true)][string]$ReferenceName
    )
    $path = [IO.Path]::Combine(
        $Metadata.CommonDirectoryIdentity.FinalPath,
        'packed-refs')
    $identity = [WinterGate.Native]::TryGetReadableFileIdentity($path)
    if ($null -eq $identity) { return $null }
    $text = Read-VerifiedGateText `
        -Path $path -Identity $identity -MaximumBytes 4194304
    $matchedObject = $null
    foreach ($line in ($text -split "`r?`n")) {
        if ([string]::IsNullOrEmpty($line) -or $line.StartsWith('#')) {
            continue
        }
        if ($line -cmatch '^\^[0-9a-f]{40}([0-9a-f]{24})?$') {
            continue
        }
        if ($line -cnotmatch '^([0-9a-f]{40}([0-9a-f]{24})?) (refs/.+)$') {
            throw 'Git packed-refs contains a malformed record.'
        }
        if ($Matches[3] -ceq $ReferenceName) {
            if ($null -ne $matchedObject) {
                throw "Git packed-refs duplicates '$ReferenceName'."
            }
            $matchedObject = $Matches[1]
        }
    }
    if ($null -eq $matchedObject) { return $null }
    [pscustomobject][ordered]@{
        Commit = $matchedObject
        Identity = $identity
    }
}

function Get-ProjectHeadState {
    $metadata = Resolve-GitMetadataDirectory
    if ($null -eq $metadata) {
        return [pscustomobject][ordered]@{
            Commit = $null
            Metadata = $null
            DirectoryIdentities = [object[]]@()
            FileIdentities = [object[]]@()
        }
    }
    $headPath = [IO.Path]::Combine(
        $metadata.GitDirectoryIdentity.FinalPath,
        'HEAD')
    $headIdentity = [WinterGate.Native]::GetReadableFileIdentity($headPath)
    $headText = Read-VerifiedGateText -Path $headPath -Identity $headIdentity -MaximumBytes 65536
    $headLine = Remove-GitTerminalNewline -Text $headText -Label 'Git HEAD'
    if ($headLine -cmatch '^ref: (refs/.+)$') {
        $reference = $Matches[1]
        [void](Get-SafeGitReferencePath $metadata.GitDirectoryIdentity.FinalPath $reference)
        $resolvedReference = Read-GitLooseReference $metadata $reference
        if ($null -eq $resolvedReference -and
            -not (Test-GitPerWorktreeReference $reference)) {
            $resolvedReference = Read-GitPackedReference $metadata $reference
        }
        if ($null -eq $resolvedReference) {
            throw "Git HEAD reference has no current commit: $reference"
        }
        $commit = $resolvedReference.Commit
        $referenceIdentity = $resolvedReference.Identity
    } else {
        $commit = ConvertTo-GitObjectId -Text $headLine -Label 'Git HEAD'
        $referenceIdentity = $null
    }
    $directoryIdentities = @($metadata.GitDirectoryIdentity)
    if (-not [WinterGate.Native]::SameStablePath(
        $metadata.GitDirectoryIdentity,
        $metadata.CommonDirectoryIdentity)) {
        $directoryIdentities += $metadata.CommonDirectoryIdentity
    }
    $fileIdentities = @($metadata.MetadataFileIdentities) + @($headIdentity)
    if ($null -ne $referenceIdentity) {
        $fileIdentities += $referenceIdentity
    }

    [pscustomobject][ordered]@{
        Commit = $commit
        Metadata = $metadata
        DirectoryIdentities = [object[]]$directoryIdentities
        FileIdentities = [object[]]$fileIdentities
    }
}

function Assert-GitCommitOverride {
    param($Commit)
    $environment = [Environment]::GetEnvironmentVariables()
    if (-not $environment.Contains('GIT_COMMIT')) { return }
    $override = [string]$environment['GIT_COMMIT']
    if ($null -eq $Commit) {
        throw 'GIT_COMMIT was supplied but ProjectRoot is not a Git worktree.'
    }
    if ($override -cnotmatch '^[0-9a-f]{40}([0-9a-f]{24})?$' -or
        $override -cne $Commit) {
        throw 'GIT_COMMIT does not exactly match the current ProjectRoot HEAD.'
    }
}

function Assert-ProjectHeadCommit {
    if (-not $script:HeadTrackingInitialized) { return }
    $current = Get-ProjectHeadState
    if (($null -eq $script:HeadCommit) -ne ($null -eq $current.Commit) -or
        ($null -ne $script:HeadCommit -and
         $script:HeadCommit -cne $current.Commit)) {
        throw 'ProjectRoot Git HEAD changed during the gate run.'
    }
    if ($script:HeadState.DirectoryIdentities.Count -ne
            $current.DirectoryIdentities.Count -or
        $script:HeadState.FileIdentities.Count -ne
            $current.FileIdentities.Count) {
        throw 'ProjectRoot Git metadata identity set changed during the gate run.'
    }
    for ($index = 0;
         $index -lt $script:HeadState.DirectoryIdentities.Count;
         $index++) {
        if (-not [WinterGate.Native]::SameStablePath(
            $script:HeadState.DirectoryIdentities[$index],
            $current.DirectoryIdentities[$index])) {
            throw 'ProjectRoot Git directory identity changed during the gate run.'
        }
    }
    for ($index = 0;
         $index -lt $script:HeadState.FileIdentities.Count;
         $index++) {
        if (-not [WinterGate.Native]::SameStablePath(
            $script:HeadState.FileIdentities[$index],
            $current.FileIdentities[$index])) {
            throw 'ProjectRoot Git file identity changed during the gate run.'
        }
    }
    Assert-GitCommitOverride -Commit $current.Commit
}

# END LOOP 3.4-P1 FINAL GIT IDENTITY LAYER


# BEGIN LOOP 3.3-P2 STEP AND PROVISIONAL MANIFEST BUILDERS
function New-GateStep {
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [ValidatePattern('^[a-z0-9][a-z0-9-]*$')]
        [string]$Name,
        [Parameter(Mandatory = $true, Position = 1)]
        [ValidateSet('Python', 'RenPySuite')]
        [string]$Kind,
        [Parameter(Mandatory = $true, Position = 2)]
        [string]$Executable,
        [Parameter(Mandatory = $true, Position = 3)]
        [AllowEmptyCollection()]
        [string[]]$Arguments,
        [Parameter(Mandatory = $true, Position = 4)]
        [ValidateRange(1, 1860)]
        [int]$TimeoutSeconds,
        [Parameter(Mandatory = $true, Position = 5)]
        [ValidateSet(
            'exit-zero', 'runner-passed', 'capability-json', 'canon-json',
            'manual-review', 'portrait-json', 'overlap-json',
            'show-before-json', 'nested-quote-json'
        )]
        [string]$Postcondition,
        [Parameter(Position = 6)]
        [string[]]$RequiredFiles = @()
    )
    if (-not [IO.Path]::IsPathRooted($Executable)) {
        throw "Step '$Name' executable must be absolute."
    }
    foreach ($argument in $Arguments) {
        if ($null -eq $argument) {
            throw "Step '$Name' has a null process argument."
        }
    }
    foreach ($required in $RequiredFiles) {
        if (-not [IO.Path]::IsPathRooted($required)) {
            throw "Step '$Name' required file must be absolute: $required"
        }
    }
    $dependencyLease = $null
    $leaseRegistered = $false
    try {
        $dependencyLease = [WinterGate.Native]::AcquireStepDependencyLease(
            $Executable,
            [string[]]$RequiredFiles.Clone())
        [void]$script:StepDependencyLeases.Add($dependencyLease)
        $leaseRegistered = $true
        [pscustomobject][ordered]@{
            Name = $Name
            Kind = $Kind
            Executable = $dependencyLease.ExecutablePath
            DependencyLease = $dependencyLease
            Arguments = [string[]]$Arguments.Clone()
            TimeoutSeconds = $TimeoutSeconds
            Postcondition = $Postcondition
            RequiredFiles = [string[]]$RequiredFiles.Clone()
        }
    }
    catch [WinterGate.WinterGatePathIdentityException] {
        throw [InvalidOperationException]::new(
            ("Manifest dependency is unsafe for step '$Name'. " +
             $_.Exception.Message),
            $_.Exception)
    }
    finally {
        if ($null -ne $dependencyLease -and -not $leaseRegistered) {
            $dependencyLease.Dispose()
        }
    }
}

function Get-StructuralGateManifest {
    $sourceContract = Get-ExpectedProjectFilePath `
        $script:ProjectIdentity.FinalPath 'Tools\test_governance_winter_interlude.py'
    $runner = Get-ExpectedProjectFilePath `
        $script:ProjectIdentity.FinalPath 'Tools\Run-RenPySuite.ps1'
    $runnerEvidenceIdentity = New-VerifiedGateChildDirectory `
        -ParentIdentity $script:EvidenceIdentity -LeafName 'runner'
    [void]$script:GateDirectoryIdentities.Add($runnerEvidenceIdentity)

    $steps = New-Object 'System.Collections.Generic.List[object]'
    [void]$steps.Add((New-GateStep `
        'source-contract' 'Python' $script:PythonIdentity.FinalPath `
        ([string[]]@('-m', 'unittest', 'Tools.test_governance_winter_interlude', '-v')) `
        $ToolTimeoutSeconds 'exit-zero' ([string[]]@($sourceContract))))

    $suites = [string[]]@(
        'test_winter_interlude_state',
        'test_winter_interlude_routing',
        'test_winter_interlude_ending_invariance',
        'test_winter_interlude_route_matrix',
        'test_winter_interlude_mid_save'
    )
    for ($index = 0; $index -lt $suites.Count; $index++) {
        $ordinal = $index + 2
        $suite = $suites[$index]
        $saveIdentity = New-VerifiedGateChildDirectory `
            -ParentIdentity $script:SavedirsIdentity `
            -LeafName ('{0:D2}-{1}' -f $ordinal, $suite)
        [void]$script:GateDirectoryIdentities.Add($saveIdentity)
        $arguments = [string[]]@(
            '-NoLogo', '-NoProfile', '-NonInteractive',
            '-ExecutionPolicy', 'Bypass', '-File', $runner,
            '-ProjectRoot', $script:ProjectIdentity.FinalPath,
            '-SaveDir', $saveIdentity.FinalPath,
            '-Mode', 'Suite', '-Suite', $suite,
            '-Expect', 'PASSED',
            '-EvidenceDir', $runnerEvidenceIdentity.FinalPath,
            '-TimeoutSeconds', [string]$RenPyTimeoutSeconds
        )
        [void]$steps.Add((New-GateStep `
            $suite.Replace('_', '-') 'RenPySuite' `
            $script:TrustedPowerShellIdentity.FinalPath $arguments `
            ($RenPyTimeoutSeconds + 60) 'runner-passed' `
            ([string[]]@($runner))))
    }
    [object[]]$steps.ToArray()
}

function Get-GateArtifactStem {
    param(
        [Parameter(Mandatory = $true)][int]$Ordinal,
        [Parameter(Mandatory = $true)][string]$StepName
    )
    '{0}-{1:D2}-{2}-{3}' -f `
        $Gate.ToLowerInvariant(), $Ordinal, $StepName, $script:HeadToken
}

function Get-GateStructuredOutputPath {
    param(
        [Parameter(Mandatory = $true)]$Step,
        [Parameter(Mandatory = $true)][int]$Ordinal
    )
    if ($Step.Postcondition -notin @(
        'capability-json',
        'canon-json',
        'portrait-json',
        'overlap-json',
        'show-before-json',
        'nested-quote-json'
    )) {
        return $null
    }
    $leaf = "$(Get-GateArtifactStem -Ordinal $Ordinal -StepName $Step.Name).output.json"
    if ($Step.Postcondition -eq 'portrait-json') {
        return Join-Path `
            (Join-Path $script:EvidenceIdentity.FinalPath 'portrait') `
            $leaf
    }
    Join-Path $script:EvidenceIdentity.FinalPath $leaf
}

function Get-GateStructuredOutputDirectoryIdentity {
    param([Parameter(Mandatory = $true)][string]$Path)

    $fullPath = [IO.Path]::GetFullPath($Path)
    $parentPath = [IO.Path]::GetFullPath(
        [IO.Path]::GetDirectoryName($fullPath)).TrimEnd('\')
    $matches = New-Object 'System.Collections.Generic.List[object]'
    foreach ($identity in $script:GateDirectoryIdentities) {
        $registeredPath = [IO.Path]::GetFullPath(
            $identity.FinalPath).TrimEnd('\')
        if ([string]::Equals(
            $parentPath,
            $registeredPath,
            [StringComparison]::OrdinalIgnoreCase)) {
            [void]$matches.Add($identity)
        }
    }
    if ($matches.Count -ne 1) {
        throw [FormatException]::new(
            'Structured output must have exactly one registered direct parent.')
    }
    $matches[0]
}

function Get-NarrativeGateManifest {
    $project = $script:ProjectIdentity.FinalPath
    $phase = if ($NarrativePhase -eq 'Batch') { 'batch' } else { 'final' }
    $checker = Get-ExpectedProjectFilePath `
        $project 'Tools\check_winter_narrative_capabilities.py'
    $canon = Get-ExpectedProjectFilePath $project 'Tools\scan_canon.py'
    $aiSmell = Get-ExpectedProjectFilePath $project 'Tools\scan_ai_smell.py'
    $portrait = Get-ExpectedProjectFilePath $project 'scan_missing_portraits.py'
    $overlap = Get-ExpectedProjectFilePath `
        $project 'scan_narration_overlap.py'
    $showBefore = Get-ExpectedProjectFilePath `
        $project 'Tools\scan_show_before_prevention.py'
    $nestedQuotes = Get-ExpectedProjectFilePath `
        $project 'Tools\scan_nested_quotes.py'
    $sourceContract = Get-ExpectedProjectFilePath `
        $project 'Tools\test_governance_winter_interlude.py'
    $runner = Get-ExpectedProjectFilePath `
        $project 'Tools\Run-RenPySuite.ps1'
    $target = Get-ExpectedProjectFilePath `
        $project 'game\governance_winter_interlude.rpy'

    $portraitIdentity = New-VerifiedGateChildDirectory `
        -ParentIdentity $script:EvidenceIdentity `
        -LeafName 'portrait'
    $runnerEvidenceIdentity = New-VerifiedGateChildDirectory `
        -ParentIdentity $script:EvidenceIdentity `
        -LeafName 'runner'
    $routeSaveIdentity = New-VerifiedGateChildDirectory `
        -ParentIdentity $script:SavedirsIdentity `
        -LeafName '09-test_winter_interlude_route_matrix'
    [void]$script:GateDirectoryIdentities.Add($portraitIdentity)
    [void]$script:GateDirectoryIdentities.Add($runnerEvidenceIdentity)
    [void]$script:GateDirectoryIdentities.Add($routeSaveIdentity)

    $capabilityJson = Join-Path `
        $script:EvidenceIdentity.FinalPath `
        ("$(Get-GateArtifactStem 1 'narrative-capability').output.json")
    $canonJson = Join-Path `
        $script:EvidenceIdentity.FinalPath `
        ("$(Get-GateArtifactStem 2 'canon').output.json")
    $portraitJson = Join-Path `
        $portraitIdentity.FinalPath `
        ("$(Get-GateArtifactStem 4 'missing-portraits').output.json")
    $overlapJson = Join-Path `
        $script:EvidenceIdentity.FinalPath `
        ("$(Get-GateArtifactStem 5 'narration-overlap').output.json")
    $showBeforeJson = Join-Path `
        $script:EvidenceIdentity.FinalPath `
        ("$(Get-GateArtifactStem 6 'show-before').output.json")
    $nestedQuoteJson = Join-Path `
        $script:EvidenceIdentity.FinalPath `
        ("$(Get-GateArtifactStem 7 'nested-quotes').output.json")

    [object[]]@(
        (New-GateStep 'narrative-capability' 'Python' `
            $script:PythonIdentity.FinalPath `
            ([string[]]@(
                '-B', $checker,
                '--phase', $phase,
                '--format', 'json',
                '--output', $capabilityJson
            )) $ToolTimeoutSeconds 'capability-json' `
            ([string[]]@($checker))),
        (New-GateStep 'canon' 'Python' `
            $script:PythonIdentity.FinalPath `
            ([string[]]@(
                '-B', $canon,
                '--format', 'json',
                '--output', $canonJson
            )) $ToolTimeoutSeconds 'canon-json' `
            ([string[]]@($canon))),
        (New-GateStep 'ai-smell' 'Python' `
            $script:PythonIdentity.FinalPath `
            ([string[]]@('-B', $aiSmell, $target)) `
            $ToolTimeoutSeconds 'manual-review' `
            ([string[]]@($aiSmell, $target))),
        (New-GateStep 'missing-portraits' 'Python' `
            $script:PythonIdentity.FinalPath `
            ([string[]]@(
                '-B', $portrait,
                '--file', $target,
                '--format', 'json',
                '--output', $portraitJson
            )) $ToolTimeoutSeconds 'portrait-json' `
            ([string[]]@($portrait, $target))),
        (New-GateStep 'narration-overlap' 'Python' `
            $script:PythonIdentity.FinalPath `
            ([string[]]@(
                '-B', $overlap,
                '--file', $target,
                '--format', 'json',
                '--output', $overlapJson
            )) $ToolTimeoutSeconds 'overlap-json' `
            ([string[]]@($overlap, $target))),
        (New-GateStep 'show-before' 'Python' `
            $script:PythonIdentity.FinalPath `
            ([string[]]@(
                '-B', $showBefore,
                '--file', $target,
                '--format', 'json',
                '--output', $showBeforeJson
            )) $ToolTimeoutSeconds 'show-before-json' `
            ([string[]]@($showBefore, $target))),
        (New-GateStep 'nested-quotes' 'Python' `
            $script:PythonIdentity.FinalPath `
            ([string[]]@(
                '-B', $nestedQuotes,
                '--file', $target,
                '--format', 'json',
                '--output', $nestedQuoteJson
            )) $ToolTimeoutSeconds 'nested-quote-json' `
            ([string[]]@($nestedQuotes, $target))),
        (New-GateStep 'source-contract' 'Python' `
            $script:PythonIdentity.FinalPath `
            ([string[]]@(
                '-m', 'unittest',
                'Tools.test_governance_winter_interlude', '-v'
            )) $ToolTimeoutSeconds 'exit-zero' `
            ([string[]]@($sourceContract))),
        (New-GateStep 'route-matrix' 'RenPySuite' `
            $script:TrustedPowerShellIdentity.FinalPath `
            ([string[]]@(
                '-NoLogo', '-NoProfile', '-NonInteractive',
                '-ExecutionPolicy', 'Bypass',
                '-File', $runner,
                '-ProjectRoot', $project,
                '-SaveDir', $routeSaveIdentity.FinalPath,
                '-Mode', 'Suite',
                '-Suite', 'test_winter_interlude_route_matrix',
                '-Expect', 'PASSED',
                '-EvidenceDir', $runnerEvidenceIdentity.FinalPath,
                '-TimeoutSeconds', [string]$RenPyTimeoutSeconds
            )) ($RenPyTimeoutSeconds + 60) 'runner-passed' `
            ([string[]]@($runner)))
    )
}

# END LOOP 3.3-P2 STEP AND PROVISIONAL MANIFEST BUILDERS
# BEGIN LOOP 3.4-P2 FINAL PROJECT AND DIRECTORY RECHECKS
function Assert-ProjectRootIdentity {
    Assert-GatePathState `
        -ExpectedIdentity $script:ProjectIdentity `
        -Label 'ProjectRoot' | Out-Null
}

function Assert-RunTreeDirectoryIdentities {
    foreach ($identity in @(
        $script:RunRootIdentity,
        $script:EvidenceIdentity,
        $script:SavedirsIdentity)) {
        Assert-GatePathState `
            -ExpectedIdentity $identity `
            -Label "base gate directory '$($identity.FinalPath)'" | Out-Null
    }
    Assert-ProtectedPlayerSaveState `
        $script:ProtectedSaveRoots `
        $script:RunRootIdentity
}

function Assert-AllGateDirectoryIdentities {
    Assert-ProjectRootIdentity
    foreach ($identity in $script:GateDirectoryIdentities) {
        Assert-GatePathState `
            -ExpectedIdentity $identity `
            -Label "registered gate directory '$($identity.FinalPath)'" |
            Out-Null
    }
    Assert-ProjectHeadCommit
    Assert-ProtectedPlayerSaveState `
        $script:ProtectedSaveRoots `
        $script:RunRootIdentity
}

function Assert-NonEvidenceGateDirectoryIdentities {
    Assert-ProjectRootIdentity
    foreach ($identity in $script:GateDirectoryIdentities) {
        if ([WinterGate.Native]::SameObject(
            $identity,
            $script:EvidenceIdentity)) {
            continue
        }
        Assert-GatePathState `
            -ExpectedIdentity $identity `
            -Label "registered pre-write gate directory '$($identity.FinalPath)'" |
            Out-Null
    }
    Assert-ProjectHeadCommit
    Assert-ProtectedPlayerSaveState `
        $script:ProtectedSaveRoots `
        $script:RunRootIdentity
}

# END LOOP 3.4-P2 FINAL PROJECT AND DIRECTORY RECHECKS


# BEGIN LOOP 3.3-P3 JSON BRIDGE AND VALIDATION RESULT
function Get-IdentityEvidenceObject {
    param([Parameter(Mandatory = $true)]$Identity)
    [pscustomobject][ordered]@{
        final_path = $Identity.FinalPath
        volume_serial_number = $Identity.VolumeSerialNumber
        file_index = $Identity.FileIndex
    }
}

function Write-GateEvidenceJson {
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [Parameter(Mandatory = $true)]$Value
    )
    Assert-NonEvidenceGateDirectoryIdentities
    $fullPath = [IO.Path]::GetFullPath($Path)
    $json = $Value | ConvertTo-Json -Depth 32
    [WinterGate.Native]::WriteUtf8JsonCreateNew(
        $fullPath,
        $json,
        $script:EvidenceIdentity)
    Assert-AllGateDirectoryIdentities
}

function Write-GateSummaryJson {
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [Parameter(Mandatory = $true)]$Value,
        [switch]$RunTreeOnly
    )
    if (-not $script:EvidencePublicationSafe) {
        throw 'A live process tree makes summary publication unsafe.'
    }
    if ($RunTreeOnly) {
        Assert-RunTreeDirectoryIdentities
    } else {
        Assert-AllGateDirectoryIdentities
    }
    $normalJson = $Value | ConvertTo-Json -Depth 32
    $collisionValue = $normalJson | ConvertFrom-Json
    $collisionError =
        'Unowned gate-summary.json was quarantined before gate-owned publication.'
    $collisionValue.status = 'failed'
    $collisionValue.failure_kind = 'validation'
    $collisionValue.error = $collisionError
    $script:SummaryPublicationAttempted = $true
    $script:QuarantinedSummaryPath =
        [WinterGate.Native]::WriteOwnedSummaryUtf8Json(
            [IO.Path]::GetFullPath($Path),
            $normalJson,
            ($collisionValue | ConvertTo-Json -Depth 32),
            $script:EvidenceIdentity)
    if ($null -ne $script:QuarantinedSummaryPath) {
        $Value.status = 'failed'
        $Value.failure_kind = 'validation'
        $Value.error = $collisionError
    }
    $script:SummaryCommittedByGate = $true
    if ($RunTreeOnly) {
        Assert-RunTreeDirectoryIdentities
    } else {
        Assert-AllGateDirectoryIdentities
    }
}

function Close-GateStructuredOutputReservations {
    $reservations = $script:StructuredOutputReservations
    if ($null -eq $reservations) {
        return
    }

    $script:StructuredOutputReservations = $null
    $firstError = $null
    for ($index = $reservations.Count - 1; $index -ge 0; $index--) {
        try {
            $reservations[$index].Dispose()
        }
        catch {
            if ($null -eq $firstError) {
                $firstError = $_
            }
        }
    }
    $reservations.Clear()
    if ($null -ne $firstError) {
        throw $firstError
    }
}

function Close-GateStepDependencyLeases {
    $leases = $script:StepDependencyLeases
    if ($null -eq $leases) {
        return
    }

    $script:StepDependencyLeases = $null
    $firstError = $null
    for ($index = $leases.Count - 1; $index -ge 0; $index--) {
        try {
            $leases[$index].Dispose()
        }
        catch {
            if ($null -eq $firstError) {
                $firstError = $_
            }
        }
    }
    $leases.Clear()
    if ($null -ne $firstError) {
        throw $firstError
    }
}

function New-ValidationGateResult {
    param(
        [Parameter(Mandatory = $true)]$Step,
        [Parameter(Mandatory = $true)][int]$Ordinal,
        [Parameter(Mandatory = $true)][string]$ResultRelative,
        [Parameter(Mandatory = $true)][string]$ErrorText
    )
    [pscustomobject][ordered]@{
        ordinal = $Ordinal
        name = $Step.Name
        kind = $Step.Kind
        executable = $Step.Executable
        arguments = [string[]]$Step.Arguments.Clone()
        working_directory = $script:ProjectIdentity.FinalPath
        process_started = $false
        process_id = $null
        started_utc = $null
        ended_utc = $null
        exit_code = $null
        timed_out = $false
        tree_drained = $true
        had_live_descendants_after_root_exit = $false
        elapsed_milliseconds = $null
        stdout = $null
        stderr = $null
        result = $ResultRelative
        postcondition = $Step.Postcondition
        manual_review_required = ($Step.Postcondition -eq 'manual-review')
        status = 'failed'
        failure_kind = 'validation'
        error = $ErrorText
    }
}

# END LOOP 3.3-P3 JSON BRIDGE AND VALIDATION RESULT
function Assert-ExactJsonProperties {
    param(
        [Parameter(Mandatory = $true)]$Object,
        [Parameter(Mandatory = $true)][string[]]$Expected,
        [Parameter(Mandatory = $true)][string]$Label
    )
    if ($null -eq $Object) {
        throw [FormatException]::new("$Label must be an object.")
    }
    $actual = [string[]]@($Object.PSObject.Properties.Name)
    if ($actual.Count -ne $Expected.Count) {
        throw [FormatException]::new("$Label has the wrong property count.")
    }
    foreach ($name in $Expected) {
        if (-not ($actual -ccontains $name)) {
            throw [FormatException]::new(
                "$Label is missing exact property '$name'.")
        }
    }
}

function Assert-JsonInteger {
    param(
        $Value,
        [Parameter(Mandatory = $true)][string]$Label,
        [switch]$Positive
    )
    if (-not ($Value -is [int] -or $Value -is [long])) {
        throw [FormatException]::new("$Label must be an integer.")
    }
    if ($Positive -and [long]$Value -le 0) {
        throw [FormatException]::new("$Label must be positive.")
    }
    if (-not $Positive -and [long]$Value -lt 0) {
        throw [FormatException]::new("$Label must be nonnegative.")
    }
}

function Assert-ProjectRelativeJsonPath {
    param(
        $Value,
        [Parameter(Mandatory = $true)][string]$Label
    )
    if (-not ($Value -is [string]) -or
        [string]::IsNullOrWhiteSpace($Value) -or
        $Value.Contains('\') -or
        [IO.Path]::IsPathRooted($Value) -or
        $Value.IndexOfAny([char[]]@('*', '?', '"', '<', '>', '|', ':')) -ge 0) {
        throw [FormatException]::new(
            "$Label must be a project-relative forward-slash path.")
    }
    foreach ($part in $Value.Split('/')) {
        if ([string]::IsNullOrEmpty($part) -or
            $part -eq '.' -or
            $part -eq '..') {
            throw [FormatException]::new(
                "$Label has a non-normal path component.")
        }
    }
}

function Assert-JsonFinding {
    param(
        [Parameter(Mandatory = $true)]$Finding,
        [Parameter(Mandatory = $true)][string]$Label
    )
    Assert-ExactJsonProperties $Finding ([string[]]@(
        'path', 'line', 'rule', 'message'
    )) $Label
    Assert-ProjectRelativeJsonPath $Finding.path "$Label.path"
    Assert-JsonInteger $Finding.line "$Label.line" -Positive
    if (-not ($Finding.rule -is [string]) -or
        [string]::IsNullOrWhiteSpace($Finding.rule) -or
        -not ($Finding.message -is [string]) -or
        [string]::IsNullOrWhiteSpace($Finding.message)) {
        throw [FormatException]::new(
            "$Label rule/message must be nonempty strings.")
    }
}

function Read-GateStructuredJson {
    param(
        [Parameter(Mandatory = $true)]$Reservation,
        [Parameter(Mandatory = $true)][ref]$HasContent
    )

    $HasContent.Value = $false
    $snapshot = [WinterGate.Native]::FreezeStructuredOutput(
        $Reservation,
        1048576)
    if (-not [bool]$snapshot.HasContent) {
        return $null
    }

    $HasContent.Value = $true
    $raw = [string]$snapshot.Text
    [WinterGate.Native]::ValidateStrictJson($raw)
    $document = $raw | ConvertFrom-Json -ErrorAction Stop
    if ($null -eq $document -or
        $document -is [Array] -or
        $document.GetType().FullName -cne
            'System.Management.Automation.PSCustomObject') {
        throw [FormatException]::new('Structured JSON root must be one object.')
    }
    $document
}

function Get-GateJsonOutcome {
    param(
        [Parameter(Mandatory = $true)][string]$Postcondition,
        [Parameter(Mandatory = $true)]$Document
    )

    if ($Postcondition -eq 'capability-json') {
        Assert-ExactJsonProperties $Document ([string[]]@(
            'schema_version', 'tool', 'phase', 'ready', 'capabilities'
        )) 'capability document'
        Assert-JsonInteger $Document.schema_version 'schema_version'
        if ([long]$Document.schema_version -ne 1 -or
            -not ($Document.tool -is [string]) -or
            $Document.tool -cne 'winter_narrative_capabilities') {
            throw [FormatException]::new('Capability schema/tool is wrong.')
        }
        $expectedPhase = if ($NarrativePhase -eq 'Batch') {
            'batch'
        } else {
            'final'
        }
        if (-not ($Document.phase -is [string]) -or
            $Document.phase -cne $expectedPhase -or
            -not ($Document.ready -is [bool])) {
            throw [FormatException]::new(
                'Capability phase/ready type is inconsistent.')
        }
        Assert-ExactJsonProperties $Document.capabilities ([string[]]@(
            'canon_json', 'portrait_json', 'overlap_json',
            'show_before_json', 'nested_quote_json',
            'batch_contracts', 'final_contracts'
        )) 'capabilities'
        foreach ($property in $Document.capabilities.PSObject.Properties) {
            if (-not ($property.Value -is [bool])) {
                throw [FormatException]::new(
                    "Capability '$($property.Name)' must be Boolean.")
            }
        }
        $required = @(
            $Document.capabilities.canon_json,
            $Document.capabilities.portrait_json,
            $Document.capabilities.overlap_json,
            $Document.capabilities.show_before_json,
            $Document.capabilities.nested_quote_json,
            $Document.capabilities.batch_contracts
        )
        $passes = $Document.ready -and -not ($required -contains $false)
        if ($NarrativePhase -eq 'Final') {
            $passes = $passes -and $Document.capabilities.final_contracts
        }
        return [pscustomobject]@{ Passes = [bool]$passes }
    }

    if ($Postcondition -eq 'canon-json') {
        Assert-ExactJsonProperties $Document ([string[]]@(
            'schema_version',
            'tool',
            'blocking_count',
            'anti_logic',
            'geography',
            'terminology',
            'canon_deviation',
            'informational_occurrences'
        )) 'canon document'
        Assert-JsonInteger $Document.schema_version 'schema_version'
        if ([long]$Document.schema_version -ne 1 -or
            -not ($Document.tool -is [string]) -or
            $Document.tool -cne 'canon') {
            throw [FormatException]::new('Canon schema/tool is wrong.')
        }
        Assert-JsonInteger $Document.blocking_count 'blocking_count'
        $computed = 0
        foreach ($category in @(
            'anti_logic',
            'geography',
            'terminology',
            'canon_deviation'
        )) {
            $values = $Document.$category
            if (-not ($values -is [Array])) {
                throw [FormatException]::new(
                    "Canon $category must be an array.")
            }
            for ($index = 0; $index -lt $values.Count; $index++) {
                Assert-JsonFinding `
                    $values[$index] `
                    "$category[$index]"
            }
            $computed += $values.Count
        }
        if (-not ($Document.informational_occurrences -is [Array])) {
            throw [FormatException]::new(
                'informational_occurrences must be an array.')
        }
        for (
            $index = 0;
            $index -lt $Document.informational_occurrences.Count;
            $index++
        ) {
            $occurrence = $Document.informational_occurrences[$index]
            Assert-ExactJsonProperties $occurrence ([string[]]@(
                'term', 'path', 'line'
            )) "informational_occurrences[$index]"
            if (-not ($occurrence.term -is [string]) -or
                [string]::IsNullOrWhiteSpace($occurrence.term)) {
                throw [FormatException]::new(
                    'Occurrence term must be nonempty.')
            }
            Assert-ProjectRelativeJsonPath `
                $occurrence.path `
                'occurrence.path'
            Assert-JsonInteger `
                $occurrence.line `
                'occurrence.line' `
                -Positive
        }
        if ([long]$Document.blocking_count -ne $computed) {
            throw [FormatException]::new(
                'Canon blocking_count is inconsistent.')
        }
        return [pscustomobject]@{ Passes = ($computed -eq 0) }
    }

    $expectedTool = @{
        'portrait-json' = 'missing_portraits'
        'overlap-json' = 'narration_overlap'
        'show-before-json' = 'show_before_prevention'
        'nested-quote-json' = 'nested_quotes'
    }[$Postcondition]
    if ([string]::IsNullOrWhiteSpace($expectedTool)) {
        throw [FormatException]::new(
            "Unknown structured postcondition '$Postcondition'.")
    }

    Assert-ExactJsonProperties $Document ([string[]]@(
        'schema_version',
        'tool',
        'scanned_files',
        'blocking_count',
        'findings'
    )) 'scanner document'
    Assert-JsonInteger $Document.schema_version 'schema_version'
    if ([long]$Document.schema_version -ne 1 -or
        -not ($Document.tool -is [string]) -or
        $Document.tool -cne $expectedTool) {
        throw [FormatException]::new('Scanner schema/tool is wrong.')
    }
    if (-not ($Document.scanned_files -is [Array])) {
        throw [FormatException]::new('scanned_files must be an array.')
    }
    foreach ($scanned in $Document.scanned_files) {
        Assert-ProjectRelativeJsonPath $scanned 'scanned_files entry'
    }
    if (-not ($Document.scanned_files -ccontains
        'game/governance_winter_interlude.rpy')) {
        throw [FormatException]::new(
            'Scanner did not prove the winter target was scanned.')
    }
    if (-not ($Document.findings -is [Array])) {
        throw [FormatException]::new('findings must be an array.')
    }
    for ($index = 0; $index -lt $Document.findings.Count; $index++) {
        Assert-JsonFinding `
            $Document.findings[$index] `
            "findings[$index]"
    }
    Assert-JsonInteger $Document.blocking_count 'blocking_count'
    if ([long]$Document.blocking_count -ne $Document.findings.Count) {
        throw [FormatException]::new(
            'Scanner blocking_count is inconsistent.')
    }
    [pscustomobject]@{
        Passes = ($Document.findings.Count -eq 0)
    }
}

# BEGIN LOOP 3.4-P3 FINAL STEP DEPENDENCY RECHECK
function Get-GateStepDependencyValidationError {
    param([Parameter(Mandatory = $true)]$Step)
    try {
        if ($null -ne $Step.DependencyLease.FirstMissingRequiredFilePath) {
            return (
                "Step '$($Step.Name)' required file was missing at " +
                'manifest construction: ' +
                $Step.DependencyLease.FirstMissingRequiredFilePath
            )
        }
        $Step.DependencyLease.AssertStable()
    }
    catch {
        $unwrapped = Get-UnwrappedException $_.Exception
        if ($unwrapped -is [WinterGate.WinterGatePathIdentityException]) {
            return $unwrapped.Message
        }
        throw
    }
    return $null
}

# END LOOP 3.4-P3 FINAL STEP DEPENDENCY RECHECK


# BEGIN LOOP 3.3-P4 PROCESS MAPPING AND PUBLIC BRIDGE SHELL
function Invoke-GateStep {
    param(
        [Parameter(Mandatory = $true)]$Step,
        [Parameter(Mandatory = $true)][int]$Ordinal
    )
    Assert-AllGateDirectoryIdentities
    $stem = Get-GateArtifactStem -Ordinal $Ordinal -StepName $Step.Name
    $stdoutLeaf = "$stem.stdout.txt"
    $stderrLeaf = "$stem.stderr.txt"
    $resultLeaf = "$stem.result.json"
    $stdoutPath = Join-Path $script:EvidenceIdentity.FinalPath $stdoutLeaf
    $stderrPath = Join-Path $script:EvidenceIdentity.FinalPath $stderrLeaf
    $resultPath = Join-Path $script:EvidenceIdentity.FinalPath $resultLeaf
    $stdoutRelative = "evidence/$stdoutLeaf"
    $stderrRelative = "evidence/$stderrLeaf"
    $resultRelative = "evidence/$resultLeaf"
    $arguments = [string[]]$Step.Arguments.Clone()

    $validationError = Get-GateStepDependencyValidationError $Step
    if ($null -ne $validationError) {
        $failed = New-ValidationGateResult `
            -Step $Step -Ordinal $Ordinal `
            -ResultRelative $resultRelative -ErrorText $validationError
        Write-GateEvidenceJson -Path $resultPath -Value $failed
        return $failed
    }

    $jsonOutput = Get-GateStructuredOutputPath -Step $Step -Ordinal $Ordinal
    $jsonReservation = $null
    $reservationError = $null
    if ($null -ne $jsonOutput) {
        $reservationRegistered = $false
        try {
            $jsonOutputDirectoryIdentity =
                Get-GateStructuredOutputDirectoryIdentity -Path $jsonOutput
            $jsonReservation =
                [WinterGate.Native]::ReserveStructuredOutput(
                    $jsonOutput,
                    $jsonOutputDirectoryIdentity)
            [void]$script:StructuredOutputReservations.Add(
                $jsonReservation)
            $reservationRegistered = $true
        }
        catch {
            if ($null -ne $jsonReservation -and
                -not $reservationRegistered) {
                $unregisteredReservation = $jsonReservation
                $jsonReservation = $null
                $unregisteredReservation.Dispose()
            }
            $unwrapped = Get-UnwrappedException $_.Exception
            if ($unwrapped -is
                    [WinterGate.WinterGatePathIdentityException] -or
                $unwrapped -is [FormatException]) {
                $reservationError =
                    "Structured output is not a new regular file path: $jsonOutput"
            }
            else {
                throw
            }
        }
    }

    if ($null -ne $reservationError) {
        $failed = New-ValidationGateResult `
            -Step $Step -Ordinal $Ordinal `
            -ResultRelative $resultRelative -ErrorText $reservationError
        Write-GateEvidenceJson -Path $resultPath -Value $failed
        return $failed
    }
    Assert-AllGateDirectoryIdentities

    $process = [WinterGate.Native]::RunProcessTree(
        $Step.DependencyLease,
        $arguments,
        $script:ProjectIdentity.FinalPath,
        $stdoutPath,
        $stderrPath,
        [int]($Step.TimeoutSeconds * 1000),
        $script:EvidenceIdentity,
        $jsonReservation)

    if ($process.ProcessStarted -and -not $process.TreeDrained) {
        $script:EvidencePublicationSafe = $false
        throw [InvalidOperationException]::new(
            "Step '$($Step.Name)' left a live process tree; evidence publication is unsafe.")
    }
    $postRunValidationError =
        Get-GateStepDependencyValidationError $Step
    $unownedSummaryDetected = $null -ne (
        [WinterGate.Native]::TryGetReadableFileIdentity($script:SummaryPath))
    Assert-NonEvidenceGateDirectoryIdentities
    $failureKind = $null
    $errorText = $null

    if ($unownedSummaryDetected) {
        $failureKind = 'validation'
        $errorText =
            'Unowned gate-summary.json appeared while a gate step was running.'
    }
    elseif ($null -ne $postRunValidationError) {
        $failureKind = 'validation'
        $errorText = $postRunValidationError
    }
    elseif (-not $process.ProcessStarted) {
        $failureKind = 'process'
        $errorText = $process.StartError
    }
    elseif ($process.ProcessStarted -and
            -not [bool]$process.OutputEvidenceValid) {
        $failureKind = 'validation'
        $errorText =
            "Step '$($Step.Name)' output evidence identity validation failed."
        if (-not [string]::IsNullOrWhiteSpace(
            [string]$process.OutputEvidenceError)) {
            $errorText += " $([string]$process.OutputEvidenceError)"
        }
    }
    elseif ($process.TimedOut) {
        $failureKind = 'timeout'
        $errorText = "Step '$($Step.Name)' exceeded $($Step.TimeoutSeconds) seconds."
    }
    elseif (-not $process.TreeDrained -or
            $process.HadLiveDescendantsAfterRootExit -or
            -not [string]::IsNullOrWhiteSpace($process.StartError)) {
        $failureKind = 'process_tree'
        $errorText = if (-not [string]::IsNullOrWhiteSpace($process.StartError)) {
            $process.StartError
        } else {
            "Step '$($Step.Name)' violated its bounded process tree."
        }
    }

    if ($null -eq $failureKind -and $null -ne $jsonOutput) {
        $jsonHasContent = $false
        Assert-NonEvidenceGateDirectoryIdentities
        try {
            $document = Read-GateStructuredJson `
                -Reservation $jsonReservation `
                -HasContent ([ref]$jsonHasContent)
            if ($jsonHasContent) {
                $outcome = Get-GateJsonOutcome `
                    -Postcondition $Step.Postcondition `
                    -Document $document
            }
        }
        catch {
            $failureKind = 'invalid_evidence'
            $errorText =
                "Invalid JSON evidence for '$($Step.Name)': $($_.Exception.Message)"
        }
        Assert-NonEvidenceGateDirectoryIdentities
        if ($null -eq $failureKind -and -not $jsonHasContent) {
            if ([int]$process.ExitCode -ne 0) {
                $failureKind = 'process'
                $errorText =
                    "Step '$($Step.Name)' exited $([int]$process.ExitCode) without JSON output."
            }
            else {
                $failureKind = 'invalid_evidence'
                $errorText =
                    "Step '$($Step.Name)' did not create its JSON output."
            }
        }
        elseif ($null -eq $failureKind) {
            if (-not $outcome.Passes) {
                $failureKind = 'postcondition'
                $errorText =
                    "Structured postcondition failed for '$($Step.Name)'."
            }
            elseif ([int]$process.ExitCode -ne 0) {
                $failureKind = 'process'
                $errorText =
                    "Step '$($Step.Name)' exited $([int]$process.ExitCode)."
            }
        }
    }
    elseif ($null -eq $failureKind) {
        if ([int]$process.ExitCode -ne 0) {
            $failureKind = 'process'
            $errorText =
                "Step '$($Step.Name)' exited $([int]$process.ExitCode)."
        }
        elseif ($Step.Postcondition -eq 'manual-review' -and
                -not [IO.File]::Exists($stdoutPath)) {
            $failureKind = 'postcondition'
            $errorText =
                "Manual-review stdout is missing for '$($Step.Name)'."
        }
        elseif ($Step.Postcondition -notin @(
            'exit-zero', 'runner-passed', 'manual-review'
        )) {
            $failureKind = 'validation'
            $errorText =
                "Unknown postcondition '$($Step.Postcondition)'."
        }
    }

    $outputEvidenceTrusted = [bool]$process.OutputEvidenceValid
    $result = [pscustomobject][ordered]@{
        ordinal = $Ordinal
        name = $Step.Name
        kind = $Step.Kind
        executable = $Step.Executable
        arguments = [string[]]$arguments.Clone()
        working_directory = $script:ProjectIdentity.FinalPath
        process_started = [bool]$process.ProcessStarted
        process_id = $process.ProcessId
        started_utc = if ($null -eq $process.StartedUtc) {
            $null
        } else { ([DateTime]$process.StartedUtc).ToString('o') }
        ended_utc = if ($null -eq $process.EndedUtc) {
            $null
        } else { ([DateTime]$process.EndedUtc).ToString('o') }
        exit_code = $process.ExitCode
        timed_out = [bool]$process.TimedOut
        tree_drained = [bool]$process.TreeDrained
        had_live_descendants_after_root_exit =
            [bool]$process.HadLiveDescendantsAfterRootExit
        elapsed_milliseconds = $process.ElapsedMilliseconds
        stdout = if ($outputEvidenceTrusted) { $stdoutRelative } else { $null }
        stderr = if ($outputEvidenceTrusted) { $stderrRelative } else { $null }
        result = $resultRelative
        postcondition = $Step.Postcondition
        manual_review_required = ($Step.Postcondition -eq 'manual-review')
        status = if ($null -eq $failureKind) { 'passed' } else { 'failed' }
        failure_kind = $failureKind
        error = $errorText
    }
    Write-GateEvidenceJson -Path $resultPath -Value $result
    $result
}

function Invoke-WinterInterludeGate {
    Add-WinterGateNativeTypes
    $script:TrustedPowerShellIdentity = Assert-WinterGateHostIdentity
    $script:ProjectIdentity = Resolve-GateProject `
        -ProjectRoot $ProjectRoot `
        -WasSpecified:$projectRootWasSpecified
    $script:ProtectedSaveRoots = @(Get-ProtectedPlayerSaveRoots)
    $runTree = New-VerifiedRunRoot `
        -Candidate $RunRoot `
        -CandidateWasSpecified:$runRootWasSpecified `
        -ProjectIdentity $script:ProjectIdentity `
        -ProtectedSaveRoots $script:ProtectedSaveRoots
    $script:RunRootIdentity = $runTree.Identity
    $script:EvidenceIdentity = $runTree.EvidenceIdentity
    $script:SavedirsIdentity = $runTree.SavedirsIdentity
    $script:GateDirectoryIdentities =
        New-Object 'System.Collections.Generic.List[object]'
    [void]$script:GateDirectoryIdentities.Add($script:RunRootIdentity)
    [void]$script:GateDirectoryIdentities.Add($script:EvidenceIdentity)
    [void]$script:GateDirectoryIdentities.Add($script:SavedirsIdentity)
    $script:StructuredOutputReservations =
        New-Object 'System.Collections.Generic.List[object]'
    $script:StepDependencyLeases =
        New-Object 'System.Collections.Generic.List[object]'
    $script:EvidencePublicationSafe = $true
    $script:SummaryCommittedByGate = $false
    $script:SummaryPublicationAttempted = $false
    $script:QuarantinedSummaryPath = $null
    $script:HeadTrackingInitialized = $false
    $script:HeadState = $null
    $script:HeadCommit = $null
    $script:HeadToken = 'no-head'
    $summary = [pscustomobject][ordered]@{
        schema_version = 1
        gate = $Gate
        narrative_phase = if ($Gate -eq 'Narrative') {
            $NarrativePhase
        } else { $null }
        status = 'passed'
        failure_kind = $null
        error = $null
        started_utc = [DateTime]::UtcNow.ToString('o')
        ended_utc = $null
        head_token = $script:HeadToken
        host = [pscustomobject][ordered]@{
            edition = $PSVersionTable.PSEdition
            version = $PSVersionTable.PSVersion.ToString()
            executable = Get-IdentityEvidenceObject `
                $script:TrustedPowerShellIdentity
        }
        project_root = Get-IdentityEvidenceObject $script:ProjectIdentity
        run_root = Get-IdentityEvidenceObject $script:RunRootIdentity
        steps = [object[]]@()
    }
    $script:SummaryPath = Join-Path `
        $script:EvidenceIdentity.FinalPath `
        'gate-summary.json'
    try {
        [Console]::Out.WriteLine(
            "Winter gate run root: $($script:RunRootIdentity.FinalPath)")
        Assert-ProjectRootIdentity
        $script:HeadState = Get-ProjectHeadState
        $script:HeadCommit = $script:HeadState.Commit
        $script:HeadToken = if ($null -eq $script:HeadCommit) {
            'no-head'
        } else { $script:HeadCommit.Substring(0, 12) }
        $summary.head_token = $script:HeadToken
        $script:HeadTrackingInitialized = $true
        Assert-GitCommitOverride -Commit $script:HeadCommit
        $script:PythonIdentity = Resolve-PythonExecutable
        [object[]]$manifest = if ($Gate -eq 'Structural') {
            @(Get-StructuralGateManifest)
        } else { @(Get-NarrativeGateManifest) }
        $manifestNames = [string[]]@($manifest | ForEach-Object { $_.Name })
        if (@($manifestNames | Select-Object -Unique).Count -ne $manifestNames.Count) {
            throw 'Manifest step names are not unique.'
        }
        foreach ($index in 0..($manifest.Count - 1)) {
            $result = Invoke-GateStep `
                -Step $manifest[$index] -Ordinal ($index + 1)
            $summary.steps = [object[]]@($summary.steps + $result)
            if ($result.status -eq 'failed') {
                $summary.status = 'failed'
                $summary.failure_kind = $result.failure_kind
                $summary.error = $result.error
                break
            }
        }
        $summary.ended_utc = [DateTime]::UtcNow.ToString('o')
        Write-GateSummaryJson -Path $script:SummaryPath -Value $summary
        if ($summary.status -ne 'passed') {
            throw [InvalidOperationException]::new($summary.error)
        }
    }
    catch [WinterGate.WinterGatePathIdentityException] {
        $pathError = $_
        if (-not $script:EvidencePublicationSafe) { throw }
        try { Assert-RunTreeDirectoryIdentities }
        catch { throw $pathError }
        if (-not $script:SummaryCommittedByGate -and
            -not $script:SummaryPublicationAttempted) {
            $summary.status = 'failed'
            $summary.failure_kind = 'validation'
            $summary.error = $pathError.Exception.Message
            $summary.ended_utc = [DateTime]::UtcNow.ToString('o')
            Write-GateSummaryJson `
                -Path $script:SummaryPath `
                -Value $summary `
                -RunTreeOnly
        }
        throw $pathError
    }
    catch {
        $ordinaryError = $_
        if (-not $script:EvidencePublicationSafe) { throw }
        if (-not $script:SummaryCommittedByGate -and
            -not $script:SummaryPublicationAttempted) {
            $summary.status = 'failed'
            $summary.failure_kind = 'validation'
            $summary.error = $ordinaryError.Exception.Message
            $summary.ended_utc = [DateTime]::UtcNow.ToString('o')
            Write-GateSummaryJson `
                -Path $script:SummaryPath `
                -Value $summary `
                -RunTreeOnly
        }
        throw $ordinaryError
    }
}
# END LOOP 3.3-P4 PROCESS MAPPING AND PUBLIC BRIDGE SHELL
$script:StructuredOutputReservations = $null
$script:StepDependencyLeases = $null
$script:ProtectedSaveRoots = $null
$script:EvidencePublicationSafe = $false
$exitCode = 0
try {
    Invoke-WinterInterludeGate
}
catch {
    [Console]::Error.WriteLine($_.ToString())
    $exitCode = 1
}
finally {
    try {
        Close-GateStructuredOutputReservations
    }
    catch {
        [Console]::Error.WriteLine($_.ToString())
        $exitCode = 1
    }
    try {
        if ($script:EvidencePublicationSafe) {
            Close-GateStepDependencyLeases
        }
    }
    catch {
        [Console]::Error.WriteLine($_.ToString())
        $exitCode = 1
    }
}
exit $exitCode
