T = {
'map/map-screen': {'title': 'Kortskærmen', 'desc': 'Dianas hovedskærm: knapperne øverst og bjælken nederst.', 'body': '''
Kortet er Dianas hovedskærm. Alt andet starter herfra.

{{img:phone-map|Dianas kort omkring Antwerpen, med grønne områder, et spot og linjer}}

## Bjælken nederst

Fra venstre mod højre: **Kort**, **Spots**, **Meld**, **Agenda**, **Feltinfo**, **Regler** og **Indstillinger**. Tryk på én for at åbne den skærm.

:::tip[Tilbage til din egen position]
Tryk på **Kort** i bjælken nederst når som helst: kortet centrerer igen på, hvor du er, og zoomet bliver, som det er. Diana tager en ny GPS-måling, hvis den seneste er ældre end to minutter eller mindre præcis end 30 m. Uden GPS centrerer den på din locator fra Indstillinger, og siger det.
:::

## Knapperne øverst

| Knap | Hvad den gør |
|---|---|
| **⌕** | Søg på navn eller referencenummer. Se {{link:map/search}}. |
| **◐** | Kortstil: Liberty, Positron, Bright eller Dark. |
| **≡** | Lag og sprog. Se {{link:map/layers-and-styles}}. |

Øverst til venstre står en linje med, hvor mange referencer der er indlæst, fx *"947 WWFF-områder · 1 uden grænse"*.

## Bevæg dig rundt

- **Træk** med én finger for at flytte kortet.
- **Knib** med to fingre for at zoome ind eller ud, eller brug **+** og **−** til højre.
- **Tryk** på et område, et punkt eller et spot for at åbne dets panel. Se {{link:map/area-panel}}.

## Hvad ser jeg?

Farverne, punkterne og linjerne forklares i {{link:map/reading-the-map}}. Hvorfor én reference er et område og en anden kun et punkt, forklares i {{link:map/points-and-areas}}.
'''},
'map/points-and-areas': {'title': 'Punkter og områder', 'desc': 'Hvorfor én reference er et grønt område og en anden en blå prik, og hvordan du ændrer det.', 'body': '''
På kortet vises en WWFF-reference på én af tre måder. Hvilken afhænger af, hvad Diana ved om den, og af det land, du har valgt.

| Hvad du ser | Hvad det betyder | Kan Diana afgøre, om du er inde? |
|---|---|---|
| **Grønt område** | En reference med sin rigtige grænse, i det land du har valgt. | Ja |
| **Stiplet ring med en orange prik** | En reference i dit land uden grænse. Kun et omtrentligt sted. | Nej |
| **Blå prik** | En reference i et andet land. Tæt sammen danner de en cirkel med et tal. | Nej |

## Hvorfor et område?

Et område kræver en grænsefil. Diana har sådanne filer for **fem lande** i dag: Belgien (ONFF), Holland (PAFF), Tyskland (DLFF), Danmark (OZFF) og Portugal (CTFF), og der kommer hele tiden flere til. De nationale WWFF-koordinatorer leverer dem.

Diana indlæser grænserne for **ét land ad gangen**: det, du har valgt under Indstillinger. Så forbliver kortet hurtigt på en telefon.

## Hvorfor en prik?

- Referencen ligger i et land, hvor Diana **ingen grænsefil** har. Så kender Diana kun positionen fra WWFF-fortegnelsen.
- Eller landet **har** grænser i Diana, men det er **ikke det land, du har valgt**. Så vises det også som en prik, indtil du indlæser det land.

## Hvorfor en stiplet ring?

Inden for et land med grænser har enkelte referencer ingen grænse i filen, fx oversøiske områder under Holland. De vises som en stiplet ring på det omtrentlige sted.

## Detaljerne får du altid

Uanset hvad du ser: **tryk på det**. Et panel åbner med alt, hvad Diana ved. For en blå prik er det reference, land og navn, locator og zoner, retning og afstand fra dig, antal QSO'er eller **ATNO** hvis den aldrig er blevet aktiveret, og et link til mere information. Se {{link:map/area-panel}}.

## Hvornår og hvordan du ændrer det

Når du tager til et andet land, eller vil se den rigtige grænse for en reference, der nu er en prik:

**Fra panelet (hurtigst)**

1. Tryk på den blå prik.
2. Har Diana grænserne for det land, siger panelet det og viser knappen **Vis [land] i detaljer**.
3. Tryk på den. Diana indlæser det land og åbner den samme reference igen, nu med sin grænse.

**Fra Indstillinger**

1. Tryk på **Indstillinger** nederst til højre.
2. Vælg landet under **Dit land**. Lande markeret **Med grænser** får deres områder; **Kun punkter** forbliver prikker.
3. Ændringen sker med det samme. Under menuen siger Diana, hvad den har indlæst, fx *"OZFF, … områder med grænser indlæst"*.

Dit spotfilter (dit land eller Globalt) ændres ikke, når du vælger et andet land. Mere i {{link:settings/your-country}}.

:::note[Et nyt reservat først som prik]
Hvilke referencer der findes, kommer fra WWFF-fortegnelsen, hver nat. Grænserne kommer fra en fil, som Diana-holdet udgiver. Derfor kan et helt nyt reservat først dukke op som et punkt og få sin omrids senere.
:::
'''},
'map/reading-the-map': {'title': 'Sådan læser du kortet', 'desc': 'Hvad hver farve, prik og linje på kortet betyder.', 'body': '''
Alt på kortet betyder noget. Dette er signaturforklaringen.

{{img:map-legend|Kort omkring Antwerpen og Roosendaal med grønne områder, blå klynger, en grøn prikket linje og en orange stiplet linje}}

## Områder og referencer

| Hvad du ser | Betydning |
|---|---|
| Grønt område med et nummer | En reference med sin rigtige grænse, i dit land. Nummeret er referencen, fx `ONFF-0602`. |
| Orange kant | Det område, du lige har trykket på. |
| Stiplet ring med en orange prik | En reference i dit land uden grænse: et omtrentligt sted. |
| Blå prik | En reference i et andet land. |
| Blå cirkel med et tal | Flere blå prikker tæt sammen. Tryk for at zoome ind; den deler sig. |
| Grå linje | En landegrænse på baggrundskortet. |

Fra zoomniveau 11 får hver prik sin reference som etiket.

## Spots og annonceringer

| Hvad du ser | Betydning |
|---|---|
| Grønt pulserende antenneikon | En station i luften nu, med kaldesignal, frekvens og mode ved siden af. |
| **Grøn prikket linje** | Fra dig til en station, der er i luften nu. |
| Falmet spot | Et spot, der er ældre end 30 minutter. |
| Hvid prik med orange ring | En annonceret aktivering fra agendaen. |
| **Orange stiplet linje** | Fra dig til en annonceret aktivering, med kaldesignal og tidspunkt. |
| Din position | En markør. Når din position er mindre præcis end omkring 10 m, viser en stiplet ring usikkerheden. |

:::tip[For mange linjer?]
Slå dem fra under **≡** › **Linjer til spots**. Diana husker valget. **⤢ Vis alle spots** viser alle spots og din egen position på én gang.
:::

Hvorfor nogle referencer er områder og andre prikker: {{link:map/points-and-areas}}.
'''},
'map/area-panel': {'title': 'Oplysninger om et område', 'desc': 'Tryk på et område eller en prik: panelet med alt, hvad Diana ved, og at spotte derfra.', 'body': '''
Tryk på et område, en prik eller et spot på kortet. Et panel glider op nedefra med alt, hvad Diana ved om den reference. Diana viser kun, hvad den faktisk ved: aldrig et tomt felt.

{{img:phone-area-panel|Panel for ONFF-0685 Hobokense Polder med areal, forvalter, betegnelse, IUCN-kategori og locator}}

## Hvad står der i panelet

For et **område med grænse**:

- Reference, region og navn.
- Hvad områdefilen indeholder: **areal** i hektar, **forvalter**, **betegnelse**, **IUCN-kategori**, **udpeget siden**. Ikke alle reservater har det hele; det er et hul i kildedataene, ikke noget Diana skjuler.
- **Antal QSO'er** og **seneste aktivering**, fra WWFF-fortegnelsen.
- **Locator**, **CQ-zone**, **ITU-zone** og **ITU-region**.
- **Mere info**: reservatets hjemmeside, når WWFF-fortegnelsen har en. Den åbner i din browser, så Diana og kortet bliver, hvor de var.

For en **reference uden grænse** (stiplet ring): det samme panel uden arealtallene, og en bemærkning om, at Diana ikke kan afgøre, om du er inde i den.

For en **blå prik** i et andet land: reference, land og navn, locator og zoner, **Fra dig** (retning og afstand), antal QSO'er eller **ATNO** i rødt hvis den aldrig er blevet aktiveret, og Mere info.

## Spot eller annoncér fra panelet

Nederst i hvert panel er der to knapper:

- **Spot dig selv her** åbner spot-formularen med referencen allerede udfyldt. Se {{link:spots/spot-yourself}}.
- **Annoncér en aktivering** åbner agenda-formularen med referencen udfyldt. Se {{link:spots/announce}}.

## Luk panelet

Stryg panelet **nedad**, eller tryk på **×**. Kortet bliver, hvor det er. På en telefon er der kun ét panel forneden ad gangen.
'''},
'map/overlapping-areas': {'title': 'Overlappende områder', 'desc': 'Når referencer ligger oven i hinanden, og hvordan du skifter mellem dem.', 'body': '''
Referencer overlapper nogle gange: et lille reservat ligger ofte inde i et større naturområde. Står du på det stykke jord, er du i dem alle på én gang.

## Hvordan Diana viser det

Diana tegner altid det **mindste** område øverst, så du kan trykke på det. Et tryk åbner det mindste område under din finger: tryk inde i reservatet for reservatet, og i landskabet omkring for det større område.

## Skift til det andet område

1. Tryk på kortet inde i reservatet. Panelet for det **mindste** område åbner.
2. Rul ned i panelet til **"Dette punkt ligger også i disse referencer"**. De andre områder står dér som knapper, med navn og størrelse.
3. Tryk på en knap. Panelet viser nu det område, med sin egen grænse i orange.
4. Tilbage igen? Det panel har en knap til det område, du kom fra.

## Med din GPS-position

Står du i flere områder på én gang, siger infokortet nederst på kortet det, fx *"Du er i 2 områder"*, med afstanden til den nærmeste grænse. Diana åbner så panelet for det mindste område, med de andre som knapper.

:::tip[Hvad det betyder for din aktivering]
Står du i alle disse områder, giver WWFF-reglerne dig lov til at aktivere dem sammen. Læs reglerne i Diana under **Regler**, eller den officielle tekst på wwff.co. Se {{link:rules/wwff-rules}}.
:::

:::caution[Ikke for referencer uden grænse]
En stiplet ring er kun et omtrentligt sted. Dér kan Diana ikke afgøre, om du er inde, og derfor heller ikke vise overlap.
:::
'''},
'map/am-i-inside': {'title': 'Står jeg i området?', 'desc': 'Hvordan Diana fortæller dig, om du er inde, og hvordan du læser nøjagtigheden.', 'body': '''
Et infokort nederst på kortet svarer på det spørgsmål, enhver aktivator har: **står jeg i reservatet?**

## Hvad infokortet siger

- **I ét område**: hvilket, og afstanden til den nærmeste grænse.
- **I flere på én gang** (når områder overlapper): hvor mange, og panelet for det mindste åbner. Se {{link:map/overlapping-areas}}.
- **Udenfor**: det nærmeste område og hvor langt væk det er.

Hvert svar slutter med, hvor god din position var, fx *"position ±6 m"*.

:::note[Områder i flere dele]
Nogle referencer består af adskilte delområder. Panelet siger så, hvor mange. Hele din station skal stå inde i ét af dem.
:::

## Hvorfor det tager et par sekunder

En telefon, der lige har vækket sin GPS, svarer først ud fra wifi og mobilmaster, og den position kan være flere hundrede meter forkert. Derfor bliver Diana ved med at lytte, mens nøjagtigheden bliver bedre, og viser hvad den har indtil videre: *"Skærper positionen… ±380 m"*. Den svarer, så snart positionen er god nok, eller efter tolv sekunder med den bedste, den har fået. Er den stadig grov, siger svaret det.

## Sådan læser du nøjagtigheden

| Nøjagtighed | Hvad det typisk betyder |
|---|---|
| ±10 m eller bedre | Satellitter. Pålidelig, også tæt på en grænse. |
| ±20 til 50 m | Rimelig. Pas på tæt på en grænse. |
| ±100 m eller værre | Wifi eller mobilmaster, ofte indendørs. Ikke godt nok til at være sikker. |

Når usikkerheden er større end omkring 10 m, tegnes en **stiplet ring** om din markør med præcis den radius. En stram ring betyder satellitter; en ring, der dækker hele karreen, betyder at svaret kom fra wifi.

:::tip[Få en bedre position]
Gå udenfor, med åben himmel over dig, og vent et par sekunder. Forbliver den grov på mere end omkring 75 m? Så må webstedet måske kun bruge en omtrentlig placering. En besked foreslår så, at du tjekker placeringsindstillingen: se {{link:help/location-problems}}.
:::

## To fælder Diana holder øje med

- **Indendørs** kommer en wifi-position ofte inden for et sekund og påstår ±20 m. Så præcis tror wifi-databasen selv, den er, ikke den reelle nøjagtighed. Diana svarer, men lytter videre resten af de tolv sekunder og retter svaret om nødvendigt.
- **Telefoner, der lover mere, end de kan.** Diana sammenligner målingerne fra de seneste 45 sekunder. En enkelt vild måling ignoreres. Modsiger målingerne hinanden, siger svaret *"målinger modsiger hinanden"*. At gå tæller ikke som spredning.

:::caution
Diana kan kun svare på dette for områder **med** grænse. For en stiplet ring eller en blå prik kan den ikke. Se {{link:map/points-and-areas}}.
:::
'''},
'map/layers-and-styles': {'title': 'Lag og kortstil', 'desc': 'Slå dele af kortet til og fra, og vælg en kortstil.', 'body': '''
## Lag (≡)

Tryk på **≡** øverst til højre på kortet. Du kan slå disse til og fra:

| Lag | Hvad det viser |
|---|---|
| **Områder** | De grønne områder i dit land. |
| **Referencenumre** | Etiketterne som `ONFF-0602`. |
| **Uden grænse (punkt)** | De stiplede ringe for referencer uden grænse. |
| **Spots på kortet** | Live-spots og annonceringer. De kommer fra WWFF Spotline og opdateres hvert 30. sekund. |
| **Linjer til spots** | De grønne prikkede og orange stiplede linjer fra dig. |
| **Andre WWFF-områder** | De blå prikker i resten af verden. |

I samme menu finder du **⤢ Vis alle spots** og sprogknapperne. Diana husker dine valg.

## Kortstil (◐)

Tryk på **◐** for et andet baggrundskort:

- **Liberty**: standard, med terrænfarver.
- **Positron**: meget lys og rolig, god i stærkt sollys.
- **Bright**: flere farver og detaljer.
- **Dark**: mørk, skånsom for øjnene om natten.

:::tip
I felten, i stærkt sollys, er **Positron** ofte lettest at læse.
:::
'''},
'map/search': {'title': 'Søgning', 'desc': 'Find en reference på navn eller nummer, hvor som helst i verden.', 'body': '''
Tryk på **⌕** øverst på kortet og skriv.

- **Et navn**, fx `Kalmthoutse Heide`.
- **En fuld reference**, fx `ONFF-0012` eller `OZFF-0012`.
- **Kun et nummer**, fx `0012`. Så søger Diana kun i dit eget land.

Alle WWFF-referencer i verden kan findes. Resultater fra det indlæste land står først. Tryk på et resultat: kortet zoomer derhen og åbner dets panel.

:::tip
Søgning virker også offline: listen over referencer ligger på din enhed.
:::
'''},
}
