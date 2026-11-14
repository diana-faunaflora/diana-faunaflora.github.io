T = {
'help/location-problems': {'title': 'Problemer med placering', 'desc': 'Ingen position, eller en position der forbliver grov: hvad du tjekker, pr. enhed.', 'body': '''
Diana beder altid om den mest præcise position, din enhed kan give. Om et websted får den præcise position eller en bevidst sløret position, er en indstilling på din telefon eller i din browser, ikke i Diana.

## Først: prøv udenfor

Indendørs giver wifi alene ofte omkring ±100 m. Gå udenfor, med åben himmel over dig, vent ti sekunder og tryk på **Kort** i bjælken nederst. Ofte er det nok.

## Stadig grov eller ingen position? Tjek indstillingen

**Android med Chrome**

1. Åbn appen **Indstillinger** på din telefon.
2. Gå til **Apps** › **Chrome** › **Tilladelser** › **Placering**.
3. Vælg **Tillad kun, mens appen er i brug** og slå **Brug præcis placering** til.
4. Tjek også selve webstedet: tryk i Chrome på ikonet til venstre for adresselinjen › **Tilladelser** › **Placering**: tilladt.

**iPhone eller iPad med Safari**

1. Åbn appen **Indstillinger**.
2. Gå til **Anonymitet & sikkerhed** › **Lokalitetstjenester** › **Safari-websteder**.
3. Vælg **Når appen er i brug** og slå **Præcis lokalitet** til.

**iPhone eller iPad med en anden browser** (fx Chrome)

1. Åbn appen **Indstillinger**.
2. Gå til **Anonymitet & sikkerhed** › **Lokalitetstjenester** › din browser.
3. Vælg **Når appen er i brug** og slå **Præcis lokalitet** til.

**Computer**

Klik på låseikonet ved adresselinjen og tillad **Placering** for dette websted. En bærbar får sin position fra wifi og er sjældent bedre end omkring ±50 m.

## "Placering er blokeret for dette websted"

Du (eller nogen) har tidligere sagt nej. Diana kan ikke spørge igen: kun du kan tillade det, i browserens eller telefonens indstillinger ovenfor. Genindlæs derefter Diana.

## Uden placering

Diana virker også uden placering. Udfyld din locator under **Indstillinger** › **Din station**. Afstande og linjer regnes så fra midten af dit locator-felt. Kun *står jeg i området* kræver virkelig en præcis position.

Se også {{link:map/am-i-inside}}.
'''},
'help/scripts-blocked': {'title': 'Fast på startskærmen', 'desc': 'Script-blokeringer og strikse browsere: hvad Diana har brug for, og intet mere.', 'body': '''
Diana er en web-app: uden JavaScript kører intet. Stopper en blokering scriptsene, bliver Diana på startskærmen. Efter et stykke tid dukker der en boks op dér, der siger det.

## Løsning

1. Tillad kun scripts for **diana-onff.github.io**. Ikke `github.io` og ikke `github.com`: Diana har ikke brug for nogen af dem.
2. **Genindlæs siden**: **F5** eller **Ctrl+R** (Mac: **Cmd+R**). På en telefon trækker du siden ned eller trykker på genindlæs. Uden at genindlæse bliver den gamle blokering stående, også efter du har klikket på "Stol på".
3. Stadig fast? En anden udvidelse kan også blokere (en annonceblokering, en privatlivsudvidelse). Slå dem fra én ad gangen for dette websted.
4. Starter Diana, men kortet forbliver tomt? Tillad `blob:`-workers for diana-onff.github.io (se nedenfor).

## Hvad Diana indlæser

**Scripts**: alle fra diana-onff.github.io selv.

| Fil | Hvad det er |
|---|---|
| `vendor/maplibre-gl.js` | MapLibre, kortbiblioteket. En kopi på Dianas eget websted, ikke fra et CDN. |
| `js/*.js` | Dianas egen kode. |
| `sw.js` | Service workeren, der holder Diana kørende offline. |

Ingen inline-scripts og ingen `eval`. Én undtagelse, kun med dit samtykke: har du sagt ja til statistik, Umami-scriptet fra `cloud.umami.is`.

**Kort-worker**: MapLibre tegner kortet i en baggrunds-worker, der startes fra en `blob:`-adresse. En blokering, der afviser `blob:`-workers, lader Diana starte, men kortet forbliver blankt.

**Data**:

| Vært | Hvorfor |
|---|---|
| `tiles.openfreemap.org` | Kortfliser og skrifttyper til etiketter |
| `spots.wwff.co` | Live-spots og agenda |
| `diana-spotline.diana-onff.workers.dev` | Kun når du sender et spot eller en annoncering |
| `raw.githubusercontent.com` | Rumvejr til Forhold |
| `cloud.umami.is` | Kun hvis du har sagt ja til statistik |

Din position sendes aldrig nogen steder hen.
'''},
'help/updates': {'title': 'Opdateringer', 'desc': 'Hvordan Diana opdaterer sig selv, og hvad du gør, hvis en ny version ikke dukker op.', 'body': '''
Diana opdaterer sig selv. Du skal aldrig downloade noget.

## Sådan virker det

- **Dataene** (referencer, antal QSO'er, grænser) opdateres hver nat. Diana henter dem friske ved hver start og bruger kopien på din telefon, når dækningen er svag.
- **Selve appen**: når du åbner Diana med dækning, ser den efter en ny version. En ny version annonceres kun, når der virkelig er en.

## Dukker en ny version ikke op?

1. Sørg for, at du har dækning.
2. Åbn **Indstillinger** og tryk på **Søg efter opdateringer** nederst.
3. Sammenlign versionslinjen med den i **Nyheder**. Se {{link:settings/version-and-updates}}.
4. Stadig den gamle version? Luk Diana helt (stryg den væk fra dine seneste apps) og åbn den igen.

:::note
Appens versioner står i **Nyheder**, den nyeste øverst, på hollandsk og engelsk.
:::
'''},
'help/data-and-limits': {'title': 'Dine data og begrænsningerne', 'desc': 'Hvad der bliver på din enhed, hvorfor intet synkroniseres, og hvad Diana ikke kan.', 'body': '''
## Alt bliver på én enhed, i én browser

Dine kaldesignaler, locator, land, hurtige ord, sprog, valg om statistik og PIN-koderne til dine annonceringer ligger i den lokale lagring i den ene browser. Intet synkroniseres.

- Bruger du Diana på din telefon og på din bærbare? Sæt den op på begge. Der er ingen konto til at forbinde dem.
- **At rydde browserdata** (historik, cookies og webstedsdata), at bruge et **privat vindue** eller at **fjerne den installerede app** sletter disse indstillinger. Diana starter så forfra ved velkomstskærmen.

:::caution[PIN-koderne til dine annonceringer]
De ligger i den samme lagring. Ryd browseren, og de er væk. Skriv vigtige PIN-koder ned et andet sted også.
:::

## Hvad Diana ikke kan

- **Live-data afhænger af andre.** Spots og agenda kommer fra WWFF Spotline. Er den nede, siger Spots-skærmen det. Udbredelsesforholdene kommer fra NOAA; fanen siger, hvor gamle de er.
- **Grænser findes kun, hvor der er leveret en fil**: i dag fem lande. Andre steder er referencer punkter, og Diana kan ikke afgøre, om du er inde. Se {{link:map/points-and-areas}}.
- **Ikke alle reservater har fulde oplysninger.** Mange har kun et navn og en reference. Det er et hul i kildedataene.
- **Diana logger ikke** og uploader ikke logs. Det bliver hos dit eget logprogram og WWFF.

## Brug af dataene

Grænserne og aktiveringstallene kommer fra WWFF-programmerne, WDPA, offentlige kilder og WWFF Spotline, og forbliver deres ejeres data. Se {{link:about/data-sources}}.
'''},
'help/faq': {'title': 'Ofte stillede spørgsmål', 'desc': 'Korte svar på de spørgsmål, der oftest dukker op.', 'body': '''
## Koster Diana noget?

Nej. Diana er gratis, uden reklamer og uden konto.

## Er Diana en officiel WWFF-app?

Nej. Diana er et frivilligt projekt, der støtter WWFF-hobbyen. Den bruger WWFF's offentlige tjenester, som Spotline og fortegnelsen.

## Sender Diana min position nogen steder hen?

Nej. Din position bruges kun på din egen skærm. Et spot sender dit kaldesignal, frekvens, mode, reference og bemærkning, aldrig din position. Se {{link:start/privacy}}.

## Virker Diana uden dækning?

Ja, med de senest indlæste data: det kort, du allerede har set, referencerne, Feltinfo Placering og båndplanen. Live-spots og at sende et spot kræver dækning.

## Hvorfor er min reference et punkt og ikke et område?

Fordi Diana ikke har en grænse for den, eller fordi den ligger i et andet land end det, du har indlæst. Se {{link:map/points-and-areas}}.

## Kan jeg logge i Diana?

Nej. Diana hjælper før og under aktiveringen. Din log bliver i dit logprogram. Under **Regler** viser Diana det rigtige filnavn.

## Mine indstillinger er væk. Hvad skete der?

Browserdataene blev ryddet, appen blev fjernet, eller du brugte et privat vindue. Se {{link:help/data-and-limits}}.

## Kan mit nationale program også få grænser?

Ja. Den nationale koordinator sender områdefilen (KMZ) til Diana-holdet. Mere i {{link:about/about-diana}}.

## Jeg har fundet en fejl. Hvor melder jeg den?

Kontaktoplysningerne står på privatlivssiden i appen (**Indstillinger** › **Privatliv**). Nævn din versionslinje: {{link:settings/version-and-updates}}.
'''},
}
