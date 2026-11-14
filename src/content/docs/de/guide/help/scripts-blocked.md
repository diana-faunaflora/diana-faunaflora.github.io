---
title: "Hängt auf dem Startbildschirm"
description: "Skriptblocker und strenge Browser: was Diana braucht, und nicht mehr."
sidebar:
  order: 2
---

Diana ist eine Web-App: ohne JavaScript läuft nichts. Hält ein Blocker die Skripte an, bleibt Diana auf dem Startbildschirm. Nach einer Weile erscheint dort ein Kasten, der das sagt.

## Lösen

1. Erlaube Skripte nur für **diana-onff.github.io**. Nicht `github.io` und nicht `github.com`: beides braucht Diana nicht.
2. **Lade die Seite neu**: **F5** oder **Strg+R** (Mac: **Cmd+R**). Auf dem Smartphone ziehst du die Seite nach unten oder tippst auf Neu laden. Ohne Neuladen bleibt die alte Sperre, auch wenn du schon auf „Vertrauen“ geklickt hast.
3. Hängt es immer noch? Vielleicht blockiert eine zweite Erweiterung mit (ein Werbeblocker, eine Datenschutz-Erweiterung). Schalte sie für diese Seite nacheinander aus.
4. Diana startet, aber die Karte bleibt leer? Erlaube `blob:`-Worker für diana-onff.github.io (siehe unten).

## Was Diana lädt

**Skripte**: alle von diana-onff.github.io selbst.

| Datei | Was es ist |
|---|---|
| `vendor/maplibre-gl.js` | MapLibre, die Kartenbibliothek. Eine Kopie auf Dianas eigener Seite, nicht von einem CDN. |
| `js/*.js` | Dianas eigener Code. |
| `sw.js` | Der Service Worker, der Diana offline am Laufen hält. |

Keine Inline-Skripte und kein `eval`. Eine Ausnahme, nur mit deiner Zustimmung: wenn du Ja zur Statistik gesagt hast, das Umami-Skript von `cloud.umami.is`.

**Karten-Worker**: MapLibre zeichnet die Karte in einem Hintergrund-Worker, der von einer `blob:`-Adresse gestartet wird. Ein Blocker, der `blob:`-Worker verweigert, lässt Diana starten, aber die Karte bleibt leer.

**Daten**:

| Host | Wozu |
|---|---|
| `tiles.openfreemap.org` | Kartenkacheln und Schriften der Beschriftung |
| `spots.wwff.co` | Live-Spots und Agenda |
| `diana-spotline.diana-onff.workers.dev` | Nur wenn du einen Spot oder eine Ankündigung sendest |
| `raw.githubusercontent.com` | Weltraumwetter für Bedingungen |
| `cloud.umami.is` | Nur wenn du Ja zur Statistik gesagt hast |

Deine Position wird nie irgendwohin geschickt.
