---
name: transkription
description: Transkribiert Audio/Video-Dateien oder YouTube-URLs zu strukturiertem Transkript mit Zeitstempeln via faster-whisper large-v3. Trigger: "transkribiere", "erstelle Transkript", bei Audio/Video-Input als erster Schritt.
---

Transkribiere den gegebenen Input zu einem strukturierten Transkript.

## Input-Typen
- **Lokale Datei:** Pfad zu Audio (.mp3, .m4a, .wav) oder Video (.mp4, .mov)
- **YouTube-URL:** Video zuerst herunterladen mit yt-dlp
- **Text (Google-Rezension):** Direkt weiterleiten – keine Transkription nötig, übergib an content-extraktion

## Ausführung (Audio/Video)

```bash
# Bei YouTube-URL – zuerst Audio herunterladen:
yt-dlp -x --audio-format mp3 -o "/tmp/interview.%(ext)s" "[URL]"

# Transkription mit faster-whisper:
python3 -c "
from faster_whisper import WhisperModel
model = WhisperModel('faster-community/whisper-large-v3', device='auto')
segments, info = model.transcribe('/tmp/interview.mp3', language='de')
for segment in segments:
    print(f'[{segment.start:.1f}s - {segment.end:.1f}s] {segment.text.strip()}')
"
```

## Output-Format

```
# Transkript
**Datum:** [heute]
**Quelle:** [Dateiname oder URL]
**Dauer:** [X Minuten]

## Inhalt

[00:00] Erster Abschnitt...
[01:23] Zweiter Abschnitt...

## Volltext (für Weiterverarbeitung)
[Transkript ohne Zeitstempel, sauber formatiert]
```

Sprecherwechsel mit [SPRECHER A] / [SPRECHER B] markieren, wenn erkennbar.
Füllwörter ("ähm", "äh") im Volltext entfernen, im Inhalt-Block belassen.
