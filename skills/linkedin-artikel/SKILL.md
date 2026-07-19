---
name: linkedin-artikel
description: Erstellt einen langen LinkedIn-Artikel oder Erfahrungsbericht aus Interview-Material oder Content-Extraktion. Trigger: "schreibe LinkedIn-Artikel", "Langform", "Erfahrungsbericht", "Case Study".
---

Schreibe einen LinkedIn-Artikel basierend auf dem gegebenen Interview-Material oder der Content-Extraktion.

Nutze den `schreibstil`-Skill für Tonalität und Stimme.

## Artikeltypen (User wählt oder du empfiehlst basierend auf Material)

- **Kundenerfahrung / Case Study:** Zeigt die Transformation des Kunden
- **Interview-Format:** Frage-Antwort-Struktur mit Einleitung und Fazit
- **Erfahrungsbericht:** Narrative Story in Ich-Perspektive (aus Kundensicht geschrieben)

## Struktur

```
# [Headline – präzise, neugierig machend, kein Clickbait]

[Hook – 2–3 Sätze, die sofort neugierig machen oder einen Schmerz ansprechen]

---

## [Abschnitt 1: Ausgangssituation]
Wo stand die Person vor der Zusammenarbeit?
[150–200 Wörter, konkret und nachvollziehbar]

## [Abschnitt 2: Der Weg / Die Veränderung]
Was hat sich verändert, welche Schritte wurden unternommen?
[200–300 Wörter]

## [Abschnitt 3: Das Ergebnis]
Wo steht die Person heute, was hat sich konkret verbessert?
[150–200 Wörter, mit konkreten Details/Zahlen wenn vorhanden]

## Fazit
[Kernbotschaft + natürlicher, nicht aufdringlicher CTA – bei Coaching-Bezug die MEF-Formel aus `schreibstil`: „Schreib mir 'MEF'"]

---
*[Optional: Dankesnotiz an die interviewte Person]*
```

## Stilregeln
Alle Stil- und Tonregeln kommen aus `schreibstil` (eine Quelle der Wahrheit – hier nicht duplizieren).
Zusätzlich nur artikelspezifisch:
- Kurze Absätze und Zwischenüberschriften für gute Lesbarkeit im LinkedIn-Editor
- Konkrete Zahlen und Fakten wo vorhanden

## Länge
Gesamtlänge 600–1.000 Wörter. Unter 500 Wörtern ist es kein Artikel, sondern ein Post → dann `social-post` nutzen und das dem User sagen.

## Selbst-Check vor der Ausgabe
1. Alle wörtlichen Zitate gegen das Quellmaterial abgeglichen (nichts geglättet oder erfunden)?
2. Zahlen und Fakten stammen aus dem Material – nichts dazuerfunden?
3. Selbst-Check aus `schreibstil` bestanden (Hook, Floskeln, CTA-Regel)?
4. Gesamtlänge im Rahmen (600–1.000 Wörter)?

## Output
Fertiger Artikel, kopierbereit für LinkedIn-Editor.
Zeichenanzahl am Ende angeben – mit `wc -m` gezählt, nicht geschätzt.
