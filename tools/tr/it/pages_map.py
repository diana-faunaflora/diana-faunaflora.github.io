T = {
'map/map-screen': {'title': 'La schermata della mappa', 'desc': 'La schermata principale di Diana: i pulsanti in alto e la barra in basso.', 'body': '''
La mappa è la schermata principale di Diana. Tutto il resto parte da qui.

{{img:phone-map|La mappa di Diana intorno ad Anversa, con aree verdi, uno spot e delle linee}}

## La barra in basso

Da sinistra a destra: **Mappa**, **Spots**, **Spot**, **Agenda**, **Info campo**, **Regole** e **Impostazioni**. Toccane una per aprire quella schermata.

:::tip[Tornare alla tua posizione]
Tocca **Mappa** nella barra in basso in qualsiasi momento: la mappa si ricentra dove ti trovi, e lo zoom resta com’è. Diana fa una nuova misura GPS se l’ultima ha più di due minuti o è meno precisa di 30 m. Senza GPS si centra sul tuo locator delle Impostazioni, e lo dice.
:::

## I pulsanti in alto

| Pulsante | Cosa fa |
|---|---|
| **⌕** | Cerca per nome o numero di referenza. Vedi {{link:map/search}}. |
| **◐** | Stile della mappa: Liberty, Positron, Bright o Dark. |
| **≡** | Livelli e lingua. Vedi {{link:map/layers-and-styles}}. |

In alto a sinistra una riga indica quante referenze sono caricate, per esempio *"947 riferimenti WWFF · 1 senza confine"*.

## Muoversi

- **Trascina** con un dito per spostare la mappa.
- **Pizzica** con due dita per ingrandire o ridurre, oppure usa **+** e **−** a destra.
- **Tocca** un’area, un punto o uno spot per aprire il suo pannello. Vedi {{link:map/area-panel}}.

## Cosa vedo?

Colori, punti e linee sono spiegati in {{link:map/reading-the-map}}. Perché una referenza è un’area e un’altra solo un punto è spiegato in {{link:map/points-and-areas}}.
'''},
'map/points-and-areas': {'title': 'Punti e aree', 'desc': 'Perché una referenza è un’area verde e un’altra un punto blu, e come cambiarlo.', 'body': '''
Sulla mappa una referenza WWFF appare in uno di tre modi. Quale dipende da ciò che Diana sa di essa, e dal paese che hai scelto.

| Cosa vedi | Cosa significa | Diana può dire se sei dentro? |
|---|---|---|
| **Area verde** | Una referenza con il suo confine reale, nel paese che hai scelto. | Sì |
| **Anello tratteggiato con un punto arancione** | Una referenza del tuo paese senza confine. Solo una posizione approssimativa. | No |
| **Punto blu** | Una referenza in un altro paese. Vicini tra loro formano un cerchio con un numero. | No |

## Perché un’area?

Un’area ha bisogno di un file dei confini. Oggi Diana ha questi file per **cinque paesi**: Belgio (ONFF), Paesi Bassi (PAFF), Germania (DLFF), Danimarca (OZFF) e Portogallo (CTFF), e se ne aggiungono continuamente altri. Li forniscono i coordinatori nazionali WWFF.

Diana carica i confini di **un paese alla volta**: quello che hai scelto nelle Impostazioni. Così la mappa resta veloce sul telefono.

## Perché un punto?

- La referenza si trova in un paese per cui Diana **non ha un file dei confini**. Allora Diana conosce solo la posizione dall’elenco WWFF.
- Oppure il paese **ha** i confini in Diana, ma **non è il paese che hai scelto**. Allora appare anch’esso come punto, finché non carichi quel paese.

## Perché un anello tratteggiato?

In un paese con confini, alcune referenze non hanno un confine nel file, per esempio territori d’oltremare dei Paesi Bassi. Appaiono come un anello tratteggiato nella posizione approssimativa.

## I dettagli li hai sempre

Qualunque cosa tu veda, **toccala**: si apre un pannello con tutto ciò che Diana sa. Per un punto blu sono referenza, paese e nome, locator e zone, direzione e distanza da te, numero di QSO o **ATNO** se non è mai stata attivata, e un link a maggiori informazioni. Vedi {{link:map/area-panel}}.

## Quando e come cambiarlo

Quando vai in un altro paese, o vuoi vedere il confine reale di una referenza che ora è un punto:

**Dal pannello (più rapido)**

1. Tocca il punto blu.
2. Se Diana ha i confini di quel paese, il pannello lo dice e mostra il pulsante **Mostra [paese] in dettaglio**.
3. Toccalo. Diana carica quel paese e riapre la stessa referenza, ora con il suo confine.

**Dalle Impostazioni**

1. Tocca **Impostazioni** in basso a destra.
2. In **Il tuo paese**, scegli il paese. I paesi segnati **Con confini** ricevono le loro aree; **Solo punti** resta a punti.
3. Il cambiamento è immediato. Sotto il menu Diana dice cosa ha caricato, per esempio *"PAFF, 281 aree con confini caricate"*.

Il tuo filtro degli spot (il tuo paese o Mondiale) non cambia quando scegli un altro paese. Di più in {{link:settings/your-country}}.

:::note[Una nuova riserva prima come punto]
Le referenze esistenti arrivano dall’elenco WWFF, ogni notte. I confini arrivano da un file pubblicato dal team di Diana. Una riserva appena nata può quindi comparire prima come punto e ricevere il contorno più tardi.
:::
'''},
'map/reading-the-map': {'title': 'Leggere la mappa', 'desc': 'Cosa significa ogni colore, punto e linea sulla mappa.', 'body': '''
Tutto sulla mappa ha un significato. Questa è la legenda.

{{img:map-legend|Mappa intorno ad Anversa e Roosendaal con aree verdi, gruppi blu, una linea verde punteggiata e una linea arancione tratteggiata}}

## Aree e referenze

| Cosa vedi | Significato |
|---|---|
| Area verde con un numero | Una referenza con il suo confine reale, nel tuo paese. Il numero è la referenza, per esempio `ONFF-0602`. |
| Contorno arancione | L’area che hai appena toccato. |
| Anello tratteggiato con un punto arancione | Una referenza del tuo paese senza confine: una posizione approssimativa. |
| Punto blu | Una referenza in un altro paese. |
| Cerchio blu con un numero | Diversi punti blu vicini. Toccalo per ingrandire; si divide. |
| Linea grigia | Un confine nazionale sulla mappa di base. |

Dal livello di zoom 11 ogni punto riceve la sua referenza come etichetta.

## Spot e annunci

| Cosa vedi | Significato |
|---|---|
| Icona d’antenna verde pulsante | Una stazione in aria adesso, con nominativo, frequenza e modo accanto. |
| **Linea verde punteggiata** | Da te verso una stazione in aria adesso. |
| Spot sbiadito | Uno spot più vecchio di 30 minuti. |
| Punto bianco con anello arancione | Un’attivazione annunciata in agenda. |
| **Linea arancione tratteggiata** | Da te verso un’attivazione annunciata, con nominativo e orario. |
| La tua posizione | Un indicatore. Quando la posizione è meno precisa di circa 10 m, un anello tratteggiato mostra il margine. |

:::tip[Troppe linee?]
Disattivale in **≡** › **Linee verso gli spot**. Diana ricorda la scelta. **⤢ Mostra tutti gli spot** inquadra tutti gli spot e la tua posizione in un colpo.
:::

Perché alcune referenze sono aree e altre punti: {{link:map/points-and-areas}}.
'''},
'map/area-panel': {'title': 'Dettagli dell’area', 'desc': 'Tocca un’area o un punto: il pannello con tutto ciò che Diana sa, e spottarti da lì.', 'body': '''
Tocca un’area, un punto o uno spot sulla mappa. Dal basso sale un pannello con tutto ciò che Diana sa di quella referenza. Diana mostra solo ciò che sa davvero: mai una casella vuota.

{{img:phone-area-panel|Pannello di ONFF-0685 Hobokense Polder con superficie, gestore, designazione, categoria IUCN e locator}}

## Cosa c’è nel pannello

Per un’**area con confine**:

- Referenza, regione e nome.
- Ciò che contiene il file dell’area: **superficie** in ettari, **gestore**, **designazione**, **categoria IUCN**, **designato dal**. Non tutte le riserve hanno tutto; è una lacuna dei dati di origine, non qualcosa che Diana nasconde.
- Il **numero di QSO** e l’**ultima attivazione**, dall’elenco WWFF.
- Il **locator**, la **zona CQ**, la **zona ITU** e la **regione ITU**.
- **Maggiori info**: il sito della riserva, quando l’elenco WWFF ne ha uno. Si apre nel tuo browser, così Diana e la mappa restano dove erano.

Per una **referenza senza confine** (anello tratteggiato): lo stesso pannello senza i dati dell’area, e una nota che dice che Diana non può sapere se sei dentro.

Per un **punto blu** in un altro paese: referenza, paese e nome, locator e zone, **Da te** (direzione e distanza), il numero di QSO o **ATNO** in rosso se non è mai stata attivata, e Maggiori info.

## Spottarti o annunciare dal pannello

In fondo a ogni pannello ci sono due pulsanti:

- **Spottati qui** apre il modulo dello spot con la referenza già compilata. Vedi {{link:spots/spot-yourself}}.
- **Annuncia un’attivazione** apre il modulo dell’agenda con la referenza compilata. Vedi {{link:spots/announce}}.

## Chiudere il pannello

Trascina il pannello **verso il basso**, o tocca **×**. La mappa resta dov’è. Sul telefono è visibile un solo pannello in basso alla volta.
'''},
'map/overlapping-areas': {'title': 'Aree sovrapposte', 'desc': 'Quando le referenze si sovrappongono, e come passare dall’una all’altra.', 'body': '''
A volte le referenze si sovrappongono: una piccola riserva si trova spesso dentro un’area naturale più grande. Su quel pezzo di terreno sei in tutte contemporaneamente.

## Come lo mostra Diana

Diana disegna sempre l’area **più piccola** sopra, così puoi toccarla. Un tocco apre l’area più piccola sotto il tuo dito: tocca dentro la riserva per la riserva, e nel terreno intorno per l’area più grande.

## Passare all’altra area

1. Tocca la mappa dentro la riserva. Si apre il pannello dell’area **più piccola**.
2. Scorri il pannello fino a **"Questo punto è anche dentro queste referenze"**. Le altre aree sono lì come pulsanti, con nome e dimensione.
3. Tocca un pulsante. Il pannello mostra ora quell’area, con il suo confine in arancione.
4. Per tornare? Quel pannello ha un pulsante verso l’area da cui venivi.

## Con la tua posizione GPS

Se ti trovi in più aree contemporaneamente, la scheda in fondo alla mappa lo dice, per esempio *"Sei in 2 riferimenti"*, con la distanza dal confine più vicino. Diana apre allora il pannello dell’area più piccola, con le altre come pulsanti.

:::tip[Cosa significa per la tua attivazione]
Se sei in tutte quelle aree, le regole WWFF ti permettono di attivarle insieme. Leggi le regole in Diana in **Regole**, o il testo ufficiale su wwff.co. Vedi {{link:rules/wwff-rules}}.
:::

:::caution[Non per le referenze senza confine]
Un anello tratteggiato è solo una posizione approssimativa. Lì Diana non può sapere se sei dentro, e quindi nemmeno mostrare sovrapposizioni.
:::
'''},
'map/am-i-inside': {'title': 'Sono dentro l’area?', 'desc': 'Come Diana ti dice se sei dentro, e come leggere la precisione.', 'body': '''
Una scheda in fondo alla mappa risponde alla domanda di ogni attivatore: **sono dentro la riserva?**

## Cosa dice la scheda

- **Dentro un’area**: quale, e la distanza dal confine più vicino.
- **Dentro più aree insieme** (quando le aree si sovrappongono): quante, e si apre il pannello della più piccola. Vedi {{link:map/overlapping-areas}}.
- **Fuori**: l’area più vicina e quanto dista.

Ogni risposta termina con la qualità della tua posizione, per esempio *"posizione ±6 m"*.

:::note[Aree fatte di più parti]
Alcune referenze sono composte da parti separate. Il pannello dice allora quante. Tutta la tua stazione deve stare dentro una di esse.
:::

## Perché ci vogliono alcuni secondi

Un telefono che ha appena svegliato il GPS risponde prima da wifi e celle, e quella posizione può sbagliare di centinaia di metri. Per questo Diana continua ad ascoltare mentre la precisione migliora, e mostra ciò che ha finora: *"Affinamento… ±380 m"*. Risponde appena la posizione è abbastanza buona, o dopo dodici secondi con la migliore ottenuta. Se è ancora grossolana, la risposta lo dice.

## Leggere la precisione

| Precisione | Cosa significa di solito |
|---|---|
| ±10 m o meglio | Satelliti. Affidabile, anche vicino a un confine. |
| da ±20 a 50 m | Ragionevole. Attenzione vicino a un confine. |
| ±100 m o peggio | Wifi o celle, spesso al chiuso. Non abbastanza per essere sicuri. |

Quando il margine supera circa 10 m, attorno al tuo indicatore viene disegnato un **anello tratteggiato** esattamente di quel raggio. Un anello stretto significa satelliti; un anello che copre tutto l’isolato significa che la risposta è arrivata dal wifi.

:::tip[Ottenere una posizione migliore]
Esci all’aperto, con il cielo libero sopra di te, e aspetta qualche secondo. Resta grossolana, oltre circa 75 m? Forse il sito può usare solo una posizione approssimativa. Compare allora un avviso che suggerisce di controllare l’impostazione di localizzazione: vedi {{link:help/location-problems}}.
:::

## Due trappole che Diana sorveglia

- **Al chiuso**, una posizione da wifi arriva spesso in un secondo dichiarando ±20 m. È la precisione che il database wifi si attribuisce, non quella reale. Diana risponde, ma continua ad ascoltare per il resto dei dodici secondi e corregge la risposta se serve.
- **Telefoni che promettono più di quanto possono.** Diana confronta le letture degli ultimi 45 secondi. Una singola lettura assurda viene ignorata. Se le letture si contraddicono, la risposta dice *"letture in contraddizione"*. Camminare non conta come dispersione.

:::caution
Diana può rispondere solo per le aree **con** confine. Per un anello tratteggiato o un punto blu non può. Vedi {{link:map/points-and-areas}}.
:::
'''},
'map/layers-and-styles': {'title': 'Livelli e stile della mappa', 'desc': 'Attivare e disattivare parti della mappa, e scegliere uno stile.', 'body': '''
## Livelli (≡)

Tocca **≡** in alto a destra sulla mappa. Puoi attivare e disattivare:

| Livello | Cosa mostra |
|---|---|
| **Aree** | Le aree verdi del tuo paese. |
| **Numeri di riferimento** | Le etichette come `ONFF-0602`. |
| **Senza confine (punto)** | Gli anelli tratteggiati delle referenze senza confine. |
| **Spot sulla mappa** | Spot in diretta e annunci. Arrivano da WWFF Spotline e si aggiornano ogni 30 secondi. |
| **Linee verso gli spot** | Le linee verdi punteggiate e arancioni tratteggiate da te. |
| **Altre aree WWFF** | I punti blu del resto del mondo. |

Lo stesso menu contiene **⤢ Mostra tutti gli spot** e i pulsanti della lingua. Diana ricorda le tue scelte.

## Stile della mappa (◐)

Tocca **◐** per un’altra mappa di base:

- **Liberty**: quella predefinita, con i colori del terreno.
- **Positron**: molto chiara e tranquilla, ottima sotto il sole forte.
- **Bright**: più colori e dettagli.
- **Dark**: scura, riposante per gli occhi di notte.

:::tip
Sul campo, con il sole forte, **Positron** è spesso la più leggibile.
:::
'''},
'map/search': {'title': 'Cercare', 'desc': 'Trovare una referenza per nome o numero, ovunque nel mondo.', 'body': '''
Tocca **⌕** in cima alla mappa e scrivi.

- **Un nome**, per esempio `Kalmthoutse Heide`.
- **Una referenza completa**, per esempio `ONFF-0012` o `DLFF-0210`.
- **Solo un numero**, per esempio `0012`. Allora Diana cerca solo nel tuo paese.

Tutte le referenze WWFF del mondo possono essere trovate. I risultati del paese caricato compaiono per primi. Tocca un risultato: la mappa vi si avvicina e apre il suo pannello.

:::tip
La ricerca funziona anche offline: l’elenco delle referenze è sul tuo dispositivo.
:::
'''},
}
