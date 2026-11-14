---
title: "Privacy"
description: "What Diana knows, what it does not know, and why."
sidebar:
  order: 9
---

Diana is built so that your data stays with you. This page sums up the privacy page in the app (**Settings** › **Privacy** › **Open the privacy page**).

## In short

- Your callsign, locator and settings stay in the browser of this device. Nothing is sent anywhere.
- Your GPS position is used only on the screen in front of you. It is never sent anywhere.
- Spotting yourself sends your callsign, frequency, mode and reference to WWFF Spotline, never your position.
- With your separate permission, Diana can count an anonymous visit. Nothing is counted unless you say yes, and you can change your mind any time under Settings.
- Diana sets no advertising cookies and builds no profile of you.

## What stays on this device

Your callsign, portable callsign, locator, and settings such as bands, the distance for Field info, quick words and language, together with your statistics choice and whether you have seen the welcome screen. Diana also keeps an offline copy of the map tiles and of the app itself, so it keeps working without signal. That is ordinary browser cache, not personal data.

## Services Diana talks to

| Service | Why |
|---|---|
| WWFF Spotline (`spots.wwff.co`) | Live spots and the agenda. Receives your callsign, frequency, mode, reference and remark when you spot yourself. Never your position. |
| OpenFreeMap (`tiles.openfreemap.org`) | The map tiles, built from OpenStreetMap data. No cookies. |
| The Diana relay (a Cloudflare Worker) | Passes your spot or announcement on to Spotline. Counts requests per hashed IP address against abuse, never logs your callsign, position or remark. |
| Umami (`cloud.umami.is`) | Counts an anonymous visit, only with your permission. No cookies, no personal data. |

## What a self-spot sends

Exactly this, and nothing else: the activator’s callsign, the spotter’s callsign, the frequency, the mode, the reference and an optional remark you typed yourself. Never your position.

## Clearing everything

**Settings** › **Privacy** › **Clear everything on this device** removes everything Diana stored on this device: your callsign, settings, offline map tiles and your statistics choice. Diana then starts again at the welcome screen.

## Your rights and contact

Because Diana keeps your personal settings only on your own device, viewing, correcting or deleting them is as simple as opening Settings. For anything about the anonymous statistics, or a complaint, the privacy page in the app gives the contact address. In Belgium you can also turn to the Data Protection Authority (gegevensbeschermingsautoriteit.be).
