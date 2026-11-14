---
title: "Privacy"
description: "Wat Diana weet, wat niet, en waarom."
sidebar:
  order: 9
---

Diana is zo gebouwd dat je gegevens bij jou blijven. Deze pagina vat de privacypagina in de app samen (**Instellingen** › **Privacy** › **Open de privacypagina**).

## In het kort

- Je roepnaam, locator en instellingen blijven in de browser van dit toestel. Er wordt niets opgestuurd.
- Je gps-positie wordt alleen gebruikt op het scherm voor je. Ze wordt nooit ergens naartoe gestuurd.
- Jezelf spotten stuurt je roepnaam, frequentie, mode en referentie naar WWFF Spotline, nooit je positie.
- Met je aparte toestemming kan Diana een anoniem bezoek meetellen. Er wordt niets geteld tenzij je ja zegt, en je kan op elk moment van gedacht veranderen onder Instellingen.
- Diana plaatst geen reclamecookies en bouwt geen profiel van je op.

## Wat op dit toestel blijft

Je roepnaam, portable roepnaam, locator, en instellingen zoals banden, de afstand voor Veldinfo, snelknoppen en taal, samen met je keuze over statistieken en of je het welkomstscherm al zag. Diana houdt ook een offline kopie bij van de kaarttegels en van de app zelf, zodat ze blijft werken zonder bereik. Dat is gewone browsercache, geen persoonsgegevens.

## Diensten waarmee Diana praat

| Dienst | Waarom |
|---|---|
| WWFF Spotline (`spots.wwff.co`) | Live spots en de agenda. Ontvangt je roepnaam, frequentie, mode, referentie en opmerking wanneer je jezelf spot. Nooit je positie. |
| OpenFreeMap (`tiles.openfreemap.org`) | De kaarttegels, opgebouwd uit OpenStreetMap-gegevens. Geen cookies. |
| Het Diana-doorgeefluik (een Cloudflare Worker) | Stuurt je spot of aankondiging door naar Spotline. Telt aanvragen per gehasht IP-adres tegen misbruik, logt nooit je roepnaam, positie of opmerking. |
| Umami (`cloud.umami.is`) | Telt een anoniem bezoek, alleen met jouw toestemming. Geen cookies, geen persoonsgegevens. |

## Wat een zelf-spot verstuurt

Precies dit, en niets anders: de roepnaam van de activator, de roepnaam van de spotter, de frequentie, de mode, de referentie en een optionele opmerking die je zelf typte. Nooit je positie.

## Alles wissen

**Instellingen** › **Privacy** › **Wis alles op dit toestel** verwijdert alles wat Diana op dit toestel bewaarde: je roepnaam, instellingen, offline kaarttegels en je keuze over statistieken. Diana begint daarna opnieuw bij het welkomstscherm.

## Jouw rechten en contact

Omdat Diana je persoonlijke instellingen alleen op je eigen toestel bewaart, is inkijken, verbeteren of wissen zo eenvoudig als Instellingen openen. Voor alles over de anonieme statistieken, of een klacht, staat het contactadres op de privacypagina in de app.
