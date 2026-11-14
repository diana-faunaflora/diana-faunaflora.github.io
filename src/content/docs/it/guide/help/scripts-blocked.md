---
title: "Bloccato sulla schermata di avvio"
description: "Blocca-script e browser restrittivi: di cosa ha bisogno Diana, e niente di più."
sidebar:
  order: 2
---

Diana è un’app web: senza JavaScript non funziona nulla. Se un blocco ferma gli script, Diana resta sulla schermata di avvio. Dopo un po’ compare lì un riquadro che lo dice.

## Risolvere

1. Consenti gli script solo per **diana-onff.github.io**. Non `github.io` e non `github.com`: a Diana non servono.
2. **Ricarica la pagina**: **F5** o **Ctrl+R** (Mac: **Cmd+R**). Sul telefono trascina la pagina verso il basso o tocca ricarica. Senza ricaricare, il vecchio blocco resta, anche dopo aver fatto clic su "Considera attendibile".
3. Ancora bloccato? Una seconda estensione può bloccare a sua volta (un blocco pubblicità, un’estensione per la privacy). Disattivale una alla volta per questo sito.
4. Diana parte ma la mappa resta vuota? Consenti i worker `blob:` per diana-onff.github.io (vedi sotto).

## Cosa carica Diana

**Script**: tutti da diana-onff.github.io stesso.

| File | Cos’è |
|---|---|
| `vendor/maplibre-gl.js` | MapLibre, la libreria delle mappe. Una copia sul sito di Diana, non da una CDN. |
| `js/*.js` | Il codice di Diana. |
| `sw.js` | Il service worker che fa funzionare Diana offline. |

Nessuno script inline e nessun `eval`. Un’eccezione, solo con il tuo consenso: se hai detto sì alle statistiche, lo script Umami da `cloud.umami.is`.

**Worker della mappa**: MapLibre disegna la mappa in un worker in background avviato da un indirizzo `blob:`. Un blocco che rifiuta i worker `blob:` lascia partire Diana ma lascia la mappa vuota.

**Dati**:

| Host | Perché |
|---|---|
| `tiles.openfreemap.org` | Tessere della mappa e caratteri delle etichette |
| `spots.wwff.co` | Spot in diretta e agenda |
| `diana-spotline.diana-onff.workers.dev` | Solo quando invii uno spot o un annuncio |
| `raw.githubusercontent.com` | Meteo spaziale per Condizioni |
| `cloud.umami.is` | Solo se hai detto sì alle statistiche |

La tua posizione non viene mai inviata da nessuna parte.
