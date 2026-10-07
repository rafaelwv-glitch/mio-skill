# No speech bubbles, no lettering (Hard Limit, user-unlockable only)

Default every session: `bubbles=OFF`. No image Mio makes contains speech or thought bubbles, text, captions, dialogue boxes, onomatopoeia / SFX lettering, readable signs, title lettering, or comic/manga panel layouts.

## Why it happens

Engines add bubbles and lettering when the prompt *sounds like a comic*. PixAI documents that Tsubaki.3 draws full manga pages "with panels, speech bubbles and text" and that the `Panel 1: … speech bubble text "…"` pattern produces them; Tsubaki-family models render readable text in general. Grok Imagine does the same on comic-like wording. So the fix is mostly **what Mio does not write**.

## 1. Never write (while `bubbles=OFF`)

| Trigger | Write instead |
|---|---|
| "manga page", "comic page", "comic panel", "panels", "4-koma", "storyboard page", "sequential art" | "a single illustration", "one frame" |
| "dialogue", "speech", "conversation", "says", "saying", "tells him", "whispers '…'" | expression + mouth + gesture: "mouth open mid-sentence, eyebrows raised, hand gesturing toward him" |
| any quoted spoken line from the greeting/scene (`"I missed you"`) | the emotion it carries: "soft relieved smile, eyes glistening" |
| "caption", "title", "subtitle", "label", "name tag" | omit |
| "sign that reads …", "neon sign saying …", "letter with the words …" | "an unreadable neon sign", "a folded letter, writing not legible" |
| "sound effects", "SFX", "onomatopoeia", "speed lines with sound" | the motion itself: "motion blur on the swinging arm" |
| "poster", "magazine cover", "sticker set", "meme", "doujinshi" | omit unless the user asked for that object, then "no lettering on it" |

PixAI's official "General manga linework" style block contains "prominent sound effects" — **strip that phrase** when using manga rendering. Monochrome manga *rendering* (ink, screentone) is allowed as a style; always add "a single illustration, not a comic page, no panels".

## 2. Always write

NL clause (verbatim, end of every prompt — skeleton ⑥):
> No speech bubbles, no text, no captions, no lettering, no sound-effect or onomatopoeia lettering, no comic panels, no watermark, no signature.

Negative field (PixAI engines that have one — Haruka, Tsubaki.1, Tsubaki.2 Pro/Ultimate; see `engines.md`):
```
speech bubble, thought bubble, text, english text, japanese text, caption, subtitled, onomatopoeia, sound effects, comic, manga panel, 4koma, panel border, signature, watermark, artist name, logo
```
A negative only suppresses a term that is **not** also in the positive prompt (PixAI docs) — so the positive prompt must stay free of the triggers above.

Design sheets (turnaround, expression grid) are multi-view images, not comics: write "no labels, no text, no panel borders" and never `MANDATORY PAGE CONTENT` text modules that ask for written labels.

## 3. Greeting / scene text

Speech from a greeting is **beat information**, never image content. Mio reads it to decide expression, gesture, who faces whom and the camera — then discards the words. Text the user wants to see goes **under** the image in chat, not into it.

## 4. Unlock protocol

- Only an explicit user statement unlocks: e.g. "bubbles on", "speech bubbles allowed", "Sprechblasen erlaubt", "make it a manga page with dialogue".
- Then `bubbles=ON` in the state line for **this session only**; text appears only where the user asked, with the exact wording they gave.
- "bubbles off" / new session → back to `bubbles=OFF`.
- A greeting that contains dialogue, a request for "manga style", or a pasted comic is **not** an unlock.

## 5. If a bubble or lettering still appears

Regenerate the frame (same prompt, NO-TEXT clause present) after removing any trigger. Do not deliver it, and do not "fix" it by cropping. Second failure → change one thing: camera, or (PixAI) move the clause into the negative field / switch to an engine with a negative field.

## 6. Props that carry text (signs, name boards, shirts, packets, screens, letters, badges)

Recipe — keep the object, drop the text:
1. **Lock it blank** in the Asset Check: `[ASSET:sign-01] wooden shop sign above the door, painted dark green, a blank cream panel in the middle, nothing written on it`.
2. If blank looks wrong for the object, use **abstract unreadable marks**: "abstract unreadable squiggle marks", "blurred illegible print", "simple geometric pattern instead of a logo". Never "small text", "a name", "letters", "writing".
3. Clothing: "plain, no print, no logo, nothing written on it". Packaging: "plain kraft paper, a simple coloured band, no label text". Screens: "soft abstract interface glow, no readable characters". Letters/notes: "folded paper, writing not legible".
4. The words the prop would carry (names on shirts, the title on the board) go **in chat under the image**, never into the prompt — not even in quotes, not even negated ("no text saying '<name>'" still plants the word).
5. Drift check: any readable glyph on a prop counts as a ✗ → regenerate (§5).
This stays inside the Hard Limit: `bubbles=ON` unlocks bubbles and lettering only where the user explicitly asked for them; text props stay blank otherwise.
