# Style library

**Rule 1 — default `JC-KEYART` (2.3.0):** when no style is set, Mio uses **`JC-KEYART`** (below) as the canvas style. Only if the user asks for options does Mio propose 2–3 fitting IDs from the Fit Map (one short line each), with `JC-KEYART` as slot 1. All other IDs remain available by name.
**Rule 2 — lock is law:** the chosen ID + 4–6 of its tokens become `[CANVAS-STYLE]`, reprinted verbatim every frame. A locked style never changes silently — only on explicit user request, then locks are reprinted. Mixing two IDs requires an explicit ask; write both IDs in the block.
**Rule 3 — one canvas, one style:** every character on the canvas (OC, `{{user}}`, NPCs, crowd) inherits `[CANVAS-STYLE]` (`storyboard-consistency.md` §5). A style describes rendering only; skin, hair and eye colours belong to each character's `[IDENTITY-COLOURS]`.
**Rule 4 — external sources stay themselves:** a registered asset uses `[STYLE-SOURCE] EXT:<label>` (`original-art.md`). Library IDs are vocabulary for describing it, never a replacement.
**Rule 5 — greeting-recommended (★):** `SEMIGLOSS` and `GAMECG` drift least on close-up beats; include one of them in suggestions for greeting storyboards.
**Rule 6 — descriptors, not people:** styles are described by visible traits. Studio/era/platform names appear only as user-facing labels; never require a living artist's name in a prompt.
**Rule 7 — no text:** no style brings lettering with it. Manga/comic *rendering* is allowed; panels, bubbles and SFX are not (`no-text.md`).

Format: `ID` · label · **tokens** (NL; pick 4–6) · tag hint (HARUKA) · use / avoid.

## DEFAULT style — `JC-KEYART` · dense glossy dark high-fantasy anime key art (2.3.0)

Locked as Mio's **default** by the user on 2026-10-29 (source: style study of a live JuicyChat bot's art, style only, never its characters). Used whenever no style is named (SKILL.md §2). All other library IDs stay available on request or via the Fit Map.

### Style block (slot ①, copy verbatim)
[CANVAS-STYLE] JC-KEYART — 2D anime illustration of an original fictional adult, not a photograph. Dark high-fantasy anime key art, glossy game-splash finish. Thin, crisp, uniform dark-brown lineart with dense ornamental interior detail. Hard cel shadows over smooth airbrushed gradients. Strong glossy specular highlights with bright white hotspots on metal, gems and the hair band; crisp single catchlights in layered anime irises; satin skin. Cool navy-indigo shadows (never pure black) lit by saturated jewel-tone accents (emerald, royal blue, violet, gold) and a warm torchlight counter-light; moonlit rim light from behind; floating light motes; faint haze; fully rendered gothic-fantasy environment.

### Prop rule and full-body framing (every prompt)
- **Every prop named, no unrequested props.** List each prop as "exactly N <prop>", say which hand holds it, then add: "no other props; nothing else in the hands". Name the background furniture too (e.g. "exactly two hanging lanterns") and end with "no other props, no skulls, no vials, no glass tanks, no scrolls". Style refs carry props over, so always say "take ONLY the rendering style, not the characters, props or backgrounds".
- **Full-body framing:** "entire figure visible head to toe, both feet fully in frame with floor space below the feet, small headroom above the head, figure centred". Never combine it with close-up words.

### Framing variants (slot ⑤)
- **3:4 bio portrait:** full-body framing as above, slightly low angle, figure filling about 85% of the height, background environment rendered behind.
- **16:9 greeting:** cinematic wide shot, characters at mid-ground on a diagonal, deep environment with haze, a dominant magic glow in one third, crowds or armies only if named.
- **9:16 greeting:** vertical cinematic shot, full figure in the lower two-thirds, tall architecture or a magic effect rising above, low angle.
- **1:1 PFP:** bust shot from mid-chest up, face in the upper third, three-quarter view, eye catchlights and the hair gloss emphasised, background soft and blurred but in palette.

### Style read (vocabulary)
- **Medium:** 2D digital anime key art, a polished SDXL-anime "illustrious/pony-style" finish. It's dense, high-detail, game-splash quality. It isn't painterly-loose and it isn't photoreal.
- **Linework:** thin, crisp, dark-brown/black lines with uniform weight. The fine interior lines on filigree, chainmail and embroidery are very dense. Faces have light lines.
- **Shading:** a hybrid. Hard cel shadow shapes on faces and skin sit on smooth airbrushed gradients. Cloth gets soft, rendered folds. Metal and gems get glossy speculars with bright white hotspots.
- **Palette and temperature:** cool overall. The ambient is deep navy/indigo-black, lit by jewel-tone accents: necromantic emerald-green fire, royal blue + ivory + gold, violet velvet, and warm orange torch/fire as a counter-light. Saturation is high in the accents and low in the shadows. Blacks are lifted to navy, never pure black.
- **Lighting:** always several sources. Cool moonlight/blue rim from the back windows, a warm key from torches, and coloured magic glow (green or blue) that casts coloured bounce onto the figure. Floating light motes and embers appear often, and wet floors give reflections.
- **Eyes:** medium-large anime eyes with layered irises, a darker top band, one strong catchlight and a soft lower gradient. Lashes are defined but not heavy.
- **Hair:** strand-detailed clumps with a glossy band highlight and many fine flyaway strands. Long hair is wavy and voluminous.
- **Skin:** smooth and warm-neutral, with a soft cel shadow under the jaw/collarbone, a slight blush, and a satin sheen on the shoulders.
- **Faces and proportions:** mature adult faces (late 20s to 60s, which shows the cast's age range), defined jaws and noses. Bodies are tall at 1:7 to 1:8, with heroic but realistic anatomy.
- **Backgrounds:** a fully rendered environment every time. Gothic castle halls, vaults, balconies, a white-and-teal city, ruins. They're dense with props (braziers, banners, ivy, pillars, spires through windows), with atmospheric haze and depth.
- **Composition and camera:** bios are a 3:4 full-body or 3/4 standing portrait, slightly low angle, figure centred and filling the height. Greetings are 16:9 or 9:16 cinematic wides with crowds and dynamic diagonals.
- **Engine hints:** the look and the 1086×1448 / 995×560 sizes point to JuicyChat's SDXL-anime models (the Yuzz Highball / illustrious-type finish). The high detail and glossy speculars rule out Grok's satin look, though Grok Imagine gets close.

### Prompt templates (replace [CHARACTER] and [PROPS])
#### JC: Yuzz Highball (CFG 7, 28–30 steps; 3:4 / 16:9 / 9:16 / 1:1)
```
masterpiece, best quality, very aesthetic, absurdres, anime, dark fantasy, high fantasy, key art, solo, adult, mature, [CHARACTER TAGS], [PROP TAGS], ornate clothes, gold trim, filigree, full body, standing, feet in frame, from below, gothic castle interior, moonlight, window, night, dark blue theme, rim lighting, backlighting, multiple light sources, glowing, light particles, reflective floor, detailed background, intricate details, thin lineart, cel shading, glossy, specular highlights, shiny metal, sparkling gems, shiny hair, detailed eyes, eye highlights, sharp focus
```
Subject tag: `1woman, mature female` or `1man, mature male`. For 1:1 swap `full body, standing, feet in frame` for `upper body, portrait`; for 16:9 use `wide shot, scenery`.
Negative:
```
lowres, worst quality, low quality, bad anatomy, bad hands, extra fingers, missing fingers, extra limbs, child, loli, shota, petite, aged down, gap teeth, missing tooth, text, speech bubble, logo, watermark, signature, username, photorealistic, realistic, 3d, photo, blurry, flat colors, matte, thick lineart, sketch, monochrome, simple background, cropped legs, out of frame
```

#### PixAI / Mio: Tsubaki.3
```
character: original, a single [FORMAT] illustration. [CANVAS-STYLE block verbatim]. [FORMAT framing line]. [CHARACTER: adult, 25+, mature face, head-to-body 1:7, hair, eyes, outfit, pose]. Props: [exactly N named props, which hand]; no other props, nothing else in the hands. Setting: [named location and furniture]; no other props. The light does not change skin tone or hair colour. No speech bubbles, no text, no captions, no lettering, no sound-effect or onomatopoeia lettering, no comic panels, no watermark, no signature. Correct hands, five fingers, no extra limbs.
```
Negative: `photorealistic, 3d render, photo, child, teen, petite, gap teeth, missing tooth, text, letters, watermark, matte, flat colours, thick outlines, sketch, blurry, extra fingers, cropped feet, extra props`
Use one bio PNG as `@image1` with the line "take only the rendering style".

#### Grok Imagine
Use the same structure as Tsubaki.3, without `character: original,`, opening with: "From references 1 and 2 take ONLY the rendering style, not the characters, props or backgrounds. Match the references' rendering exactly; do not restyle." Attach two bio PNGs (tested with bio_06 and bio_10). Known limit: Grok's gloss lands a step below JC's.

### Animation — Grok Imagine video (JC-KEYART)
- **Start from an approved JC-KEYART still** (PNG) as the first frame; never animate from text alone. Prompt describes motion only, the still carries the style.
- **Keep the gloss and lighting:** "keep the exact rendering of the source image: glossy specular highlights on metal, gems and hair, crisp thin lineart, hard cel shadows, navy-indigo shadows, the same coloured light sources and rim light; no change in colour grading, exposure or light direction".
- **Camera:** static, or one slow move only (slow push-in, slow pan or gentle parallax); no cuts, no zoom bursts, no shake, no orbit.
- **Motion:** small, physical and continuous: hair and cloth sway, cape/skirt drift, floating light motes and embers rising, flame and magic-glow flicker, breathing, a blink, a slow head turn or hand gesture. One main action per clip.
- **Loop-safe:** "the final frame returns to the same pose, camera position and lighting as the first frame; motion is cyclic (sway out and back), seamless loop". Avoid one-way actions (walking out, drawing a sword fully) in loop clips; put those in a non-loop beat.
- **No ghosting / morphing:** "stable anatomy and face, no ghosting, no double exposure, no motion trails, no morphing, no flicker on lineart, five fingers on each hand, identity unchanged".
- **No extra props or text:** "no new objects, props, characters or text appear; nothing enters the hands; background stays as in the source".
- Template:
```
Animate the source image. [ONE MAIN ACTION]. Secondary motion: [hair/cloth sway, motes, flame flicker]. Camera: [static | slow push-in]. Keep the exact rendering of the source image: glossy specular highlights on metal, gems and hair, crisp thin lineart, hard cel shadows, navy-indigo shadows, same coloured lights and rim light, no colour or exposure shift. Stable face and anatomy, adult proportions unchanged, no ghosting, no double exposure, no motion trails, no morphing. No new objects, props, characters or text. Final frame returns to the first frame's pose, camera and lighting for a seamless loop.
```
- Delivery: animated WebP (loop), ≤ ~3 MB for hosting; PNG first-frame still alongside. QA the start/end frames for a visible jump and every frame for added props, ghosting or gap teeth.

## Fit Map (suggestions when the user asks for style options)

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
