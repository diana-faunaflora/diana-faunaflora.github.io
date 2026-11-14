---
title: "Stuck on the start screen"
description: "Script blockers and strict browsers: what Diana needs, and nothing more."
sidebar:
  order: 2
---

Diana is a web app: without JavaScript nothing runs. If a blocker stops the scripts, Diana stays on the start screen. After a while a box appears there saying so.

## Solving it

1. Allow scripts for **diana-onff.github.io** only. Not `github.io` and not `github.com`: Diana needs neither.
2. **Reload the page**: **F5** or **Ctrl+R** (Mac: **Cmd+R**). On a phone, pull the page down or tap reload. Without reloading, the old block stays, even after you clicked "Trust".
3. Still stuck? A second extension may block too (an ad blocker, a privacy extension). Switch them off one at a time for this site.
4. Diana starts but the map stays empty? Allow `blob:` workers for diana-onff.github.io (see below).

## What Diana loads

**Scripts**: all from diana-onff.github.io itself.

| File | What it is |
|---|---|
| `vendor/maplibre-gl.js` | MapLibre, the map library. A copy on Diana’s own site, not from a CDN. |
| `js/*.js` | Diana’s own code. |
| `sw.js` | The service worker that keeps Diana working offline. |

No inline scripts and no `eval`. One exception, only with your consent: if you said yes to statistics, the Umami script from `cloud.umami.is`.

**Map worker**: MapLibre draws the map in a background worker started from a `blob:` address. A blocker that refuses `blob:` workers lets Diana start but leaves the map blank.

**Data**:

| Host | Why |
|---|---|
| `tiles.openfreemap.org` | Map tiles and label fonts |
| `spots.wwff.co` | Live spots and agenda |
| `diana-spotline.diana-onff.workers.dev` | Only when you send a spot or announcement |
| `raw.githubusercontent.com` | Space weather for Conditions |
| `cloud.umami.is` | Only if you said yes to statistics |

Your position is never sent anywhere.
