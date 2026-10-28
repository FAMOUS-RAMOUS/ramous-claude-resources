---
name: skillopt-sleep
description: "Verbessert vorhandene Skills anhand bestätigter wiederkehrender Korrekturen mit Microsoft SkillOpt-Sleep. Bei „Skills verbessern“, „SkillOpt“, „Schlafzyklus“ oder ausdrücklich gewünschter Auswertung vergangener Aufgaben nutzen."
---

# Skills anhand der Nutzung verbessern

Verwende die geprüfte lokale SkillOpt-Sleep-Einrichtung unter `/Users/famous_ramous/Documents/Codex/2026-10-27/ki-systemoptimierung/werkzeuge/skillopt/`. Quelle und festgelegter Commit stehen dort in `QUELLE.json`. Lade bei Bedarf die Herstelleranleitung `quelle/plugins/codex/skills/skillopt-sleep/SKILL.md` und `quelle/docs/sleep/README.md`.

## Ablauf

1. Auftrag, zuständiges Projekt und vorhandenen Zielskill feststellen. Keine parallele Regelsammlung oder doppelten aktiven Skill anlegen. Bestätigte wiederkehrende Korrekturen und tatsächlich beobachtete Ergebnisse verwenden; Werbeversprechen und Einzelfälle sind kein allgemeiner Erfolgsnachweis.
2. `python3.11 <Werkzeugpfad>/ausfuehren.py status --project <Projekt>` zeigt den Stand. Für reale Aufgaben zunächst lokal `harvest --project <Projekt> --source codex --target-skill-path <Ziel-SKILL.md> --max-sessions 3 --max-tasks 4 --output <Aufgabendatei.json>` verwenden. Der Hersteller liest Codex-Archive; fehlende Archivdaten nicht als erfolgreiche Auswertung darstellen.
3. Aufgaben vor einem Modelllauf lesen und nötigenfalls auf das autorisierte Material beschränken oder schwärzen. Nur den geprüften Aufgabenexport mit `reviewed: true` und `--tasks-file` für echte Modellläufe verwenden. Keine kompletten privaten Gesprächsverläufe, Kundendaten, Zugangsdaten oder Rohbelege in GitHub sichern. Ein Export mit `reviewed: true` ersetzt nicht die tatsächliche Prüfung.
4. `dry-run --project <Projekt> --target-skill-path <Ziel-SKILL.md> --backend mock --tasks-file <Datei> --json` prüft den technischen Ablauf ohne Modellaufruf. Für die beauftragte Optimierung `run` mit `--backend codex`, denselben geprüften Aufgaben und begrenzter Aufgabenzahl verwenden; das nutzt das bestehende Codex-Kontingent. Kein Modell-Override setzen. `handoff` ist für getrennte frische Kontexte vorgesehen, nicht für eine selbst bewertete Antwort im laufenden Kontext.
5. Bericht, ursprüngliche und vorgeschlagene Anweisung vergleichen: unabhängige Prüfaufgaben, Ausgangs-/Endwerte, einzelne Verschlechterungen, Quellenumfang und Grenzen nennen. Vor Übernahme geändertes vollständiges Bündel mit vorhandenem SkillSpector prüfen. Konkrete bestehende Auftragsfreigaben nutzen; keine erneute Freigabe für bereits beauftragte harmlose Verbesserungen verlangen. Ungeklärte relevante Risiken nur im betroffenen Schritt klären.
6. Bestandssicherung und Hashprüfung erhalten; akzeptierte, geprüfte Änderungen über den Engine-Befehl `adopt` mit expliziter Auswahl übernehmen, anschließend tatsächliche Datei zurücklesen und im vorhandenen GitHub-Repository sichern. Kein Umgehen einer abgelehnten Validierung durch manuelles Übertragen desselben Vorschlags. Nur übertragbare, belegte Änderungen übernehmen.

Der lokale Aufruf setzt `evolve_memory=false`, `gate_mode=on`, `gate_no_regression=true`, höchstens vier Aufgaben, vier Textänderungen und keine automatische Übernahme. So werden weder fremde CLAUDE.md-Regeln erzeugt noch laufende Dateien unbemerkt geändert. Einen automatischen Nachtlauf nur bei ausdrücklich beauftragter Zeitplanung über die vorhandene Codex-Automationsfunktion einrichten; keine zweite Cron-Routine. Installation und einmaliger Test allein sind noch keine eingerichtete Nacht-Automation.

## Ausgabe und Selbstcheck

Deutsch berichten: ausgewertete Quelle/Aufgaben, tatsächlich geprüfter Skill, konkreter Vorschlag, Prüfwerte, Übernahmestatus, Speicher- und GitHub-Readback. Prüfen: Waren Aufgaben wirklich getrennt? Stammt die Verbesserung aus dem echten Modelllauf oder nur dem simulierten `mock`-Test? Sind bestandene Tests von Bewährung im Alltag getrennt? Keine pauschalen Faktoren wie „zehnmal besser“ zusagen.
