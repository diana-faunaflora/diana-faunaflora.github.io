---
title: "Sta ik in het gebied?"
description: "Hoe Diana zegt of je binnen staat, en hoe je de nauwkeurigheid leest."
sidebar:
  order: 6
---

Een kaart onderaan de kaart beantwoordt de vraag die elke activator heeft: **sta ik in het reservaat?**

## Wat de kaart zegt

- **In één gebied**: welk, en de afstand tot de dichtste grens.
- **In meerdere tegelijk** (als gebieden overlappen): hoeveel, en het paneel van het kleinste opent. Zie [Overlappende gebieden](/nl/guide/map/overlapping-areas/).
- **Erbuiten**: het dichtstbijzijnde gebied en hoe ver het is.

Elk antwoord eindigt met hoe goed je positie was, bijvoorbeeld *"positie ±6 m"*.

:::note[Gebieden uit meerdere percelen]
Sommige referenties bestaan uit losse percelen. Het paneel zegt dan hoeveel. Je volledige station moet binnen één ervan staan.
:::

## Waarom het een paar seconden duurt

Een gsm die net zijn gps wakker maakt, antwoordt eerst vanuit wifi en gsm-masten, en die positie kan honderden meter afwijken. Daarom blijft Diana luisteren terwijl de nauwkeurigheid beter wordt, en toont ze wat ze al heeft: *"Scherpstellen… ±380 m"*. Ze antwoordt zodra de positie goed genoeg is, of na twaalf seconden met de beste die ze kreeg. Is die nog altijd ruw, dan zegt het antwoord dat.

## De nauwkeurigheid lezen

| Nauwkeurigheid | Wat het meestal betekent |
|---|---|
| ±10 m of beter | Satellieten. Betrouwbaar, ook dicht bij een grens. |
| ±20 tot 50 m | Redelijk. Opletten dicht bij een grens. |
| ±100 m of slechter | Wifi of gsm-masten, vaak binnenshuis. Niet goed genoeg om zeker te zijn. |

Is de marge groter dan ongeveer 10 m, dan tekent Diana een **stippelring** rond je markering, precies met die straal. Een kleine ring betekent satellieten; een ring over het hele huizenblok betekent dat het antwoord van wifi kwam.

:::tip[Een betere positie krijgen]
Ga naar buiten, met vrije hemel boven je, en wacht een paar seconden. Blijft het ruw, boven ongeveer 75 m? Dan mag de site waarschijnlijk alleen een benaderde locatie gebruiken. Een melding stelt dan voor om de locatie-instelling na te kijken: zie [Problemen met locatie](/nl/guide/help/location-problems/).
:::

## Twee valkuilen waar Diana op let

- **Binnenshuis** komt een wifi-positie vaak binnen één seconde binnen met ±20 m. Zo nauwkeurig denkt de wifi-databank zelf te zijn, niet de echte nauwkeurigheid. Diana antwoordt, maar blijft de rest van de twaalf seconden luisteren en past het antwoord aan als het moet.
- **Gsm’s die meer beloven dan ze kunnen.** Diana vergelijkt de metingen van de laatste 45 seconden. Eén wilde meting wordt genegeerd. Spreken de metingen elkaar tegen, dan zegt het antwoord *"metingen spreken elkaar tegen"*. Wandelen telt niet als spreiding.

:::caution
Diana kan dit alleen beantwoorden voor gebieden **met** een grens. Bij een stippelring of een blauw bolletje kan ze het niet zeggen. Zie [Punten en vlakken](/nl/guide/map/points-and-areas/).
:::
