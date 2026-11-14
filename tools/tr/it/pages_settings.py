T = {
'settings/overview': {'title': 'Impostazioni', 'desc': 'Come aprire le Impostazioni, e a cosa serve ogni parte.', 'body': '''
Tutto ciò che hai impostato nella procedura guidata, e qualcosa in più, si trova in **Impostazioni**.

{{img:phone-settings|La schermata Impostazioni con La tua stazione e Il tuo paese}}

## Aprire le Impostazioni

1. Tocca **Impostazioni** nella barra in basso (l’ingranaggio, tutto a destra).
2. Scorri fino alla parte che vuoi cambiare.
3. Cambiala. Tutto viene salvato subito: non c’è un pulsante Salva. Vedi per un attimo *"Salvato su questo dispositivo"*.

## Cosa contengono

| Parte | Cosa imposti | Pagina |
|---|---|---|
| **La tua stazione** | Nominativo, nominativo portatile, locator | {{link:settings/your-station}} |
| **Il tuo paese** | Quale paese viene caricato in dettaglio, e il filtro degli spot | {{link:settings/your-country}} |
| **Parole rapide per uno spot** | Cinque parole da aggiungere con un tocco | {{link:settings/quick-words}} |
| **Info campo** | Fin dove guarda la scheda Aree intorno a te | {{link:settings/field-info-distance}} |
| **Elenco bande all’annuncio** | Tutte le bande o solo HF | {{link:settings/band-list}} |
| **Lingua** | Una delle otto, o seguire il browser | {{link:settings/language}} |
| **Privacy** | Pagina privacy, statistiche, cancella tutto | {{link:settings/privacy-settings}} |
| **Installa come app** | Installa su questo dispositivo | {{link:start/install-android}} |
| In fondo | Versione, aggiornamenti, novità, ripeti la procedura | {{link:settings/version-and-updates}} |

:::caution[Solo su questo dispositivo]
Tutto ciò che inserisci qui resta nel browser di questo dispositivo. Usi Diana anche su un altro dispositivo? Inseriscilo anche lì. Diana non ha un account per collegarli. Vedi {{link:help/data-and-limits}}.
:::
'''},
'settings/your-station': {'title': 'La tua stazione', 'desc': 'Nominativo, nominativo portatile e locator, e come leggere la riga della posizione.', 'body': '''
**Impostazioni** › **La tua stazione**. Chi sei e, più o meno, dove sei.

| Campo | Cosa inserire | Cosa ne fa Diana |
|---|---|---|
| **Nominativo** | Il tuo nominativo abituale, per esempio `IU2ABC`. | Usato come spotter, e decide il paese che Diana propone. |
| **Nominativo portatile** | Quello che usi sul campo, per esempio `IU2ABC/P`. | Inserito come attivatore quando ti spotti o annunci. |
| **Locator Maidenhead** | Sei caratteri, per esempio `JN45LM`. | Il tuo punto di partenza finché non c’è GPS: per la mappa, le distanze e le linee verso gli spot. |

*"Locator non valido (es. JO21EE)"* significa un errore di battitura: due lettere, due cifre, due lettere.

## Prendere il locator dal GPS

1. Mettiti dove vuoi il locator, possibilmente all’aperto.
2. Tocca **Prendi dal GPS**.
3. Diana inserisce il locator dalla tua posizione attuale.

## La riga della posizione

Sotto il locator una riga dice quanto era buona la tua ultima posizione, per esempio *"Ultima posizione: ±8 m · 2 min fa"*.

| Leggi | Cosa significa | Cosa fare |
|---|---|---|
| ±10 m o meglio | Satelliti. Va bene. | Niente. |
| circa da ±50 a 100 m | Di solito wifi, al chiuso. | Prova all’aperto. |
| Troppo grossolana per dire se sei in un’area | Non basta per dentro o fuori. | Esci all’aperto, con cielo libero. |
| Resta grossolana anche fuori | Forse il sito può usare solo una posizione approssimativa. | Controlla l’impostazione di localizzazione del telefono: {{link:help/location-problems}}. |
| *"Nessuna posizione GPS su questo dispositivo finora."* | Posizione non consentita, o non ancora chiesta. | Consenti la posizione, o affidati al tuo locator. |

:::note
Non esiste un’impostazione per dove si apre la mappa. Si apre sempre dove sei, altrimenti sul tuo locator, altrimenti nel paese del tuo nominativo.
:::
'''},
'settings/your-country': {'title': 'Il tuo paese', 'desc': 'Quale paese Diana carica in dettaglio, e in cosa differisce dal filtro degli spot.', 'body': '''
**Impostazioni** › **Il tuo paese**. Una scelta per tutto: quale paese Diana carica con i suoi confini reali, e quali spot e voci d’agenda mostra il pulsante del tuo paese. Degli altri paesi Diana mostra sempre solo punti.

## Le due parti

| Parte | Cosa fa |
|---|---|
| **Paese** | Il paese caricato in dettaglio. Nell’elenco c’è scritto **Con confini** o **Solo punti**. |
| **Mostra** | Il tuo paese o **Mondiale**. Il filtro della schermata Spots, lo stesso interruttore di quella schermata. |

Sotto l’elenco Diana dice cosa ha per quel paese, per esempio *"ONFF, 947 aree con confini caricate"*, oppure che per l’OKFF non ci sono confini, solo punti sulla mappa.

## Quando cambiarlo

- **Vai all’estero**: scegli il paese che visiti. Se Diana ha i suoi confini, lì le aree compaiono per intero. Vedi {{link:travel/abroad}}.
- **Ti interessa una referenza oltre il confine**: tocca il suo punto blu e usa **Mostra [paese] in dettaglio**; fa la stessa cosa che cambiarlo qui.

## Passo dopo passo

1. Tocca **Impostazioni** in basso a destra.
2. Apri l’elenco in **Il tuo paese** e scegli il paese.
3. Il cambiamento è immediato. Leggi la riga sotto l’elenco per vedere cosa è stato caricato.
4. Vuoi gli spot di tutto il mondo o solo di quel paese? Sceglilo in **Mostra**.

:::note
Scegliere un altro paese non cambia mai **Mostra**. E viceversa: cambiare il filtro degli spot non carica un altro paese.
:::

Perché una referenza è un’area o un punto: {{link:map/points-and-areas}}.
'''},
'settings/quick-words': {'title': 'Parole rapide per uno spot', 'desc': 'Cinque parole da aggiungere alla nota di uno spot con un tocco.', 'body': '''
**Impostazioni** › **Parole rapide per uno spot**. Cinque parole che puoi aggiungere alla nota di uno spot con un tocco, per non dover scrivere sul campo.

## Impostarle

1. Compila fino a cinque caselle, ognuna con una parola o una breve frase.
2. Una casella vuota semplicemente non crea un pulsante.
3. Quando ti spotti, compaiono come pulsanti sotto la nota. Vedi {{link:spots/spot-yourself}}.

## Idee

Inserisci ciò che si adatta alla tua stazione: un modo, la tua potenza, l’antenna, un breve stato. Tienile brevi: una nota ha al massimo 100 caratteri.

:::caution
Niente ringraziamenti né richieste di banda: uno spot va al DX cluster, dove è solo rumore.
:::
'''},
'settings/field-info-distance': {'title': 'Distanza di Info campo', 'desc': 'Fin dove guarda la scheda Aree intorno a te.', 'body': '''
**Impostazioni** › **Info campo**. Fin dove la scheda **Aree** di Info campo guarda intorno alla tua posizione: **10, 25, 50 o 100 km**.

| Scegli | Quando |
|---|---|
| **10 km** | Molte aree vicine tra loro, come nelle Fiandre. Un elenco corto e chiaro. |
| **25 km** | Una buona via di mezzo per la maggior parte dei luoghi. |
| **50 km** | Meno aree intorno, o sei disposto a guidare. |
| **100 km** | In campagna, o all’estero con poche referenze. |

L’elenco mostra al massimo cento righe alla volta; **Mostra altri** dà il resto. Vedi {{link:field-info/areas-nearby}}.
'''},
'settings/band-list': {'title': 'Elenco bande all’annuncio', 'desc': 'Tutte le bande o solo HF nell’elenco del modulo di annuncio.', 'body': '''
**Impostazioni** › **Elenco bande all’annuncio**. Quali bande offre l’elenco della schermata di annuncio.

| Scelta | Bande |
|---|---|
| **Tutte le bande** | Da 160 m a 23 cm. |
| **Solo HF** | 80, 40, 30, 20, 15 e 10 m. |

Quasi tutte le attivazioni avvengono sulle bande HF. Con **Solo HF** l’elenco resta corto e scorri meno sul telefono. Lavori anche in VHF o UHF? Scegli **Tutte le bande**.

Vedi {{link:spots/announce}}.
'''},
'settings/language': {'title': 'Lingua', 'desc': 'Scegliere la lingua dell’app.', 'body': '''
**Impostazioni** › **Lingua**. Diana parla inglese, olandese, francese, tedesco, danese, italiano, spagnolo e portoghese.

- Scegline una delle otto, o **Segui il browser** per usare la lingua del tuo browser.
- Senza scelta, Diana parte in inglese.
- Puoi cambiare lingua anche da **≡** sulla mappa, o al primo passo della procedura guidata.

Tutto cambia subito. I nomi delle aree non vengono mai tradotti: sono nomi ufficiali e vanno nel tuo log esattamente come sono pubblicati.

:::note
Le "Novità" (le note di rilascio) esistono solo in olandese e inglese.
:::
'''},
'settings/privacy-settings': {'title': 'Privacy e statistiche', 'desc': 'La pagina privacy, la tua scelta sulle statistiche e cancellare tutto.', 'body': '''
**Impostazioni** › **Privacy**. Cosa conserva Diana, cosa invia, e la tua scelta sulle statistiche anonime.

## Cosa trovi qui

- **Apri la pagina privacy**: con quali servizi comunica Diana e perché. Riassunto in {{link:start/privacy}}.
- **Statistiche anonime**: **Sì, aiuto volentieri** o **No, preferisco di no**. Cambiala quando vuoi.
- **Cancella tutto su questo dispositivo**: rimuove tutto ciò che Diana ha salvato qui.

## Cambiare la scelta sulle statistiche

1. Tocca **Impostazioni** › **Privacy**.
2. Tocca **Sì, aiuto volentieri** o **No, preferisco di no**.
3. Vedi *"Salvato."*. È tutto.

:::tip[Perché un sì aiuta]
Le statistiche vengono contate con Umami: nessun cookie, nessun profilo, niente che ti identifichi. Per i volontari dietro Diana è l’unico modo per sapere che l’app viene usata e quali schermate contano. Diana funziona esattamente allo stesso modo in entrambi i casi.
:::

## Cancellare tutto

1. Tocca **Cancella tutto su questo dispositivo**.
2. Diana chiede conferma: questo rimuove nominativo, impostazioni, tessere offline e la tua scelta sulle statistiche.
3. Conferma. Diana riparte dalla schermata di benvenuto.

Usalo quando cedi il dispositivo, o vuoi ricominciare da capo.
'''},
'settings/version-and-updates': {'title': 'Versione e aggiornamenti', 'desc': 'Leggere la riga della versione, cercare aggiornamenti e ripetere la procedura guidata.', 'body': '''
In fondo alle **Impostazioni**: quale versione hai, quanto sono freschi i dati, e se c’è qualcosa di nuovo.

## Leggere la riga della versione

`v2.2.12 · 6757ec3 · 14/11/2026`

| Parte | Significato |
|---|---|
| `v2.2.12` | La versione dell’app. |
| `6757ec3` | Un codice per questa precisa build dell’app. |
| `14/11/2026` | La data di quella versione. |

Il codice cambia solo quando cambia l’app stessa, non quando l’aggiornamento notturno porta nuovi dati. La **riga dei dati** sotto dice quanto sono freschi i dati della mappa.

## I pulsanti

- **Cerca aggiornamenti**: Diana controlla se è pronta una nuova versione e la carica.
- **Novità**: cosa ha portato ogni versione, la più recente in alto.
- **Ripeti la procedura guidata iniziale**: la procedura parte dalle tue impostazioni attuali. Alla fine ripropone il giro.

:::tip[Qualcuno ti chiede che versione hai?]
Leggi ad alta voce la riga della versione. È esattamente ciò che serve per aiutarti.
:::

Di più sugli aggiornamenti che sembrano non arrivare: {{link:help/updates}}.
'''},
}
