#!/usr/bin/env python3
"""Lokaler Aufruf für den geprüften Microsoft-Sleep-Kern, ohne Zusatzpakete."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "quelle"))

def main():
    args = sys.argv[1:]
    if not args or args[0] not in {"status", "harvest", "dry-run", "run", "adopt"}:
        raise SystemExit("Erlaubt: status, harvest, dry-run, run, adopt. Zeitplanung erfolgt über Codex.")
    if "--auto-adopt" in args:
        raise SystemExit("Änderungen nach Prüfung über adopt übernehmen.")
    if args[0] in {"run", "dry-run"}:
        backend = args[args.index("--backend") + 1] if "--backend" in args else "mock"
        if backend not in {"mock", "codex", "handoff"}:
            raise SystemExit("Hier eingerichtet: mock, codex oder handoff.")
        if backend != "mock" and "--tasks-file" not in args:
            raise SystemExit("Vor dem Modelllauf geprüften Aufgabenexport mit --tasks-file angeben.")
    from skillopt_sleep import __main__ as cli
    original = cli.load_config
    def scoped_config(**overrides):
        cfg = original(**overrides)
        cfg.data.update({"evolve_memory": False, "gate_mode": "on",
                         "gate_no_regression": True, "auto_adopt": False,
                         "state_dir": str(ROOT / "zustand"), "evidence_log": False,
                         "max_tasks_per_night": min(int(cfg.get("max_tasks_per_night", 4)), 4),
                         "max_tokens_per_night": 60000, "edit_budget": min(int(cfg.get("edit_budget", 4)), 4),
                         "model": "", "optimizer_model": "", "target_model": ""})
        return cfg
    cli.load_config = scoped_config
    return cli.main(args)

if __name__ == "__main__":
    raise SystemExit(main())
