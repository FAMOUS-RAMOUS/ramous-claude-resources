---
name: social-post
description: Erstellt plattformspezifische Social-Media-Posts aus Content-Extraktion oder Interview-Material. Für Instagram, Facebook, LinkedIn (Kurzform), X. Trigger: "erstelle Posts", "Social Media Content", "schreibe Post für [Plattform]".
---

Erstelle Social-Media-Posts für die angegebenen Plattformen basierend auf der gegebenen Content-Extraktion.

Nutze immer den `schreibstil`-Skill für Tonalität und Stimme – dort sind auch Emoji-Regeln, Signaturen und die MEF-CTA-Formel („Schreib mir 'MEF'") definiert. Bei Coaching-Bezug den CTA einbauen.

Für lange LinkedIn-Artikel nicht diesen Skill nutzen, sondern `linkedin-artikel`.

## Plattform-Spezifikationen

### Instagram
- **Format:** Emotion zuerst → Story → CTA
- **Länge:** 150–300 Wörter
- **Emojis:** Sparsam, 1–4 pro Post (Instagram-Ausnahme laut `schreibstil`), passend zum Inhalt
- **Hashtags:** 15–20, am Ende als Block
- **Hook:** Erste Zeile muss zum Weiterlesen zwingen (Cliffhanger, Frage, starke Aussage)

### Facebook
- **Format:** Persönlich, erzählerisch, nahbar
- **Länge:** 100–200 Wörter
- **Emojis:** Optional, 1–2
- **Hashtags:** 3–5
- **Ton:** Authentisch, nicht werblich

### LinkedIn (Kurzform)
- **Format:** Hook → Problem/Situation → Ergebnis/Insight → CTA
- **Länge:** 150–300 Wörter
- **Struktur:** Kurze Absätze, viel Weißraum
- **Hashtags:** 3–5 relevante Branchen-Tags
- **Ton:** Professionell, direkt, substanziell

### X (Twitter)
- **Format:** Kernaussage in 1–2 Sätzen
- **Länge:** max. 280 Zeichen
- **Optional:** Thread-Version mit 3–5 Tweets

## Output-Format
Jeden Post klar abgetrennt mit Plattform-Label und bereit zum Kopieren:

```
📱 INSTAGRAM
---
[Post]

📘 FACEBOOK
---
[Post]

💼 LINKEDIN
---
[Post]

🐦 X
---
[Post/Thread]
```

## Selbst-Check vor der Ausgabe

Jeden Post einzeln prüfen – bei einem „Nein" umschreiben statt abgeben:

1. Wortzahl/Zeichenzahl innerhalb der Plattform-Spezifikation? Bei X die 280 Zeichen tatsächlich zählen, nicht schätzen.
2. Hashtag-Anzahl korrekt (Instagram 15–20, Facebook 3–5, LinkedIn 3–5, X keine Pflicht)?
3. Hook-Test: Funktioniert die erste Zeile allein, ohne den Rest? Würde sie beim Scrollen stoppen?
4. Selbst-Check aus `schreibstil` bestanden (Floskeln, Emojis, MEF-CTA-Regel)?
5. Ist jeder Post eigenständig für seine Plattform geschrieben – nicht derselbe Text 4× minimal variiert? Instagram erzählt emotionaler, LinkedIn substanzieller, X verdichtet auf eine Aussage.
