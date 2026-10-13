# Gateway Engineering redesign preview

A static preview of the redesigned Gateway Engineering homepage (the "Apple-style" design). It lives beside the
current Gatsby site and doesn't touch it: Vercel serves only this folder.

- `index.html`: the whole page (markup, styles and scroll animations), with no build step and no dependencies
- `assets/`: the photos, logos and the promo video loop
- `vercel.json`: keeps the preview out of search engines and caches assets for a day

## Run it locally

Any static file server works, for example:

```sh
cd preview
python3 -m http.server 8080
```

Then open http://localhost:8080. Scroll animations need a window at least 760px wide. Narrower windows, and
visitors who ask for reduced motion, get the static layout.

## Deploy to Vercel

Create a Vercel project from this repository with **Root Directory** set to `preview`, **Framework Preset** set to
"Other", and no build command. Every push to the project's production branch then redeploys the preview.

## Where it comes from

The page is exported from the design canvas artboard by `design/export-apple-artboard.py`. The export turns the
canvas runtime's template features (refs, click handlers, the conditional mobile menu and canvas asset URLs) into
plain HTML and a small script. Until the design is final, change it on the canvas and re-export rather than
editing `index.html` by hand, or the next export will overwrite the edits.

Placeholders still to replace before launch:

- `assets/video/promo-loop.mp4` is cut from free stock footage until the real promo is shot
- Contact links go to the footer's contact details because there is no contact page yet
