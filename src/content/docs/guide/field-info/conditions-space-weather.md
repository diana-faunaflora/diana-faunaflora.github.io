---
title: "Conditions: space weather"
description: "The Kp dial, SFI, A index and sunspots, and what they mean."
sidebar:
  order: 4
  label: "Space weather"
---

The **Conditions** tab starts with today’s space weather: a dial with the **Kp index** and three numbers under it.

![Field info, Conditions tab, with the Kp dial on 2, quiet, and the band bars](../../../../assets/screens/phone-field-conditions.webp)

## The Kp dial

Kp measures how restless the Earth’s magnetic field is, on a scale from 0 to 9. The lower, the better for the higher bands. Diana shows the official three-hourly value from NOAA, and next to it an estimate of the last minutes.

| Kp | Word in Diana | What it means |
|---|---|---|
| 0 to 2 | quiet | No effect. Normal conditions. |
| 3 | unsettled | Slightly restless. Usually no noticeable effect yet. |
| 4 | active | 20, 15 and 10 m drop one step. |
| 5 and 6 | storm G1, G2 | Minor storm: 20, 15 and 10 m worse. 80 and 40 m hardly notice it. |
| 7 to 9 | storm G3 to G5 | Strong storm: all bands worse, the high ones most. |

:::note
Kp is a worldwide value, not a measurement at your position.
:::

## The three numbers

| Number | What it tells you |
|---|---|
| **SFI** | Solar flux. The higher, the better the high bands open. Around 70 is low, above 150 is high. |
| **A** | How restless the magnetic field was over the whole day. Low is good. |
| **Sunspots** | Goes with the SFI: more sunspots, more chance of DX on the high bands. |

SFI, A and sunspots are daily figures; Diana says which day they are from.

## How old are the figures?

Under the dial it says when the figures were updated, for example *"Updated at 14:37 (12 min ago)"*. Diana tries to fetch them twice an hour, but in practice there can be a few hours between two updates.

- Older than **eight hours**: the message turns orange.
- Kp value older than **twelve hours**: Diana says so separately.

The source is NOAA SWPC. What it means per band: [The band bars](/guide/field-info/conditions-bands/).
