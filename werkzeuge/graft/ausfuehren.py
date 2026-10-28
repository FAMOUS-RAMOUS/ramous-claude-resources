#!/usr/bin/env python3
"""Graft lokal ausführen, ohne Telemetrie oder automatische Versionsprüfung."""
import os
import subprocess
import sys
from pathlib import Path
root = Path(__file__).resolve().parent
env = os.environ.copy()
env["DO_NOT_TRACK"] = "1"
raise SystemExit(subprocess.call(["/opt/homebrew/bin/node", str(root / "node_modules/@nanonets/graft/dist/bin/graft.js"), *sys.argv[1:]], env=env))
