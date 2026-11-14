---
title: "Privacy"
description: "Cosa sa Diana, cosa non sa, e perché."
sidebar:
  order: 9
---

Diana è costruita in modo che i tuoi dati restino con te. Questa pagina riassume la pagina privacy dell’app (**Impostazioni** › **Privacy** › **Apri la pagina privacy**).

## In breve

- Il tuo nominativo, il locator e le impostazioni restano nel browser di questo dispositivo. Non viene inviato nulla da nessuna parte.
- La tua posizione GPS è usata solo sullo schermo davanti a te. Non viene mai inviata da nessuna parte.
- Spottarti invia il tuo nominativo, la frequenza, il modo e la referenza a WWFF Spotline, mai la tua posizione.
- Con il tuo permesso separato, Diana può contare una visita anonima. Senza il tuo sì non si conta nulla, e puoi cambiare idea in qualsiasi momento nelle Impostazioni.
- Diana non usa cookie pubblicitari e non crea un tuo profilo.

## Cosa resta su questo dispositivo

Il tuo nominativo, il nominativo portatile, il locator, e impostazioni come bande, distanza di Info campo, parole rapide e lingua, insieme alla tua scelta sulle statistiche e al fatto di aver visto la schermata di benvenuto. Diana conserva anche una copia offline delle tessere della mappa e dell’app stessa, per continuare a funzionare senza rete. È normale cache del browser, non dati personali.

## I servizi con cui Diana comunica

| Servizio | Perché |
|---|---|
| WWFF Spotline (`spots.wwff.co`) | Spot in diretta e agenda. Riceve nominativo, frequenza, modo, referenza e nota quando ti spotti. Mai la tua posizione. |
| OpenFreeMap (`tiles.openfreemap.org`) | Le tessere della mappa, costruite con i dati OpenStreetMap. Nessun cookie. |
| Il relè di Diana (un Cloudflare Worker) | Passa il tuo spot o annuncio a Spotline. Conta le richieste per indirizzo IP con hash contro gli abusi, non registra mai nominativo, posizione o nota. |
| Umami (`cloud.umami.is`) | Conta una visita anonima, solo con il tuo permesso. Nessun cookie, nessun dato personale. |

## Cosa invia uno spot di te stesso

Esattamente questo, e nient’altro: il nominativo dell’attivatore, il nominativo dello spotter, la frequenza, il modo, la referenza e una nota facoltativa scritta da te. Mai la tua posizione.

## Cancellare tutto

**Impostazioni** › **Privacy** › **Cancella tutto su questo dispositivo** rimuove tutto ciò che Diana ha salvato su questo dispositivo: nominativo, impostazioni, tessere offline e la tua scelta sulle statistiche. Diana riparte allora dalla schermata di benvenuto.

## I tuoi diritti e contatti

Poiché Diana conserva le tue impostazioni personali solo sul tuo dispositivo, consultarle, correggerle o cancellarle è semplice come aprire le Impostazioni. Per qualsiasi domanda sulle statistiche anonime, o per un reclamo, la pagina privacy dell’app indica l’indirizzo di contatto.
