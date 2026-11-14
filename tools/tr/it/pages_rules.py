T = {
'rules/wwff-rules': {'title': 'Le regole WWFF in Diana', 'desc': 'La selezione di regole WWFF nell’app, e il nome corretto per il tuo file di log.', 'body': '''
Tocca **Regole** nella barra in basso. Si apre la scheda **Regole**: una selezione delle regole ufficiali WWFF che contano di più sul campo, nella tua lingua.

{{img:phone-rules|La schermata Regole con le regole sull’area di referenza}}

## Cosa contiene

Le regole 3.5, 3.6, 4.4, 4.7, 6.8, 6.9 e 6.11 delle WWFF Global Rules, in tre gruppi:

- **L’area**: stare dentro l’area di referenza, referenze che confinano con un’altra o la contengono, attivarne più di una insieme.
- **I QSO**: regole sui collegamenti stessi.
- **I log**: come nominare e caricare il tuo log.

Sono regole WWFF, quindi valgono anche per l’IFF e per ogni altro programma nazionale.

:::note[Traduzioni]
I testi nelle altre lingue sono tradotti dal team di Diana. Fa fede il testo inglese del WWFF. Ogni traduzione rimanda al PDF ufficiale.
:::

## Il nome del tuo file di log

La regola 6.8 richiede un nome di file preciso. Diana mostra un esempio con ogni parte spiegata:

`ON3VZ@ONFF-0104 20261002.adi`

| Parte | Significato |
|---|---|
| `ON3VZ` | Il tuo nominativo. |
| `@` | Separatore. |
| `ONFF-0104` | La referenza. |
| (spazio) | Uno spazio. |
| `20261002` | La data: anno, mese, giorno. |
| `.adi` | Un file di log ADIF. |

La regola 6.9 rimanda alla ricerca ufficiale dei log WWFF: [wwff.co/logsearch](https://wwff.co/logsearch/).

:::tip
Diana non tiene il log per te. Ti aiuta prima e durante l’attivazione; il tuo log resta nel tuo programma di log.
:::
'''},
'rules/band-plan': {'title': 'Il piano di banda', 'desc': 'Dove puoi trasmettere su ogni banda, con le frequenze preferite WWFF.', 'body': '''
Nella schermata **Regole**, tocca la scheda **Piano di banda**.

{{img:phone-bandplan|Il piano di banda con i segmenti CW, digitale e SSB di 80, 40 e 30 m}}

## Come leggerlo

Per ogni banda:

- Una **barra** con i segmenti **CW**, **digitale** e **SSB**, con le loro frequenze, per esempio *CW da 3,500 a 3,570 MHz*.
- La frequenza **FT8**, segnalata.
- Le **frequenze preferite WWFF**, evidenziate in un riquadro giallo, per esempio *SSB 7,144 · CW 7,024*.

## Perché è importante

Quando ti spotti, Diana confronta la tua frequenza con questo piano di banda e ti avvisa se il tuo modo non corrisponde al segmento. Vedi {{link:spots/spot-yourself}}.

:::tip
In una giornata di molte attivazioni, inizia vicino alla frequenza preferita WWFF: è lì che i cacciatori ascoltano per primi.
:::
'''},
}
