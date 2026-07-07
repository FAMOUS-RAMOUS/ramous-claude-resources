---
name: bild-generator
description: Generiert plattformoptimierte Bilder via Nano Banana 2 (Modell gemini-3.1-flash-image, Google AI Studio) aus Post-Text. Erstellt automatisch einen passenden Bildprompt und speichert das Bild lokal. Trigger: "generiere Bild", "erstelle Bild für Post", "Bild für Instagram/LinkedIn", nach Content-Erstellung.
---

Generiere ein passendes Bild für den gegebenen Post via Nano Banana 2 (offizieller Modellname: `gemini-3.1-flash-image`).

## Voraussetzung
Google AI Studio API-Key muss gesetzt sein – VOR dem API-Aufruf prüfen:
```bash
if [ -z "$GOOGLE_API_KEY" ]; then echo "GOOGLE_API_KEY fehlt – in Google AI Studio erstellen und mit export GOOGLE_API_KEY=... setzen"; fi
```
Fehlt der Key, den User informieren und NICHT weitermachen (siehe Memory: Billing muss in Google AI Studio aufgeladen sein).

## Schritt 1: Bildprompt erstellen

Analysiere den Post-Text und erstelle einen Prompt nach diesen Regeln:

### Stil-Vorgaben für Famous Ramous
- **Ästhetik:** Dramatisch, kontrastreich, dunkel mit Lichtakzenten – kein Pastell, kein Stockfoto-Feeling
- **Atmosphäre:** Kraft, Entschlossenheit, Transformation – der Moment kurz vor dem Durchbruch
- **Menschen:** Athletisch, fokussiert, nicht posierend – echte Momente
- **Kein Text im Bild** – niemals Schrift, Logos oder Zahlen generieren
- **Kein generisches Fitness-Klischee** – keine bunten Hanteln, kein Protein-Shake
- **Stil:** Cinematic, fotografisch realistisch, dramatisches Licht

### Prompt-Formel
```
[Hauptmotiv], [Atmosphäre], cinematic photography, dramatic lighting,
high contrast, dark background with strong light accents, photorealistic,
no text, no logos, professional sports photography style
```

### Beispiel-Prompts nach Thema

**Transformation/Erfolg:**
"A person standing in a gym looking determined after an intense workout,
dramatic side lighting, dark background, cinematic photography,
high contrast, photorealistic, no text"

**Handeln/Motivation:**
"A person taking a powerful first step forward on a dark path with bright
light ahead, dramatic lighting, cinematic photography, high contrast,
photorealistic, no text"

**Interview/Testimonial:**
"Two people in a meaningful conversation, authentic moment, warm dramatic
lighting, dark background, candid photography style, photorealistic, no text"

## Schritt 2: Bildformat je Plattform

| Plattform | Format | aspect_ratio |
|---|---|---|
| Instagram (Post/Story) | 9:16 Portrait | "9:16" |
| LinkedIn | 1:1 Square | "1:1" |
| Facebook | 16:9 Landscape | "16:9" |
| X (Twitter) | 16:9 Landscape | "16:9" |

## Schritt 3: API-Aufruf

```python
from google import genai
from google.genai import types
import os, sys
from datetime import datetime

api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    sys.exit("FEHLER: GOOGLE_API_KEY ist nicht gesetzt.")

client = genai.Client(api_key=api_key)

def generate_image(prompt, aspect_ratio="1:1", platform="linkedin"):
    timestamp = datetime.now().strftime("%Y-%m-%d")
    output_dir = "/Users/famous_ramous/Claude/outputs/content/images"
    os.makedirs(output_dir, exist_ok=True)
    output_path = f"{output_dir}/{timestamp}-{platform}.png"

    response = client.models.generate_content(
        model="gemini-3.1-flash-image",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE"],
            image_config=types.ImageConfig(aspect_ratio=aspect_ratio),
        ),
    )

    image_parts = [
        p for p in response.candidates[0].content.parts
        if getattr(p, "inline_data", None)
    ]
    if not image_parts:
        raise RuntimeError(
            "Keine Bilddaten in der Antwort – vermutlich Safety-Filter oder Billing-Problem. "
            f"Antwort: {response.candidates[0].finish_reason}"
        )

    with open(output_path, "wb") as f:
        f.write(image_parts[0].inline_data.data)

    return output_path
```

**Bei API-Fehlern** (z. B. Modellname nicht gefunden, geändertes Config-Feld): kurz die aktuelle Doku prüfen (ai.google.dev/gemini-api/docs → Image generation) statt zu raten – Google benennt Bildmodelle regelmäßig um. Fehler dem User klar melden, inkl. wahrscheinlicher Ursache (fehlendes Billing, Safety-Filter, veralteter Modellname).

## Output
- Bild gespeichert unter: `~/Claude/outputs/content/images/[Datum]-[Plattform].png`
- Pfad zurückgeben für Weiterverarbeitung
- Bei mehreren Plattformen: je ein Bild pro Format generieren
