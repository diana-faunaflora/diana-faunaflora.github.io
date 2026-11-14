---
title: "Privatliv"
description: "Hvad Diana ved, hvad den ikke ved, og hvorfor."
sidebar:
  order: 9
---

Diana er bygget, så dine data bliver hos dig. Denne side opsummerer privatlivssiden i appen (**Indstillinger** › **Privatliv** › **Åbn privatlivssiden**).

## Kort sagt

- Dit kaldesignal, din locator og dine indstillinger bliver i browseren på denne enhed. Intet sendes nogen steder hen.
- Din GPS-position bruges kun på skærmen foran dig. Den sendes aldrig nogen steder hen.
- Når du spotter dig selv, sendes dit kaldesignal, frekvens, mode og reference til WWFF Spotline, aldrig din position.
- Med din særskilte tilladelse kan Diana tælle et anonymt besøg. Intet tælles uden dit ja, og du kan ændre mening når som helst under Indstillinger.
- Diana sætter ingen reklamecookies og opbygger ingen profil af dig.

## Hvad der bliver på denne enhed

Dit kaldesignal, portable kaldesignal, locator og indstillinger som bånd, afstanden til Feltinfo, hurtige ord og sprog, sammen med dit valg om statistik og om du har set velkomstskærmen. Diana gemmer også en offline-kopi af kortfliserne og af selve appen, så den virker videre uden dækning. Det er almindelig browser-cache, ikke personoplysninger.

## Tjenester Diana taler med

| Tjeneste | Hvorfor |
|---|---|
| WWFF Spotline (`spots.wwff.co`) | Live-spots og agendaen. Modtager dit kaldesignal, frekvens, mode, reference og bemærkning, når du spotter dig selv. Aldrig din position. |
| OpenFreeMap (`tiles.openfreemap.org`) | Kortfliserne, lavet ud fra OpenStreetMap-data. Ingen cookies. |
| Dianas relæ (en Cloudflare Worker) | Sender dit spot eller din annoncering videre til Spotline. Tæller forespørgsler pr. hashet IP-adresse mod misbrug, logger aldrig dit kaldesignal, din position eller bemærkning. |
| Umami (`cloud.umami.is`) | Tæller et anonymt besøg, kun med din tilladelse. Ingen cookies, ingen personoplysninger. |

## Hvad et selv-spot sender

Præcis dette, og intet andet: aktivatorens kaldesignal, spotterens kaldesignal, frekvensen, mode, referencen og en valgfri bemærkning, du selv har skrevet. Aldrig din position.

## Ryd alt

**Indstillinger** › **Privatliv** › **Ryd alt på denne enhed** fjerner alt, hvad Diana har gemt på denne enhed: dit kaldesignal, indstillinger, offline-kortfliser og dit valg om statistik. Diana starter så forfra ved velkomstskærmen.

## Dine rettigheder og kontakt

Fordi Diana kun gemmer dine personlige indstillinger på din egen enhed, er det lige så nemt at se, rette eller slette dem som at åbne Indstillinger. For alt om den anonyme statistik, eller en klage, angiver privatlivssiden i appen kontaktadressen. I Danmark kan du også henvende dig til Datatilsynet (datatilsynet.dk).
