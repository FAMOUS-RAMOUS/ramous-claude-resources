---
name: interview-content-pipeline
description: Orchestriert die vollständige Content-Pipeline aus Interview-Aufnahmen, YouTube-URLs oder Google-Rezensionen. Produziert Social-Media-Posts und LinkedIn-Artikel. Trigger: "Erstelle Content aus Interview", "verarbeite Interview", "Interview zu Posts", "Rezension zu Content".
---

Führe die vollständige Interview → Content Pipeline durch.

## Trigger-Beispiele
- "Erstelle Content aus diesem Interview: [Datei/URL]"
- "Verarbeite diese Google-Rezension: [Text]"
- "Interview zu Posts: [Input]"

## Input-Typen
- **A – Audio/Video-Datei:** lokaler Pfad (.mp3, .m4a, .mp4, .mov)
- **B – YouTube-URL:** Link zum Video
- **C – Text:** Google-Rezension oder bereits vorhandener Interviewtext

---

## Pipeline

### Schritt 1: Transkription
*Nur bei Input A oder B. Bei Text (C) direkt zu Schritt 2.*

Lade den `/transkription` Skill.
- Input: Dateipfad oder URL
- Output: Strukturiertes Transkript mit Zeitstempeln

---

### ✋ CHECKPOINT 1 (nur bei A/B)
Zeige das vollständige Transkript.
Frage: **"Transkript sieht gut aus? Soll ich fortfahren, oder gibt es Korrekturen?"**
→ Warte auf Bestätigung bevor Schritt 2 startet.

---

### Schritt 2: Content-Extraktion
Lade den `/content-extraktion` Skill.
- Input: Transkript (aus Schritt 1) oder Originaltext (bei C)
- Output: Strukturierte Extraktion mit Kernbotschaft, Zitaten, Story-Bogen, Headlines

---

### ✋ CHECKPOINT 2
Zeige die vollständige Content-Extraktion.
Frage: **"Stimmen die Kernaussagen und Zitate? Und: Für welche Plattformen soll ich Content erstellen?"**

Zeige Auswahl:
```
[ ] Instagram
[ ] Facebook
[ ] LinkedIn (Kurzform-Post)
[ ] LinkedIn (langer Artikel)
[ ] X (Twitter)
[ ] Alle
```
→ Warte auf Bestätigung und Plattform-Auswahl.

---

### Schritt 3: Content-Erstellung

Lade `/schreibstil` als Basis für Tonalität.

**Für Instagram, Facebook, LinkedIn-Post, X:**
→ Lade `/social-post` Skill
- Input: Content-Extraktion + gewählte Plattformen

**Für LinkedIn-Artikel:**
→ Lade `/linkedin-artikel` Skill
- Input: Content-Extraktion + Transkript

Beide können parallel laufen wenn beides gewählt wurde.

---

### ✋ CHECKPOINT 3
Zeige alle fertigen Outputs.
Frage: **"Hier sind deine fertigen Inhalte. Was möchtest du anpassen?"**

---

### Schritt 4: Finale Ausgabe

Präsentiere alle Outputs übersichtlich formatiert:

```
════════════════════════════════════════
📱 INSTAGRAM
[Post + Hashtags]

📘 FACEBOOK
[Post]

💼 LINKEDIN (Post)
[Post]

📝 LINKEDIN (Artikel)
[Artikel]

🐦 X
[Tweet / Thread]
════════════════════════════════════════
```

Biete an, die Outputs als Markdown-Datei zu speichern:
`~/Documents/Content/[YYYY-MM-DD]-[Thema].md`

---

## Skill-Übersicht dieses Systems
| Skill | Aufgabe |
|---|---|
| `transkription` | Audio/Video → Text |
| `content-extraktion` | Text → Struktur + Zitate |
| `social-post` | Struktur → Plattform-Posts |
| `linkedin-artikel` | Struktur → Langform-Artikel |
| `schreibstil` | Tonalität / Stimme (shared) |
