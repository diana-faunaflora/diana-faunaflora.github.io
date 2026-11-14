---
title: "La schermata di avvio"
description: "Cosa vedi mentre Diana si avvia, e cosa fare se resta bloccata sulla schermata di avvio."
sidebar:
  order: 5
---

A ogni avvio vedi prima la schermata di avvio: il disegno di un’attivazione, un segnale radio che la attraversa, una barra di avanzamento e il numero di versione. Nel frattempo Diana legge i dati delle referenze e prepara la mappa.

La schermata di avvio scompare da sola appena la mappa è disegnata, e al massimo dopo nove secondi.

## Diana ha bisogno degli script

Diana è un’app web: tutto ciò che fa gira come JavaScript nel tuo browser. Se il browser o un’estensione blocca gli script, nulla può partire e resti sulla schermata di avvio.

Dopo un po’ compare sulla schermata di avvio un riquadro che lo spiega. Allora:

1. Consenti gli script solo per **diana-onff.github.io**. Non per `github.io` né per `github.com`: a Diana non servono.
2. **Ricarica la pagina.** Su computer premi **F5** o **Ctrl+R** (Mac: **Cmd+R**). Su telefono trascina la pagina verso il basso o tocca il pulsante di ricarica del browser.
3. Ancora bloccato? Forse un’altra estensione blocca a sua volta, per esempio un blocco pubblicità. Disattivale una alla volta per questo sito.

:::caution[Ricaricare è indispensabile]
La maggior parte dei bloccatori applica una nuova regola solo a una pagina ricaricata. Senza ricaricare, il vecchio blocco resta, anche dopo aver fatto clic su "Considera attendibile".
:::

Tutti gli script arrivano dall’indirizzo di Diana. Non viene caricato nulla da altri siti, tranne lo script delle statistiche, e solo se dici di sì. Dettagli in [Bloccato sulla schermata di avvio](/it/guide/help/scripts-blocked/).

## La primissima volta

Su un dispositivo che non ha mai aperto Diana, dopo la schermata di avvio seguono due brevi passaggi: la [Schermata di benvenuto](/it/guide/start/welcome-screen/) e [La procedura guidata iniziale](/it/guide/start/setup-wizard/).
