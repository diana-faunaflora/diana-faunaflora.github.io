---
title: "Sono dentro l’area?"
description: "Come Diana ti dice se sei dentro, e come leggere la precisione."
sidebar:
  order: 6
---

Una scheda in fondo alla mappa risponde alla domanda di ogni attivatore: **sono dentro la riserva?**

## Cosa dice la scheda

- **Dentro un’area**: quale, e la distanza dal confine più vicino.
- **Dentro più aree insieme** (quando le aree si sovrappongono): quante, e si apre il pannello della più piccola. Vedi [Aree sovrapposte](/it/guide/map/overlapping-areas/).
- **Fuori**: l’area più vicina e quanto dista.

Ogni risposta termina con la qualità della tua posizione, per esempio *"posizione ±6 m"*.

:::note[Aree fatte di più parti]
Alcune referenze sono composte da parti separate. Il pannello dice allora quante. Tutta la tua stazione deve stare dentro una di esse.
:::

## Perché ci vogliono alcuni secondi

Un telefono che ha appena svegliato il GPS risponde prima da wifi e celle, e quella posizione può sbagliare di centinaia di metri. Per questo Diana continua ad ascoltare mentre la precisione migliora, e mostra ciò che ha finora: *"Affinamento… ±380 m"*. Risponde appena la posizione è abbastanza buona, o dopo dodici secondi con la migliore ottenuta. Se è ancora grossolana, la risposta lo dice.

## Leggere la precisione

| Precisione | Cosa significa di solito |
|---|---|
| ±10 m o meglio | Satelliti. Affidabile, anche vicino a un confine. |
| da ±20 a 50 m | Ragionevole. Attenzione vicino a un confine. |
| ±100 m o peggio | Wifi o celle, spesso al chiuso. Non abbastanza per essere sicuri. |

Quando il margine supera circa 10 m, attorno al tuo indicatore viene disegnato un **anello tratteggiato** esattamente di quel raggio. Un anello stretto significa satelliti; un anello che copre tutto l’isolato significa che la risposta è arrivata dal wifi.

:::tip[Ottenere una posizione migliore]
Esci all’aperto, con il cielo libero sopra di te, e aspetta qualche secondo. Resta grossolana, oltre circa 75 m? Forse il sito può usare solo una posizione approssimativa. Compare allora un avviso che suggerisce di controllare l’impostazione di localizzazione: vedi [Problemi di posizione](/it/guide/help/location-problems/).
:::

## Due trappole che Diana sorveglia

- **Al chiuso**, una posizione da wifi arriva spesso in un secondo dichiarando ±20 m. È la precisione che il database wifi si attribuisce, non quella reale. Diana risponde, ma continua ad ascoltare per il resto dei dodici secondi e corregge la risposta se serve.
- **Telefoni che promettono più di quanto possono.** Diana confronta le letture degli ultimi 45 secondi. Una singola lettura assurda viene ignorata. Se le letture si contraddicono, la risposta dice *"letture in contraddizione"*. Camminare non conta come dispersione.

:::caution
Diana può rispondere solo per le aree **con** confine. Per un anello tratteggiato o un punto blu non può. Vedi [Punti e aree](/it/guide/map/points-and-areas/).
:::
