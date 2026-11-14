---
title: "The start screen"
description: "What you see while Diana starts, and what to do if it stays on the start screen."
sidebar:
  order: 5
---

Every time Diana starts, you first see the start screen: a drawing of an activation, a radio signal running across it, a progress line and the version number. Meanwhile Diana reads the reference data and prepares the map.

The start screen disappears by itself as soon as the map is drawn, and after nine seconds at the latest.

## Diana needs scripts

Diana is a web app: everything it does runs as JavaScript in your browser. If your browser or an extension blocks scripts, nothing can start and you stay on the start screen.

After a while a box appears on the start screen saying exactly that. Then:

1. Allow scripts for **diana-onff.github.io** only. Not for `github.io` or `github.com`: Diana needs neither.
2. **Reload the page.** On a computer press **F5** or **Ctrl+R** (Mac: **Cmd+R**). On a phone, pull the page down or tap the reload button of the browser.
3. Still stuck? Another extension may be blocking too, such as an ad blocker. Switch them off one at a time for this site.

:::caution[Reloading is essential]
Most blockers only apply a new rule to a page that is loaded again. Without reloading, the old block stays in place, even after you clicked "Trust".
:::

All scripts come from Diana’s own address. Nothing is loaded from other sites, except the statistics script, and only if you say yes to it. Details in [Stuck on the start screen](/guide/help/scripts-blocked/).

## The very first time

On a device that has never opened Diana, two short things follow the start screen: the [Welcome screen](/guide/start/welcome-screen/) and [The setup wizard](/guide/start/setup-wizard/).
