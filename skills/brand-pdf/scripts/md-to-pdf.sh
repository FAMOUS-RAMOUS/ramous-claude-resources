#!/usr/bin/env bash
# md-to-pdf.sh — Konvertiert eine Markdown-Datei in eine schöne, brand-konforme PDF.
#
# Verwendung:
#   ./scripts/md-to-pdf.sh <pfad-zur-md-datei>
#
# Beispiel:
#   ./scripts/md-to-pdf.sh outputs/mef/01-pitch/mef-start-pilot-pitch.md
#
# Die PDF wird im selben Ordner abgelegt wie das Markdown.
# Engine: Typst · Template: templates/famous-ramous.typ (Brand CI Gold/Schwarz/Weiß).

set -e

if [ -z "$1" ]; then
  echo "Fehler: Bitte gib die Markdown-Datei an."
  echo "Beispiel: ./scripts/md-to-pdf.sh outputs/mef/01-pitch/mef-start-pilot-pitch.md"
  exit 1
fi

INPUT="$1"

if [ ! -f "$INPUT" ]; then
  echo "Fehler: Datei nicht gefunden: $INPUT"
  exit 1
fi

# Skill-Wurzel (Verzeichnis, in dem dieses Skript liegt → eine Ebene höher)
SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEMPLATE="$SKILL_DIR/templates/famous-ramous.typ"

# Typst-Root ist "/", damit Eingabedateien überall liegen dürfen.
# Logo daher als absoluter Pfad (Typst löst ihn relativ zu --root auf).
LOGO="$SKILL_DIR/Logo/Famous_Ramous_Logo_gold_trans.png"

OUTPUT="${INPUT%.md}.pdf"

pandoc "$INPUT" \
  -o "$OUTPUT" \
  --pdf-engine=typst \
  --pdf-engine-opt="--root=/" \
  --template="$TEMPLATE" \
  -V logo="$LOGO" \
  -V papersize=a4

echo "✅ PDF erstellt: $OUTPUT"
