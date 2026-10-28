# Wiederherstellung der geprüften Reel-Werkzeuge

Stand: 28.10.2026. Diese Sicherung enthält drei aktive Skill-Bündel sowie lokale Aufrufe, genaue Paket-Lockdateien und Herkunftsnachweise. Sie enthält keine Modelle, Binärprogramme, Gesprächsarchive, Videos, Kontodaten oder Zugangsdaten. Bestehende unabhängige Skill-Versionen bleiben in der Git-Historie.

## Einmalige Skill-Ablage

`skillopt-sleep`, `code-kontext` und `hypit` jeweils nur einmal im gemeinsamen Benutzer-Skill-Verzeichnis ablegen. Ein Katalogverweis in `.codex/skills` auf `.agents/skills` ist keine zweite Kopie. Vorhandene gleichnamige Skills nicht ungeprüft überschreiben. Die hier festgehaltene lokale Anbindung nennt Rachids aktuellen Werkzeugpfad; auf einem anderen Rechner muss dieser konkrete Pfad passend angepasst werden.

## Microsoft SkillOpt-Sleep

Original: https://github.com/microsoft/SkillOpt, Commit `e2edfa9721ce41c98e50fa129da87cf1f53c2f7f`. Diesen unveränderten Quellstand unter dem Werkzeugordner als `quelle/` wiederherstellen. Der Aufruf importiert ausschließlich den `skillopt_sleep`-Kern aus der Standardbibliothek; keine pauschale Pip-Installation der optionalen Forschungs-, Weboberflächen- oder fremden Agentenpakete nötig. `python3.11 ausfuehren.py status --project <Projekt>` prüft den Einstieg.

Die Nachtplanung ist eine bestehende Codex-Routine `n-chtliche-skill-optimierung` im führenden Chat. Sie startet nominell täglich 03:00 Uhr in der lokalen Systemzeitzone des ausführenden Macs und bereitet geprüfte Vorschläge vor. Keine zweite Cron-Routine aus dieser Sicherung erzeugen. Eine gesicherte Anweisung beweist keinen bereits erfolgreichen Nachtlauf. Bei einer Wiederherstellung zuerst den vorhandenen Routinenbestand prüfen; die Routine selbst und private Aufgabenexporte werden hier nicht dupliziert.

## Graft / Trail

Originalprojekt: https://github.com/trailhq/Trail-Code. Das festgelegte offizielle Paket ist `@nanonets/graft@0.28.0`; `package-lock.json` hält den aufgelösten Stand fest. Im Werkzeugordner `DO_NOT_TRACK=1 npm ci --ignore-scripts --no-fund --no-audit` verwenden. Der lokale Aufruf setzt `DO_NOT_TRACK=1` dauerhaft für seine Kindprozesse. Damit sind Nutzungsstatistik und automatische Versionsabfragen aus. Keine globalen Hooks oder Mehragenten-Installer sind für die lokale CLI-Navigation nötig. Native Parser sind durch den statischen SkillSpector nicht vollständig abgedeckt; Paketintegrität und dokumentierte Prüfgrenzen beachten.

## Codebase Memory

Original: https://github.com/DeusData/codebase-memory-mcp, Freigabe `v0.12.1`, Commit `a7158ac2f48ca646b4527341b76f930f2aeff87e`. Das offizielle Mac-arm64-Archiv mit dem Hersteller-SHA-256 `9bfcbe38414b47969a3e1d1c1999f5357409387c86fa3d24221b5458267660d2` prüfen und die ausführbare Datei unter `bin/codebase-memory-mcp` bereitstellen. Den passenden Plattformstand auf einem anderen Betriebssystem gesondert prüfen. Die vorhandene Sigstore-Blob-Signatur konnte mit dem vorhandenen gh-Prüfwerkzeug nicht validiert werden; nicht als vollständig geprüfte Provenienz ausgeben. Die Mac-Codesign-Integritätsprüfung war erfolgreich, sie ersetzt keine vollständige Quell-/Malwareprüfung.

Der Aufruf setzt einen eigenen Cache und `CBM_ALLOWED_ROOT` auf das aktuelle Arbeitsverzeichnis. Vor Index-/Graphabfragen in das ausdrücklich bearbeitete Projekt wechseln. Keine globalen Client-Konfigurationen überschreiben und keine fremden laufenden Dienste stoppen. Für den lokalen Prozesskanal müssen die Ausführungsrechte verfügbar sein.

## Hypit

Original: https://github.com/hypit-ai/hypit, Paket `@hypit/hypit@0.3.1`. `package.json` und Lockdatei enthalten vier korrigierte Sicherheitsversionen: sharp 0.35.5, vite 8.2.4, zod 4.6.6 und esbuild 0.28.1. Im Werkzeugordner `npm ci --ignore-scripts --no-fund --no-audit` ausführen. Danach `python3.11 pakete_abgleichen.py --anwenden` verwenden: Drei Hersteller-Manifeste werden auf die tatsächlich geprüften neuen Versionen abgestimmt; die strikte Versionskontrolle selbst bleibt eingeschaltet. Ohne Argument prüft derselbe Helfer den Stand. Anschließend `python3.11 ausfuehren.py version` und eine eigene lokale Probe verwenden.

Die viersekündige lokale Renderprobe wurde mit vorhandenem Chrome und FFmpeg ohne externe Modellanfragen bestanden. Ein neuer Avatar-/Stimm-/Provider-Workflow ist dadurch nicht pauschal geprüft oder bezahlt. Die geänderte Apache-Lizenz erlaubt eigene Unternehmensarbeit; Bedingungen und Urheberhinweise bewahren. Kein Mehrmandanten- oder Weiterverkaufsprodukt aus dieser Sicherung ableiten.

## Tatsächlicher Prüfstand

Die zugänglichen Bündel wurden mit SkillSpector statisch ohne externe KI untersucht. Parserfenster, große Berichtsausgaben und native Programme begrenzen die Abdeckung; zwei große Codebase-Quellläufe wurden ohne fertigen Bericht beendet. Konkrete eingeschränkte Freigaben und Nachprüfungen stehen im lokalen Reel-Prüfprotokoll. Weder „keine bekannten Paketmeldungen“ noch eine bestandene kleine Probe beweisen generelle Fehlerfreiheit, eine feste Einsparquote oder Alltagserfolg.
