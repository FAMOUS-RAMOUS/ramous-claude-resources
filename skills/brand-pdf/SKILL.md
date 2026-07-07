---
name: brand-pdf
description: Konvertiert Markdown-Dateien in brand-konforme PDFs im Famous-Ramous-Design (Gold #C9A14A, Schwarz, Weiß, Logo, Footer „EHRLICH. GESUND. STARK."). Diesen Skill nutzen bei: "mach ein PDF daraus", "Brand-PDF", "PDF im Famous-Ramous-Design", "schönes PDF für Kunden/Pitch" – immer wenn aus Text/Markdown ein professionelles, gebrandetes PDF-Dokument entstehen soll (Pitches, Reports, Trainingspläne, Handouts).
---

# Brand-PDF (Famous Ramous Design)

Erzeugt aus einer Markdown-Datei ein PDF im Famous-Ramous-Corporate-Design: Gold/Schwarz/Weiß, Logo oben, Brand-Footer, saubere Typografie.

## Ausführung

```bash
~/.claude/skills/brand-pdf/scripts/md-to-pdf.sh "[Pfad-zur-md-Datei]"
```

- Das PDF landet im selben Ordner wie die Markdown-Datei (gleicher Name, `.pdf`).
- Liegt der Inhalt noch nicht als Datei vor: zuerst als `.md` speichern (bei Projekten nach `~/Claude/projekte/[Projekt]/outputs/`, sonst nach `~/Claude/outputs/`), dann konvertieren.

## Voraussetzungen

`pandoc` und `typst` (beide via Homebrew installiert). Falls ein Aufruf mit „command not found" scheitert: `brew install pandoc typst`.

## Bestandteile (im Skill-Ordner, zusammenhalten!)

| Datei | Zweck |
|---|---|
| `scripts/md-to-pdf.sh` | Konvertierung (pandoc → Typst) |
| `templates/famous-ramous.typ` | Brand-Template (Farben, Fonts, Footer, Logo-Einbindung) |
| `Logo/Famous_Ramous_Logo_gold_trans.png` | Standard-Logo (transparent) |
| `Logo/Famous_Ramous_Logo_goldaufblack.png` | Alternative für dunkle Designs |

Die relativen Pfade im Script hängen an dieser Struktur – Dateien nicht einzeln verschieben.

## Hinweise

- Markdown-Features: Überschriften, Listen, Tabellen, Fett/Kursiv funktionieren; sehr breite Tabellen vorher aufteilen.
- Nach der Erstellung das PDF kurz öffnen/prüfen (erste Seite), bevor es an den User geht.
- Anpassungen am Design (Farben, Footer-Claim) im `.typ`-Template vornehmen, nicht im Script.
