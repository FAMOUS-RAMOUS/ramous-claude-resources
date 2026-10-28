#!/usr/bin/env python3
"""Lokalen PPT-Master-Helfer mit fester Python-Umgebung starten."""
from pathlib import Path
import os
import subprocess
import sys

def main():
    if len(sys.argv) < 2:
        print('Aufruf: ausfuehren.py <Skript unter scripts/> [Argumente]', file=sys.stderr)
        return 2
    base=Path(__file__).resolve().parent
    scripts=(base/'skills/ppt-master/scripts').resolve()
    script=(scripts/sys.argv[1]).resolve()
    lokale_konverter={
        'attribution_guard.py',
        'source_to_md/pdf_to_md.py',
        'svg_quality_checker.py',
        'svg_to_pptx.py',
    }
    if sys.argv[1] not in lokale_konverter:
        print('Dieser Aufruf ist für die eingerichteten lokalen PDF-/Folienkonverter bestimmt.',file=sys.stderr)
        return 2
    if not script.is_relative_to(scripts) or not script.is_file() or script.suffix!='.py':
        print('Das angegebene Python-Skript gehört nicht zur installierten PPT-Master-Ablage.',file=sys.stderr)
        return 2
    python=base/'umgebung/bin/python'
    if not python.is_file():
        print('Die lokale Python-Umgebung fehlt.',file=sys.stderr)
        return 2
    # Bestehende API-Schlüssel und Python-Suchpfade nicht an lokale Konverter erben.
    keys=('PATH','HOME','LANG','LC_ALL','LC_CTYPE','TMPDIR','SYSTEMROOT','WINDIR')
    env={key:os.environ[key] for key in keys if key in os.environ}
    env['PYTHONDONTWRITEBYTECODE']='1'
    env['PYTHONNOUSERSITE']='1'
    return subprocess.run([str(python),'-B',str(script),*sys.argv[2:]],env=env,check=False).returncode

if __name__=='__main__':
    raise SystemExit(main())
