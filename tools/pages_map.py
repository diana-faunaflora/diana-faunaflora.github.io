PAGES = [
# ------------------------------------------------------------------
{'sec': 'map', 'slug': 'map-screen', 'order': 1,
'en': {'title': 'The map screen', 'desc': 'The main screen of Diana: the buttons at the top and the bar at the bottom.', 'body': '''
The map is the main screen of Diana. Everything else starts from here.

{{img:phone-map|The map of Diana around Antwerp, with green areas, a spot and lines}}

## The bar at the bottom

From left to right: **Map**, **Spots**, **Spot**, **Agenda**, **Field info**, **Rules** and **Settings**. Tap one to open that screen.

:::tip[Back to your own position]
Tap **Map** in the bottom bar at any time: the map centres on where you are again, and the zoom stays as it is. Diana takes a fresh GPS measurement if the last one was older than two minutes or less precise than 30 m. Without GPS it centres on your locator from Settings, and says so.
:::

## The buttons at the top

| Button | What it does |
|---|---|
| **⌕** | Search by name or reference number. See {{link:map/search}}. |
| **◐** | Map style: Liberty, Positron, Bright or Dark. |
| **≡** | Layers and language. See {{link:map/layers-and-styles}}. |

At the top left a line says how many references are loaded, for example *"947 WWFF references · 1 without a boundary"*.

## Moving around

- **Drag** with one finger to move the map.
- **Pinch** with two fingers to zoom in or out, or use **+** and **−** at the right.
- **Tap** an area, a point or a spot to open its panel. See {{link:map/area-panel}}.

## What do I see?

The colours, points and lines are explained in {{link:map/reading-the-map}}. Why one reference is an area and another only a point is explained in {{link:map/points-and-areas}}.
'''},
'nl': {'title': 'Het kaartscherm', 'desc': 'Het hoofdscherm van Diana: de knoppen bovenaan en de balk onderaan.', 'body': '''
De kaart is het hoofdscherm van Diana. Al de rest begint hier.

{{img:phone-map|De kaart van Diana rond Antwerpen, met groene gebieden, een spot en lijnen}}

## De balk onderaan

Van links naar rechts: **Kaart**, **Spots**, **Meld**, **Agenda**, **Veldinfo**, **Regels** en **Instellingen**. Tik erop om dat scherm te openen.

:::tip[Terug naar je eigen positie]
Tik op elk moment onderaan op **Kaart**: de kaart centreert opnieuw op waar je staat, en de zoom blijft zoals hij is. Diana neemt een nieuwe gps-meting als de vorige ouder was dan twee minuten of minder nauwkeurig dan 30 m. Zonder gps centreert ze op je locator uit Instellingen, en ze zegt dat erbij.
:::

## De knoppen bovenaan

| Knop | Wat hij doet |
|---|---|
| **⌕** | Zoeken op naam of referentienummer. Zie {{link:map/search}}. |
| **◐** | Kaartstijl: Liberty, Positron, Bright of Dark. |
| **≡** | Lagen en taal. Zie {{link:map/layers-and-styles}}. |

Linksboven staat hoeveel referenties er ingeladen zijn, bijvoorbeeld *"947 WWFF-referenties · 1 zonder grens"*.

## Bewegen op de kaart

- **Sleep** met één vinger om de kaart te verschuiven.
- **Knijp** met twee vingers om in of uit te zoomen, of gebruik **+** en **−** rechts.
- **Tik** op een gebied, een punt of een spot om het paneel te openen. Zie {{link:map/area-panel}}.

## Wat zie ik?

De kleuren, punten en lijnen staan uitgelegd in {{link:map/reading-the-map}}. Waarom de ene referentie een vlak is en de andere maar een punt, lees je in {{link:map/points-and-areas}}.
'''}},
# ------------------------------------------------------------------
{'sec': 'map', 'slug': 'points-and-areas', 'order': 2,
'en': {'title': 'Points and areas', 'desc': 'Why one reference is a green area and another a blue dot, and how to change that.', 'body': '''
On the map a WWFF reference appears in one of three ways. Which one depends on what Diana knows about it, and on the country you chose.

| What you see | What it means | Can Diana tell whether you are inside? |
|---|---|---|
| **Green area** | A reference with its real boundary, in the country you chose. | Yes |
| **Dashed ring with an orange dot** | A reference of your country without a boundary. Only an approximate spot. | No |
| **Blue dot** | A reference in another country. Close together they form a numbered circle. | No |

## Why an area?

An area needs a boundary file. Diana has those files for **five countries** today: Belgium (ONFF), the Netherlands (PAFF), Germany (DLFF), Denmark (OZFF) and Portugal (CTFF), and more are added all the time. The national WWFF coordinators supply them.

Diana loads the boundaries of **one country at a time**: the one you chose under Settings. That keeps the map fast on a phone.

## Why a dot?

- The reference lies in a country for which Diana has **no boundary file**. Then Diana only knows the position from the WWFF directory.
- Or the country **does** have boundaries in Diana, but it is **not the country you chose**. Then it is shown as a dot too, until you load that country.

## Why a dashed ring?

Within a country with boundaries, a few references have no boundary in the file, for example overseas areas of the Netherlands. They are shown as a dashed ring at the approximate spot.

## You always get the details

Whatever you see, **tap it**: a panel opens with everything Diana knows. For a blue dot that is the reference, country and name, the locator and zones, the bearing and distance from you, the QSO count or **ATNO** when it was never activated, and a link to more information. See {{link:map/area-panel}}.

## When and how to change it

When you go to another country, or want to see the real boundary of a reference that is now a dot:

**From the panel (quickest)**

1. Tap the blue dot.
2. If Diana has the boundaries of that country, the panel says so and shows a button **Show [country] in detail**.
3. Tap it. Diana loads that country and opens the same reference again, now with its boundary.

**From Settings**

1. Tap **Settings** at the bottom right.
2. Under **Your country**, choose the country. Countries marked **With boundaries** get their areas; **Points only** stays dots.
3. The change is immediate. Under the menu Diana says what it loaded, for example *"PAFF, 281 areas with boundaries loaded"*.

Your spots filter (your country or Worldwide) does not change when you pick another country. More in {{link:settings/your-country}}.

:::note[A new reserve as a dot first]
Which references exist comes from the WWFF directory, every night. The boundaries come from a file the Diana team publishes. So a brand-new reserve can appear as a point first and get its outline later.
:::
'''},
'nl': {'title': 'Punten en vlakken', 'desc': 'Waarom de ene referentie een groen vlak is en de andere een blauw bolletje, en hoe je dat aanpast.', 'body': '''
Op de kaart verschijnt een WWFF-referentie op een van drie manieren. Welke hangt af van wat Diana erover weet, en van het land dat je koos.

| Wat je ziet | Wat het betekent | Kan Diana zeggen of je erin staat? |
|---|---|---|
| **Groen vlak** | Een referentie met haar echte grens, in het land dat je koos. | Ja |
| **Stippelring met oranje stip** | Een referentie van jouw land zonder grens. Alleen een benaderde plek. | Nee |
| **Blauw bolletje** | Een referentie in een ander land. Dicht bij elkaar vormen ze een cirkel met een getal. | Nee |

## Waarom een vlak?

Voor een vlak is een grensbestand nodig. Diana heeft zulke bestanden vandaag voor **vijf landen**: België (ONFF), Nederland (PAFF), Duitsland (DLFF), Denemarken (OZFF) en Portugal (CTFF), en er komen er voortdurend bij. De nationale WWFF-coördinatoren leveren ze aan.

Diana laadt de grenzen van **één land tegelijk**: het land dat je koos bij Instellingen. Zo blijft de kaart vlot op een gsm.

## Waarom een bolletje?

- De referentie ligt in een land waarvoor Diana **geen grensbestand** heeft. Dan kent Diana alleen de positie uit de WWFF-directory.
- Of het land **heeft** wel grenzen in Diana, maar het is **niet het land dat je koos**. Dan zie je ook een bolletje, tot je dat land inlaadt.

## Waarom een stippelring?

Binnen een land met grenzen hebben enkele referenties geen grens in het bestand, bijvoorbeeld overzeese gebieden van Nederland. Die zie je als een stippelring op de benaderde plek.

## De details krijg je altijd

Wat je ook ziet, **tik erop**: er opent een paneel met alles wat Diana weet. Voor een blauw bolletje is dat de referentie, het land en de naam, de locator en zones, richting en afstand vanaf jou, het aantal QSO’s of **ATNO** als ze nog nooit geactiveerd werd, en een link naar meer informatie. Zie {{link:map/area-panel}}.

## Wanneer en hoe pas je het aan

Als je naar een ander land gaat, of de echte grens wil zien van een referentie die nu een bolletje is:

**Vanuit het paneel (het snelst)**

1. Tik op het blauwe bolletje.
2. Heeft Diana de grenzen van dat land, dan zegt het paneel dat en toont het een knop **Toon [land] in detail**.
3. Tik erop. Diana laadt dat land en opent dezelfde referentie opnieuw, nu met haar grens.

**Vanuit Instellingen**

1. Tik rechtsonder op **Instellingen**.
2. Kies onder **Jouw land** het land. Landen met **Met grenzen** krijgen hun vlakken; **Alleen punten** blijft bolletjes.
3. De wijziging gaat meteen in. Onder de keuzelijst zegt Diana wat ze inlaadde, bijvoorbeeld *"PAFF, 281 gebieden met grenzen ingeladen"*.

Je spotfilter (jouw land of Wereldwijd) verandert niet als je een ander land kiest. Meer in {{link:settings/your-country}}.

:::note[Een nieuw reservaat eerst als bolletje]
Welke referenties er bestaan, komt elke nacht uit de WWFF-directory. De grenzen komen uit een bestand dat het Diana-team publiceert. Een gloednieuw reservaat kan dus eerst als punt verschijnen en later zijn omtrek krijgen.
:::
'''}},
# ------------------------------------------------------------------
{'sec': 'map', 'slug': 'reading-the-map', 'order': 3,
'en': {'title': 'Reading the map', 'desc': 'What every colour, point and line on the map means.', 'body': '''
Everything on the map has a meaning. This is the legend.

{{img:map-legend|Map around Antwerp and Roosendaal with green areas, blue clusters, a green dotted line and an orange dashed line}}

## Areas and references

| What you see | Meaning |
|---|---|
| Green area with a number | A reference with its real boundary, in your country. The number is the reference, for example `ONFF-0602`. |
| Orange outline | The area you just tapped. |
| Dashed ring with an orange dot | A reference of your country without a boundary: an approximate spot. |
| Blue dot | A reference in another country. |
| Blue circle with a number | Several blue dots close together. Tap it to zoom in; it splits apart. |
| Grey line | A country border on the base map. |

From zoom level 11 every dot gets its reference as a label.

## Spots and announcements

| What you see | Meaning |
|---|---|
| Green pulsing antenna icon | A station on the air now, with callsign, frequency and mode next to it. |
| **Green dotted line** | From you to a station that is on the air now. |
| Faded spot | A spot older than 30 minutes. |
| White dot with an orange ring | An announced activation from the agenda. |
| **Orange dashed line** | From you to an announced activation, labelled with callsign and time. |
| Your position | A marker. When your position is less precise than about 10 m, a dashed ring shows the margin. |

:::tip[Too many lines?]
Switch them off under **≡** › **Lines to the spots**. Diana remembers the choice. **⤢ Fit all spots** frames all spots and your own position at once.
:::

Why some references are areas and others dots: {{link:map/points-and-areas}}.
'''},
'nl': {'title': 'De kaart lezen', 'desc': 'Wat elke kleur, elk punt en elke lijn op de kaart betekent.', 'body': '''
Alles op de kaart heeft een betekenis. Dit is de legende.

{{img:map-legend|Kaart rond Antwerpen en Roosendaal met groene gebieden, blauwe groepjes, een groene stippellijn en een oranje streepjeslijn}}

## Gebieden en referenties

| Wat je ziet | Betekenis |
|---|---|
| Groen vlak met een nummer | Een referentie met haar echte grens, in jouw land. Het nummer is de referentie, bijvoorbeeld `ONFF-0602`. |
| Oranje rand | Het gebied dat je net aantikte. |
| Stippelring met oranje stip | Een referentie van jouw land zonder grens: een benaderde plek. |
| Blauw bolletje | Een referentie in een ander land. |
| Blauwe cirkel met een getal | Meerdere blauwe bolletjes dicht bij elkaar. Tik erop om in te zoomen; ze vallen uiteen. |
| Grijze lijn | Een landsgrens op de basiskaart. |

Vanaf zoomniveau 11 krijgt elk bolletje zijn referentie als label.

## Spots en aankondigingen

| Wat je ziet | Betekenis |
|---|---|
| Groen pulserend antenne-icoon | Een station dat nu in de lucht is, met roepnaam, frequentie en mode ernaast. |
| **Groene stippellijn** | Van jou naar een station dat nu in de lucht is. |
| Vervaagde spot | Een spot ouder dan 30 minuten. |
| Wit bolletje met oranje rand | Een aangekondigde activatie uit de agenda. |
| **Oranje streepjeslijn** | Van jou naar een aangekondigde activatie, met roepnaam en uur. |
| Jouw positie | Een markering. Is je positie minder nauwkeurig dan ongeveer 10 m, dan toont een stippelring de marge. |

:::tip[Te veel lijnen?]
Zet ze uit onder **≡** › **Lijnen naar de spots**. Diana onthoudt je keuze. **⤢ Alle spots in beeld** zet alle spots en je eigen positie in één keer in beeld.
:::

Waarom sommige referenties vlakken zijn en andere bolletjes: {{link:map/points-and-areas}}.
'''}},
# ------------------------------------------------------------------
{'sec': 'map', 'slug': 'area-panel', 'order': 4,
'en': {'title': 'Area details', 'desc': 'Tap an area or point: the panel with everything Diana knows, and spotting from there.', 'body': '''
Tap an area, a dot or a spot on the map. A panel slides up from the bottom with everything Diana knows about that reference. Diana shows only what it really knows: never an empty box.

{{img:phone-area-panel|Panel of ONFF-0685 Hobokense Polder with area, manager, designation, IUCN category and locator}}

## What is in the panel

For an **area with a boundary**:

- Reference, region and name.
- What the area file carries: **area** in hectares, **managed by**, **designation**, **IUCN category**, **designated since**. Not every reserve has all of these; that is a gap in the source data, not something Diana hides.
- The **QSO count** and **last activation**, from the WWFF directory.
- The **locator**, **CQ zone**, **ITU zone** and **ITU region**.
- **More info**: the reserve’s website, when the WWFF directory has one. It opens in your browser, so Diana and the map stay where they were.

For a **reference without a boundary** (dashed ring): the same panel without the area figures, and a note that Diana cannot tell whether you are inside it.

For a **blue dot** in another country: reference, country and name, locator and zones, **From you** (bearing and distance), the QSO count or **ATNO** in red when it was never activated, and More info.

## Spot or announce from the panel

At the bottom of every panel are two buttons:

- **Spot yourself here** opens the spot form with the reference already filled in. See {{link:spots/spot-yourself}}.
- **Announce an activation** opens the agenda form with the reference filled in. See {{link:spots/announce}}.

## Closing the panel

Swipe the panel **down**, or tap **×**. The map stays where it is. On a phone, one bottom panel is visible at a time.
'''},
'nl': {'title': 'Info over een gebied', 'desc': 'Tik een gebied of punt aan: het paneel met alles wat Diana weet, en van daaruit spotten.', 'body': '''
Tik op een gebied, een bolletje of een spot op de kaart. Onderaan schuift een paneel open met alles wat Diana over die referentie weet. Diana toont alleen wat ze echt weet: nooit een leeg vak.

{{img:phone-area-panel|Paneel van ONFF-0685 Hobokense Polder met oppervlakte, beheerder, aanduiding, IUCN-categorie en locator}}

## Wat er in het paneel staat

Voor een **gebied met grens**:

- Referentie, regio en naam.
- Wat het gebiedsbestand meegeeft: **oppervlakte** in hectare, **beheerder**, **aanduiding**, **IUCN-categorie**, **aangeduid sinds**. Niet elk reservaat heeft dat allemaal; dat is een gat in de brongegevens, niet iets wat Diana verbergt.
- Het **aantal QSO’s** en de **laatste activatie**, uit de WWFF-directory.
- De **locator**, **CQ-zone**, **ITU-zone** en **ITU-regio**.
- **Meer info**: de website van het reservaat, als de WWFF-directory er een heeft. Die opent in je browser, zodat Diana en de kaart blijven waar ze waren.

Voor een **referentie zonder grens** (stippelring): hetzelfde paneel zonder de oppervlaktecijfers, met de melding dat Diana niet kan zeggen of je erbinnen staat.

Voor een **blauw bolletje** in een ander land: referentie, land en naam, locator en zones, **Vanaf jou** (richting en afstand), het aantal QSO’s of **ATNO** in het rood als ze nog nooit geactiveerd werd, en Meer info.

## Spotten of aankondigen vanuit het paneel

Onderaan elk paneel staan twee knoppen:

- **Meld jezelf actief** opent het spotformulier met de referentie al ingevuld. Zie {{link:spots/spot-yourself}}.
- **Activatie aankondigen** opent het agendaformulier met de referentie ingevuld. Zie {{link:spots/announce}}.

## Het paneel sluiten

Veeg het paneel naar **beneden**, of tik op **×**. De kaart blijft waar ze is. Op een gsm zie je één paneel tegelijk.
'''}},
# ------------------------------------------------------------------
{'sec': 'map', 'slug': 'overlapping-areas', 'order': 5,
'en': {'title': 'Overlapping areas', 'desc': 'When references lie on top of each other, and how to switch between them.', 'body': '''
References sometimes overlap: a small reserve often lies inside a larger nature area. Standing on that piece of ground, you are in all of them at once.

## How Diana shows it

Diana always draws the **smallest** area on top, so you can tap it. A tap opens the smallest area under your finger: tap inside the reserve for the reserve, and in the land around it for the larger area.

## Switching to the other area

1. Tap the map inside the reserve. The panel of the **smallest** area opens.
2. Scroll down in the panel to **"This point is also inside these references"**. The other areas are listed there as buttons, with name and size.
3. Tap a button. The panel now shows that area, with its own boundary in orange.
4. Going back? That panel has a button to the area you came from.

## With your GPS position

If you stand in several areas at once, the card at the bottom of the map says so, for example *"You are inside 2 references"*, with the distance to the nearest boundary. Diana then opens the panel of the smallest area, with the others as buttons.

:::tip[What this means for your activation]
If you are in all those areas, the WWFF rules let you activate them together. Read the rules in Diana under **Rules**, or the official text on wwff.co. See {{link:rules/wwff-rules}}.
:::

:::caution[Not for references without a boundary]
A dashed ring is only an approximate spot. There Diana cannot tell whether you are inside, so it cannot show overlap either.
:::
'''},
'nl': {'title': 'Overlappende gebieden', 'desc': 'Wanneer referenties over elkaar liggen, en hoe je tussen beide wisselt.', 'body': '''
Referenties liggen soms over elkaar: een klein reservaat ligt vaak binnen een groter natuurgebied. Sta je op dat stuk grond, dan sta je in allemaal tegelijk.

## Hoe Diana het toont

Diana tekent het **kleinste** gebied altijd bovenaan, zodat je het kan aantikken. Een tik opent het kleinste gebied onder je vinger: tik binnen het reservaat voor het reservaat, en in het land eromheen voor het grotere gebied.

## Naar het andere gebied gaan

1. Tik op de kaart binnen het reservaat. Het paneel van het **kleinste** gebied opent.
2. Scroll in het paneel naar **"Dit punt ligt ook in deze referenties"**. Daar staan de andere gebieden als knoppen, met naam en oppervlakte.
3. Tik op een knop. Het paneel toont nu dat gebied, met zijn eigen grens in het oranje.
4. Terug? In dat paneel staat een knop naar het gebied waar je vandaan kwam.

## Met je gps-positie

Sta je in meerdere gebieden tegelijk, dan zegt de kaart onderaan dat, bijvoorbeeld *"Je staat in 2 gebieden"*, met de afstand tot de dichtste grens. Diana opent dan het paneel van het kleinste gebied, met de andere als knoppen.

:::tip[Wat dit betekent voor je activatie]
Sta je in al die gebieden, dan mag je ze volgens de WWFF-regels samen activeren. Lees de regels in Diana onder **Regels**, of de officiële tekst op wwff.co. Zie {{link:rules/wwff-rules}}.
:::

:::caution[Niet bij referenties zonder grens]
Een stippelring is alleen een benaderde plek. Daar kan Diana niet zeggen of je binnen staat, en dus ook geen overlap tonen.
:::
'''}},
# ------------------------------------------------------------------
{'sec': 'map', 'slug': 'am-i-inside', 'order': 6,
'en': {'title': 'Am I inside the area?', 'desc': 'How Diana tells you whether you are inside, and how to read the accuracy.', 'body': '''
A card at the bottom of the map answers the question every activator has: **am I inside the reserve?**

## What the card says

- **Inside one area**: which one, and the distance to the nearest boundary.
- **Inside several at once** (when areas overlap): how many, and the panel of the smallest one opens. See {{link:map/overlapping-areas}}.
- **Outside**: the nearest area and how far it is.

Every answer ends with how good your position was, for example *"position ±6 m"*.

:::note[Areas made of several parcels]
Some references consist of separate parcels. The panel then says how many. Your whole station must stand inside one of them.
:::

## Why it takes a few seconds

A phone that has just woken its GPS first answers from wifi and cell masts, and that position can be hundreds of metres out. So Diana keeps listening while the accuracy improves, and shows what it has so far: *"Sharpening the fix… ±380 m"*. It answers once the position is good enough, or after twelve seconds with the best one it got. If that one is still rough, the answer says so.

## Reading the accuracy

| Accuracy | What it usually means |
|---|---|
| ±10 m or better | Satellites. Reliable, also close to a boundary. |
| ±20 to 50 m | Reasonable. Careful close to a boundary. |
| ±100 m or worse | Wifi or cell masts, often indoors. Not good enough to be sure. |

When the margin is larger than about 10 m, a **dashed ring** is drawn around your marker at exactly that radius. A tight ring means satellites; a ring covering the whole block means the answer came from wifi.

:::tip[Getting a better position]
Go outside, with open sky above you, and wait a few seconds. Stays it rough at more than about 75 m? Then the site may only use an approximate location. A banner then suggests checking the location setting: see {{link:help/location-problems}}.
:::

## Two traps Diana watches for

- **Indoors**, a wifi position often arrives within a second claiming ±20 m. That is how accurate the wifi database believes itself to be, not the real accuracy. Diana answers, but keeps listening for the rest of the twelve seconds and corrects the answer if needed.
- **Phones that claim more than they can do.** Diana compares the readings of the last 45 seconds. A single wild reading is ignored. If the readings contradict each other, the answer says *"readings contradict each other"*. Walking is not counted as scatter.

:::caution
Diana can only answer this for areas **with** a boundary. For a dashed ring or a blue dot it cannot tell. See {{link:map/points-and-areas}}.
:::
'''},
'nl': {'title': 'Sta ik in het gebied?', 'desc': 'Hoe Diana zegt of je binnen staat, en hoe je de nauwkeurigheid leest.', 'body': '''
Een kaart onderaan de kaart beantwoordt de vraag die elke activator heeft: **sta ik in het reservaat?**

## Wat de kaart zegt

- **In één gebied**: welk, en de afstand tot de dichtste grens.
- **In meerdere tegelijk** (als gebieden overlappen): hoeveel, en het paneel van het kleinste opent. Zie {{link:map/overlapping-areas}}.
- **Erbuiten**: het dichtstbijzijnde gebied en hoe ver het is.

Elk antwoord eindigt met hoe goed je positie was, bijvoorbeeld *"positie ±6 m"*.

:::note[Gebieden uit meerdere percelen]
Sommige referenties bestaan uit losse percelen. Het paneel zegt dan hoeveel. Je volledige station moet binnen één ervan staan.
:::

## Waarom het een paar seconden duurt

Een gsm die net zijn gps wakker maakt, antwoordt eerst vanuit wifi en gsm-masten, en die positie kan honderden meter afwijken. Daarom blijft Diana luisteren terwijl de nauwkeurigheid beter wordt, en toont ze wat ze al heeft: *"Scherpstellen… ±380 m"*. Ze antwoordt zodra de positie goed genoeg is, of na twaalf seconden met de beste die ze kreeg. Is die nog altijd ruw, dan zegt het antwoord dat.

## De nauwkeurigheid lezen

| Nauwkeurigheid | Wat het meestal betekent |
|---|---|
| ±10 m of beter | Satellieten. Betrouwbaar, ook dicht bij een grens. |
| ±20 tot 50 m | Redelijk. Opletten dicht bij een grens. |
| ±100 m of slechter | Wifi of gsm-masten, vaak binnenshuis. Niet goed genoeg om zeker te zijn. |

Is de marge groter dan ongeveer 10 m, dan tekent Diana een **stippelring** rond je markering, precies met die straal. Een kleine ring betekent satellieten; een ring over het hele huizenblok betekent dat het antwoord van wifi kwam.

:::tip[Een betere positie krijgen]
Ga naar buiten, met vrije hemel boven je, en wacht een paar seconden. Blijft het ruw, boven ongeveer 75 m? Dan mag de site waarschijnlijk alleen een benaderde locatie gebruiken. Een melding stelt dan voor om de locatie-instelling na te kijken: zie {{link:help/location-problems}}.
:::

## Twee valkuilen waar Diana op let

- **Binnenshuis** komt een wifi-positie vaak binnen één seconde binnen met ±20 m. Zo nauwkeurig denkt de wifi-databank zelf te zijn, niet de echte nauwkeurigheid. Diana antwoordt, maar blijft de rest van de twaalf seconden luisteren en past het antwoord aan als het moet.
- **Gsm’s die meer beloven dan ze kunnen.** Diana vergelijkt de metingen van de laatste 45 seconden. Eén wilde meting wordt genegeerd. Spreken de metingen elkaar tegen, dan zegt het antwoord *"metingen spreken elkaar tegen"*. Wandelen telt niet als spreiding.

:::caution
Diana kan dit alleen beantwoorden voor gebieden **met** een grens. Bij een stippelring of een blauw bolletje kan ze het niet zeggen. Zie {{link:map/points-and-areas}}.
:::
'''}},
# ------------------------------------------------------------------
{'sec': 'map', 'slug': 'layers-and-styles', 'order': 7,
'en': {'title': 'Layers and map style', 'desc': 'Switch parts of the map on and off, and pick a map style.', 'body': '''
## Layers (≡)

Tap **≡** at the top right of the map. You can switch these on and off:

| Layer | What it shows |
|---|---|
| **Reference areas** | The green areas of your country. |
| **Reference numbers** | The labels such as `ONFF-0602`. |
| **No boundary (point)** | The dashed rings of references without a boundary. |
| **Spots on the map** | Live spots and announcements. They come from WWFF Spotline and refresh every 30 seconds. |
| **Lines to the spots** | The green dotted and orange dashed lines from you. |
| **Other WWFF areas** | The blue dots of the rest of the world. |

The same menu holds **⤢ Fit all spots** and the language buttons. Diana remembers your choices.

## Map style (◐)

Tap **◐** for another base map:

- **Liberty**: the default, with terrain colours.
- **Positron**: very light and calm, good in bright sunlight.
- **Bright**: more colour and detail.
- **Dark**: dark, easy on the eyes at night.

:::tip
In the field, in strong sunlight, **Positron** is often the easiest to read.
:::
'''},
'nl': {'title': 'Lagen en kaartstijl', 'desc': 'Delen van de kaart aan- en uitzetten, en een kaartstijl kiezen.', 'body': '''
## Lagen (≡)

Tik rechtsboven op de kaart op **≡**. Dit kan je aan- en uitzetten:

| Laag | Wat ze toont |
|---|---|
| **Natuurgebieden** | De groene vlakken van jouw land. |
| **Referentienummers** | De labels zoals `ONFF-0602`. |
| **Zonder grens (punt)** | De stippelringen van referenties zonder grens. |
| **Spots op de kaart** | Live spots en aankondigingen. Ze komen van WWFF Spotline en verversen elke 30 seconden. |
| **Lijnen naar de spots** | De groene stippellijnen en oranje streepjeslijnen vanaf jou. |
| **Andere WWFF-gebieden** | De blauwe bolletjes van de rest van de wereld. |

In hetzelfde menu staan **⤢ Alle spots in beeld** en de taalknoppen. Diana onthoudt je keuzes.

## Kaartstijl (◐)

Tik op **◐** voor een andere basiskaart:

- **Liberty**: de standaard, met terreinkleuren.
- **Positron**: heel licht en rustig, goed in fel zonlicht.
- **Bright**: meer kleur en detail.
- **Dark**: donker, rustig voor de ogen ’s nachts.

:::tip
In het veld, in fel zonlicht, leest **Positron** vaak het makkelijkst.
:::
'''}},
# ------------------------------------------------------------------
{'sec': 'map', 'slug': 'search', 'order': 8,
'en': {'title': 'Searching', 'desc': 'Find a reference by name or number, anywhere in the world.', 'body': '''
Tap **⌕** at the top of the map and type.

- **A name**, for example `Kalmthoutse Heide`.
- **A full reference**, for example `ONFF-0012` or `DLFF-0210`.
- **Only a number**, for example `0012`. Then Diana looks only in your own country.

Every WWFF reference worldwide can be found. Results from the country you loaded come first. Tap a result: the map zooms to it and opens its panel.

:::tip
Searching works offline too: the list of references is on your device.
:::
'''},
'nl': {'title': 'Zoeken', 'desc': 'Een referentie vinden op naam of nummer, overal ter wereld.', 'body': '''
Tik bovenaan de kaart op **⌕** en typ.

- **Een naam**, bijvoorbeeld `Kalmthoutse Heide`.
- **Een volledige referentie**, bijvoorbeeld `ONFF-0012` of `DLFF-0210`.
- **Alleen een nummer**, bijvoorbeeld `0012`. Dan zoekt Diana alleen in je eigen land.

Elke WWFF-referentie ter wereld is te vinden. Resultaten uit het land dat je inlaadde, komen eerst. Tik op een resultaat: de kaart zoomt erheen en opent het paneel.

:::tip
Zoeken werkt ook offline: de lijst met referenties staat op je toestel.
:::
'''}},
]
