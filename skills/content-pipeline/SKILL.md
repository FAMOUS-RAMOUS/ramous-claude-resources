---
name: content-pipeline
description: Orchestriert die vollständige Content-Pipeline aus eigenen Aufnahmen, YouTube-Videos oder Texten aus der Wissensdatenbank. Produziert Social-Media-Posts, Karussell-Slides und bereitet Video-Clips vor. Trigger: "Content Pipeline", "verarbeite mein Video", "mach Content aus", "erstelle Content aus meiner Aufnahme".
---

Führe die vollständige Content-Pipeline für eigene Inhalte durch.

**Unterschied zu interview-content-pipeline:** Dieser Orchestrator verarbeitet EIGENEN Content von Rachid (Wissen, Erfahrungen, Aufnahmen). Die interview-content-pipeline ist für Kundenstimmen und Interviews.

## Trigger-Beispiele
- „Content Pipeline: [Datei/URL]"
- „Verarbeite mein Video: [Pfad]"
- „Mach Content aus diesem Text: [Text]"
- „Erstelle Slides und Posts aus meiner Aufnahme"

## Input-Typen
- **A – eigene Audio/Video-Datei:** lokaler Pfad (.mp3, .m4a, .mp4, .mov)
- **B – YouTube-URL:** eigenes Video oder referenziertes Video
- **C – Text:** Artikel, Notiz, Wissensdatenbank-Eintrag

---

## Pipeline

### Schritt 1: Transkription
*Nur bei Input A oder B. Bei Text (C) direkt zu Schritt 2.*

Lade den `/transkription` Skill.
- Input: Dateipfad oder URL
- Output: Strukturiertes Transkript mit Zeitstempeln

---

### ✋ CHECKPOINT 1 (nur bei A/B)
Zeige das Transkript.
Frage: **„Transkript passt? Soll ich fortfahren?"**
→ Warte auf Bestätigung.

---

### Schritt 2: Content-Analyse
Lade den `/content-analyse` Skill.
- Input: Transkript oder Text
- Output: Kerninsights, Hooks, Clip-Momente, Content-Winkel

---

### ✋ CHECKPOINT 2
Zeige die vollständige Content-Analyse.
Frage: **„Stimmen die Kerninsights? Welche Formate soll ich erstellen?"**

Zeige Auswahl:
```
[ ] Instagram (Posts)
[ ] Facebook (Post)
[ ] LinkedIn (Kurzform-Post)
[ ] LinkedIn (Karussell-Slides)
[ ] Instagram (Karussell-Slides)
[ ] X (Twitter/Thread)
[ ] Alle
```
→ Warte auf Bestätigung und Format-Auswahl.

---

### Schritt 3: Content-Erstellung

Lade `/schreibstil` als Basis für Tonalität.

**Für Social Posts (Instagram, Facebook, LinkedIn-Post, X):**
→ Lade `/social-post` Skill
- Input: Content-Analyse + gewählte Plattformen

**Für Karussell-Slides (LinkedIn oder Instagram):**
→ Lade `/slides` Skill
- Input: Content-Analyse + Zielplattform
- Beide Plattformen können parallel erstellt werden

**Für Video-Clips:** *(noch nicht verfügbar)*
→ Markiere die clip-würdigen Momente aus der Content-Analyse mit Zeitstempeln für manuelle Weiterverarbeitung.

---

### ✋ CHECKPOINT 3
Zeige alle fertigen Outputs.
Frage: **„Hier ist dein Content. Was möchtest du anpassen?"**

---

### Schritt 4: Finale Ausgabe

```
════════════════════════════════════════
📱 INSTAGRAM (Post)
[Post + Hashtags]

📘 FACEBOOK
[Post]

💼 LINKEDIN (Post)
[Post]

🎠 LINKEDIN (Karussell)
[Slide 1–N]

🎠 INSTAGRAM (Karussell)
[Slide 1–N]

🐦 X
[Tweet / Thread]

🎬 VIDEO-CLIP-MOMENTE
[Zeitstempel + Begründung]
════════════════════════════════════════
```

Biete an, die Outputs zu speichern:
`~/Documents/Content/[YYYY-MM-DD]-[Thema].md`

---

## Geteilte Skills (wiederverwendet aus System 1)
| Skill | Funktion |
|---|---|
| `transkription` | Audio/Video → Text |
| `social-post` | Text → Plattform-Posts |
| `schreibstil` | Tonalität / Stimme |

## Neue Skills dieses Systems
| Skill | Funktion |
|---|---|
| `content-analyse` | Eigenen Content → Insights + Hooks |
| `slides` | Insights → Karussell-Slides |
