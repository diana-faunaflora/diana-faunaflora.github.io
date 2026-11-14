---
title: "Am I inside the area?"
description: "How Diana tells you whether you are inside, and how to read the accuracy."
sidebar:
  order: 6
---

A card at the bottom of the map answers the question every activator has: **am I inside the reserve?**

## What the card says

- **Inside one area**: which one, and the distance to the nearest boundary.
- **Inside several at once** (when areas overlap): how many, and the panel of the smallest one opens. See [Overlapping areas](/guide/map/overlapping-areas/).
- **Outside**: the nearest area and how far it is.

Every answer ends with how good your position was, for example *"position ±6 m"*.

:::note[Areas made of several parcels]
Some references consist of separate parcels. The panel then says how many. Your whole station must stand inside one of them.
:::

## Why it takes a few seconds

A phone that has just woken its GPS first answers from wifi and cell masts, and that position can be hundreds of metres out. So Diana keeps listening while the accuracy improves, and shows what it has so far: *"Sharpening the fix… ±380 m"*. It answers once the position is good enough, or after twelve seconds with the best one it got. If that one is still rough, the answer says so.

## Reading the accuracy

| Accuracy | What it usually means |
|---|---|
| ±10 m or better | Satellites. Reliable, also close to a boundary. |
| ±20 to 50 m | Reasonable. Careful close to a boundary. |
| ±100 m or worse | Wifi or cell masts, often indoors. Not good enough to be sure. |

When the margin is larger than about 10 m, a **dashed ring** is drawn around your marker at exactly that radius. A tight ring means satellites; a ring covering the whole block means the answer came from wifi.

:::tip[Getting a better position]
Go outside, with open sky above you, and wait a few seconds. Stays it rough at more than about 75 m? Then the site may only use an approximate location. A banner then suggests checking the location setting: see [Location problems](/guide/help/location-problems/).
:::

## Two traps Diana watches for

- **Indoors**, a wifi position often arrives within a second claiming ±20 m. That is how accurate the wifi database believes itself to be, not the real accuracy. Diana answers, but keeps listening for the rest of the twelve seconds and corrects the answer if needed.
- **Phones that claim more than they can do.** Diana compares the readings of the last 45 seconds. A single wild reading is ignored. If the readings contradict each other, the answer says *"readings contradict each other"*. Walking is not counted as scatter.

:::caution
Diana can only answer this for areas **with** a boundary. For a dashed ring or a blue dot it cannot tell. See [Points and areas](/guide/map/points-and-areas/).
:::
