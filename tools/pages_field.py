PAGES = [
# ------------------------------------------------------------------
{'sec': 'field-info', 'slug': 'overview', 'order': 1,
'en': {'title': 'Field info', 'desc': 'Everything about the place where you are, in three tabs.', 'body': '''
**Field info** is about the place where you are standing. It has three tabs:

| Tab | What it shows |
|---|---|
| **Areas** | The WWFF references around you. See {{link:field-info/areas-nearby}}. |
| **Location** | Where you are in radio terms: time, locator, zones. See {{link:field-info/location}}. |
| **Conditions** | Space weather and what it means for the bands. See {{link:field-info/conditions-space-weather}} and {{link:field-info/conditions-bands}}. |

## Opening Field info

1. Tap **Field info** in the bottom bar (the circle with a dot).
2. Tap the tab you want at the top: **Areas**, **Location** or **Conditions**.
3. Under the title, check where Diana starts from: *"from your GPS position"* or *"from your locator JO21EE"*.

:::caution[No position?]
If you see *"Diana does not know where you are yet"*, allow location (see {{link:start/welcome-screen}}) or fill in your locator under **Settings** › **Your station**. With only a locator, Diana works from the centre of that square, which can be a few kilometres off.
:::
'''},
'nl': {'title': 'Veldinfo', 'desc': 'Alles over de plek waar je staat, in drie tabbladen.', 'body': '''
**Veldinfo** gaat over de plek waar je staat. Er zijn drie tabbladen:

| Tabblad | Wat het toont |
|---|---|
| **Gebieden** | De WWFF-referenties rond je. Zie {{link:field-info/areas-nearby}}. |
| **Locatie** | Waar je staat in radiotermen: tijd, locator, zones. Zie {{link:field-info/location}}. |
| **Condities** | Ruimteweer en wat het betekent voor de banden. Zie {{link:field-info/conditions-space-weather}} en {{link:field-info/conditions-bands}}. |

## Veldinfo openen

1. Tik onderaan op **Veldinfo** (het rondje met de stip).
2. Tik bovenaan op het tabblad dat je wil: **Gebieden**, **Locatie** of **Condities**.
3. Kijk onder de titel van waar Diana vertrekt: *"vanaf je GPS-positie"* of *"vanaf je locator JO21EE"*.

:::caution[Geen positie?]
Zie je *"Diana weet nog niet waar je bent"*, sta dan locatie toe (zie {{link:start/welcome-screen}}) of vul je locator in bij **Instellingen** › **Jouw station**. Met alleen een locator rekent Diana vanaf het midden van dat vak, en dat kan enkele kilometers afwijken.
:::
'''}},
# ------------------------------------------------------------------
{'sec': 'field-info', 'slug': 'areas-nearby', 'order': 2,
'en': {'title': 'Areas nearby', 'desc': 'The WWFF references around you, sorted the way you want.', 'body': '''
The **Areas** tab lists the WWFF references around your position, within the distance you chose in Settings (10, 25, 50 or 100 km). References across the border are in it too.

{{img:phone-field-areas|Field info, Areas tab, with references near Antwerp sorted by distance}}

## One line per reference

| What you see | Meaning |
|---|---|
| Reference and name | For example `ONFF-0842 · Boshoek`. |
| Distance and bearing | In a straight line from you, for example `1.5 km · 62°`. |
| QSO count | How many contacts were made from there, according to the WWFF directory. |
| Last active | The date of the last activation. |
| *no activation date known* | The directory has a reference but no date. |
| *not in the WWFF directory* | Diana knows the area, but the directory has nothing on it. That does not mean it was never activated. |

## Sorting: which order to choose?

| Button | When to use it |
|---|---|
| **Distance** | The nearest first. When you want to set up quickly. |
| **Last active** | The areas that were off the air the longest first. That is where a pile-up is most likely. |
| **QSO count** | The least worked areas first. When you want to give hunters a new one. |

## Opening an area

1. Tap a line.
2. The map opens, zoomed in on that area, with its panel and boundary.
3. More than a hundred areas nearby? Tap **Show more** at the bottom.

## Changing the distance

**Settings** › **Field info** › 10, 25, 50 or 100 km. See {{link:settings/field-info-distance}}.

:::note
The QSO counts and dates come from the WWFF directory, refreshed every night. Where the directory has nothing, the screen says so rather than calling it "never activated".
:::
'''},
'nl': {'title': 'Gebieden in de buurt', 'desc': 'De WWFF-referenties rond je, gesorteerd zoals jij wil.', 'body': '''
Het tabblad **Gebieden** toont de WWFF-referenties rond je positie, binnen de afstand die je bij Instellingen koos (10, 25, 50 of 100 km). Ook referenties over de grens staan erin.

{{img:phone-field-areas|Veldinfo, tabblad Gebieden, met referenties bij Antwerpen gesorteerd op afstand}}

## Eén regel per referentie

| Wat je ziet | Betekenis |
|---|---|
| Referentie en naam | Bijvoorbeeld `ONFF-0842 · Boshoek`. |
| Afstand en richting | In rechte lijn vanaf jou, bijvoorbeeld `1,5 km · 62°`. |
| Aantal QSO’s | Hoeveel verbindingen er volgens de WWFF-directory vanuit gemaakt zijn. |
| Laatst actief | De datum van de laatste activatie. |
| *geen activatiedatum bekend* | De directory kent de referentie, maar geen datum. |
| *niet in de WWFF-directory* | Diana kent het gebied, maar de directory heeft er niets over. Dat wil niet zeggen dat het nooit geactiveerd werd. |

## Sorteren: welke volgorde kies je?

| Knop | Wanneer gebruiken |
|---|---|
| **Afstand** | Het dichtstbijzijnde eerst. Als je snel ergens wil opzetten. |
| **Laatst actief** | De gebieden die het langst niet in de lucht waren eerst. Daar is de kans op een pile-up het grootst. |
| **Aantal QSO’s** | De minst gewerkte gebieden eerst. Als je hunters een nieuwe referentie wil geven. |

## Een gebied openen

1. Tik op een regel.
2. De kaart opent, ingezoomd op dat gebied, met het paneel en de grens.
3. Meer dan honderd gebieden in de buurt? Tik onderaan op **Toon meer**.

## De afstand aanpassen

**Instellingen** › **Veldinfo** › 10, 25, 50 of 100 km. Zie {{link:settings/field-info-distance}}.

:::note
De QSO-aantallen en datums komen uit de WWFF-directory, die elke nacht ververst wordt. Waar de directory niets heeft, zegt het scherm dat, in plaats van "nooit geactiveerd".
:::
'''}},
# ------------------------------------------------------------------
{'sec': 'field-info', 'slug': 'location', 'order': 3,
'en': {'title': 'Location in radio terms', 'desc': 'Time, locator, position and zones of the place where you are.', 'body': '''
The **Location** tab gives everything you need about your own spot during a QSO or in your log. Diana works it out on your device itself, so it works without signal too.

{{img:phone-field-location|Field info, Location tab, with UTC and local time, locator, accuracy and zones}}

| Box | How to read it |
|---|---|
| **Time** | UTC and your local time with time zone. Your log is always in UTC. |
| **Locator** | Your Maidenhead locator in six characters (`JO21FD`) and in eight (`JO21FD70`). In a QSO you usually give the six. |
| **Position** | In decimal degrees and in degrees, minutes and seconds, with the accuracy in metres. |
| **Zones** | Your CQ zone, ITU zone and ITU region. Belgium is CQ 14, ITU 27, region 1. |
| *border nearby: also …* | You are close to a zone border, or your position is uncertain. Both numbers are then possible. |
| **Nearest WWFF** | The nearest references, anywhere in the world, in a straight line. |

:::note[Where the zones come from]
The CQ and ITU zones come from a public dataset, simplified to about 3 km. That is why near a border the tile also names the neighbouring zone.
:::
'''},
'nl': {'title': 'Locatie in radiotermen', 'desc': 'Tijd, locator, positie en zones van de plek waar je staat.', 'body': '''
Het tabblad **Locatie** geeft alles wat je tijdens een QSO of in je log nodig hebt over je eigen plek. Diana rekent het op je toestel zelf uit, dus het werkt ook zonder bereik.

{{img:phone-field-location|Veldinfo, tabblad Locatie, met UTC en lokale tijd, locator, nauwkeurigheid en zones}}

| Vak | Hoe je het leest |
|---|---|
| **Tijd** | UTC en je lokale tijd met tijdzone. Je log is altijd in UTC. |
| **Locator** | Je Maidenhead-locator in zes tekens (`JO21FD`) en in acht (`JO21FD70`). In een QSO geef je meestal de zes. |
| **Positie** | In decimale graden en in graden, minuten en seconden, met de nauwkeurigheid in meter. |
| **Zones** | Je CQ-zone, ITU-zone en ITU-regio. België ligt in CQ 14, ITU 27, regio 1. |
| *grens dichtbij: ook …* | Je staat dicht bij een zonegrens, of je positie is onzeker. Beide nummers zijn dan mogelijk. |
| **Dichtstbijzijnde WWFF** | De dichtste referenties, waar ook ter wereld, in rechte lijn. |

:::note[Waar de zones vandaan komen]
De CQ- en ITU-zones komen uit een openbare dataset, vereenvoudigd tot op zo’n 3 km. Daarom noemt het vak dicht bij een grens ook de buurzone.
:::
'''}},
# ------------------------------------------------------------------
{'sec': 'field-info', 'slug': 'conditions-space-weather', 'order': 4,
'en': {'title': 'Conditions: space weather', 'label': 'Space weather', 'desc': 'The Kp dial, SFI, A index and sunspots, and what they mean.', 'body': '''
The **Conditions** tab starts with today’s space weather: a dial with the **Kp index** and three numbers under it.

{{img:phone-field-conditions|Field info, Conditions tab, with the Kp dial on 2, quiet, and the band bars}}

## The Kp dial

Kp measures how restless the Earth’s magnetic field is, on a scale from 0 to 9. The lower, the better for the higher bands. Diana shows the official three-hourly value from NOAA, and next to it an estimate of the last minutes.

| Kp | Word in Diana | What it means |
|---|---|---|
| 0 to 2 | quiet | No effect. Normal conditions. |
| 3 | unsettled | Slightly restless. Usually no noticeable effect yet. |
| 4 | active | 20, 15 and 10 m drop one step. |
| 5 and 6 | storm G1, G2 | Minor storm: 20, 15 and 10 m worse. 80 and 40 m hardly notice it. |
| 7 to 9 | storm G3 to G5 | Strong storm: all bands worse, the high ones most. |

:::note
Kp is a worldwide value, not a measurement at your position.
:::

## The three numbers

| Number | What it tells you |
|---|---|
| **SFI** | Solar flux. The higher, the better the high bands open. Around 70 is low, above 150 is high. |
| **A** | How restless the magnetic field was over the whole day. Low is good. |
| **Sunspots** | Goes with the SFI: more sunspots, more chance of DX on the high bands. |

SFI, A and sunspots are daily figures; Diana says which day they are from.

## How old are the figures?

Under the dial it says when the figures were updated, for example *"Updated at 14:37 (12 min ago)"*. Diana tries to fetch them twice an hour, but in practice there can be a few hours between two updates.

- Older than **eight hours**: the message turns orange.
- Kp value older than **twelve hours**: Diana says so separately.

The source is NOAA SWPC. What it means per band: {{link:field-info/conditions-bands}}.
'''},
'nl': {'title': 'Condities: ruimteweer', 'label': 'Ruimteweer', 'desc': 'De Kp-meter, SFI, A-index en zonnevlekken, en wat ze betekenen.', 'body': '''
Het tabblad **Condities** begint met het ruimteweer van vandaag: een meter met de **Kp-index** en drie getallen eronder.

{{img:phone-field-conditions|Veldinfo, tabblad Condities, met de Kp-meter op 2, rustig, en de bandbalken}}

## De Kp-meter

Kp meet hoe onrustig het aardmagnetisch veld is, op een schaal van 0 tot 9. Hoe lager, hoe beter voor de hogere banden. Diana toont de officiële waarde per drie uur van NOAA, met daarnaast een schatting van de laatste minuten.

| Kp | Woord in Diana | Wat het betekent |
|---|---|---|
| 0 tot 2 | rustig | Geen invloed. Normale condities. |
| 3 | onrustig | Licht onrustig. Meestal nog geen merkbaar effect. |
| 4 | actief | 20, 15 en 10 m zakken een stap. |
| 5 en 6 | storm G1, G2 | Kleine storm: 20, 15 en 10 m slechter. 80 en 40 m merken er weinig van. |
| 7 tot 9 | storm G3 tot G5 | Zware storm: alle banden slechter, de hoge het meest. |

:::note
Kp is een wereldwijde waarde, geen meting op jouw positie.
:::

## De drie getallen

| Getal | Wat het zegt |
|---|---|
| **SFI** | Zonneflux. Hoe hoger, hoe beter de hoge banden openen. Rond 70 is laag, boven 150 is hoog. |
| **A** | Hoe onrustig het magneetveld de hele dag was. Laag is goed. |
| **Zonnevlekken** | Hangt samen met de SFI: meer vlekken, meer kans op DX op de hoge banden. |

SFI, A en zonnevlekken zijn daggegevens; Diana zegt van welke dag.

## Hoe oud zijn de gegevens?

Onder de meter staat wanneer de gegevens bijgewerkt werden, bijvoorbeeld *"Bijgewerkt om 14:37 (12 min geleden)"*. Diana probeert ze twee keer per uur op te halen, maar in de praktijk kunnen er een paar uur tussen twee updates zitten.

- Ouder dan **acht uur**: de melding wordt oranje.
- Kp-waarde ouder dan **twaalf uur**: Diana zegt dat apart.

De bron is NOAA SWPC. Wat het betekent per band: {{link:field-info/conditions-bands}}.
'''}},
# ------------------------------------------------------------------
{'sec': 'field-info', 'slug': 'conditions-bands', 'order': 5,
'en': {'title': 'Conditions: the bands', 'label': 'The band bars', 'desc': 'How to read the colour bar of each band across the day.', 'body': '''
Under the space weather, the **Conditions** tab shows a colour bar for each band: 80, 40, 20, 15 and 10 m.

## Reading a band bar

1. Each bar is **one band**. Next to the band it says what it is for, for example *"NVIS and EU"*.
2. The bar runs from left to right across five parts of the day: **morning, midday, afternoon, evening and night**. Diana works them out from sunrise and sunset at your position.
3. The **colour** is the expectation: green is good, yellow fair, red poor.
4. The thin vertical **marker** is **now**. On the right it says what applies now, for example *"now: good"*.

## What the labels mean

| Label | Reach |
|---|---|
| **NVIS** | Close by, up to about 400 km. Ideal to be worked within your own country. |
| **EU** | Within Europe. |
| **DX** | Further away, outside Europe. |

| Band | Label in Diana |
|---|---|
| 80 m | NVIS, EU at night |
| 40 m | NVIS and EU |
| 20 m | EU and DX |
| 15 m | DX |
| 10 m | DX |

:::caution[An indication, not a promise]
The bars are Diana’s own rough estimate, based on SFI, Kp, the season and the time of day at your position. It is not a NOAA forecast. A band shown as "poor" can still be open: always listen for a moment.
:::

:::tip[Example in the field]
Kp 2, quiet, SFI 91, in the evening in the Ardennes: 40 m is on good and is your best chance for Belgium and Europe. 15 m is on poor in the evening; no need to start there.
:::

Without a position, Diana still shows the bars, but without the marker for now.
'''},
'nl': {'title': 'Condities: de banden', 'label': 'De bandbalken', 'desc': 'Hoe je de kleurbalk van elke band over de dag leest.', 'body': '''
Onder het ruimteweer toont het tabblad **Condities** een kleurbalk per band: 80, 40, 20, 15 en 10 m.

## Een bandbalk lezen

1. Elke balk is **één band**. Naast de band staat waarvoor hij dient, bijvoorbeeld *"NVIS en EU"*.
2. De balk loopt van links naar rechts over vijf dagdelen: **ochtend, middag, namiddag, avond en nacht**. Diana berekent ze uit zonsopgang en zonsondergang op jouw plek.
3. De **kleur** is de verwachting: groen is goed, geel matig, rood slecht.
4. Het dunne verticale **streepje** is **nu**. Rechts staat wat nu geldt, bijvoorbeeld *"nu: goed"*.

## Wat de labels betekenen

| Label | Bereik |
|---|---|
| **NVIS** | Dichtbij, tot ongeveer 400 km. Ideaal om in eigen land gewerkt te worden. |
| **EU** | Binnen Europa. |
| **DX** | Verder weg, buiten Europa. |

| Band | Label in Diana |
|---|---|
| 80 m | NVIS, EU ’s nachts |
| 40 m | NVIS en EU |
| 20 m | EU en DX |
| 15 m | DX |
| 10 m | DX |

:::caution[Een indicatie, geen belofte]
De balken zijn een ruwe schatting van Diana zelf, op basis van SFI, Kp, het seizoen en het dagdeel op jouw plek. Het is geen voorspelling van NOAA. Een band die "slecht" toont, kan toch open zijn: luister altijd even.
:::

:::tip[Voorbeeld in het veld]
Kp 2, rustig, SFI 91, ’s avonds in de Ardennen: 40 m staat op goed en is je beste kans voor België en Europa. 15 m staat ’s avonds op slecht; daar hoef je niet te beginnen.
:::

Zonder positie toont Diana de balken ook, maar zonder het streepje voor nu.
'''}},
]
