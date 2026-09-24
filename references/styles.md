# Style library

**Rule 1 — defaults:** only `MOE`, `CEL00`, `PAINT` are used without being asked (LOOKS slots).
**Rule 2 — on request:** every other ID is used only when the user names it, picks it from a list, or supplies art that maps to it.
**Rule 3 — lock:** the chosen ID + 4–6 of its tokens become the `[STYLE]` block, reprinted verbatim every frame. Mixing two IDs requires an explicit user ask; write both IDs in the block.
**Rule 5 — Greeting-recommended (★):** `SEMIGLOSS` and `GAMECG` drift least on close-up beats. Suggest them for greeting storyboards when the user asks which style to use; still never apply unasked.
**Rule 4 — descriptors, not people:** styles are described by visible traits. Studio/era names appear only as a user-facing label; never require a living artist's name in a prompt.

Format: `ID` · label · **tokens** (NL; pick 4–6) · tag hint (HARUKA) · use / avoid.

## Defaults

- `MOE` · soft bishoujo · **vibrant soft shading, large glossy eyes, clean bishoujo polish, pastel accents, sparkle highlights** · `moe, soft shading, sparkling eyes` · cute greetings. Avoid on heat beats (under-age read risk).
- `CEL00` · 2000s TV cel · **flat cel shading, hard colour holds, TV anime screencap finish, clean thick-thin lineart, limited palette** · `anime screencap, cel shading, 2000s (style)` · classic look, comedy.
- `PAINT` · Pixiv painterly sensual · **clean delicate linework, soft painterly airbrush gradients, glossy illustrated skin highlights, dense eyelashes, luminous soft palette, semi-realistic anime that stays 2D** · `delicate lineart, painterly, soft shading, glossy skin` · default for adult/sensual illustration.

## On request — modern anime & game art

- `KEYVIS` · modern TV key visual · **crisp lineart, soft cel with gradient shadows, rim light, detailed background, polished key-visual finish**
- `GACHA` · gacha/game splash art · **ornate layered costume, glossy highlights, dynamic key art pose, particle effects, game splash composition, high detail accessories**
- ★ `GAMECG` · game CG / official art · **game CG illustration, soft bloom, rich fabric folds, cinematic key light, official-art polish**
- ★ `SEMIGLOSS` · semi-real gloss · **thin sharp lineart, multi-highlight glassy eyes, glossy hair sheen, nose shine, smooth painterly skin**
- `VNCG` · visual novel / galgame CG (PixAI block) · **visual novel CG style, Japanese bishoujo illustration, soft cel shading, romantic lighting, polished character rendering**
- `KYO` · soft emotional TV drama · **delicate eye detail, fine individual hair strands, soft emotional lighting, gentle pastel grading, subtle blush**
- `SKYCINE` · cinematic sky/film anime · **vivid detailed skies, towering clouds, lens flare, glowing light shafts, hyper-detailed painted backgrounds, cinematic atmosphere**
- `GHIBLISH` · hand-painted pastoral · **hand-drawn feel, watercolor-painted backgrounds, soft natural palette, gentle rounded character design, nostalgic warmth**
- `SHONEN` · action shonen · **bold confident lineart, high-contrast cel shadows, speed lines, dynamic foreshortening, saturated primaries**
- `SEINEN` · dark seinen · **muted desaturated palette, heavy shadows, realistic proportions, gritty textures, cinematic framing**
- `CYBER` · cyberpunk anime · **neon rim lighting, holographic glows, techwear detail, wet reflective streets, teal-magenta palette**
- `DARKFAN` · dark fantasy · **dramatic chiaroscuro, ornate armor and cloth, desaturated jewel tones, painterly smoke and embers**

## On request — retro

- `RETRO90` · 1990s TV cel · **1990s anime screencap, cel paint with visible paint edges, hand-drawn linework, film grain, slight VHS colour bleed, muted saturated palette** (+ genre: shoujo / mecha / noir)
- `OVA80` · late-80s OVA · **detailed hand-inked linework, airbrushed highlights, dramatic backlight, sharp angular faces, rich dark palette, film grain**
- `SHOUJO90` · retro shoujo · **fine warm-brown linework, sparkle motifs, parallel blush hatching, soft cel-hybrid gradients, high-key pastels, flower accents**
- `CITYPOP` · city-pop / 80s poster · **flat pastel gradients, sunset palette, clean retro lineart, poster composition, glossy highlights**

## On request — manga & comics

- `MANGA` · modern monochrome manga (PixAI block) · **black ink lines, white highlights, grey screentones, smooth digital lines, expressive faces, speed/radiating lines**
- `MANGAFINE` · fine manga lines · **black-and-white line art, simple diagonal hatching on shadows, minimal composition, clean modern draftsmanship**
- `RETROMANGA` · 90s manga ink · **heavy ink weights, halftone dots in shadows, expressive retro hair shapes, high-contrast blacks**
- `MANHWA` · webtoon/manhwa colour · **clean thin ink lines, polished soft gradient shading, elongated elegant proportions, glossy hair, dramatic vertical webtoon framing**
- `WEBTOONFLAT` · flat webtoon · **flat colour fills, minimal shading, bright clean palette, simple backgrounds, bold silhouettes**
- `SKETCH` · pencil/ink sketch · **loose pencil construction lines, cross-hatching, unfinished edges, paper texture**

## On request — sheets & special

- `SHEET` · character design sheet (PixAI flat block) · **pure flat colouring, no shading, no highlights, solid colour fills, clean anime lineart, washed-out pale palette, production model sheet** — use for turnarounds and ISO sheets
- `CHIBI` · SD/chibi (**non-sexual only**, keep 25 in text) · **super-deformed 1:2 proportions, rounded shapes, simple eyes, bright flat colours**
- `FIGURE` · PVC figure look (fictional character only) · **glossy painted plastic surface, smooth highlights, figure base, studio light**
- `UKIYOE` · woodblock · **bold contour lines, flat colour areas, traditional Japanese composition, paper grain**
- `PIXEL` · pixel art · **8-bit pixel art, limited palette, retro console sprites**
- `WATERCOLOR` · watercolour anime · **transparent watercolour washes, soft bleeding edges, light pencil lines, paper texture**

## Effect blocks (add-ons, never a style by themselves)

- `+LENS` · chromatic aberration, film grain, bloom, slight overexposure, glossy specular highlights
- `+DETAIL` · hyper-detailed illustration, detailed background, intricate fine textures, precise linework on background objects
- `+CHIARO` · extreme chiaroscuro, deep blacks, bright highlights, harsh directional light, almost no midtones
- `+LINES` · crisp clean lineart, sharp outlines, flat cel shading, defined anatomy
- `+BGREAL` · slightly realistic, blurred-depth background behind a 2D character

## Showing styles

When the user asks "what styles can you do?": list IDs + labels in one compact block (no images). When they pick 1–3, render the **same locked character** in each; never change FACE/BODY while testing styles.
