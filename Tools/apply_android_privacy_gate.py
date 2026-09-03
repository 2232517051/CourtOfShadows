#!/usr/bin/env python3
"""Install Court of Shadows' native privacy gate into a Ren'Py RAPT tree."""

from __future__ import annotations

import argparse
from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]
OVERLAY = ROOT / "Tools" / "android_privacy"
JAVA_RELATIVE = Path("app/src/main/java/org/renpy/android/ConsentActivity.java")


def copy_file(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def apply(rapt: Path) -> None:
    required = (rapt / "templates", rapt / "prototype" / "app")
    if not all(path.is_dir() for path in required):
        raise SystemExit(f"Not a Ren'Py RAPT directory: {rapt}")

    copy_file(
        OVERLAY / "app-AndroidManifest.xml",
        rapt / "templates" / "app-AndroidManifest.xml",
    )
    for tree in ("prototype", "project"):
        target_root = rapt / tree
        if tree == "project" and not target_root.is_dir():
            continue
        copy_file(OVERLAY / "ConsentActivity.java", target_root / JAVA_RELATIVE)

    print(f"Native privacy gate installed in {rapt}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("rapt", type=Path, help="Path to the SDK's rapt directory")
    args = parser.parse_args()
    apply(args.rapt.resolve())


if __name__ == "__main__":
    main()
