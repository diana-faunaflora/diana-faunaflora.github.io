T = {
'about/data-sources': {'title': 'Datakilder', 'desc': 'Hvor hver oplysning i Diana kommer fra.', 'body': '''
Diana kombinerer åbne og offentlige kilder. Kun kilder, der må bruges, er med.

| Hvad | Kilde | Hvor friskt |
|---|---|---|
| WWFF-referencer, antal QSO'er, seneste aktivering, websted | Den officielle WWFF-fortegnelse | Hver nat |
| Områdegrænser | Områdefiler (KMZ) fra de nationale WWFF-koordinatorer | Når en ny fil udgives |
| Live-spots og agenda | WWFF Spotline (`spots.wwff.co`) | Hvert 30. sekund |
| Kort | OpenFreeMap, bygget på OpenStreetMap | Live |
| CQ- og ITU-zoner | Et offentligt datasæt (HB9HIL, MIT-licens), forenklet til omkring 3 km | Med appen |
| ITU-regioner | ITU Radio Regulations, artikel 5, med landegrænser fra Natural Earth | Med appen |
| Rumvejr | NOAA SWPC | Flere gange om dagen |

Grænserne og aktiveringstallene forbliver deres ejeres data: WWFF-programmerne, WDPA, offentlige kilder og WWFF Spotline. De må ikke videredistribueres eller genbruges andre steder uden deres tilladelse.
'''},
'about/about-diana': {'title': 'Om Diana', 'desc': 'Hvorfor navnet, hvem der laver den, licensen, og hvordan koordinatorer leverer grænser.', 'body': '''
## Hvorfor Diana?

Diana er den romerske gudinde for jagt og skove. Det er præcis, hvad WWFF handler om: naturområder, og jægere på jagt efter hver ny reference. Hjorten og buen i logoet henviser til hende.

## Hvem laver den

Diana er et frivilligt projekt, bygget som hobby af radioamatører, for at støtte WWFF-aktiviteten. Det er ikke en officiel WWFF-tjeneste; den bruger kun deres offentlige tjenester.

## Licens

- **Gratis for alle**, uden reklamer, uden konto.
- **Ikke til kommerciel brug.** Dianas kode er tilgængelig under PolyForm Noncommercial License: kun personlig, hobby- og ikke-kommerciel brug.
- Tilbydes som den er, uden nogen garanti, og så vidt loven tillader det, uden ansvar for fejl eller huller i de data, den viser.

De fulde vilkår står i licensen ved kildekoden: [github.com/diana-onff](https://github.com/diana-onff).

## Til nationale koordinatorer: jeres grænser i Diana

Diana viser rigtige grænser overalt, hvor et nationalt program leverer en områdefil. For at tilføje jeres land, eller opdatere det:

1. Forbered jeres områdefil som **KMZ**, efter [KMZ-formatvejledningen (PDF)](https://diana-onff.github.io/kmz-guide.pdf).
2. Send den til **wwffmembers@gmail.com**.
3. Diana-holdet tjekker den, laver selv den første upload og frigiver den, når alt er i orden.

## Præsentationen

En introduktion til Diana som slides, til programmer og koordinatorer: se linket på forsiden af dette websted.
'''},
}
