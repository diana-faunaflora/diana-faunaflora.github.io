T = {
'spots/on-air': {'title': 'Chi è in aria', 'desc': 'La schermata Spots: spot WWFF in diretta, ATNO, direzione e distanza.', 'body': '''
Tocca **Spots** nella barra in basso. La schermata **Spot e agenda** mostra chi è in aria da un’area WWFF in questo momento. L’elenco arriva in diretta da WWFF Spotline e si aggiorna ogni 30 secondi.

{{img:phone-spots-world|La schermata Spots, scheda In aria, Mondiale, con un elenco di stazioni}}

## Una riga per stazione

| Cosa vedi | Significato |
|---|---|
| Nominativo | L’attivatore, per esempio `F5MQU/P`. |
| Numero di QSO | Quanti collegamenti sono già stati fatti da quella referenza, secondo l’elenco WWFF. |
| **ATNO** in rosso | *All Time New One*: questa referenza non è mai stata attivata. La preferita dei cacciatori. |
| Frequenza, modo, referenza | Per esempio `10112 kHz · CW · FFF-4038`. |
| Minuti | Da quanto tempo è arrivato lo spot. |
| Direzione e distanza | Da te, per esempio `191° · 440 km`. |

## Il tuo paese o mondiale

Sotto le schede scegli **il tuo paese** (per esempio IFF) o **Mondiale**. Diana ricorda la scelta e la mantiene allineata alla stessa impostazione nelle Impostazioni. Il paese indicato dal pulsante segue la tua impostazione del paese: finché non ne scegli uno, Diana lo ricava dal nominativo (I… dà IFF, ON… ONFF, DL… DLFF).

## Aprire uno spot

1. Tocca una riga.
2. La mappa si apre, ingrandita su quell’area, con un pannello: frequenza e modo, la riserva, il locator sul posto e il tuo, la nota, il numero di QSO, Maggiori info e una bussola con la direzione.
3. **← Torna a Spots**, o il tasto indietro di Android, ti riporta all’elenco.
4. **×** o trascinare verso il basso chiude solo il pannello e mantiene la mappa.

:::note[Spotline non raggiungibile?]
Allora la schermata lo dice, invece di mostrare vecchi spot senza avviso.
:::
'''},
'spots/agenda': {'title': 'L’agenda', 'desc': 'Attivazioni annunciate: chi prevede cosa, e quando.', 'body': '''
Nella schermata **Spots**, tocca la scheda **Agenda**. Vedi tutte le attivazioni annunciate, con referenza, bande e modi, e data e ora in UTC.

{{img:phone-agenda|La scheda Agenda con attivazioni annunciate}}

## Leggere l’agenda

- **In corso**: un punto arancione e *"in diretta fino a …"*.
- **Ancora da venire**: in grigio, con data e ora d’inizio.
- **ATNO** in rosso: la referenza non è mai stata attivata.

La tua scelta tra **il tuo paese** e **Mondiale** vale anche qui.

## Aprire un annuncio

Tocca una riga. La mappa si apre su quell’area con banda e modo, la riserva, il locator, la nota e la direzione. **← Torna a Spots** ti riporta indietro.

## Annunciare tu stesso

Tocca **+ Annuncia** in cima all’agenda. Vedi {{link:spots/announce}}.

:::tip[Anche sulla mappa]
Gli annunci sono sulla mappa come un punto bianco con un anello arancione, con una linea arancione tratteggiata da te. Vedi {{link:map/reading-the-map}}.
:::
'''},
'spots/spot-yourself': {'title': 'Spottati', 'desc': 'Fai sapere ai cacciatori che sei in aria, tramite WWFF Spotline.', 'body': '''
In aria e pronto? Spottati, così i cacciatori ti trovano. Lo spot va a WWFF Spotline e da lì al DX cluster.

{{img:phone-spot-yourself|La schermata Spot con referenza, nominativi, frequenza, modo e nota}}

## Passo dopo passo

1. Tocca **Spot** nella barra in basso, o **Spottati qui** nel pannello di un’area.
2. Controlla la **referenza**. Se sei dentro un’area, o arrivi da un pannello, Diana l’ha già compilata e dice da dove viene.
3. I tuoi **nominativi** arrivano dalle Impostazioni: il nominativo portatile come attivatore, quello abituale come spotter.
4. Inserisci la **frequenza** in kHz, per esempio `7144`, e scegli il **modo**.
5. Facoltativo: una breve **nota**, fino a 100 caratteri. Tocca una delle tue **parole rapide** per aggiungerla con un tocco.
6. Tocca **Verifica**. Spotline esamina il tuo spot senza pubblicarlo, e ti dice cosa ne pensa.
7. Accettato? Tocca **Invia spot**. Ricevi una conferma con il numero del tuo spot.

## Perché prima Verifica, poi Invia?

Ogni richiesta a Spotline viene presa da un budget condiviso da tutti gli utenti. *Verifica* garantisce che uno spot sia corretto prima che costi un invio vero. Se cambi qualcosa dopo la verifica, *Invia* si richiude: il via libera valeva per lo spot com’era allora.

## Cosa Diana controlla per te

- Il formato del **nominativo**, l’intervallo della **frequenza** e la lunghezza della **nota**, come Spotline.
- Il **piano di banda**: un avviso quando il tuo modo non corrisponde al segmento della tua frequenza.
- La **referenza**, rispetto all’elenco di Diana. La risposta è immediata, anche senza rete.

:::caution[Cosa non va in una nota]
Niente ringraziamenti né richieste di banda. Ogni spot va al DX cluster, dove è solo rumore. Spotline filtra anche il linguaggio inappropriato.
:::

## Quando qualcosa va storto

- **Premuto due volte con una connessione scarsa?** Diana dice che lo spot c’era già. Niente viene pubblicato due volte.
- **Spotline rifiuta?** Ricevi la spiegazione di Spotline stesso.
- **L’invio non funziona proprio?** Diana offre **Invia alla vecchia maniera**: lo spot va al modulo di Spotline in una nuova scheda. Vedi tu la loro risposta, ma Diana non può confermarla.

Non sei ancora in aria, stai solo pianificando? Usa l’agenda: {{link:spots/announce}}.
'''},
'spots/announce': {'title': 'Annunciare un’attivazione', 'desc': 'Mettere un’attivazione prevista nell’agenda WWFF, e conservare il tuo PIN.', 'body': '''
Stai pianificando un’attivazione? Annunciala, così i cacciatori sono pronti. L’annuncio va nell’agenda WWFF su Spotline.

{{img:phone-announce|La schermata Annuncia con nominativi, referenza, inizio e fine, bande e modi}}

## Tre modi per arrivarci

- **Agenda** nella barra in basso.
- **+ Annuncia** nella scheda Agenda della schermata Spots.
- **Annuncia un’attivazione** nel pannello di un’area: la referenza è già compilata.

## Passo dopo passo

1. Controlla il **nominativo dell’attivatore** e **il tuo nominativo**. Qualcun altro può annunciare per un attivatore.
2. Inserisci la **referenza WWFF**, per esempio `ONFF-0104`.
3. Scegli **inizio** e **fine**. Li scegli sull’orologio del tuo dispositivo; Diana li converte in UTC prima che lascino il tuo dispositivo.
4. Facoltativo: spunta le **bande** e i **modi** (anche più di uno, per esempio *40 m, 20 m · CW, SSB*) e aggiungi una nota.
5. Tocca **Verifica** e, una volta accettato, **Invia annuncio**.
6. **Annotati il PIN.**

:::danger[Conserva il tuo PIN]
Il PIN è l’unico modo per modificare o annullare questo annuncio più tardi, sul sito di Spotline. Diana non può farlo al posto tuo, e un PIN perso non si recupera. Per questo Diana tiene sotto il modulo un elenco di tutto ciò che hai annunciato da questo dispositivo (referenza, data, PIN). Tocca **✕** per rimuovere una riga. Quell’elenco esiste solo su questo dispositivo.
:::

## Limiti

- Al massimo **un mese** in anticipo, e la fine non prima dell’inizio. Spotline applica le stesse regole.
- Al massimo **16 annunci al giorno** da un dispositivo tramite Diana, per proteggere il budget condiviso. L’uso normale resta molto al di sotto.
- Per gli annunci non esiste la "vecchia maniera". Se non funziona, riprova più tardi.

Quali bande offre l’elenco (tutte, o solo HF) è un’impostazione: {{link:settings/band-list}}.
'''},
}
