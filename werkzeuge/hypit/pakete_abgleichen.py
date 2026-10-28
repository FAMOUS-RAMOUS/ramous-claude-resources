#!/usr/bin/env python3
"""Die geprüften Hypit-Abhängigkeiten mit den strikten Manifestprüfungen abgleichen."""
import json
import sys
from pathlib import Path
root = Path(__file__).resolve().parent
apply = sys.argv[1:] == ["--anwenden"]
if sys.argv[1:] not in ([], ["--anwenden"]):
    raise SystemExit("Ohne Argument prüfen; --anwenden trägt die geprüften Versionsdeklarationen ein.")
for row in json.loads((root / "Versionskorrekturen.json").read_text()):
    name = row["paket"]
    if "/" in name or name in {".", ".."}:
        raise SystemExit("Ungültiger Paketname")
    path = root / "node_modules" / "@hypit" / name / "package.json"
    data = json.loads(path.read_text())
    changed = False
    for dep, versions in row["änderungen"].items():
        wanted = versions["nachher"]
        installed = json.loads((root / "node_modules" / dep / "package.json").read_text())["version"]
        if installed != wanted:
            raise SystemExit(f"{dep}: erwartet {wanted}, installiert {installed}")
        found = False
        for section in ("dependencies", "optionalDependencies"):
            deps = data.get(section, {})
            if dep not in deps:
                continue
            found = True
            if deps[dep] not in (versions["vorher"], wanted):
                raise SystemExit(f"{name}: unbekannte Deklaration für {dep}")
            changed |= deps[dep] != wanted
            deps[dep] = wanted
        if not found:
            raise SystemExit(f"{name}: erwartete Abhängigkeit fehlt")
    if changed and not apply:
        raise SystemExit(f"{name}: geprüfte Anpassung steht aus; --anwenden verwenden")
    if changed:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print(f"{name}: geprüfte Versionen stimmen überein")
