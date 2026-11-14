---
title: "Het startscherm"
description: "Wat je ziet terwijl Diana opstart, en wat je doet als ze op het startscherm blijft hangen."
sidebar:
  order: 5
---

Telkens Diana opstart, zie je eerst het startscherm: een tekening van een activatie, een radiosignaal dat erover loopt, een voortgangslijn en het versienummer. Ondertussen leest Diana de referentiegegevens in en bouwt ze de kaart op.

Het startscherm verdwijnt vanzelf zodra de kaart getekend is, en uiterlijk na negen seconden.

## Diana heeft scripts nodig

Diana is een web-app: alles wat ze doet, draait als JavaScript in je browser. Blokkeert je browser of een extensie scripts, dan kan niets starten en blijf je op het startscherm.

Na een tijdje verschijnt er op het startscherm een vak dat precies dat zegt. Doe dan dit:

1. Sta scripts toe voor **diana-onff.github.io**, en alleen daarvoor. Niet voor `github.io` of `github.com`: die heeft Diana niet nodig.
2. **Laad de pagina opnieuw.** Op een computer druk je op **F5** of **Ctrl+R** (Mac: **Cmd+R**). Op een gsm trek je de pagina naar beneden of tik je op de herlaadknop van de browser.
3. Nog altijd vast? Dan blokkeert misschien nog een andere extensie, zoals een advertentieblokker. Zet ze voor deze site een voor een uit.

:::caution[Herladen is nodig]
De meeste blokkers passen een nieuwe regel pas toe op een pagina die opnieuw geladen wordt. Zonder herladen blijft de oude blokkering staan, ook als je al op "Vertrouwen" klikte.
:::

Alle scripts komen van het eigen adres van Diana. Er wordt niets van andere sites geladen, behalve het statistiekscript, en dat alleen als je er ja op zegt. Details in [Vast op het startscherm](/nl/guide/help/scripts-blocked/).

## De allereerste keer

Op een toestel dat Diana nog nooit opende, volgen na het startscherm nog twee korte dingen: het [Welkomstscherm](/nl/guide/start/welcome-screen/) en [De opstartwizard](/nl/guide/start/setup-wizard/).
