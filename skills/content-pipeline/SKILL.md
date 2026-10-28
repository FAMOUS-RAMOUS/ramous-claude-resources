---
name: content-pipeline
description: "Orchestriert die vollständige Content-Pipeline aus eigenen Aufnahmen, YouTube-Videos oder Texten aus der Wissensdatenbank. Produziert Social-Media-Posts, Karussell-Slides und bereitet Video-Clips vor. Trigger: \"Content Pipeline\", \"verarbeite mein Video\", \"mach Content aus\", \"erstelle Content aus meiner Aufnahme\"."
---

## Gespeicherte Gestaltungseffekte für Rachids Videos

Bei einer neuen Videoübergabe den vorhandenen Skill `videoeffekte` unter `/Users/famous_ramous/.agents/skills/videoeffekte/SKILL.md` berücksichtigen. Er enthält die sechs gewünschten Effekte und die einmalige Auswahl-/Vorschau-Regel. Bei Video-Bearbeitung oder Content-Erstellung vor der Gestaltung laden; eine nötige Frage in die vorhandene Format-/Effektauswahl integrieren, nicht doppelt fragen. Ein bereits erteilter Ausprobierauftrag führt direkt zum dort beschriebenen Vergleich aller sechs Varianten. Bei bloßen Lern-/Referenzreels zuerst die Quelle auswerten und die Anwendung auf eigene Videos anbieten; fremdes Material nicht ungefragt als eigenes Veröffentlichungsvideo bearbeiten. Bestehendes Werkzeug und konkrete Freigaben beibehalten. Gespeicherte Effekte sind keine Zusage bereits fertig implementierter Render-Vorlagen.

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

## Eine Quelle, passende Formate

Bei mehreren beauftragten Ausgaben ein gemeinsames Quellenpaket und den aktuellen bestätigten Stil aus `schreibstil` verwenden. Nach der Content-Analyse die tragfähigen Aussagen oder Szenen auswählen; pro Beitrag eine klare Hauptaussage mit ihrem Beleg und ihrer Funktion für den Auftrag bestimmen. Eine Liste mit drei bis sieben Kandidaten kann bei umfangreichem Material helfen, ist keine Pflichtausgabe.

Den Inhalt je Plattform eigenständig aufbauen: Kurzvideo als gesprochene Aussage mit sichtbarem Beleg, Karussell als nachvollziehbare Folge, Artikel als vertiefte Argumentation. Keine identische Langfassung überall einkürzen und dabei Belege, Einschränkungen oder Bedeutung verlieren. Rachids Stimme bleibt gleich; Einstieg, Umfang und Darstellung dürfen sich ändern.

Vor der Ausgabe zusammengehörige Formate gegeneinander prüfen: Stimmen Zahlen, Quellen, Kernaussage und Einschränkungen überein? Wiederholen sich Beiträge ohne zusätzlichen Nutzen? Nur die beauftragten Formate liefern; Reihenfolge oder Veröffentlichungsplan nur bei entsprechendem Auftrag ergänzen. Die vorhandenen Checkpoints und Veröffentlichungsfreigaben bleiben maßgeblich.

## Pipeline

### Schritt 1: Transkription
*Nur bei Input A oder B. Bei Text (C) direkt zu Schritt 2.*

Lade den `/transkription` Skill.
- Input: Dateipfad oder URL
- Output: Strukturiertes Transkript mit Zeitstempeln

---

### ✋ CHECKPOINT 1 (nur bei A/B)
Verlinke die vollständige Transkriptdatei und nenne kurz Sprache, Dauer und unsichere Stellen.
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
→ Markiere die clip-würdigen Momente mit Zeitstempeln. Wenn fertige Kurzclips ausgewählt wurden, verwende `create-shorts` und prüfe dessen lokale Voraussetzungen.

Wenn ein Videoskript oder Aufnahmeplan beauftragt ist, die Umsetzung vor dem Dreh konkret machen: kurze Tabelle mit gesprochenem Text, eingeblendetem Text, Bild/Handlung und ungefährer Dauer je Abschnitt. Die Dauer anhand des tatsächlichen Sprechtexts prüfen; keine starre Wortzahl als passenden 30-/45-Sekunden-Clip ausgeben. Die gespeicherte Effektauswahl aus `videoeffekte` berücksichtigen. Ein Dreh-/Schnittplan ist noch kein gerendertes Video.

Bei ausdrücklich gewünschtem Hook-Vergleich zwei inhaltlich unterschiedliche Einstiege mit kurzer Testhypothese vorbereiten, den restlichen Clip möglichst gleich halten und die passende Messgröße vorab benennen. Redaktionelle Empfehlung nicht als gemessenen Gewinner bezeichnen; aus wenigen oder ungleich verteilten organischen Aufrufen keine gesicherte Ursache ableiten. Keine feste Pflicht zu zehn Hooks oder drei täglichen Posts.

Bei beauftragter Content-Planung zusammengehörige Aufnahmen nach Motiv/Ort bündeln und fehlendes Material sichtbar machen; Frequenz und Umfang mit der bestätigten Kapazität abgleichen. Veröffentlichung, Kommentare oder Direktnachrichten entstehen daraus nicht automatisch.

---

### ✋ CHECKPOINT 3
Zeige alle fertigen Outputs.
Frage: **„Hier ist dein Content. Was möchtest du anpassen?"**

---

### Schritt 4: Finale Ausgabe

Nur die gewählten Plattformen und Formate ausgeben; das folgende Schema ist eine Auswahlvorlage. Ergebnisse im outputs-Ordner der aktuellen Aufgabe bzw. des Projekts speichern; außerhalb einer Aufgabe gilt der folgende Standardpfad.

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
`~/Codex/outputs/content/[YYYY-MM-DD]-[Thema].md`
Existiert die Datei bereits (z. B. weil die Interview-Pipeline am selben Tag dasselbe Thema hatte), NIE überschreiben – stattdessen `-2`, `-3` … anhängen.

---

### Schritt 5: Bilder (optional)

Frage: **„Soll ich passende Bilder zu den Posts generieren?"**
Wenn ja → Lade den `/bild-generator` Skill.
- Input: die fertigen Post-Texte + gewählte Plattformen (bestimmt die Formate)
- Nutze das hier verfügbare Bildwerkzeug gemäß `bild-generator`. Gemini nur bei ausdrücklicher Werkzeugwahl; keine neue Dienstanbindung als Voraussetzung.

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
