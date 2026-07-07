---
name: neues-projekt
description: Legt ein neues Projekt in der zentralen Projektstruktur ~/Claude/projekte/ an (Ordner mit dateien/, outputs/ und PROJEKT.md). Diesen Skill IMMER nutzen, wenn der User ein neues Projekt starten will – z. B. bei "Neues Projekt", "lege ein Projekt an", "erstelle ein Projekt für …", "starte ein Projekt", "ich will an etwas Neuem arbeiten" – auch wenn das Wort "Projekt" nur beiläufig fällt und noch kein Name genannt wurde.
---

# Neues Projekt anlegen

Alle Projekte von Rachid liegen zentral unter `~/Claude/projekte/` (siehe Memory „Ordnersystem Claude"). Dieser Skill legt dort ein neues Projekt an – mit derselben Logik wie der Shell-Befehl `~/Claude/neues-projekt.sh`.

## Schritt 1: Projektnamen bestimmen

- Nimm den Namen aus der Nachricht des Users (z. B. „Neues Projekt Kalenderplanung" → `kalenderplanung`).
- Wandle ihn um: Kleinbuchstaben, Leerzeichen → Bindestriche. Umlaute (ä, ö, ü, ß) bleiben erhalten – niemals als ae/oe/ue/ss umschreiben.
- **Kein Name genannt?** Frage kurz nach: „Wie soll das Projekt heißen?" – nicht raten.

## Schritt 2: Projekt anlegen

Nutze die bestehende Shell-Funktion, damit Terminal-Befehl und Skill immer identisch arbeiten:

```bash
source ~/Claude/neues-projekt.sh && neues-projekt <name>
```

Das erzeugt:

```
~/Claude/projekte/JJJJ-MM_<name>/
├── dateien/     ← Eingangsmaterial des Users
├── outputs/     ← Ergebnisse
└── PROJEKT.md   ← Ziel, Stand, nächste Schritte
```

- Meldet die Funktion „Projekt existiert schon", dann kein neues anlegen – dem User sagen, dass es das Projekt bereits gibt, und direkt damit weiterarbeiten.
- Falls das Script fehlen sollte (Fallback): Struktur mit `mkdir -p` und der PROJEKT.md-Vorlage von Hand anlegen, exakt wie oben.

## Schritt 3: PROJEKT.md ausfüllen

Hat der User schon beschrieben, worum es geht, trage es direkt ein:
- **Ziel:** in 1–2 Sätzen aus der Beschreibung des Users
- **Aktueller Stand:** „Projekt angelegt am [Datum]" plus was schon vorliegt
- **Nächste Schritte:** erste konkrete Schritte als Checkboxen, falls ableitbar

Nichts erfinden – was der User nicht gesagt hat, bleibt leer.

## Schritt 4: Bestätigen

Antworte auf Deutsch, kurz:
- Pfad des neuen Projekts
- Was in PROJEKT.md steht
- Frage, ob es direkt losgehen soll

**Beispiel:**
User: „Neues Projekt Sommer-Challenge – ich will eine 6-Wochen-Challenge für meine Klienten planen."
→ Anlegen von `~/Claude/projekte/2026-07_sommer-challenge/`, Ziel in PROJEKT.md eintragen („6-Wochen-Challenge für Klienten planen"), bestätigen und fragen, womit gestartet werden soll.
