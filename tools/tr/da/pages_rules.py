T = {
'rules/wwff-rules': {'title': 'WWFF-regler i Diana', 'desc': 'Udvalget af WWFF-regler i appen, og det rigtige navn til din logfil.', 'body': '''
Tryk på **Regler** i bjælken nederst. Fanen **Regler** åbner: et udvalg af de officielle WWFF-regler, der betyder mest i felten, på dit sprog.

{{img:phone-rules|Regler-skærmen med reglerne om referenceområdet}}

## Hvad den indeholder

Reglerne 3.5, 3.6, 4.4, 4.7, 6.8, 6.9 og 6.11 i WWFF Global Rules, i tre grupper:

- **Området**: at stå inde i referenceområdet, referencer der grænser op til eller indeholder en anden, at aktivere flere på én gang.
- **QSO'er**: regler om selve forbindelserne.
- **Logs**: hvordan du navngiver og uploader din log.

Det er WWFF-regler, så de gælder også for OZFF og alle andre nationale programmer.

:::note[Oversættelser]
Teksterne på andre sprog er oversat af Diana-holdet. Det er WWFF's engelske tekst, der gælder. Hver oversættelse linker til den officielle PDF.
:::

## Navnet på din logfil

Regel 6.8 kræver et fast filnavn. Diana viser et eksempel med hver del markeret:

`ON3VZ@ONFF-0104 20261002.adi`

| Del | Betydning |
|---|---|
| `ON3VZ` | Dit kaldesignal. |
| `@` | Skilletegn. |
| `ONFF-0104` | Referencen. |
| (mellemrum) | Ét mellemrum. |
| `20261002` | Datoen: år, måned, dag. |
| `.adi` | En ADIF-logfil. |

Regel 6.9 henviser til WWFF's officielle logsøgning: [wwff.co/logsearch](https://wwff.co/logsearch/).

:::tip
Diana logger ikke for dig. Den hjælper dig før og under aktiveringen; din log bliver i dit eget logprogram.
:::
'''},
'rules/band-plan': {'title': 'Båndplanen', 'desc': 'Hvor du må sende pr. bånd, med WWFF-foretrukne frekvenser.', 'body': '''
Tryk på fanen **Båndplan** på skærmen **Regler**.

{{img:phone-bandplan|Båndplanen med CW-, digital- og SSB-segmenterne på 80, 40 og 30 m}}

## Sådan læser du den

For hvert bånd:

- En **bjælke** med segmenterne for **CW**, **digital** og **SSB**, med deres frekvenser, fx *CW 3.500 til 3.570 MHz*.
- **FT8**-frekvensen, markeret.
- De **WWFF-foretrukne frekvenser**, fremhævet i en gul boks, fx *SSB 7.144 · CW 7.024*.

## Hvorfor det betyder noget

Når du spotter dig selv, tjekker Diana din frekvens mod denne båndplan og advarer dig, hvis din mode ikke passer til segmentet. Se {{link:spots/spot-yourself}}.

:::tip
På en travl aktiveringsdag er det bedst at starte nær den WWFF-foretrukne frekvens: dér lytter jægerne først.
:::
'''},
}
