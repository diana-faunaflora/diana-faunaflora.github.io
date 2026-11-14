# Diana Fauna & Flora: info site and user guide

The public information site and user guide of [Diana](https://diana-onff.github.io/),
the free map app for WWFF activators and hunters.

Live at **https://diana-faunaflora.github.io/**

- Start page (presentation of the app) in every language at `/`, `/nl/`, …
- User guide at `/guide/…` (English, the default) and `/<lang>/guide/…` for nl, fr, de,
  da, it, es and pt. Translations live in tools/tr/<lang>/ (guide) and
  src/i18n/landing-<lang>.mjs (start page); a missing page falls back to English.
- Search in the guide, per language, built in (Pagefind). No server, no cookies, no tracking.
- The presentation as PDF in eight languages: `public/presentation/`.

Built with [Astro](https://astro.build) and [Starlight](https://starlight.astro.build).
GitHub Actions builds and publishes the site on every push to `main`.

## Changing a text

Every page of the guide is one Markdown file:

| Language | Folder |
|---|---|
| English | `src/content/docs/guide/<section>/<page>.md` |
| Dutch | `src/content/docs/nl/guide/<section>/<page>.md` |
| Other languages | `src/content/docs/<fr\|de\|da\|it\|es\|pt>/guide/<section>/<page>.md` (create the same file name) |

To change a page on GitHub:

1. Open the file, click the pencil (**Edit this file**).
2. Change the text. Keep the block between the two `---` lines at the top (title, description, order).
3. Click **Commit changes**. After one or two minutes the site is updated.

Useful in Markdown:

- `**bold**`, `*italic*`, `` `ONFF-0104` `` for references, frequencies and file names.
- A numbered list (`1.`, `2.`) is shown as step circles.
- A box: `:::tip[Title]` … `:::` (also `:::note`, `:::caution`, `:::danger`).
- A link to another page: `[Overlapping areas](/guide/map/overlapping-areas/)`
  (Dutch: `/nl/guide/…`).
- A screenshot: `![Description](../../../../assets/screens/phone-map.webp)` (one `../` more
  in a language folder). Files whose name starts with `phone-` are shown in a phone frame.

The start page texts are in `src/i18n/landing.mjs` (English and Dutch; copy the `en` block
to add a language).

## Structure

```
astro.config.mjs          site settings, languages
src/sidebar.mjs           sections of the guide and their names in 8 languages
src/content/docs/         the guide pages (Markdown)
src/i18n/landing.mjs      texts of the start page
src/components/           start page and header button
src/styles/               house style (fonts, colours) of guide and start page
src/scripts/landing.js    slider, live spots, live numbers, search on the start page
src/assets/               logo, screenshots
public/presentation/      the presentation PDFs
tools/                    the generator that wrote the first version of the pages
.github/workflows/        build and publish on GitHub Pages
```

`tools/gen.py` wrote the first version of every guide page from `tools/pages_*.py`. After
that, edit the Markdown files directly; running the generator again overwrites them.

## Building on your own computer (optional)

Needs Node.js 22.

```
npm ci
npm run dev       # live preview on http://localhost:4321/
npm run build     # the finished site in dist/
```

## Privacy

The site sets no cookies and counts nothing. The fonts are served from the site itself.
The start page reads the live spots straight from WWFF Spotline and the numbers from the
Diana app’s own data files.

## Licence

Same as Diana: PolyForm Noncommercial. Data and screenshots remain the property of their
owners.
