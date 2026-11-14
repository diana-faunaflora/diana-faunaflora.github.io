---
title: "Startskærmen"
description: "Hvad du ser, mens Diana starter, og hvad du gør, hvis den bliver hængende på startskærmen."
sidebar:
  order: 5
---

Hver gang Diana starter, ser du først startskærmen: en tegning af en aktivering, et radiosignal der løber hen over den, en fremskridtslinje og versionsnummeret. I mellemtiden læser Diana referencedataene og gør kortet klar.

Startskærmen forsvinder af sig selv, så snart kortet er tegnet, og senest efter ni sekunder.

## Diana har brug for scripts

Diana er en web-app: alt, hvad den gør, kører som JavaScript i din browser. Blokerer browseren eller en udvidelse scripts, kan intet starte, og du bliver på startskærmen.

Efter et stykke tid dukker der en boks op på startskærmen, som siger netop det. Så:

1. Tillad kun scripts for **diana-onff.github.io**. Ikke for `github.io` eller `github.com`: Diana har ikke brug for nogen af dem.
2. **Genindlæs siden.** På en computer trykker du **F5** eller **Ctrl+R** (Mac: **Cmd+R**). På en telefon trækker du siden ned eller trykker på browserens genindlæs-knap.
3. Stadig fast? Måske blokerer en anden udvidelse også, fx en annonceblokering. Slå dem fra én ad gangen for dette websted.

:::caution[Det er vigtigt at genindlæse]
De fleste blokeringer anvender først en ny regel på en side, der indlæses igen. Uden at genindlæse bliver den gamle blokering stående, også efter du har klikket på "Stol på".
:::

Alle scripts kommer fra Dianas egen adresse. Intet hentes fra andre websteder, undtagen statistik-scriptet, og kun hvis du siger ja til det. Detaljer i [Fast på startskærmen](/da/guide/help/scripts-blocked/).

## Allerførste gang

På en enhed, der aldrig har åbnet Diana, følger to korte ting efter startskærmen: [Velkomstskærmen](/da/guide/start/welcome-screen/) og [Opstartsguiden](/da/guide/start/setup-wizard/).
