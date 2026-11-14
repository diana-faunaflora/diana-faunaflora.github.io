---
title: "Condities: ruimteweer"
description: "De Kp-meter, SFI, A-index en zonnevlekken, en wat ze betekenen."
sidebar:
  order: 4
  label: "Ruimteweer"
---

Het tabblad **Condities** begint met het ruimteweer van vandaag: een meter met de **Kp-index** en drie getallen eronder.

![Veldinfo, tabblad Condities, met de Kp-meter op 2, rustig, en de bandbalken](../../../../../assets/screens/phone-field-conditions.webp)

## De Kp-meter

Kp meet hoe onrustig het aardmagnetisch veld is, op een schaal van 0 tot 9. Hoe lager, hoe beter voor de hogere banden. Diana toont de officiële waarde per drie uur van NOAA, met daarnaast een schatting van de laatste minuten.

| Kp | Woord in Diana | Wat het betekent |
|---|---|---|
| 0 tot 2 | rustig | Geen invloed. Normale condities. |
| 3 | onrustig | Licht onrustig. Meestal nog geen merkbaar effect. |
| 4 | actief | 20, 15 en 10 m zakken een stap. |
| 5 en 6 | storm G1, G2 | Kleine storm: 20, 15 en 10 m slechter. 80 en 40 m merken er weinig van. |
| 7 tot 9 | storm G3 tot G5 | Zware storm: alle banden slechter, de hoge het meest. |

:::note
Kp is een wereldwijde waarde, geen meting op jouw positie.
:::

## De drie getallen

| Getal | Wat het zegt |
|---|---|
| **SFI** | Zonneflux. Hoe hoger, hoe beter de hoge banden openen. Rond 70 is laag, boven 150 is hoog. |
| **A** | Hoe onrustig het magneetveld de hele dag was. Laag is goed. |
| **Zonnevlekken** | Hangt samen met de SFI: meer vlekken, meer kans op DX op de hoge banden. |

SFI, A en zonnevlekken zijn daggegevens; Diana zegt van welke dag.

## Hoe oud zijn de gegevens?

Onder de meter staat wanneer de gegevens bijgewerkt werden, bijvoorbeeld *"Bijgewerkt om 14:37 (12 min geleden)"*. Diana probeert ze twee keer per uur op te halen, maar in de praktijk kunnen er een paar uur tussen twee updates zitten.

- Ouder dan **acht uur**: de melding wordt oranje.
- Kp-waarde ouder dan **twaalf uur**: Diana zegt dat apart.

De bron is NOAA SWPC. Wat het betekent per band: [De bandbalken](/nl/guide/field-info/conditions-bands/).
