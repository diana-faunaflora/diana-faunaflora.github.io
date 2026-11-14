---
title: "Fast på startskærmen"
description: "Script-blokeringer og strikse browsere: hvad Diana har brug for, og intet mere."
sidebar:
  order: 2
---

Diana er en web-app: uden JavaScript kører intet. Stopper en blokering scriptsene, bliver Diana på startskærmen. Efter et stykke tid dukker der en boks op dér, der siger det.

## Løsning

1. Tillad kun scripts for **diana-onff.github.io**. Ikke `github.io` og ikke `github.com`: Diana har ikke brug for nogen af dem.
2. **Genindlæs siden**: **F5** eller **Ctrl+R** (Mac: **Cmd+R**). På en telefon trækker du siden ned eller trykker på genindlæs. Uden at genindlæse bliver den gamle blokering stående, også efter du har klikket på "Stol på".
3. Stadig fast? En anden udvidelse kan også blokere (en annonceblokering, en privatlivsudvidelse). Slå dem fra én ad gangen for dette websted.
4. Starter Diana, men kortet forbliver tomt? Tillad `blob:`-workers for diana-onff.github.io (se nedenfor).

## Hvad Diana indlæser

**Scripts**: alle fra diana-onff.github.io selv.

| Fil | Hvad det er |
|---|---|
| `vendor/maplibre-gl.js` | MapLibre, kortbiblioteket. En kopi på Dianas eget websted, ikke fra et CDN. |
| `js/*.js` | Dianas egen kode. |
| `sw.js` | Service workeren, der holder Diana kørende offline. |

Ingen inline-scripts og ingen `eval`. Én undtagelse, kun med dit samtykke: har du sagt ja til statistik, Umami-scriptet fra `cloud.umami.is`.

**Kort-worker**: MapLibre tegner kortet i en baggrunds-worker, der startes fra en `blob:`-adresse. En blokering, der afviser `blob:`-workers, lader Diana starte, men kortet forbliver blankt.

**Data**:

| Vært | Hvorfor |
|---|---|
| `tiles.openfreemap.org` | Kortfliser og skrifttyper til etiketter |
| `spots.wwff.co` | Live-spots og agenda |
| `diana-spotline.diana-onff.workers.dev` | Kun når du sender et spot eller en annoncering |
| `raw.githubusercontent.com` | Rumvejr til Forhold |
| `cloud.umami.is` | Kun hvis du har sagt ja til statistik |

Din position sendes aldrig nogen steder hen.
