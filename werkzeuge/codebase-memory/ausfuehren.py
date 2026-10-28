#!/usr/bin/env python3
"""Lokale Codebase-Abfragen auf das aktuelle beauftragte Projekt begrenzen."""
import os
import subprocess
import sys
from pathlib import Path
root = Path(__file__).resolve().parent
env = os.environ.copy()
env["CBM_CACHE_DIR"] = str(root / "cache")
env["CBM_ALLOWED_ROOT"] = str(Path.cwd().resolve())
raise SystemExit(subprocess.call([str(root / "bin/codebase-memory-mcp"), *sys.argv[1:]], env=env))
