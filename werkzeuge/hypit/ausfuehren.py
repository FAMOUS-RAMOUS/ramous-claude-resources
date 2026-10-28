#!/usr/bin/env python3
"""Die geprüfte lokale Hypit-Version verwenden, keine automatische Neuinstallation."""
from pathlib import Path
import os
import subprocess
import sys
root = Path(__file__).resolve().parent
env = os.environ.copy()
env["DO_NOT_TRACK"] = "1"
raise SystemExit(subprocess.call(["/opt/homebrew/bin/node", str(root / "node_modules/@hypit/hypit/bin/hypit.mjs"), *sys.argv[1:]], env=env))
