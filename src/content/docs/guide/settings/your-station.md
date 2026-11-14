---
title: "Your station"
description: "Callsign, portable callsign and locator, and how to read the position line."
sidebar:
  order: 2
---

**Settings** › **Your station**. Who you are and roughly where you are.

| Field | What to fill in | What Diana does with it |
|---|---|---|
| **Callsign** | Your normal callsign, for example `ON3VZ`. | Used as the spotter, and decides which country Diana proposes. |
| **Portable callsign** | What you use in the field, for example `ON3VZ/P`. | Filled in as the activator when you spot yourself or announce. |
| **Maidenhead locator** | Six characters, for example `JO21EE`. | Your starting point while there is no GPS: for the map, the distances and the lines to spots. |

*"No valid locator (e.g. JO21EE)"* means a typing error: two letters, two digits, two letters.

## Taking the locator from GPS

1. Stand where you want the locator for, outside if possible.
2. Tap **Take from GPS**.
3. Diana fills in the locator from your current position.

## The position line

Under the locator a line says how good your last position was, for example *"Last position: ±8 m · 2 min ago"*.

| You read | What it means | What to do |
|---|---|---|
| ±10 m or better | Satellites. Fine. | Nothing. |
| about ±50 to 100 m | Usually wifi, indoors. | Try outside. |
| *"Too coarse to say whether you are inside an area"* | Not good enough for inside-or-outside. | Go outside with open sky. |
| Stays coarse outside too | The site may only use an approximate location. | Check the location setting of your phone: [Location problems](/guide/help/location-problems/). |
| *"No GPS position on this device yet"* | Location not allowed, or not asked yet. | Allow location, or rely on your locator. |

:::note
There is no setting for where the map opens. It always opens where you are, otherwise at your locator, otherwise in your callsign’s country.
:::
