---
title: "Vast op het startscherm"
description: "Scriptblokkers en strenge browsers: wat Diana nodig heeft, en niets meer."
sidebar:
  order: 2
---

Diana is een web-app: zonder JavaScript draait er niets. Houdt een blokker de scripts tegen, dan blijft Diana op het startscherm. Na een tijdje verschijnt daar een vak dat dat zegt.

## Zo los je het op

1. Sta scripts toe voor **diana-onff.github.io**, en alleen daarvoor. Niet `github.io` en niet `github.com`: die heeft Diana niet nodig.
2. **Laad de pagina opnieuw**: **F5** of **Ctrl+R** (Mac: **Cmd+R**). Op een gsm trek je de pagina naar beneden of tik je op herladen. Zonder herladen blijft de oude blokkering staan, ook als je al op "Vertrouwen" klikte.
3. Nog vast? Misschien blokkeert een tweede extensie (een advertentieblokker, een privacy-extensie). Zet ze voor deze site een voor een uit.
4. Diana start maar de kaart blijft leeg? Sta `blob:`-workers toe voor diana-onff.github.io (zie hieronder).

## Wat Diana laadt

**Scripts**: allemaal van diana-onff.github.io zelf.

| Bestand | Wat het is |
|---|---|
| `vendor/maplibre-gl.js` | MapLibre, de kaartbibliotheek. Een kopie op Diana’s eigen site, niet van een CDN. |
| `js/*.js` | Diana’s eigen code. |
| `sw.js` | De service worker die Diana offline laat werken. |

Geen inline scripts en geen `eval`. Eén uitzondering, alleen met jouw toestemming: als je ja zei tegen statistieken, het Umami-script van `cloud.umami.is`.

**Kaartworker**: MapLibre tekent de kaart in een achtergrondworker die start vanaf een `blob:`-adres. Een blokker die `blob:`-workers weigert, laat Diana starten maar houdt de kaart leeg.

**Gegevens**:

| Adres | Waarom |
|---|---|
| `tiles.openfreemap.org` | Kaarttegels en lettertypes van de labels |
| `spots.wwff.co` | Live spots en agenda |
| `diana-spotline.diana-onff.workers.dev` | Alleen als je een spot of aankondiging verstuurt |
| `raw.githubusercontent.com` | Ruimteweer voor Condities |
| `cloud.umami.is` | Alleen als je ja zei tegen statistieken |

Je positie wordt nooit ergens naartoe gestuurd.
