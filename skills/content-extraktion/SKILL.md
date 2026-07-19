---
name: content-extraktion
description: Extrahiert aus einem Interview-Transkript oder Google-Rezension die Kernaussagen, Zitate, Story-Bogen und Hooks für Content-Erstellung. Trigger: "extrahiere Content", "analysiere Interview", nach Transkription als zweiter Schritt.
---

Analysiere den gegebenen Text und extrahiere alles Relevante für die Content-Erstellung.

## Input
- Interview-Transkript (aus transkription-Skill)
- Google-Rezension (Rohtext)
- Beliebiger Interviewtext

## Ausgabe

```
# Content-Extraktion

## 1. Kernbotschaft (1 Satz)
[Was ist die eine zentrale Aussage?]

## 2. Story-Bogen
- **Ausgangssituation:** [Wo war der Kunde/Interviewpartner vorher?]
- **Wendepunkt:** [Was hat sich verändert?]
- **Ergebnis:** [Wo steht er/sie heute?]

## 3. Starke Zitate (wörtlich, direkt aus dem Text)
1. "[Zitat 1]"
2. "[Zitat 2]"
3. "[Zitat 3]"

## 4. Emotionale Momente
[Stellen, die besonders berühren, überraschen oder inspirieren – mit Kontext]

## 5. Headline-Kandidaten (5 Vorschläge)
1. ...
2. ...
3. ...
4. ...
5. ...

## 6. Hashtag-Vorschläge
[10–15 relevante Hashtags, Mischung aus Reichweite und Nische]

## 7. Content-Empfehlung
- Kurzform geeignet? [Ja/Nein + Begründung]
- Langform geeignet? [Ja/Nein + Begründung]
- Stärkstes Format: [Social Post / LinkedIn-Artikel / beides]
```

## Wichtige Regeln
Bleibe so nah wie möglich am Originaltext. Keine Erfindungen, keine Übertreibungen.
Wenn etwas unklar ist, weise darauf hin anstatt zu spekulieren.

**Zitat-Treue (vor der Ausgabe prüfen):** Jedes Zitat unter Punkt 3 muss wortwörtlich so im Originaltext stehen – nicht geglättet, nicht zusammengefasst, nicht „schöner" formuliert. Auslassungen mit […] markieren. Vor der Ausgabe jedes Zitat einmal gegen den Originaltext abgleichen; findest du es dort nicht wörtlich, fliegt es raus oder wird als Paraphrase gekennzeichnet.
