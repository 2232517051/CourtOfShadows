from __future__ import annotations

import hashlib
import pickletools
import struct
import unittest
import zlib
from pathlib import Path
from typing import NamedTuple

from Tools.old_game_required_nodes import (
    EXACT_NODE_FIXTURES,
    REQUIRED_RUNTIME_SMOKE_SAVES,
)


ROOT = Path(__file__).resolve().parents[1]
GAME = ROOT / "game"
OLD_GAME = ROOT / "old-game"
RPYC2_HEADER = b"RENPY RPC2"
EXPECTED_CURRENT_SCRIPT_COUNT = 56
REQUIRED_GENERATIONS = {
    "script.rpyc": 1_297_438_350,
    "chapter2.rpyc": 1_297_438_144,
}
RUNTIME_SMOKE_SAVE_NAMES = {
    "7-1-LT1.save",
    "7-8-LT1.save",
    "auto_ch-southern-LT1.save",
}
EXPECTED_EXACT_NODE_FIXTURE_METADATA = {
    "7-1-LT1.save": {
        "save_version": "3.9.1",
        "save_sha256": "9AEBCE6B73C2F20C3E668F2B45C58AA0FB75EA56813F59C7D5948E0BEF68867C",
        "renpy_version": "Ren'Py 8.5.2.26010301",
        "log_sha256": "8AA7049802789A06552E8B4018721880FB483A37E7A9006130366C5612F5B55E",
        "node_count": 129,
        "node_set_sha256": "1258D0C9B2F6CAC0DD18942A2C6703302F08364E3DB4F8C51389F8EB7FD81304",
    },
}
SERIAL_ZERO_REGRESSION_NODE = ("game/chapter2.rpy", 1_501_931_358, 0)
_PICKLE_MARK = object()
_OPAQUE_PICKLE_VALUE = object()


class _EncodedGlobal(NamedTuple):
    module: object
    name: object


class _EncodedInstance(NamedTuple):
    constructor: object


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


def safely_collect_node_ids(payload: bytes) -> set[tuple[str, int, int]]:
    """Interpret pickle structure without constructing any encoded globals."""
    stack: list[object] = []
    memo: dict[int, object] = {}
    node_ids: set[tuple[str, int, int]] = set()

    def pop_mark() -> list[object]:
        index = len(stack) - 1
        while index >= 0 and stack[index] is not _PICKLE_MARK:
            index -= 1
        if index < 0:
            raise AssertionError("pickle stack has no MARK")
        items = stack[index + 1 :]
        del stack[index:]
        return items

    def record_tuple(value: tuple[object, ...]) -> None:
        if (
            len(value) == 3
            and isinstance(value[0], str)
            and value[0].startswith("game/")
            and value[0].endswith(".rpy")
            and isinstance(value[1], int)
            and not isinstance(value[1], bool)
            and isinstance(value[2], int)
            and not isinstance(value[2], bool)
        ):
            node_ids.add((value[0], value[1], value[2]))

    def record_state(instance: object, value: object) -> None:
        if not isinstance(instance, _EncodedInstance):
            return
        constructor = instance.constructor
        if not isinstance(constructor, _EncodedGlobal) or constructor.module != "renpy.ast":
            return
        state = value[1] if isinstance(value, tuple) and len(value) == 2 else value
        if not isinstance(state, dict):
            return
        filename = state.get("filename")
        generation = state.get("name_version")
        serial = state.get("name_serial", 0)
        if (
            isinstance(filename, str)
            and filename.startswith("game/")
            and filename.endswith(".rpy")
            and isinstance(generation, int)
            and not isinstance(generation, bool)
            and isinstance(serial, int)
            and not isinstance(serial, bool)
        ):
            node_ids.add((filename, generation, serial))

    for opcode, argument, position in pickletools.genops(payload):
        name = opcode.name
        if name in {"PROTO", "FRAME"}:
            continue
        if name == "MARK":
            stack.append(_PICKLE_MARK)
        elif name in {
            "SHORT_BINUNICODE",
            "BINUNICODE",
            "BININT",
            "BININT1",
            "BININT2",
            "LONG1",
            "BINFLOAT",
        }:
            stack.append(argument)
        elif name == "NONE":
            stack.append(None)
        elif name == "NEWTRUE":
            stack.append(True)
        elif name == "NEWFALSE":
            stack.append(False)
        elif name == "EMPTY_LIST":
            stack.append([])
        elif name == "EMPTY_DICT":
            stack.append({})
        elif name == "EMPTY_SET":
            stack.append([])
        elif name == "EMPTY_TUPLE":
            stack.append(())
        elif name in {"BINGET", "LONG_BINGET"}:
            stack.append(memo[argument])
        elif name == "MEMOIZE":
            memo[len(memo)] = stack[-1]
        elif name == "STACK_GLOBAL":
            global_name = stack.pop()
            module = stack.pop()
            stack.append(_EncodedGlobal(module, global_name))
        elif name == "NEWOBJ":
            stack.pop()
            constructor = stack.pop()
            stack.append(_EncodedInstance(constructor))
        elif name == "REDUCE":
            del stack[-2:]
            stack.append(_OPAQUE_PICKLE_VALUE)
        elif name == "BUILD":
            state = stack.pop()
            instance = stack.pop()
            record_state(instance, state)
            stack.append(instance)
        elif name == "TUPLE1":
            value = (stack.pop(),)
            stack.append(value)
        elif name == "TUPLE2":
            second = stack.pop()
            value = (stack.pop(), second)
            stack.append(value)
        elif name == "TUPLE3":
            third = stack.pop()
            second = stack.pop()
            value = (stack.pop(), second, third)
            record_tuple(value)
            stack.append(value)
        elif name == "TUPLE":
            value = tuple(pop_mark())
            record_tuple(value)
            stack.append(value)
        elif name == "APPEND":
            value = stack.pop()
            target = stack[-1]
            if isinstance(target, list):
                target.append(value)
        elif name == "APPENDS":
            values = pop_mark()
            target = stack[-1]
            if isinstance(target, list):
                target.extend(values)
        elif name == "SETITEM":
            value = stack.pop()
            key = stack.pop()
            target = stack[-1]
            if isinstance(target, dict):
                target[key] = value
        elif name == "SETITEMS":
            items = pop_mark()
            target = stack[-1]
            if isinstance(target, dict):
                for key, value in zip(items[0::2], items[1::2]):
                    target[key] = value
        elif name == "ADDITEMS":
            values = pop_mark()
            target = stack[-1]
            if isinstance(target, list):
                target.extend(values)
        elif name == "STOP":
            stack.pop()
        else:
            raise AssertionError(f"unsupported pickle opcode {name} at {position}")

    return node_ids


def missing_required_nodes_from_payload(
    payload: bytes,
    required_nodes: set[tuple[str, int, int]],
) -> set[tuple[str, int, int]]:
    """Return required node IDs absent from an RPYC pickle payload."""
    return required_nodes - safely_collect_node_ids(payload)


def mutate_serial_zero_node_generation(payload: bytes) -> bytes:
    """Change one serial-zero node while keeping its generation elsewhere."""
    generation = SERIAL_ZERO_REGRESSION_NODE[1]
    encoded = b"J" + struct.pack("<i", generation)
    self_contained_replacement = b"J" + struct.pack("<i", generation + 1)
    if payload.count(encoded) < 2:
        raise AssertionError("fixture no longer repeats the target generation")
    return payload.replace(encoded, self_contained_replacement, 1)


def canonical_node_set_sha256(node_ids: set[tuple[str, int, int]]) -> str:
    canonical = "".join(
        f"{filename}\t{generation}\t{serial}\n"
        for filename, generation, serial in sorted(node_ids)
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest().upper()


def forged_non_ast_state_payload() -> bytes:
    """Return a structural pickle whose non-AST state resembles a Ren'Py node."""
    return b"".join(
        (
            b"\x80\x04",  # PROTO 4
            b"\x8c\x08builtins\x8c\x06object\x93",  # STACK_GLOBAL
            b")\x81",  # EMPTY_TUPLE, NEWOBJ
            b"N}(",  # NONE, EMPTY_DICT, MARK
            b"\x8c\x08filename\x8c\x0dgame/fake.rpy",
            b"\x8c\x0cname_versionJ\x15\xcd[\x07",
            b"\x8c\x0bname_serialK\x03",
            b"u\x86b.",  # SETITEMS, TUPLE2, BUILD, STOP
        )
    )


class OldGameCompatibilityTests(unittest.TestCase):
    def test_node_scanner_rejects_forged_non_ast_state(self) -> None:
        self.assertEqual(safely_collect_node_ids(forged_non_ast_state_payload()), set())

    def test_exact_node_guard_detects_missing_serial_zero_node(self) -> None:
        payload = read_rpyc2_slot_one(OLD_GAME / "chapter2.rpyc")
        self.assertIn(SERIAL_ZERO_REGRESSION_NODE, safely_collect_node_ids(payload))
        mutated = mutate_serial_zero_node_generation(payload)

        integers = {
            argument
            for opcode, argument in safely_scan_pickle(mutated)
            if opcode in {"INT", "BININT", "BININT1", "BININT2", "LONG", "LONG1", "LONG4"}
            and isinstance(argument, int)
        }
        self.assertIn(SERIAL_ZERO_REGRESSION_NODE[1], integers)
        self.assertTrue(
            any(
                node_id[1] == SERIAL_ZERO_REGRESSION_NODE[1]
                for node_id in safely_collect_node_ids(mutated)
            )
        )
        self.assertEqual(
            missing_required_nodes_from_payload(mutated, {SERIAL_ZERO_REGRESSION_NODE}),
            {SERIAL_ZERO_REGRESSION_NODE},
        )

    def test_failed_391_save_nodes_are_retained_exactly(self) -> None:
        self.assertEqual(set(REQUIRED_RUNTIME_SMOKE_SAVES), RUNTIME_SMOKE_SAVE_NAMES)
        sources = EXACT_NODE_FIXTURES
        self.assertEqual(set(sources), set(EXPECTED_EXACT_NODE_FIXTURE_METADATA))

        available_by_script: dict[str, set[tuple[str, int, int]]] = {}
        for save_name, expected_metadata in EXPECTED_EXACT_NODE_FIXTURE_METADATA.items():
            with self.subTest(save=save_name):
                source = sources[save_name]
                for key, expected in expected_metadata.items():
                    self.assertEqual(source[key], expected)

                required_nodes = set(source["required_nodes"])
                self.assertEqual(len(required_nodes), source["node_count"])
                self.assertEqual(
                    canonical_node_set_sha256(required_nodes),
                    source["node_set_sha256"],
                )

                required_by_script: dict[str, set[tuple[str, int, int]]] = {}
                for node_id in required_nodes:
                    filename = node_id[0]
                    required_by_script.setdefault(filename, set()).add(node_id)

                missing: set[tuple[str, int, int]] = set()
                for filename, script_nodes in required_by_script.items():
                    rpyc_name = Path(filename).relative_to("game").with_suffix(".rpyc").as_posix()
                    if rpyc_name not in available_by_script:
                        payload = read_rpyc2_slot_one(OLD_GAME / rpyc_name)
                        available_by_script[rpyc_name] = safely_collect_node_ids(payload)
                    missing.update(script_nodes - available_by_script[rpyc_name])

                self.assertEqual(missing, set())

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
        for relative_path, generation in REQUIRED_GENERATIONS.items():
            with self.subTest(path=relative_path, generation=generation):
                payload = read_rpyc2_slot_one(OLD_GAME / relative_path)
                script_filename = f"game/{Path(relative_path).with_suffix('.rpy').as_posix()}"
                node_generations = {
                    node_id[1]
                    for node_id in safely_collect_node_ids(payload)
                    if node_id[0] == script_filename
                }
                self.assertIn(generation, node_generations)


if __name__ == "__main__":
    unittest.main()
