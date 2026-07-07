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

**Für Video-Clips:**
→ Markiere die clip-würdigen Momente aus der Content-Analyse mit Zeitstempeln für manuelle Weiterverarbeitung. (Automatischer Schnitt folgt, sobald Remotion/Node.js eingerichtet ist – siehe offene Baustelle im Memory.)

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
`~/Claude/outputs/content/[YYYY-MM-DD]-[Thema].md`
Existiert die Datei bereits (z. B. weil die Interview-Pipeline am selben Tag dasselbe Thema hatte), NIE überschreiben – stattdessen `-2`, `-3` … anhängen.

---

### Schritt 5: Bilder (optional)

Frage: **„Soll ich passende Bilder zu den Posts generieren?"**
Wenn ja → Lade den `/bild-generator` Skill.
- Input: die fertigen Post-Texte + gewählte Plattformen (bestimmt die Formate)
- Voraussetzung: `GOOGLE_API_KEY` gesetzt und Billing aktiv – wenn nicht, kurz erklären was fehlt und diesen Schritt überspringen

---

## Genutzte Skills
| Skill | Funktion |
|---|---|
| `transkription` | Audio/Video → Text |
| `content-analyse` | Eigener Content → Insights + Hooks |
| `schreibstil` | Tonalität / Stimme |
| `social-post` | Text → Plattform-Posts |
| `slides` | Insights → Karussell-Slides |
| `bild-generator` | Post → Bild (optional, Schritt 5) |
