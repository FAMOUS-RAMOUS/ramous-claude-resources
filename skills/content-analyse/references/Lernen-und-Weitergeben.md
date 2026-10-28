# Fachmaterial verstehen, behalten und weitergeben

## Einstieg und Quellenumfang

Ziel und vorhandenes Wissen aus dem Auftrag übernehmen: verstehen, eine konkrete Frage beantworten, praktisch anwenden oder anderen erklären. Wenn dies klar ist, ohne erneute Grundsatzfrage arbeiten. Die Quelle und das gewünschte Ergebnis bestimmen die Tiefe; eine reine Kurzfassung ersetzt kein Verständnis.

Nur die bereitgestellten oder ausdrücklich zum Lesen benannten Quellen erschließen. Die Wissensdatenbank nicht allein wegen dieses Modus durchsuchen. Bei PDFs den vorhandenen PDF-Skill und dessen tatsächlich verfügbare lokale Lese-/OCR-Werkzeuge verwenden. PPT Master ist eine mögliche vorhandene Ausgabehilfe für bearbeitbare Folien, keine Voraussetzung für das Lernen. Keine zusätzliche Cloud-OCR oder fremde Analyse-API automatisch einschalten.

Titel, Autor, Ausgabe und Seiten-/Kapitelumfang soweit vorhanden festhalten. Zuerst Inhaltsstruktur und Lesbarkeit prüfen, dann den für den Auftrag nötigen Text einschließlich relevanter Tabellen, Abbildungen und Fußnoten lesen. Bei einem ausdrücklich vollständig beauftragten Buch alle Kapitel schrittweise bearbeiten und den Stand im vorhandenen Arbeitsverzeichnis sichern; nicht nach der Einleitung auf das ganze Buch schließen. PDF-Blattnummer und gedruckte Seitenzahl unterscheiden. Fehlende Seiten, OCR-Fehler und nicht interpretierte Grafiken konkret markieren. Nur extrahiert ist noch nicht inhaltlich geprüft.

## Essenz und Verständnis

Die zentrale Frage und Antwort des Autors herausarbeiten. Die tragenden Begriffe, Mechanismen und Zusammenhänge erklären: Was ist die Aussage, warum soll sie gelten, worauf stützt sie sich und wo endet ihre Gültigkeit? Bedingungen, Gegenargumente, Ausnahmen, Einheiten und Einschränkungen mitverdichten. Nicht pauschal behaupten, zwanzig Prozent einer Quelle deckten achtzig Prozent ihres Nutzens ab.

Die Erklärung in eigenen klaren deutschen Worten formulieren. Kernaussagen mit Kapitel oder Seite rückführbar machen; wörtliche Zitate sparsam und unverändert verwenden. Quelle, eigene Schlussfolgerung und zusätzliches Beispiel unterscheidbar halten. Widersprüche zwischen Kapiteln oder Quellen benennen, statt sie still glattzuziehen. Ältere Fachliteratur als solche einordnen; wenn daraus aktuelle medizinische, rechtliche oder finanzielle Handlungsentscheidungen abgeleitet werden sollen, die maßgebliche aktuelle Fachlage gesondert prüfen. Ein Buchbeispiel ist kein belegtes Ergebnis von Rachid oder seinen Kunden.

## Lernen und Übertragen

Aus den tragenden Aussagen wenige passende Abruffragen entwickeln: Begriff erklären, Zusammenhang begründen, ähnliche Fälle unterscheiden und einen neuen Fall lösen. Fragen vor den getrennten Antworten zeigen, damit Rachid zuerst selbst erinnern kann. Antworten enthalten die kurze Begründung und die Quellenstelle, nicht nur ein Lösungswort. Schwierige Punkte gezielt erneut erklären, statt alles unverändert zu wiederholen.

Ein eigenes einfaches Anwendungsbeispiel kann helfen; es ausdrücklich als Übungsbeispiel kennzeichnen und seine Annahmen nennen. Für das Weitergeben eine verständliche kurze Erklärung mit den nötigen Einschränkungen anbieten. Je nach Auftrag passt eine Kunden-Erklärung, Unterrichtsskizze, Checkliste oder Präsentation. Keine Gesundheitspläne, Veröffentlichungen oder Kundenkommunikation allein aus dem Lernauftrag ableiten.

Bei längerem Lernen einen kurzen erneuten Abruf nach Abstand vorschlagen und offene Verständnislücken notieren. Kein starrer optimaler Wiederholungsplan, keine Erinnerungsautomation ohne Auftrag und keine garantierte Lerngeschwindigkeit. Im interaktiven Lernmodus Rachids Antwort abwarten; bei einem beauftragten vollständigen Lernpaket Fragen und Lösungen direkt liefern, ohne künstliche Freigabestopps.

## Nutzbares Ergebnis

Standard ist ein kompakter Lernbrief mit Essenz, nachvollziehbarem Erklärmodell, Anwendung, Abruffragen mit getrennten Antworten und konkreten Quellenstellen. Umfang und Zahl der Fragen am Material und Ziel ausrichten. Auf Wunsch vertiefte Kapitelnotizen, Karteikarten oder bearbeitbare Folien daraus erzeugen; dieselben Quellen und Aussagen wiederverwenden. Nicht automatisch alle Ausgabeformate produzieren.

Bei langen Quellen eine kleine Kapitelübersicht mit tatsächlich geprüftem Bereich und offenen Punkten führen. Wenn gespeichert wird, die bestehende Aufgabenablage nutzen; keine zweite Wissensdatenbank oder neue Regelsammlung anlegen. Für noch nicht bereitgestelltes Material keine erledigte Buchanalyse behaupten.

## Eingerichtete lokale PDF- und Folienwerkzeuge

Für PDF-Auslesen und native, bearbeitbare PowerPoint-Ausgabe ist PPT Master am geprüften Quellstand lokal unter `/Users/famous_ramous/Documents/Codex/2026-10-27/ki-systemoptimierung/werkzeuge/ppt-master/` eingerichtet. Es ist ein ergänzendes Werkzeugpaket, kein zweiter aktiver Analyse- oder Präsentations-Skill. Der Aufruf `ausfuehren.py` verwendet die eigene Python-Umgebung und reicht keine bestehenden API-Schlüssel an die lokalen Konverter weiter.

- PDF lesen: `python3 <Werkzeugpfad>/ausfuehren.py source_to_md/pdf_to_md.py <Eingabe.pdf> -o <Arbeitsdatei.md>`. Erzeugte Seitenmarker erhalten; wichtige Abbildungen und Tabellen zusätzlich lokal ansehen. Bei Scans die tatsächlich verfügbaren OCR-Werkzeuge des PDF-Skills verwenden, keine bereits vorhandene Textschicht vortäuschen.
- Gewünschte Lernfolien als lokale SVG-Seiten mit Quellenhinweisen und Notizen aufbauen. Vor Export: `python3 <Werkzeugpfad>/ausfuehren.py svg_quality_checker.py <Projekt>/svg_output --quick-generate --canonical-authoring --json`.
- Bearbeitbare PPTX: `python3 <Werkzeugpfad>/ausfuehren.py svg_to_pptx.py <Projekt> --quick-generate --with-notes --primary-language de-DE -o <Ausgabe.pptx>`. Den Qualitätsbericht passend zum unveränderten SVG-Stand verwenden; keine Validierung umgehen. Native Text-/Formobjekte und Quellenhinweise im Ergebnis prüfen.

`<Werkzeugpfad>` steht für den oben genannten tatsächlichen Ordner; Dateinamen als Daten behandeln und sicher als einzelne Argumente übergeben. Der lokale Aufruf ist für diese geprüften Konverter gedacht. Andere optionale Bibliotheksfunktionen, Online-Formelrenderer, Bild-/Sprach-APIs, Webserver oder Repository-Updates gehören nicht automatisch zum Lernauftrag. Vorhandene allgemeine Lese- und Präsentationswerkzeuge bleiben nutzbar. Wenn die lokale Ablage in einer anderen Umgebung fehlt, nicht als dort installiert ausgeben.

## Selbstcheck vor Ausgabe

1. Ist der tatsächlich gelesene Umfang genannt und reicht er für die ausgegebene Schlussfolgerung?
2. Sind die tragenden Aussagen, Bedingungen und wichtigen Ausnahmen mit Quellenstellen abgleichbar?
3. Sind Erklärung, Autorenaussage und eigenes Übungsbeispiel klar unterscheidbar?
4. Prüfen die Fragen Verständnis und Übertragung, und stimmen die Lösungen mit der Quelle überein?
5. Passt das Ergebnis zum Lern-/Weitergabeziel, ohne unnötige Formate oder zusätzliche Dienste?

## Methodische Grundlage

Der Einsatz von Abruffragen und erneutem Abruf mit Abstand orientiert sich an Karpicke und Roediger (2008), DOI https://doi.org/10.1126/science.1152408, sowie Dunlosky et al. (2013), DOI https://doi.org/10.1177/1529100612453266. Diese Arbeiten begründen keine feste Lerngeschwindigkeit für Rachid und keinen garantierten Transfer jedes Buches. Die obige Quellen- und Erklärarbeit ist ein Arbeitsablauf, kein experimentell bestätigtes Gesamtprogramm.
