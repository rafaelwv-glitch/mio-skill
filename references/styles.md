# Style library

**Rule 1 — suggest, don't default:** when no style is set, Mio proposes **2–3 fitting IDs** from the Fit Map (one short line each) and renders one LOOK per ID. Fallback when the brief gives nothing to go on: `KEYVIS` · `PAINT` · `CEL00`.
**Rule 2 — lock is law:** the chosen ID + 4–6 of its tokens become `[CANVAS-STYLE]`, reprinted verbatim every frame. A locked style never changes silently — only on explicit user request, then locks are reprinted. Mixing two IDs requires an explicit ask; write both IDs in the block.
**Rule 3 — one canvas, one style:** every character on the canvas (OC, `{{user}}`, NPCs, crowd) inherits `[CANVAS-STYLE]` (`storyboard-consistency.md` §5).
**Rule 4 — external sources stay themselves:** a registered asset uses `[STYLE-SOURCE] EXT:<label>` (`original-art.md`). Library IDs are vocabulary for describing it, never a replacement.
**Rule 5 — greeting-recommended (★):** `SEMIGLOSS` and `GAMECG` drift least on close-up beats; include one of them in suggestions for greeting storyboards.
**Rule 6 — descriptors, not people:** styles are described by visible traits. Studio/era/platform names appear only as user-facing labels; never require a living artist's name in a prompt.
**Rule 7 — no text:** no style brings lettering with it. Manga/comic *rendering* is allowed; panels, bubbles and SFX are not (`no-text.md`).

Format: `ID` · label · **tokens** (NL; pick 4–6) · tag hint (HARUKA) · use / avoid.

## Fit Map (suggestions when no style is set)

| Brief reads as | Suggest (pick 2–3) |
|---|---|
| dark romance, obsession, villain, yandere, gothic | `ATSUNURI` · `RIMLIGHT` · `SEINEN` |
| slice of life, office, cozy everyday | `KEYVIS` · `GPTANIME` · `KYO` |
| wholesome, affectionate, comedy, comfort | `GPTANIME` · `FLATLINE` · `MOE` |
| sensual / adult romance, bedroom, afterglow | `PAINT` · `GLOSSREAL` · ★`SEMIGLOSS` |
| greeting close-ups (any genre) | ★`SEMIGLOSS` · ★`GAMECG` · genre pick from this table |
| fantasy, adventure, royalty, magic | `GACHA` · `DARKFAN` · `ATSUNURI` |
| sci-fi, cyberpunk, city at night | `CYBER` · `RIMLIGHT` · `NEONPOP` |
| melancholy, nostalgia, summer, longing | `KUUKI` · `SUISAI` · `SKYCINE` |
| idol, fashion, pop, party | `NEONPOP` · `YUMEKAWA` · `GACHA` |
| drama, thriller, tension, crime | `SEINEN` · `RIMLIGHT` · `KEYVIS` |
| retro, 80s/90s, noir, city-pop | `RETRO90` · `OVA80` · `CITYPOP` |
| Korean webtoon feel, office romance vertical | `MANHWA` · `WEBTOONFLAT` · `GLOSSREAL` |
| target engine is PixAI Haruka / Tsubaki | engine house look (`HARUKA2` / `TSU2` / `TSU3`) + one genre pick |

Suggestion line format: `Slot n <ID> — <3–5 word look>: <why it fits>`. Never more than 3.

## Engine house looks (what each engine draws by default — and how to ask for it)

### `HARUKA2` · PixAI Haruka v2 (SDXL)
- **Look:** clean classic anime illustration; crisp even lineart; soft 2–3 tone cel with smooth gradients; refined, expressive eyes (layered pupil highlights, layered lashes, eye light); glossy hair-sheen transitions; smooth fabric folds; bright clean palette. (PixAI model page: better hands, more expressive eyes, hair shine and clothing wrinkles optimized for anime.)
- **Grok / Tsubaki NL:** "clean modern anime illustration, crisp even lineart, soft cel shading with smooth gradients, glossy layered eyes with multiple catchlights, smooth glossy hair sheen, clean bright colours, smooth fabric folds".
- **On Haruka:** tags, quality head + subject + features; defaults and negative in `engines.md`. Style variety comes from SDXL LoRAs (official "Haruka v2 style" LoRA is also offered for Tsubaki.2 — check its architecture on the LoRA page).
- **Use:** classic polished anime, single character, best hands/eyes. **Avoid:** complex multi-character interaction (traits bleed between characters on SDXL).
- **Versions:** as of 2026-10 only **Haruka v2** is an official base model. Items named "Haruka … v3" / "Haruka💤Style.3" on PixAI are **user LoRAs**, not a new Haruka.

### `TSU2` · PixAI Tsubaki.2 house look (DiT)
- **Look:** clean delicate linework, soft gradients, luminous highlights, bright yet gentle colours, smooth glossy skin, expressive glassy eyes — PixAI's own example prompts end with exactly this sentence.
- **NL tokens:** "Clean, delicate linework with soft gradients and luminous highlights. Colors are bright yet gentle, skin tones smooth and glossy, with expressive eyes." Stronger: "glossy, glass-like anime style, lively linework, highlight-heavy rendering".
- **Presets:** 35+ one-click style presets (PixAI docs say 35; the guide says 39; model page says 25+ — count uncertain). Examples seen in docs: "Desaturated, translucent", "Chibi", "Vivid colored pencil". Style words can go in the **Customize Style** field (Tsubaki.2 only). Mio names the intended look in text and never relies on a preset name it has not seen.
- **Use:** multi-character scenes in a polished glossy look. **Avoid:** needing a reference image (Tsubaki.2 has none).

### `TSU3` · PixAI Tsubaki.3 (DiT, flagship)
- **Look:** no single house style — "from photorealism to anime" in one model; locks character features *and* art style to each other across a set; physically consistent directional light; native 2K.
- **How to get a style:** break it into **line · colour application · palette · surface** and write the one or two parts the style cannot do without (PixAI Tsubaki.3 guide: watercolour = paper grain + bleed; cel = hard-edged shadow + few tones; vintage print = halftone + misregistration). On a long style jump also say what you don't want ("no smooth gradients").
- **Official style blocks** (copy as ① style): flat colouring (design sheet), stronger linework, monochrome manga (strip "prominent sound effects"), fine manga lines, cel anime screencap, realistic backgrounds, 3D-render look, ukiyo-e, GALGAME/VN CG, pixel art, lighting/lens, detail richness, high-contrast chiaroscuro. Plus the Color Palette panel for a fixed palette.
- **Use:** consistency sets, EXT assets via the reference slot, any Pixiv style below.

### `GPTANIME` · "ChatGPT anime" (soft clean, Ghibli-adjacent)
User-facing label for the look GPT image generation in ChatGPT typically produces for "anime style" requests. Descriptive reproduction, not an official preset; based on widely shared output and community descriptions — treat traits as typical, not guaranteed.
- **Look:** clean, even, medium-weight outlines; simple 2-tone soft cel with few gradients; rounded, simplified friendly faces; moderately large eyes with one or two simple highlights; matte skin with soft blush; gentle low-to-mid contrast; soft even daylight; tidy centred composition; painterly but uncluttered backgrounds (cozy interiors, green countryside, soft clouds); slightly warm colour grade. Older GPT-4o-era output often carried a strong warm amber/sepia cast; newer GPT image versions are reported to be more neutral.
- **Grok / Tsubaki NL:** "soft clean anime illustration, even medium-weight outlines, simple two-tone soft cel shading, rounded friendly facial features, gentle eyes with simple highlights, matte skin with soft blush, soft even daylight, low contrast, warm gentle colour grade, painterly uncluttered background, hand-drawn storybook warmth". Optional `+warm cast`: "subtle warm amber colour cast".
- **Haruka tags:** `anime coloring, flat color, soft shading, simple shading, warm lighting, muted colors, painterly background, soft lighting` (negative add: `glossy skin, shiny skin, high contrast`).
- **Use:** wholesome, cozy, comfort, slice of life. **Avoid on heat beats** (rounded simplified faces read young → keep adult tokens first, mature face, 1:7).

## Pixiv illustration styles (2.2)

- `ATSUNURI` · thick paint (厚塗り) · **opaque painterly brushwork, lines dissolved into paint, rich layered shadows, strong value structure, painted highlights on hair and skin, deep saturated midtones, visible brush texture** · `thick paint, painterly, impasto, realistic shading, dark background` · dark romance, fantasy, drama. Best on Tsubaki.3 (write "opaque oil-like strokes, no clean outlines").
- `GLOSSREAL` · glossy semi-realistic · **semi-realistic anime proportions, fine sharp lineart, subsurface-scattered skin, multi-highlight glossy eyes, strand-level glossy hair, realistic fabric sheen, soft cinematic light** · `semi-realistic, glossy skin, detailed eyes, shiny hair, realistic lighting` · sensual/adult romance, portraits. Stays 2D: "illustration, not a photograph".
- `SUISAI` · soft digital watercolour · **transparent soft washes, wet-edge blooms, light coloured lineart, white paper showing in highlights, pale airy palette, gentle bleed between colours** · `watercolor (medium), traditional media, pastel colors, soft lighting, light lineart` · melancholy, romance, quiet moments.
- `FLATLINE` · flat-colour lineart · **confident uniform lineart, flat colour fills, one hard shadow tone at most, limited harmonious palette, graphic negative space, no gradients** · `flat color, lineart, limited palette, no shading, simple background` · comedy, wholesome, design-forward; drifts least on simple scenes.
- `RIMLIGHT` · high-contrast rim light · **strong backlight, bright rim lines along hair and shoulders, deep shadowed front, saturated accent glow, high contrast, dark ambient, bloom on edges** · `backlighting, rim lighting, high contrast, dark, glowing, light particles` · obsession, night, confrontation.
- `YUMEKAWA` · pastel kawaii (ゆめかわいい) · **pastel pink-lavender-mint palette, soft airbrush shading, sparkles and star motifs, dreamy glow, lace and ribbon details, low contrast** · `pastel colors, sparkle, star (symbol), dreamy, soft lighting` · idol, fashion, sweet greetings. **Adult tokens first, mature face; not for heat beats.**
- `KUUKI` · atmospheric "air-feel" (空気感) · **soft volumetric light, haze and light dust, cinematic depth of field, detailed painted background, small figure in a large space, cool-warm colour contrast, quiet emotional mood** · `scenery, light rays, depth of field, cinematic lighting, atmospheric perspective` · summer, nostalgia, longing; establishing frames.
- `NEONPOP` · vivid pop · **thick bold outlines, saturated neon accents, flat colour blocks with hard shadows, graphic shapes, high-energy composition, magenta-cyan-yellow palette** · `vibrant colors, bold outline, pop art, colorful, neon` · idol, party, street. Write "graphic shapes, no lettering" — pop art invites text.
- `BRUSHSOFT` · soft brush painting (ブラシ塗り) · **soft round-brush shading, gentle gradients, thin warm lineart, glowing skin, delicate eyelashes, warm diffuse light** · `soft shading, blending, warm lighting, delicate` · romance, slice of life; halfway between `KYO` and `PAINT`.

## Library — classic & modern anime

- `MOE` · soft bishoujo · **vibrant soft shading, large glossy eyes, clean bishoujo polish, pastel accents, sparkle highlights** · `moe, soft shading, sparkling eyes` · cute greetings. Avoid on heat beats (under-age read risk).
- `CEL00` · 2000s TV cel · **flat cel shading, hard colour holds, TV anime screencap finish, clean thick-thin lineart, limited palette** · `anime screencap, cel shading, 2000s (style)` · classic look, comedy.
- `PAINT` · Pixiv painterly sensual · **clean delicate linework, soft painterly airbrush gradients, glossy illustrated skin highlights, dense eyelashes, luminous soft palette, semi-realistic anime that stays 2D** · `delicate lineart, painterly, soft shading, glossy skin` · adult/sensual illustration.
- `KEYVIS` · modern TV key visual (soft modern TV) · **crisp lineart, soft cel with gradient shadows, rim light, detailed background, polished key-visual finish**
- `GACHA` · gacha/game splash art · **ornate layered costume, glossy highlights, dynamic key art pose, particle effects, game splash composition, high detail accessories**
- ★ `GAMECG` · game CG / official art · **game CG illustration, soft bloom, rich fabric folds, cinematic key light, official-art polish**
- ★ `SEMIGLOSS` · semi-real gloss · **thin sharp lineart, multi-highlight glassy eyes, glossy hair sheen, nose shine, smooth painterly skin**
- `VNCG` · visual novel / galgame CG (PixAI block) · **visual novel CG style, Japanese bishoujo illustration, soft cel shading, romantic lighting, polished character rendering**
- `KYO` · soft emotional TV drama · **delicate eye detail, fine individual hair strands, soft emotional lighting, gentle pastel grading, subtle blush**
- `SKYCINE` · cinematic sky/film anime · **vivid detailed skies, towering clouds, lens flare, glowing light shafts, hyper-detailed painted backgrounds, cinematic atmosphere**
- `GHIBLISH` · hand-painted pastoral · **hand-drawn feel, watercolor-painted backgrounds, soft natural palette, gentle rounded character design, nostalgic warmth** (see also `GPTANIME`)
- `SHONEN` · action shonen · **bold confident lineart, high-contrast cel shadows, speed lines, dynamic foreshortening, saturated primaries**
- `SEINEN` · dark seinen · **muted desaturated palette, heavy shadows, realistic proportions, gritty textures, cinematic framing**
- `CYBER` · cyberpunk anime · **neon rim lighting, holographic glows, techwear detail, wet reflective streets, teal-magenta palette** (signs: "unreadable glowing signs")
- `DARKFAN` · dark fantasy · **dramatic chiaroscuro, ornate armor and cloth, desaturated jewel tones, painterly smoke and embers**

## Library — retro

- `RETRO90` · 1990s TV cel · **1990s anime screencap, cel paint with visible paint edges, hand-drawn linework, film grain, slight VHS colour bleed, muted saturated palette** (+ genre: shoujo / mecha / noir)
- `OVA80` · late-80s OVA · **detailed hand-inked linework, airbrushed highlights, dramatic backlight, sharp angular faces, rich dark palette, film grain**
- `SHOUJO90` · retro shoujo · **fine warm-brown linework, sparkle motifs, parallel blush hatching, soft cel-hybrid gradients, high-key pastels, flower accents**
- `CITYPOP` · city-pop / 80s poster · **flat pastel gradients, sunset palette, clean retro lineart, poster-like composition, glossy highlights** (no poster lettering)

## Library — manga & comics rendering (single illustrations; never panels or bubbles unless `bubbles=ON`)

- `MANGA` · modern monochrome manga rendering · **black ink lines, white highlights, grey screentones, smooth digital lines, expressive faces, gentle radiating lines** + "a single illustration, not a comic page, no panels"
- `MANGAFINE` · fine manga lines · **black-and-white line art, simple diagonal hatching on shadows, minimal composition, clean modern draftsmanship**
- `RETROMANGA` · 90s manga ink · **heavy ink weights, halftone dots in shadows, expressive retro hair shapes, high-contrast blacks**
- `MANHWA` · webtoon/manhwa colour · **clean thin ink lines, polished soft gradient shading, elongated elegant proportions, glossy hair, dramatic vertical framing** (PixAI: Serin model targets this look)
- `WEBTOONFLAT` · flat webtoon · **flat colour fills, minimal shading, bright clean palette, simple backgrounds, bold silhouettes**
- `SKETCH` · pencil/ink sketch · **loose pencil construction lines, cross-hatching, unfinished edges, paper texture**

## Library — sheets & special

- `SHEET` · character design sheet (PixAI flat block) · **pure flat colouring, no shading, no highlights, solid colour fills, clean anime lineart, washed-out pale palette, production model sheet** — turnarounds and ISO sheets in Mio's own designs. For EXT assets the sheet keeps the **source** rendering instead.
- `CHIBI` · SD/chibi (**non-sexual only**, keep 25 in text) · **super-deformed 1:2 proportions, rounded shapes, simple eyes, bright flat colours**
- `FIGURE` · PVC figure look (fictional character only) · **glossy painted plastic surface, smooth highlights, visible seam lines, figure base, studio light**
- `UKIYOE` · woodblock · **bold contour lines, flat colour areas, traditional Japanese composition, paper grain**
- `PIXEL` · pixel art · **visible pixel grid, limited palette, dithering, hard-edged pixels, retro game sprite**
- `WATERCOLOR` · traditional paper watercolour · **transparent watercolour washes, soft bleeding edges, light pencil lines, visible paper texture** (digital soft version: `SUISAI`)

## Effect blocks (add-ons, never a style by themselves)

- `+LENS` · chromatic aberration, film grain, bloom, slight overexposure, glossy specular highlights
- `+DETAIL` · hyper-detailed illustration, detailed background, intricate fine textures, precise linework on background objects
- `+CHIARO` · extreme chiaroscuro, deep blacks, bright highlights, harsh directional light, almost no midtones
- `+LINES` · crisp clean lineart, sharp outlines, flat cel shading, defined anatomy
- `+BGREAL` · slightly realistic, blurred-depth background behind a 2D character
- `+WARM` · subtle warm amber colour grade (for `GPTANIME`)

## Showing styles

"What styles can you do?" → IDs + labels in one compact block (no images). When the user picks 1–3, render the **same locked character** in each; never change FACE/BODY while testing styles. Testing styles does not change the canvas until the user picks one.
