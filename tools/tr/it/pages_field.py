T = {
'field-info/overview': {'title': 'Info campo', 'desc': 'Tutto sul luogo in cui ti trovi, in tre schede.', 'body': '''
**Info campo** riguarda il luogo in cui ti trovi. Ha tre schede:

| Scheda | Cosa mostra |
|---|---|
| **Aree** | Le referenze WWFF intorno a te. Vedi {{link:field-info/areas-nearby}}. |
| **Posizione** | Dove sei in termini radio: ora, locator, zone. Vedi {{link:field-info/location}}. |
| **Condizioni** | Il meteo spaziale e cosa significa per le bande. Vedi {{link:field-info/conditions-space-weather}} e {{link:field-info/conditions-bands}}. |

## Aprire Info campo

1. Tocca **Info campo** nella barra in basso (il cerchio con un punto).
2. Tocca in alto la scheda che vuoi: **Aree**, **Posizione** o **Condizioni**.
3. Sotto il titolo controlla da dove parte Diana: *"dalla tua posizione GPS"* o *"dal tuo locatore JN45LM"*.

:::caution[Nessuna posizione?]
Se Diana dice che non sa ancora dove sei, consenti la posizione (vedi {{link:start/welcome-screen}}) o inserisci il tuo locator in **Impostazioni** › **La tua stazione**. Con il solo locator, Diana parte dal centro di quel quadrato, che può essere distante qualche chilometro.
:::
'''},
'field-info/areas-nearby': {'title': 'Aree vicine', 'desc': 'Le referenze WWFF intorno a te, ordinate come vuoi.', 'body': '''
La scheda **Aree** elenca le referenze WWFF intorno alla tua posizione, entro la distanza scelta nelle Impostazioni (10, 25, 50 o 100 km). Ci sono anche le referenze oltre il confine.

{{img:phone-field-areas|Info campo, scheda Aree, con referenze vicino ad Anversa ordinate per distanza}}

## Una riga per referenza

| Cosa vedi | Significato |
|---|---|
| Referenza e nome | Per esempio `ONFF-0842 · Boshoek`. |
| Distanza e direzione | In linea d’aria da te, per esempio `1.5 km · 62°`. |
| Numero di QSO | Quanti collegamenti sono stati fatti da lì, secondo l’elenco WWFF. |
| Ultima attività | La data dell’ultima attivazione. |
| *nessuna data di attivazione nota* | L’elenco conosce la referenza ma non una data. |
| *non presente nell’elenco WWFF* | Diana conosce l’area, ma l’elenco non ha nulla. Non significa che non sia mai stata attivata. |

## Ordinare: quale ordine scegliere?

| Pulsante | Quando usarlo |
|---|---|
| **Distanza** | Le più vicine prima. Quando vuoi montare in fretta. |
| **Ultima attività** | Le aree rimaste più a lungo fuori dall’aria prima. È lì che un pile-up è più probabile. |
| **Numero di QSO** | Le aree meno lavorate prima. Quando vuoi offrire ai cacciatori una nuova. |

## Aprire un’area

1. Tocca una riga.
2. La mappa si apre, ingrandita su quell’area, con il suo pannello e il suo confine.
3. Più di cento aree vicine? Tocca **Mostra altri** in fondo.

## Cambiare la distanza

**Impostazioni** › **Info campo** › 10, 25, 50 o 100 km. Vedi {{link:settings/field-info-distance}}.

:::note
Il numero di QSO e le date arrivano dall’elenco WWFF, aggiornato ogni notte. Dove l’elenco non ha nulla, la schermata lo dice, invece di chiamarla "mai attivata".
:::
'''},
'field-info/location': {'title': 'La posizione in termini radio', 'desc': 'Ora, locator, posizione e zone del luogo in cui ti trovi.', 'body': '''
La scheda **Posizione** ti dà tutto ciò che serve sul tuo punto durante un QSO o per il tuo log. Diana lo calcola sul dispositivo stesso, quindi funziona anche senza rete.

{{img:phone-field-location|Info campo, scheda Posizione, con ora UTC e locale, locator, precisione e zone}}

| Casella | Come leggerla |
|---|---|
| **Ora** | UTC e la tua ora locale con fuso orario. Il tuo log è sempre in UTC. |
| **Locator** | Il tuo locator Maidenhead a sei caratteri (`JO21FD`) e a otto (`JO21FD70`). In QSO di solito si danno i sei. |
| **Posizione** | In gradi decimali e in gradi, minuti e secondi, con la precisione in metri. |
| **Zone** | La tua zona CQ, zona ITU e regione ITU. Il Belgio è CQ 14, ITU 27, regione 1; l’Italia è CQ 15, ITU 28. |
| *confine vicino: anche …* | Sei vicino a un confine di zona, o la tua posizione è incerta. Sono allora possibili entrambi i numeri. |
| **WWFF più vicine** | Le referenze più vicine, ovunque nel mondo, in linea d’aria. |

:::note[Da dove vengono le zone]
Le zone CQ e ITU vengono da un insieme di dati pubblico, semplificato a circa 3 km. Per questo vicino a un confine la casella indica anche la zona vicina.
:::
'''},
'field-info/conditions-space-weather': {'title': 'Condizioni: meteo spaziale', 'label': 'Meteo spaziale', 'desc': 'L’indicatore Kp, SFI, indice A e macchie solari, e cosa significano.', 'body': '''
La scheda **Condizioni** inizia con il meteo spaziale di oggi: un indicatore con l’**indice Kp** e tre numeri sotto.

{{img:phone-field-conditions|Info campo, scheda Condizioni, con l’indicatore Kp su 2, calmo, e le barre delle bande}}

## L’indicatore Kp

Il Kp misura quanto è agitato il campo magnetico terrestre, su una scala da 0 a 9. Più è basso, meglio è per le bande alte. Diana mostra il valore ufficiale a tre ore della NOAA, e accanto una stima degli ultimi minuti.

| Kp | Parola in Diana | Cosa significa |
|---|---|---|
| da 0 a 2 | calmo | Nessun effetto. Condizioni normali. |
| 3 | instabile | Leggermente agitato. Di solito ancora nessun effetto evidente. |
| 4 | attivo | 20, 15 e 10 m scendono di un livello. |
| 5 e 6 | tempesta G1, G2 | Tempesta minore: 20, 15 e 10 m peggiorano. 80 e 40 m quasi non se ne accorgono. |
| da 7 a 9 | tempesta da G3 a G5 | Tempesta forte: tutte le bande peggiorano, quelle alte di più. |

:::note
Il Kp è un valore mondiale, non una misura nella tua posizione.
:::

## I tre numeri

| Numero | Cosa ti dice |
|---|---|
| **SFI** | Flusso solare. Più è alto, meglio si aprono le bande alte. Intorno a 70 è basso, sopra 150 è alto. |
| **A** | Quanto è stato agitato il campo magnetico nell’intera giornata. Basso è buono. |
| **Macchie solari** | Vanno di pari passo con lo SFI: più macchie, più possibilità di DX sulle bande alte. |

SFI, A e macchie solari sono valori giornalieri; Diana dice di quale giorno sono.

## Quanto sono vecchi i numeri?

Sotto l’indicatore c’è scritto quando i numeri sono stati aggiornati, per esempio *"Aggiornato alle 14:37 (12 min fa)"*. Diana prova a prenderli due volte all’ora, ma in pratica tra due aggiornamenti possono passare alcune ore.

- Più vecchi di **otto ore**: il messaggio diventa arancione.
- Valore Kp più vecchio di **dodici ore**: Diana lo segnala a parte.

La fonte è NOAA SWPC. Cosa significa per ogni banda: {{link:field-info/conditions-bands}}.
'''},
'field-info/conditions-bands': {'title': 'Condizioni: le bande', 'label': 'Le barre delle bande', 'desc': 'Come leggere la barra colorata di ogni banda nell’arco della giornata.', 'body': '''
Sotto il meteo spaziale, la scheda **Condizioni** mostra una barra colorata per banda: 80, 40, 20, 15 e 10 m.

## Leggere la barra di una banda

1. Ogni barra è **una banda**. Accanto alla banda c’è scritto a cosa serve, per esempio *"NVIS ed EU"*.
2. La barra va da sinistra a destra su cinque momenti della giornata: **mattino, mezzodì, pomeriggio, sera e notte**. Diana li calcola dall’alba e dal tramonto nella tua posizione.
3. Il **colore** è l’aspettativa: verde è buona, giallo discreta, rosso scarsa.
4. La sottile **linea** verticale è **ora**. A destra c’è scritto cosa vale adesso, per esempio *"ora: buona"*.

## Cosa significano le etichette

| Etichetta | Portata |
|---|---|
| **NVIS** | Vicino, fino a circa 400 km. Ideale per essere collegato dentro il tuo paese. |
| **EU** | Dentro l’Europa. |
| **DX** | Più lontano, fuori dall’Europa. |

| Banda | Etichetta in Diana |
|---|---|
| 80 m | NVIS, EU di notte |
| 40 m | NVIS ed EU |
| 20 m | EU e DX |
| 15 m | DX |
| 10 m | DX |

:::caution[Un’indicazione, non una promessa]
Le barre sono una stima approssimativa di Diana stessa, basata su SFI, Kp, stagione e ora del giorno nella tua posizione. Non è una previsione NOAA. Una banda indicata come "scarsa" può comunque essere aperta: ascolta sempre un momento.
:::

:::tip[Esempio sul campo]
Kp 2, calmo, SFI 91, la sera nelle Ardenne: i 40 m sono su buona e sono la tua migliore possibilità per il Belgio e l’Europa. I 15 m la sera sono su scarsa; non serve cominciare da lì.
:::

Senza posizione, Diana mostra comunque le barre, ma senza la linea dell’ora.
'''},
}
