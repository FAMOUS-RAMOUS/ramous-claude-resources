---
name: video
description: Erstellt fertige Videos im Famous-Ramous-Design (Gold/Schwarz, Logo, Claim) aus Text – Zitate, Statements, Kernaussagen – als MP4 für Reels, TikTok, Shorts, Instagram-Feed, LinkedIn oder YouTube. Nutzt das Remotion-Studio unter ~/Remotion. Diesen Skill nutzen bei: "mach ein Video daraus", "Video aus diesem Zitat", "Reel erstellen", "animiertes Statement", "Statement-Video", "das als Video", "Textvideo", "Videopost" – immer wenn aus Text ein kurzes Motion-Video werden soll. NICHT für das Schneiden vorhandener Langvideos (dafür create-shorts).
command: video
arguments: "[<text oder thema>]"
allowed-tools: Bash(npx remotion *), Bash(ffmpeg *), Bash(ls *), Bash(mkdir *), Bash(cp *), Bash(open *), Read, Write, Edit
---

# /video – Textvideos im Famous-Ramous-Design

Du erzeugst aus Text ein fertiges MP4. Das Projekt liegt fest unter `~/Remotion`,
alle Videos landen in `~/Claude/outputs/`.

**Grundregel: Du schreibst keinen React-Code.** Du wählst eine Composition,
baust ein Props-JSON und rufst den Render-Befehl auf. Nur wenn ausdrücklich
ein neues Template gewünscht ist, wird am Code gearbeitet (siehe „Neues Template").

## Schritt 1: Text bestimmen

Der Text kommt aus dem Argument, aus dem laufenden Chat oder aus einer Datei.

Regeln für den Statement-Text:
- **Maximal 120 Zeichen.** Längere Aussagen kürzen, nicht kleiner setzen –
  ein Video ist kein Absatz. Bei mehr Inhalt: mehrere Videos vorschlagen.
- Kein Hashtag, kein Emoji, keine Anführungszeichen um den ganzen Satz.
- Der Ton folgt dem Skill `schreibstil`. Bei Content aus der Wissensdatenbank
  oder aus Interviews gilt Quellentreue: nichts erfinden.
- `highlight`: 1–3 Wörter, die den Kern tragen. Die stehen in Gold.
  Wichtig: Die Wörter müssen **exakt so** im Text vorkommen (Groß-/Kleinschreibung
  egal, Satzzeichen werden ignoriert).
- `kicker`: ein Wort, maximal zwei – Thema/Kategorie (z. B. „Mindset",
  „Ernährung", „Training"). Weglassen ist erlaubt.

## Schritt 2: Format wählen

| Format | Maße | Wofür |
|---|---|---|
| `9:16` | 1080×1920 | Reels, TikTok, Shorts, Stories – **Standard** |
| `1:1` | 1080×1080 | Instagram-Feed, LinkedIn |
| `16:9` | 1920×1080 | YouTube, Website, Präsentation |

Ohne Angabe von Rachid: `9:16`. Nennt er eine Plattform, leite das Format ab.
Nennt er mehrere Plattformen, rendere mehrere Dateien.

## Schritt 3: Rendern

```bash
cd ~/Remotion && npx remotion render Statement \
  ~/Claude/outputs/<name>.mp4 \
  --props='{"text":"...","kicker":"...","highlight":["..."],"format":"9:16","dauer":6}'
```

Dateiname: sprechend und klein geschrieben, mit Bindestrichen,
z. B. `statement-koerper-folgt-9x16.mp4`. Niemals bestehende Dateien
überschreiben – bei Namenskollision Zähler anhängen (`-2`).

### Alle Props der Composition `Statement`

| Prop | Typ | Standard | Bedeutung |
|---|---|---|---|
| `text` | string | – | **Pflicht.** Die Hauptaussage |
| `kicker` | string | – | Kleine Zeile über dem Text |
| `claim` | string | `EHRLICH. GESUND. STARK.` | Footer. `""` = aus |
| `highlight` | string[] | `[]` | Wörter in Gold |
| `hintergrund` | `schwarz` \| `gold` \| `bild` | `schwarz` | Bildlook |
| `bild` | string | – | Dateiname in `~/Remotion/public/`, nur bei `hintergrund:"bild"` |
| `format` | `9:16` \| `1:1` \| `16:9` | `9:16` | Seitenverhältnis |
| `dauer` | number | `6` | Länge in Sekunden |
| `logo` | boolean | `true` | Logo einblenden |

**Dauer-Faustregel:** rund 0,4 Sekunden pro Wort, mindestens 4, höchstens 10.
Der Text muss stehen bleiben, nachdem das letzte Wort eingeflogen ist.

## Composition `Zitatbild` – Standbild statt Video

Für Foto-Posts mit Textzeile (Case-Story-Bilder, Zitat-Kacheln). Rendert ein
JPG/PNG, kein Video. Gleiche Marken-Elemente wie `Statement`: Goldbalken,
Gold-Highlight, Logo, Claim.

```bash
cd ~/Remotion && npx remotion still Zitatbild ~/Claude/outputs/content/images/<name>.jpg \
  --props='{"text":"...","kicker":"Arnold, 49 · Kfz-Meister","highlight":["Heute:","das","hier."],"bild":"arnold-4x5.jpg","format":"4:5","position":"unten","handle":"@therealfamousramous"}'
```

| Prop | Typ | Standard | Bedeutung |
|---|---|---|---|
| `text` | string | – | **Pflicht.** Die Bildzeile |
| `bild` | string | – | **Pflicht.** Dateiname in `~/Remotion/public/` |
| `kicker` | string | – | Zeile über dem Text, z. B. Name und Beruf |
| `highlight` | string[] | `[]` | Wörter in Gold |
| `format` | `1:1` \| `4:5` \| `9:16` \| `16:9` | `4:5` | Seitenverhältnis |
| `position` | `oben` \| `unten` | `oben` | Wo der Textblock sitzt |
| `handle` | string | – | Unten links, z. B. `@therealfamousramous` |
| `claim` | string | `EHRLICH. GESUND. STARK.` | Unten rechts. `""` = aus |
| `logo` | boolean | `true` | Logo unten rechts |

**Regel: Gesichter bleiben frei.** Vor dem Rendern prüfen, wo die Personen im
Foto stehen, und `position` entsprechend wählen. Danach das Ergebnis ansehen
und bei Überdeckung die Gegenseite nehmen.

Formate: `4:5` für Instagram und Facebook, `1:1` für LinkedIn.

### Eigenes Hintergrundbild

Bild zuerst nach `~/Remotion/public/` kopieren, dann nur den Dateinamen
übergeben (nicht den Pfad):

```bash
cp /pfad/zum/bild.jpg ~/Remotion/public/
cd ~/Remotion && npx remotion render Statement ~/Claude/outputs/<name>.mp4 \
  --props='{"text":"...","hintergrund":"bild","bild":"bild.jpg"}'
```

## Schritt 4: Prüfen und ausliefern

Nach jedem Render **verpflichtend**:

1. Standbild aus der Mitte ziehen und **selbst anschauen**:
   ```bash
   ffmpeg -y -i ~/Claude/outputs/<name>.mp4 -ss <dauer/2> -frames:v 1 \
     -vf scale=540:-1 /tmp/video-check.png
   ```
   Lies `/tmp/video-check.png` mit dem Read-Tool.
2. Kontrollieren: Text vollständig sichtbar? Nichts abgeschnitten? Logo und
   Claim lesbar? Gold-Hervorhebung auf den richtigen Wörtern?
3. Erst dann den Pfad an Rachid melden. Niemals ein Video ausliefern, das du
   nicht angesehen hast.

Fehler beim Rendern nicht wegmoderieren – Fehlermeldung zeigen und Ursache nennen.

## Neues Template bauen

Nur auf ausdrücklichen Wunsch. Vorgehen:

1. Neue Datei unter `~/Remotion/src/<Name>Video.tsx`, Muster: `StatementVideo.tsx`.
2. Farben und Claim **immer** aus `src/marke.ts` importieren, nie hart eintragen.
3. Format und Länge über `calculateMetadata` aus den Props ableiten.
4. In `src/Root.tsx` als `<Composition>` registrieren.
5. `cd ~/Remotion && npx tsc` muss fehlerfrei durchlaufen.
6. Testrender + Standbildkontrolle wie in Schritt 4.

## Technische Randbedingungen

- Remotion **4.0.434**, Node v26, React 19.
- Der Headless-Browser wird in `remotion.config.ts` fest verdrahtet aus dem
  `create-shorts`-Skill mitbenutzt. Remotions Auto-Download läuft auf diesem
  System in eine Endlosschleife – den Pfad also **nicht** entfernen.
- Studio zum Live-Basteln: `cd ~/Remotion && npm run dev`
- Kein `npm install -g` für Remotion. Die CLI ist projektgebunden und wird
  über `npx` im Projektordner aufgerufen.
