---
title: "Forhold: rumvejr"
description: "Kp-viseren, SFI, A-indeks og solpletter, og hvad de betyder."
sidebar:
  order: 4
  label: "Rumvejr"
---

Fanen **Forhold** starter med dagens rumvejr: en viser med **Kp-indekset** og tre tal under den.

![Feltinfo, fanen Forhold, med Kp-viseren på 2, roligt, og båndbjælkerne](../../../../../assets/screens/phone-field-conditions.webp)

## Kp-viseren

Kp måler, hvor uroligt Jordens magnetfelt er, på en skala fra 0 til 9. Jo lavere, jo bedre for de højere bånd. Diana viser den officielle tre-timers værdi fra NOAA, og ved siden af et skøn over de seneste minutter.

| Kp | Ord i Diana | Hvad det betyder |
|---|---|---|
| 0 til 2 | roligt | Ingen effekt. Normale forhold. |
| 3 | uroligt | Lidt uroligt. Som regel endnu ingen mærkbar effekt. |
| 4 | aktivt | 20, 15 og 10 m falder et trin. |
| 5 og 6 | storm G1, G2 | Mindre storm: 20, 15 og 10 m dårligere. 80 og 40 m mærker det næsten ikke. |
| 7 til 9 | storm G3 til G5 | Kraftig storm: alle bånd dårligere, de høje mest. |

:::note
Kp er en global værdi, ikke en måling på din position.
:::

## De tre tal

| Tal | Hvad det fortæller dig |
|---|---|
| **SFI** | Solflux. Jo højere, jo bedre åbner de høje bånd. Omkring 70 er lavt, over 150 er højt. |
| **A** | Hvor uroligt magnetfeltet har været hele dagen. Lavt er godt. |
| **Solpletter** | Følger SFI: flere solpletter, større chance for DX på de høje bånd. |

SFI, A og solpletter er dagsværdier; Diana siger, hvilken dag de er fra.

## Hvor gamle er tallene?

Under viseren står der, hvornår tallene blev opdateret, fx *"Opdateret kl. 14:37 (for 12 min siden)"*. Diana prøver at hente dem to gange i timen, men i praksis kan der gå et par timer mellem to opdateringer.

- Ældre end **otte timer**: beskeden bliver orange.
- Kp-værdi ældre end **tolv timer**: Diana siger det særskilt.

Kilden er NOAA SWPC. Hvad det betyder pr. bånd: [Båndbjælkerne](/da/guide/field-info/conditions-bands/).
