T = {
'help/location-problems': {'title': 'Problemi di posizione', 'desc': 'Nessuna posizione, o una posizione che resta grossolana: cosa controllare, dispositivo per dispositivo.', 'body': '''
Diana chiede sempre la posizione più precisa che il tuo dispositivo può dare. Se un sito riceve la posizione esatta o una volutamente sfocata è un’impostazione del telefono o del browser, non di Diana.

## Prima di tutto: prova all’aperto

Al chiuso, il solo wifi dà spesso circa ±100 m. Esci, con il cielo libero sopra di te, aspetta dieci secondi e tocca **Mappa** nella barra in basso. Spesso basta.

## Ancora grossolana o nessuna posizione? Controlla l’impostazione

**Android con Chrome**

1. Apri l’app **Impostazioni** del telefono.
2. Vai su **App** › **Chrome** › **Autorizzazioni** › **Posizione**.
3. Scegli **Consenti solo mentre l’app è in uso** e attiva **Usa posizione esatta**.
4. Controlla anche il sito stesso: in Chrome tocca l’icona a sinistra della barra degli indirizzi › **Autorizzazioni** › **Posizione**: consentita.

**iPhone o iPad con Safari**

1. Apri l’app **Impostazioni**.
2. Vai su **Privacy e sicurezza** › **Localizzazione** › **Siti web di Safari**.
3. Scegli **Mentre usi l’app** e attiva **Posizione esatta**.

**iPhone o iPad con un altro browser** (per esempio Chrome)

1. Apri l’app **Impostazioni**.
2. Vai su **Privacy e sicurezza** › **Localizzazione** › il tuo browser.
3. Scegli **Mentre usi l’app** e attiva **Posizione esatta**.

**Computer**

Fai clic sull’icona del lucchetto accanto alla barra degli indirizzi e consenti la **Posizione** per questo sito. Un portatile ricava la posizione dal wifi ed è raramente migliore di circa ±50 m.

## "La posizione è bloccata per questo sito"

Tu (o qualcuno) hai detto no in passato. Diana non può chiedere di nuovo: solo tu puoi consentirla, nelle impostazioni del browser o del telefono qui sopra. Poi ricarica Diana.

## Senza posizione

Diana funziona anche senza posizione. Inserisci il tuo locator in **Impostazioni** › **La tua stazione**. Distanze e linee partono allora dal centro del quadrato del tuo locator. Solo *sono dentro l’area* ha davvero bisogno di una posizione precisa.

Vedi anche {{link:map/am-i-inside}}.
'''},
'help/scripts-blocked': {'title': 'Bloccato sulla schermata di avvio', 'desc': 'Blocca-script e browser restrittivi: di cosa ha bisogno Diana, e niente di più.', 'body': '''
Diana è un’app web: senza JavaScript non funziona nulla. Se un blocco ferma gli script, Diana resta sulla schermata di avvio. Dopo un po’ compare lì un riquadro che lo dice.

## Risolvere

1. Consenti gli script solo per **diana-onff.github.io**. Non `github.io` e non `github.com`: a Diana non servono.
2. **Ricarica la pagina**: **F5** o **Ctrl+R** (Mac: **Cmd+R**). Sul telefono trascina la pagina verso il basso o tocca ricarica. Senza ricaricare, il vecchio blocco resta, anche dopo aver fatto clic su "Considera attendibile".
3. Ancora bloccato? Una seconda estensione può bloccare a sua volta (un blocco pubblicità, un’estensione per la privacy). Disattivale una alla volta per questo sito.
4. Diana parte ma la mappa resta vuota? Consenti i worker `blob:` per diana-onff.github.io (vedi sotto).

## Cosa carica Diana

**Script**: tutti da diana-onff.github.io stesso.

| File | Cos’è |
|---|---|
| `vendor/maplibre-gl.js` | MapLibre, la libreria delle mappe. Una copia sul sito di Diana, non da una CDN. |
| `js/*.js` | Il codice di Diana. |
| `sw.js` | Il service worker che fa funzionare Diana offline. |

Nessuno script inline e nessun `eval`. Un’eccezione, solo con il tuo consenso: se hai detto sì alle statistiche, lo script Umami da `cloud.umami.is`.

**Worker della mappa**: MapLibre disegna la mappa in un worker in background avviato da un indirizzo `blob:`. Un blocco che rifiuta i worker `blob:` lascia partire Diana ma lascia la mappa vuota.

**Dati**:

| Host | Perché |
|---|---|
| `tiles.openfreemap.org` | Tessere della mappa e caratteri delle etichette |
| `spots.wwff.co` | Spot in diretta e agenda |
| `diana-spotline.diana-onff.workers.dev` | Solo quando invii uno spot o un annuncio |
| `raw.githubusercontent.com` | Meteo spaziale per Condizioni |
| `cloud.umami.is` | Solo se hai detto sì alle statistiche |

La tua posizione non viene mai inviata da nessuna parte.
'''},
'help/updates': {'title': 'Aggiornamenti', 'desc': 'Come Diana si aggiorna da sola, e cosa fare se una nuova versione non compare.', 'body': '''
Diana si aggiorna da sola. Non devi mai scaricare nulla.

## Come funziona

- **I dati** (referenze, numero di QSO, confini) vengono aggiornati ogni notte. Diana li prende freschi a ogni avvio, e usa la copia sul tuo telefono quando la rete è debole.
- **L’app stessa**: quando apri Diana con la rete, controlla se c’è una nuova versione. Una nuova versione viene annunciata solo quando c’è davvero.

## Una nuova versione non compare?

1. Assicurati di avere rete.
2. Apri le **Impostazioni** e tocca **Cerca aggiornamenti** in fondo.
3. Confronta la riga della versione con quella delle **Novità**. Vedi {{link:settings/version-and-updates}}.
4. Ancora la vecchia versione? Chiudi Diana del tutto (scorrila via dalle app recenti) e riaprila.

:::note
Le versioni dell’app sono nelle **Novità**, la più recente in alto, in olandese e inglese.
:::
'''},
'help/data-and-limits': {'title': 'I tuoi dati e i limiti', 'desc': 'Cosa resta sul tuo dispositivo, perché nulla si sincronizza, e cosa Diana non può fare.', 'body': '''
## Tutto resta su un dispositivo, in un browser

I tuoi nominativi, locator, paese, parole rapide, lingua, scelta sulle statistiche e i PIN dei tuoi annunci sono nella memoria locale di quel solo browser. Nulla si sincronizza.

- Usi Diana sul telefono e sul portatile? Configurala su entrambi. Non c’è un account per collegarli.
- **Cancellare i dati del browser** (cronologia, cookie e dati dei siti), usare una **finestra privata** o **rimuovere l’app installata** cancella queste impostazioni. Diana riparte allora dalla schermata di benvenuto.

:::caution[I PIN dei tuoi annunci]
Sono nella stessa memoria. Cancella il browser e spariscono. Annota i PIN importanti anche altrove.
:::

## Cosa Diana non può fare

- **I dati in diretta dipendono da altri.** Spot e agenda arrivano da WWFF Spotline. Se non è disponibile, la schermata Spots lo dice. Le condizioni di propagazione arrivano dalla NOAA; la scheda dice quanto sono vecchie.
- **I confini esistono solo dove è stato fornito un file**: oggi cinque paesi. Altrove le referenze sono punti, e Diana non può dire se sei dentro. Vedi {{link:map/points-and-areas}}.
- **Non tutte le riserve hanno dati completi.** Molte hanno solo un nome e una referenza. È una lacuna dei dati di origine.
- **Diana non tiene il log** e non carica log. Questo resta compito del tuo programma di log e del WWFF.

## Uso dei dati

I confini e i numeri delle attivazioni provengono dai programmi WWFF, dalla WDPA, da fonti pubbliche e da WWFF Spotline, e restano dati dei rispettivi proprietari. Vedi {{link:about/data-sources}}.
'''},
'help/faq': {'title': 'Domande frequenti', 'desc': 'Risposte brevi alle domande più comuni.', 'body': '''
## Diana costa qualcosa?

No. Diana è gratuita, senza pubblicità e senza account.

## Diana è un’app ufficiale WWFF?

No. Diana è un progetto di volontari che sostiene l’hobby WWFF. Usa i servizi pubblici del WWFF, come Spotline e l’elenco.

## Diana invia la mia posizione da qualche parte?

No. La tua posizione è usata solo sul tuo schermo. Uno spot invia nominativo, frequenza, modo, referenza e nota, mai la tua posizione. Vedi {{link:start/privacy}}.

## Diana funziona senza rete?

Sì, con gli ultimi dati caricati: la mappa già vista, le referenze, Info campo Posizione e il piano di banda. Gli spot in diretta e l’invio di uno spot richiedono la rete.

## Perché la mia referenza è un punto e non un’area?

Perché Diana non ha un confine per essa, o perché si trova in un paese diverso da quello che hai caricato. Vedi {{link:map/points-and-areas}}.

## Posso tenere il log in Diana?

No. Diana aiuta prima e durante l’attivazione. Il tuo log resta nel tuo programma di log. In **Regole** Diana mostra il nome di file corretto.

## Le mie impostazioni sono sparite. Cosa è successo?

I dati del browser sono stati cancellati, l’app è stata rimossa, o hai usato una finestra privata. Vedi {{link:help/data-and-limits}}.

## Anche il mio programma nazionale può avere i confini?

Sì. Il coordinatore nazionale invia il file delle aree (KMZ) al team di Diana. Di più in {{link:about/about-diana}}.

## Ho trovato un errore. Dove lo segnalo?

I contatti sono nella pagina privacy dell’app (**Impostazioni** › **Privacy**). Indica la tua riga della versione: {{link:settings/version-and-updates}}.
'''},
}
