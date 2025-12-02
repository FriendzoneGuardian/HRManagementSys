#!/usr/bin/env python3
"""
Quick installer script for this project.

What it does:
- Creates a virtual environment at `.venv` (if missing)
- Upgrades `pip` inside the venv
- Installs packages from `requirements.txt`

Usage:
  python scripts/quick_install.py         # default install
  python scripts/quick_install.py --dev   # also install dev extras (if present)

This script is cross-platform (Windows / macOS / Linux).
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VENV_DIR = ROOT / ".venv"
REQUIREMENTS = ROOT / "requirements.txt"


def run(cmd: list[str], check=True):
    print("+ ", " ".join(cmd))
    return subprocess.run(cmd, check=check)


def get_pip_executable(venv: Path) -> Path:
    if os.name == "nt":
        return venv / "Scripts" / "pip.exe"
    return venv / "bin" / "pip"


def ensure_venv(venv: Path):
    if not venv.exists():
        print(f"Creating virtual environment at {venv}")
        run([sys.executable, "-m", "venv", str(venv)])
    else:
        print(f"Using existing virtual environment at {venv}")


def install_requirements(pip_exe: Path, dev: bool):
    run([str(pip_exe), "install", "--upgrade", "pip"]) 
    if REQUIREMENTS.exists():
        print(f"Installing from {REQUIREMENTS}")
        run([str(pip_exe), "install", "-r", str(REQUIREMENTS)])
    else:
        print("requirements.txt not found — skipping requirements install")

    if dev:
        dev_file = ROOT / "requirements-dev.txt"
        if dev_file.exists():
            print(f"Installing dev packages from {dev_file}")
            run([str(pip_exe), "install", "-r", str(dev_file)])
        else:
            print("No requirements-dev.txt found — nothing extra to install")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dev", action="store_true", help="Install dev extras from requirements-dev.txt if present")
    args = parser.parse_args()

    ensure_venv(VENV_DIR)

    pip_exe = get_pip_executable(VENV_DIR)
    if not pip_exe.exists():
        print("pip executable not found in venv — something went wrong creating the venv.")
        return 2

    try:
        install_requirements(pip_exe, args.dev)
    except subprocess.CalledProcessError as e:
        print("Command failed:", e)
        return 3

    activate_hint = "`.\\.venv\\Scripts\\Activate.ps1`" if os.name == "nt" else "`source .venv/bin/activate`"
    print("\nDone. To activate the virtual environment use:")
    print(activate_hint)
    print("Then run your Flask app or other commands inside the venv.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
