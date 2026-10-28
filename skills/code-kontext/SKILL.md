---
name: code-kontext
description: "Erschließt ausdrücklich bearbeitete Software-Repositories mit lokalem Graft/Trail und Codebase Memory. Bei Code-Architektur, Aufrufketten, betroffenen Dateien oder wiederholter Code-Navigation nutzen; kein allgemeines Gedächtnis für Bücher oder private Dokumente."
---

# Lokaler Code-Kontext

Die geprüften Werkzeuge ergänzen vorhandene Projektdateien und Übergaben. Graft/Trail liefert eine lokale Codekarte und Suchkontext; Codebase Memory liefert strukturierte Graphabfragen. Sie ersetzen keine handwerkliche Prüfung der Quellstellen und garantieren keine Token-Einsparquote.

Werkzeugpfad: `/Users/famous_ramous/Documents/Codex/2026-10-27/ki-systemoptimierung/werkzeuge/`. Die tatsächlichen Versionen, Prüfungen und Grenzen stehen je Werkzeug in `QUELLE.json` und im bestehenden Prüfprotokoll `work/Reel-Serie-2026-10-28/02/`.

## Verwendung

- Nur das ausdrücklich bearbeitete Code-Projekt indexieren. Vorhandenen Index und Aktualität prüfen; nicht bei jeder Frage neu aufbauen. Keine Wissensdatenbank, Belegordner, fremden laufenden Arbeitsbereiche oder ganzen Benutzerordner einlesen.
- Graft über `python3.11 <Werkzeugpfad>/graft/ausfuehren.py <Argumente>` aufrufen. Zuerst `build <Projekt>` (deterministisch), dann `ask <Frage> <Projekt> --json`, `map`, `callers` oder `skeleton` verwenden. Telemetrie und automatische Versionsabfragen bleiben durch `DO_NOT_TRACK=1` aus. Kein `--deep` oder Cloud-Workspace allein für lokale Navigation verbinden.
- Codebase Memory über `python3.11 <Werkzeugpfad>/codebase-memory/ausfuehren.py cli <Werkzeug> <Argumente>` verwenden. `cli index_repository --help`, `cli search_graph --help`, `cli trace_call_path --help` liefern die zur installierten Version passenden Argumente. Auf das Zielprojekt begrenzen; lokale Anbindung setzt den zulässigen Stamm auf das aufgerufene Arbeitsverzeichnis, nicht auf den ganzen Mac. Vorher in das beauftragte Projekt wechseln.
- Zuerst das für die Frage passendere Werkzeug benutzen, das zweite nur bei Zusatznutzen. Keine doppelten automatischen Hooks/Watcher oder mehrere aktive Skill-Kopien einrichten. CLI-Abfragen benötigen keinen Neustart der übrigen Prozesse.
- Konkrete Ergebnisse auf die echten Quelldateien zurückführen. Änderungen können einen vorhandenen Index veralten lassen; dann gezielt nachführen. Herstellermessungen nicht als eigene gemessene Einsparung ausgeben.

## Selbstcheck

Sind nur beauftragte Quelldateien erschlossen? Ist der Index aktuell und der Dateiverweis korrekt? Ist die Antwort im Quellcode belegt? Sind lokale Verarbeitung, Modellantwort und optionale externe Funktionen sauber unterschieden? Technische Funktionsprobe und gemessene Alltagseinsparung getrennt berichten.
