[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$ProjectRoot,

    [Parameter(Mandatory = $true)]
    [string]$SaveDir,

    [ValidateSet("Suite", "Full", "Lint")]
    [string]$Mode = "Suite",

    [string]$Suite,

    [ValidateSet("PASSED", "FAILED")]
    [string]$Expect,

    [string]$ExpectedPattern,
    [string]$Variant,
    [switch]$StageLegacyFixtures,
    [string[]]$ExtraArgs = @(),
    [string]$EvidenceDir,

    [ValidateRange(1, 1800)]
    [int]$TimeoutSeconds = 120
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"
$invocationParameters = @{}
foreach ($boundName in $PSBoundParameters.Keys) {
    $invocationParameters[$boundName] = $PSBoundParameters[$boundName]
}

function Get-FullPath {
    param([Parameter(Mandatory = $true)][string]$Path)

    return [System.IO.Path]::GetFullPath($Path).TrimEnd([System.IO.Path]::DirectorySeparatorChar)
}

function Test-IsSameOrChildPath {
    param(
        [Parameter(Mandatory = $true)][string]$Candidate,
        [Parameter(Mandatory = $true)][string]$Parent
    )

    $candidatePath = (Get-FullPath $Candidate) + [System.IO.Path]::DirectorySeparatorChar
    $parentPath = (Get-FullPath $Parent) + [System.IO.Path]::DirectorySeparatorChar
    return $candidatePath.StartsWith($parentPath, [System.StringComparison]::OrdinalIgnoreCase)
}

function Quote-NativeArgument {
    param([AllowEmptyString()][string]$Value)

    if ($Value -notmatch '[\s"]') {
        return $Value
    }

    $quoted = [regex]::Replace($Value, '(\\*)"', '$1$1\"')
    $quoted = [regex]::Replace($quoted, '(\\+)$', '$1$1')
    return '"' + $quoted + '"'
}

function Find-RenPyExecutable {
    param([Parameter(Mandatory = $true)][string]$ResolvedProjectRoot)

    $candidates = New-Object System.Collections.Generic.List[string]
    if (-not [string]::IsNullOrWhiteSpace($env:RENPY_SDK)) {
        $candidates.Add((Join-Path $env:RENPY_SDK "renpy.exe"))
    }

    $command = Get-Command "renpy.exe" -CommandType Application -ErrorAction SilentlyContinue
    if ($null -ne $command) {
        $candidates.Add($command.Source)
    }

    $candidates.Add((Join-Path (Split-Path $ResolvedProjectRoot -Parent) "renpy.exe"))

    $commonGitDir = (& git -C $ResolvedProjectRoot rev-parse --path-format=absolute --git-common-dir 2>$null)
    if ($LASTEXITCODE -eq 0 -and -not [string]::IsNullOrWhiteSpace([string]$commonGitDir)) {
        $mainCheckout = Split-Path ([string]$commonGitDir).Trim() -Parent
        $candidates.Add((Join-Path (Split-Path $mainCheckout -Parent) "renpy.exe"))
    }

    foreach ($candidate in $candidates) {
        if (-not [string]::IsNullOrWhiteSpace($candidate) -and (Test-Path -LiteralPath $candidate -PathType Leaf)) {
            return (Get-FullPath $candidate)
        }
    }

    throw "Ren'Py executable not found. Set RENPY_SDK to the Ren'Py 8.5.2 SDK directory."
}

function Copy-LegacyFixtures {
    param(
        [Parameter(Mandatory = $true)][string]$ResolvedProjectRoot,
        [Parameter(Mandatory = $true)][string]$ResolvedSaveDir
    )

    $manifestPath = Join-Path $ResolvedProjectRoot "tests\fixtures\winter_legacy\manifest.json"
    if (-not (Test-Path -LiteralPath $manifestPath -PathType Leaf)) {
        throw "Legacy fixture manifest.json is missing: $manifestPath"
    }

    $manifest = Get-Content -LiteralPath $manifestPath -Raw -Encoding UTF8 | ConvertFrom-Json
    if ($manifest.savegame_suffix -ne "-LT1.save") {
        throw "Legacy fixture manifest has an unexpected savegame suffix."
    }

    foreach ($fixture in @($manifest.fixtures)) {
        $physicalFilename = [string]$fixture.physical_filename
        if ([string]::IsNullOrWhiteSpace($physicalFilename) -or
            $physicalFilename -ne [System.IO.Path]::GetFileName($physicalFilename) -or
            -not $physicalFilename.EndsWith([string]$manifest.savegame_suffix, [System.StringComparison]::Ordinal)) {
            throw "Legacy fixture physical_filename is not an exact engine-native filename: $physicalFilename"
        }

        $source = Join-Path (Split-Path $manifestPath -Parent) $physicalFilename
        if (-not (Test-Path -LiteralPath $source -PathType Leaf)) {
            throw "Legacy fixture is missing: $physicalFilename"
        }

        $actualHash = (Get-FileHash -LiteralPath $source -Algorithm SHA256).Hash.ToLowerInvariant()
        $expectedHash = ([string]$fixture.sha256).ToLowerInvariant()
        if ([string]::IsNullOrWhiteSpace($expectedHash) -or $actualHash -ne $expectedHash) {
            throw "Legacy fixture hash mismatch for $physicalFilename."
        }

        Copy-Item -LiteralPath $source -Destination (Join-Path $ResolvedSaveDir $physicalFilename) -ErrorAction Stop
    }
}

function New-EvidencePath {
    param(
        [Parameter(Mandatory = $true)][string]$ResolvedEvidenceDir,
        [Parameter(Mandatory = $true)][string]$CurrentMode,
        [string]$CurrentSuite,
        [string]$CurrentExpectation,
        [Parameter(Mandatory = $true)][string]$Head,
        [Parameter(Mandatory = $true)][string]$Extension
    )

    $timestamp = (Get-Date).ToUniversalTime().ToString("yyyyMMddTHHmmssfffZ")
    $suitePart = if ([string]::IsNullOrWhiteSpace($CurrentSuite)) { "all" } else { $CurrentSuite }
    $expectPart = if ([string]::IsNullOrWhiteSpace($CurrentExpectation)) { "NA" } else { $CurrentExpectation }
    $safeSuite = $suitePart -replace '[^A-Za-z0-9_.-]', '_'
    $headPart = if ($Head.Length -gt 12) { $Head.Substring(0, 12) } else { $Head }
    $nonce = [Guid]::NewGuid().ToString("N").Substring(0, 8)
    $name = "renpy-$CurrentMode-$safeSuite-$expectPart-$timestamp-$headPart-$nonce.$Extension".ToLowerInvariant()
    return Join-Path $ResolvedEvidenceDir $name
}

function Write-CombinedOutput {
    param(
        [Parameter(Mandatory = $true)][string]$StandardOutputPath,
        [Parameter(Mandatory = $true)][string]$StandardErrorPath,
        [Parameter(Mandatory = $true)][string]$Destination
    )

    $lines = New-Object System.Collections.Generic.List[string]
    $lines.Add("=== stdout ===")
    if (Test-Path -LiteralPath $StandardOutputPath) {
        foreach ($line in Get-Content -LiteralPath $StandardOutputPath -Encoding UTF8) { $lines.Add($line) }
    }
    $lines.Add("=== stderr ===")
    if (Test-Path -LiteralPath $StandardErrorPath) {
        foreach ($line in Get-Content -LiteralPath $StandardErrorPath -Encoding UTF8) { $lines.Add($line) }
    }
    $lines | Set-Content -LiteralPath $Destination -Encoding UTF8
}

function Invoke-RenPySuite {
    $resolvedProjectRoot = Get-FullPath $ProjectRoot
    $resolvedSaveDir = Get-FullPath $SaveDir

    if (-not (Test-Path -LiteralPath $resolvedProjectRoot -PathType Container)) {
        throw "ProjectRoot is not a directory: $resolvedProjectRoot"
    }
    if (-not (Test-Path -LiteralPath (Join-Path $resolvedProjectRoot "game") -PathType Container)) {
        throw "ProjectRoot does not contain a game directory: $resolvedProjectRoot"
    }

    # Suite mode: Suite and Expect are required.
    if ($Mode -eq "Suite") {
        if ([string]::IsNullOrWhiteSpace($Suite) -or -not $invocationParameters.ContainsKey("Expect")) {
            throw "Suite mode: Suite and Expect are required."
        }
    }
    # Full mode: Suite is not accepted and Expect=PASSED is required.
    elseif ($Mode -eq "Full") {
        if ($invocationParameters.ContainsKey("Suite")) {
            throw "Full mode: Suite is not accepted."
        }
        if (-not $invocationParameters.ContainsKey("Expect") -or $Expect -ne "PASSED") {
            throw "Full mode: Expect=PASSED is required."
        }
    }
    # Lint mode: Suite and Expect are not accepted.
    elseif ($Mode -eq "Lint") {
        if ($invocationParameters.ContainsKey("Suite")) {
            throw "Lint mode: Suite is not accepted."
        }
        if ($invocationParameters.ContainsKey("Expect")) {
            throw "Lint mode: Expect is not accepted."
        }
        if ($invocationParameters.ContainsKey("ExpectedPattern")) {
            throw "Lint mode: ExpectedPattern is not accepted."
        }
    }

    if ($Expect -eq "FAILED" -and [string]::IsNullOrWhiteSpace($ExpectedPattern)) {
        throw "FAILED expectation requires ExpectedPattern."
    }

    $pathComponents = $resolvedSaveDir -split '[\\/]'
    if ($pathComponents -contains "CourtOfShadows-save") {
        throw "SaveDir must be outside the player's CourtOfShadows-save directory."
    }
    $projectLocalSaves = Join-Path $resolvedProjectRoot "game\saves"
    if (Test-IsSameOrChildPath -Candidate $resolvedSaveDir -Parent $projectLocalSaves) {
        throw "SaveDir must not use the player's project-local save directory."
    }
    if ((Test-IsSameOrChildPath -Candidate $resolvedProjectRoot -Parent $resolvedSaveDir) -or
        (Test-IsSameOrChildPath -Candidate $resolvedSaveDir -Parent $resolvedProjectRoot)) {
        throw "SaveDir must be a unique external directory, outside ProjectRoot."
    }
    if (Test-Path -LiteralPath $resolvedSaveDir) {
        if (-not (Test-Path -LiteralPath $resolvedSaveDir -PathType Container)) {
            throw "SaveDir exists but is not a directory: $resolvedSaveDir"
        }
        if ($null -ne (Get-ChildItem -LiteralPath $resolvedSaveDir -Force | Select-Object -First 1)) {
            throw "SaveDir must be a new or empty unique directory: $resolvedSaveDir"
        }
    }
    else {
        New-Item -ItemType Directory -Path $resolvedSaveDir -Force:$false | Out-Null
    }

    if ($StageLegacyFixtures) {
        Copy-LegacyFixtures -ResolvedProjectRoot $resolvedProjectRoot -ResolvedSaveDir $resolvedSaveDir
    }

    if ([string]::IsNullOrWhiteSpace($EvidenceDir)) {
        $resolvedEvidenceDir = Join-Path (Split-Path $resolvedSaveDir -Parent) "renpy-suite-evidence"
    }
    else {
        $resolvedEvidenceDir = Get-FullPath $EvidenceDir
    }
    New-Item -ItemType Directory -Path $resolvedEvidenceDir -Force | Out-Null

    $renpyExecutable = Find-RenPyExecutable -ResolvedProjectRoot $resolvedProjectRoot
    $head = (& git -C $resolvedProjectRoot rev-parse HEAD).Trim()
    if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($head)) {
        throw "Could not resolve HEAD for evidence naming."
    }

    $arguments = New-Object System.Collections.Generic.List[string]
    $arguments.Add($resolvedProjectRoot)
    switch ($Mode) {
        "Suite" {
            $arguments.Add("test")
            $arguments.Add($Suite)
        }
        "Full" {
            $arguments.Add("test")
        }
        "Lint" {
            $arguments.Add("lint")
            $arguments.Add("--error-code")
        }
    }
    $arguments.Add("--savedir")
    $arguments.Add($resolvedSaveDir)
    foreach ($extraArgument in $ExtraArgs) {
        $arguments.Add([string]$extraArgument)
    }

    $argumentLine = (($arguments | ForEach-Object { Quote-NativeArgument $_ }) -join " ")
    $outputNonce = [Guid]::NewGuid().ToString("N")
    $stdoutPath = Join-Path $resolvedEvidenceDir ("renpy-process-{0}.stdout.tmp" -f $outputNonce)
    $stderrPath = Join-Path $resolvedEvidenceDir ("renpy-process-{0}.stderr.tmp" -f $outputNonce)
    $logPath = Join-Path $resolvedProjectRoot "log.txt"
    $process = $null
    $stdoutTask = $null
    $stderrTask = $null
    $recordedPid = $null
    $startUtc = $null
    $variantWasSet = Test-Path Env:RENPY_VARIANT
    $previousVariant = if ($variantWasSet) { $env:RENPY_VARIANT } else { $null }

    try {
        if ($invocationParameters.ContainsKey("Variant")) {
            $env:RENPY_VARIANT = $Variant
        }

        $startUtc = [DateTime]::UtcNow
        $startInfo = New-Object System.Diagnostics.ProcessStartInfo
        $startInfo.FileName = $renpyExecutable
        $startInfo.Arguments = $argumentLine
        $startInfo.UseShellExecute = $false
        $startInfo.CreateNoWindow = $true
        $startInfo.RedirectStandardOutput = $true
        $startInfo.RedirectStandardError = $true
        $process = New-Object System.Diagnostics.Process
        $process.StartInfo = $startInfo
        if (-not $process.Start()) {
            throw "Could not start the Ren'Py native process."
        }
        $stdoutTask = $process.StandardOutput.ReadToEndAsync()
        $stderrTask = $process.StandardError.ReadToEndAsync()
        $recordedPid = $process.Id
        Write-Host ("Ren'Py recorded PID: {0}; start UTC: {1:o}" -f $recordedPid, $startUtc)

        $completed = $process.WaitForExit($TimeoutSeconds * 1000)
        if (-not $completed) {
            $process.Kill()
            [void]$process.WaitForExit(10000)
            $stdoutText = $stdoutTask.GetAwaiter().GetResult()
            $stderrText = $stderrTask.GetAwaiter().GetResult()
            [System.IO.File]::WriteAllText($stdoutPath, $stdoutText)
            [System.IO.File]::WriteAllText($stderrPath, $stderrText)
            $timeoutEvidence = New-EvidencePath -ResolvedEvidenceDir $resolvedEvidenceDir -CurrentMode $Mode `
                -CurrentSuite $Suite -CurrentExpectation $Expect -Head $head -Extension "txt"
            Write-CombinedOutput -StandardOutputPath $stdoutPath -StandardErrorPath $stderrPath -Destination $timeoutEvidence
            throw "Ren'Py recorded PID $recordedPid timed out after $TimeoutSeconds seconds; output: $timeoutEvidence"
        }

        # Complete redirected stream handling before reading the native exit code.
        [void]$process.WaitForExit()
        $process.Refresh()
        $exitCode = $process.ExitCode
        $stdoutText = $stdoutTask.GetAwaiter().GetResult()
        $stderrText = $stderrTask.GetAwaiter().GetResult()
        [System.IO.File]::WriteAllText($stdoutPath, $stdoutText)
        [System.IO.File]::WriteAllText($stderrPath, $stderrText)
        if (-not $process.HasExited) {
            throw "Ren'Py recorded PID $recordedPid remained alive after the bounded wait."
        }

        if ($Mode -eq "Lint") {
            $evidencePath = New-EvidencePath -ResolvedEvidenceDir $resolvedEvidenceDir -CurrentMode $Mode `
                -CurrentSuite $null -CurrentExpectation $null -Head $head -Extension "txt"
            Write-CombinedOutput -StandardOutputPath $stdoutPath -StandardErrorPath $stderrPath -Destination $evidencePath
            if ($exitCode -ne 0) {
                throw "Ren'Py lint --error-code exited $exitCode; evidence: $evidencePath"
            }
        }
        else {
            if (-not (Test-Path -LiteralPath $logPath -PathType Leaf)) {
                throw "Fresh Ren'Py log.txt is missing."
            }
            $logInfo = Get-Item -LiteralPath $logPath
            if ($logInfo.LastWriteTimeUtc -le $startUtc) {
                throw "Ren'Py log.txt was not modified after this process started."
            }

            $logText = Get-Content -LiteralPath $logPath -Raw -Encoding UTF8
            # Require exactly one literal "[rpytest] Status:" summary from this fresh run.
            $statusMatches = [regex]::Matches($logText, '(?m)^\[rpytest\] Status:\s+([A-Z ]+?)\s*$')
            if ($statusMatches.Count -ne 1) {
                throw "Fresh log must contain exactly one [rpytest] Status; found $($statusMatches.Count)."
            }
            $actualStatus = $statusMatches[0].Groups[1].Value.Trim()
            $evidencePath = New-EvidencePath -ResolvedEvidenceDir $resolvedEvidenceDir -CurrentMode $Mode `
                -CurrentSuite $Suite -CurrentExpectation $Expect -Head $head -Extension "log"
            Copy-Item -LiteralPath $logPath -Destination $evidencePath -ErrorAction Stop
            if ($actualStatus -ne $Expect) {
                throw "Fresh log status was $actualStatus, expected $Expect; evidence: $evidencePath"
            }

            if ($Expect -eq "PASSED") {
                if ($exitCode -ne 0) {
                    throw "PASSED test run exited $exitCode; evidence: $evidencePath"
                }
            }
            else {
                if ($exitCode -eq 0) {
                    throw "FAILED test run unexpectedly exited zero; evidence: $evidencePath"
                }
                if ($logText -notmatch $ExpectedPattern) {
                    throw "FAILED test run did not contain ExpectedPattern; evidence: $evidencePath"
                }
                $crashPattern = '(?im)(ParseError|SyntaxError|ImportError|ModuleNotFoundError|FileNotFoundError|IOError:.*(?:could not|couldn''t) find|missing[- ]file|couldn''t find file|could not load)'
                if ($logText -match $crashPattern) {
                    throw "FAILED expectation was caused by a parse/import/syntax/missing-file crash; evidence: $evidencePath"
                }
            }
        }

        Write-Host ("Ren'Py {0} evidence: {1}" -f $Mode, $evidencePath)
    }
    finally {
        if ($null -ne $process) {
            $process.Refresh()
            if (-not $process.HasExited) {
                # Cleanup targets only the recorded PID represented by this Process object.
                $process.Kill()
                [void]$process.WaitForExit(10000)
            }
            $process.Refresh()
            if (-not $process.HasExited) {
                throw "Ren'Py recorded PID $recordedPid is still alive after cleanup."
            }
            $process.Dispose()
        }

        if ($invocationParameters.ContainsKey("Variant")) {
            if ($variantWasSet) {
                $env:RENPY_VARIANT = $previousVariant
            }
            else {
                Remove-Item Env:RENPY_VARIANT -ErrorAction SilentlyContinue
            }
        }

        Remove-Item -LiteralPath $stdoutPath, $stderrPath -Force -ErrorAction SilentlyContinue
    }
}

try {
    Invoke-RenPySuite
    exit 0
}
catch {
    Write-Error $_
    exit 1
}
