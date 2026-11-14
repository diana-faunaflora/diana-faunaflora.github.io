---
title: "Points and areas"
description: "Why one reference is a green area and another a blue dot, and how to change that."
sidebar:
  order: 2
---

On the map a WWFF reference appears in one of three ways. Which one depends on what Diana knows about it, and on the country you chose.

| What you see | What it means | Can Diana tell whether you are inside? |
|---|---|---|
| **Green area** | A reference with its real boundary, in the country you chose. | Yes |
| **Dashed ring with an orange dot** | A reference of your country without a boundary. Only an approximate spot. | No |
| **Blue dot** | A reference in another country. Close together they form a numbered circle. | No |

## Why an area?

An area needs a boundary file. Diana has those files for **five countries** today: Belgium (ONFF), the Netherlands (PAFF), Germany (DLFF), Denmark (OZFF) and Portugal (CTFF), and more are added all the time. The national WWFF coordinators supply them.

Diana loads the boundaries of **one country at a time**: the one you chose under Settings. That keeps the map fast on a phone.

## Why a dot?

- The reference lies in a country for which Diana has **no boundary file**. Then Diana only knows the position from the WWFF directory.
- Or the country **does** have boundaries in Diana, but it is **not the country you chose**. Then it is shown as a dot too, until you load that country.

## Why a dashed ring?

Within a country with boundaries, a few references have no boundary in the file, for example overseas areas of the Netherlands. They are shown as a dashed ring at the approximate spot.

## You always get the details

Whatever you see, **tap it**: a panel opens with everything Diana knows. For a blue dot that is the reference, country and name, the locator and zones, the bearing and distance from you, the QSO count or **ATNO** when it was never activated, and a link to more information. See [Area details](/guide/map/area-panel/).

## When and how to change it

When you go to another country, or want to see the real boundary of a reference that is now a dot:

**From the panel (quickest)**

1. Tap the blue dot.
2. If Diana has the boundaries of that country, the panel says so and shows a button **Show [country] in detail**.
3. Tap it. Diana loads that country and opens the same reference again, now with its boundary.

**From Settings**

1. Tap **Settings** at the bottom right.
2. Under **Your country**, choose the country. Countries marked **With boundaries** get their areas; **Points only** stays dots.
3. The change is immediate. Under the menu Diana says what it loaded, for example *"PAFF, 281 areas with boundaries loaded"*.

Your spots filter (your country or Worldwide) does not change when you pick another country. More in [Your country](/guide/settings/your-country/).

:::note[A new reserve as a dot first]
Which references exist comes from the WWFF directory, every night. The boundaries come from a file the Diana team publishes. So a brand-new reserve can appear as a point first and get its outline later.
:::
