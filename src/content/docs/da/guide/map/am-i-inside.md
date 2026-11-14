---
title: "Står jeg i området?"
description: "Hvordan Diana fortæller dig, om du er inde, og hvordan du læser nøjagtigheden."
sidebar:
  order: 6
---

Et infokort nederst på kortet svarer på det spørgsmål, enhver aktivator har: **står jeg i reservatet?**

## Hvad infokortet siger

- **I ét område**: hvilket, og afstanden til den nærmeste grænse.
- **I flere på én gang** (når områder overlapper): hvor mange, og panelet for det mindste åbner. Se [Overlappende områder](/da/guide/map/overlapping-areas/).
- **Udenfor**: det nærmeste område og hvor langt væk det er.

Hvert svar slutter med, hvor god din position var, fx *"position ±6 m"*.

:::note[Områder i flere dele]
Nogle referencer består af adskilte delområder. Panelet siger så, hvor mange. Hele din station skal stå inde i ét af dem.
:::

## Hvorfor det tager et par sekunder

En telefon, der lige har vækket sin GPS, svarer først ud fra wifi og mobilmaster, og den position kan være flere hundrede meter forkert. Derfor bliver Diana ved med at lytte, mens nøjagtigheden bliver bedre, og viser hvad den har indtil videre: *"Skærper positionen… ±380 m"*. Den svarer, så snart positionen er god nok, eller efter tolv sekunder med den bedste, den har fået. Er den stadig grov, siger svaret det.

## Sådan læser du nøjagtigheden

| Nøjagtighed | Hvad det typisk betyder |
|---|---|
| ±10 m eller bedre | Satellitter. Pålidelig, også tæt på en grænse. |
| ±20 til 50 m | Rimelig. Pas på tæt på en grænse. |
| ±100 m eller værre | Wifi eller mobilmaster, ofte indendørs. Ikke godt nok til at være sikker. |

Når usikkerheden er større end omkring 10 m, tegnes en **stiplet ring** om din markør med præcis den radius. En stram ring betyder satellitter; en ring, der dækker hele karreen, betyder at svaret kom fra wifi.

:::tip[Få en bedre position]
Gå udenfor, med åben himmel over dig, og vent et par sekunder. Forbliver den grov på mere end omkring 75 m? Så må webstedet måske kun bruge en omtrentlig placering. En besked foreslår så, at du tjekker placeringsindstillingen: se [Problemer med placering](/da/guide/help/location-problems/).
:::

## To fælder Diana holder øje med

- **Indendørs** kommer en wifi-position ofte inden for et sekund og påstår ±20 m. Så præcis tror wifi-databasen selv, den er, ikke den reelle nøjagtighed. Diana svarer, men lytter videre resten af de tolv sekunder og retter svaret om nødvendigt.
- **Telefoner, der lover mere, end de kan.** Diana sammenligner målingerne fra de seneste 45 sekunder. En enkelt vild måling ignoreres. Modsiger målingerne hinanden, siger svaret *"målinger modsiger hinanden"*. At gå tæller ikke som spredning.

:::caution
Diana kan kun svare på dette for områder **med** grænse. For en stiplet ring eller en blå prik kan den ikke. Se [Punkter og områder](/da/guide/map/points-and-areas/).
:::
