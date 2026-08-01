from __future__ import annotations

import pickletools
import struct
import unittest
import zlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GAME = ROOT / "game"
OLD_GAME = ROOT / "old-game"
RPYC2_HEADER = b"RENPY RPC2"
EXPECTED_CURRENT_SCRIPT_COUNT = 56
REQUIRED_GENERATIONS = {
    "script.rpyc": 1_297_438_350,
    "chapter2.rpyc": 1_297_438_144,
}


def current_script_rpycs() -> set[Path]:
    """Return the old-game paths required by the current source tree."""
    return {
        source.relative_to(GAME).with_suffix(".rpyc")
        for source in GAME.rglob("*.rpy")
    }


def read_rpyc2_slot_one(path: Path) -> bytes:
    """Read RPYC2 slot 1 without unpickling or executing its contents."""
    data = path.read_bytes()
    if not data.startswith(RPYC2_HEADER):
        raise AssertionError(f"{path} is not an RPYC2 file")

    offset = len(RPYC2_HEADER)
    while offset + 12 <= len(data):
        slot, start, length = struct.unpack_from("<III", data, offset)
        if slot == 0:
            break
        if slot == 1:
            end = start + length
            if start < offset + 12 or end > len(data):
                raise AssertionError(f"{path} has an out-of-bounds slot 1")
            return zlib.decompress(data[start:end])
        offset += 12

    raise AssertionError(f"{path} has no slot 1")


def safely_scan_pickle(payload: bytes) -> list[tuple[str, object]]:
    """Validate a pickle stream by disassembling it, never by loading it."""
    return [(opcode.name, argument) for opcode, argument, _ in pickletools.genops(payload)]


class OldGameCompatibilityTests(unittest.TestCase):
    def test_old_game_covers_every_current_script(self) -> None:
        expected = current_script_rpycs()
        actual = {
            compiled.relative_to(OLD_GAME)
            for compiled in OLD_GAME.rglob("*.rpyc")
        }

        self.assertEqual(len(expected), EXPECTED_CURRENT_SCRIPT_COUNT)
        self.assertEqual(actual, expected)

    def test_every_old_game_slot_one_is_a_scannable_pickle(self) -> None:
        for relative_path in sorted(current_script_rpycs()):
            with self.subTest(path=relative_path.as_posix()):
                payload = read_rpyc2_slot_one(OLD_GAME / relative_path)
                opcodes = safely_scan_pickle(payload)
                self.assertTrue(opcodes)
                self.assertEqual(opcodes[-1][0], "STOP")

    def test_required_release_generations_are_retained(self) -> None:
        integer_opcodes = {"INT", "BININT", "BININT1", "BININT2", "LONG", "LONG1", "LONG4"}

        for relative_path, generation in REQUIRED_GENERATIONS.items():
            with self.subTest(path=relative_path, generation=generation):
                payload = read_rpyc2_slot_one(OLD_GAME / relative_path)
                integers = {
                    argument
                    for opcode, argument in safely_scan_pickle(payload)
                    if opcode in integer_opcodes and isinstance(argument, int)
                }
                self.assertIn(generation, integers)


if __name__ == "__main__":
    unittest.main()
