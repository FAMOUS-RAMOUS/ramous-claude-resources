---
name: transkription
description: Transkribiert Audio/Video-Dateien oder YouTube-URLs zu strukturiertem Transkript mit Zeitstempeln via faster-whisper large-v3 (über ~/transcribe.py, M4-Pro-optimiert). Trigger: "transkribiere", "erstelle Transkript", bei Audio/Video-Input als erster Schritt.
---

Transkribiere den gegebenen Input zu einem strukturierten Transkript.

## Input-Typen
- **Lokale Datei:** Pfad zu Audio (.mp3, .m4a, .wav) oder Video (.mp4, .mov)
- **YouTube-URL:** Video zuerst herunterladen mit yt-dlp
- **Text (Google-Rezension):** Direkt weiterleiten – keine Transkription nötig, übergib an content-extraktion

## Ausführung (Audio/Video)

Nutze IMMER das vorhandene Script `~/transcribe.py` – es ist M4-Pro-optimiert (float16, VAD-Filter, beam_size=5) und speichert das Roh-Transkript automatisch als `[Dateiname]_transkript.txt` neben der Audiodatei:

```bash
# Bei YouTube-URL – zuerst Audio herunterladen (eindeutiger Name, nichts überschreiben):
yt-dlp -x --audio-format mp3 -o "/tmp/yt-%(id)s.%(ext)s" "[URL]"

# Transkription (deutsch ist Standard, zweites Argument nur bei anderer Sprache):
python3.11 ~/transcribe.py "[Pfad-zur-Audiodatei]" de
```

Modell: `large-v3` via faster-whisper – so wie in `~/transcribe.py` definiert. Keinen eigenen Inline-Python-Code schreiben, das Script ist die eine Quelle der Wahrheit.

## Fehlerbehandlung

- **Datei nicht gefunden:** Pfad vor dem Start mit `ls` prüfen; bei Leerzeichen im Namen Anführungszeichen verwenden.
- **yt-dlp schlägt fehl:** Fehlermeldung zeigen und prüfen, ob das Video verfügbar/regional gesperrt ist. Nicht stillschweigend weitermachen.
- **Erster Lauf:** Das Modell lädt einmalig ~3 GB herunter – den User vorwarnen, dass es beim ersten Mal dauert.

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

Sprecherwechsel: faster-whisper erkennt Sprecher NICHT automatisch. Wenn der Inhalt klar ein Dialog ist (Interview), markiere Wechsel nach bestem Verständnis aus dem Kontext mit [SPRECHER A] / [SPRECHER B] und weise darauf hin, dass die Zuordnung inhaltlich abgeleitet ist.
Füllwörter ("ähm", "äh") im Volltext entfernen, im Inhalt-Block belassen.
