PAGES = [
# ------------------------------------------------------------------
{'sec': 'settings', 'slug': 'overview', 'order': 1,
'en': {'title': 'Settings', 'desc': 'How to open Settings, and what every part is for.', 'body': '''
Everything you set up in the wizard, and a bit more, is under **Settings**.

{{img:phone-settings|The Settings screen with Your station and Your country}}

## Opening Settings

1. Tap **Settings** in the bottom bar (the gear, all the way to the right).
2. Scroll to the part you want to change.
3. Change it. Everything is saved at once: there is no save button. You briefly see *"Saved on this device"*.

## What is in it

| Part | What you set | Page |
|---|---|---|
| **Your station** | Callsign, portable callsign, locator | {{link:settings/your-station}} |
| **Your country** | Which country is loaded in detail, and the spots filter | {{link:settings/your-country}} |
| **Quick words on a spot** | Five words to add with one tap | {{link:settings/quick-words}} |
| **Field info** | How far around you the Areas tab looks | {{link:settings/field-info-distance}} |
| **Band list when announcing** | All bands or HF only | {{link:settings/band-list}} |
| **Language** | One of eight, or follow the browser | {{link:settings/language}} |
| **Privacy** | Privacy page, statistics, clear everything | {{link:settings/privacy-settings}} |
| **Install as an app** | Install on this device | {{link:start/install-android}} |
| At the bottom | Version, updates, what’s new, run the wizard again | {{link:settings/version-and-updates}} |

:::caution[Only on this device]
Everything you fill in here stays in the browser of this device. Use Diana on another device too? Fill it in there again. Diana has no account to link them. See {{link:help/data-and-limits}}.
:::
'''},
'nl': {'title': 'Instellingen', 'desc': 'Hoe je Instellingen opent, en waarvoor elk onderdeel dient.', 'body': '''
Alles wat je in de wizard instelde, en nog wat meer, staat onder **Instellingen**.

{{img:phone-settings|Het scherm Instellingen met Jouw station en Jouw land}}

## Instellingen openen

1. Tik onderaan op **Instellingen** (het tandwiel, helemaal rechts).
2. Scroll naar het onderdeel dat je wil aanpassen.
3. Pas het aan. Alles wordt meteen bewaard: er is geen bewaarknop. Je ziet kort *"Bewaard op dit toestel"*.

## Wat erin staat

| Onderdeel | Wat je instelt | Pagina |
|---|---|---|
| **Jouw station** | Roepnaam, portable roepnaam, locator | {{link:settings/your-station}} |
| **Jouw land** | Welk land in detail geladen wordt, en de spotfilter | {{link:settings/your-country}} |
| **Snelknoppen bij een spot** | Vijf woorden om met één tik toe te voegen | {{link:settings/quick-words}} |
| **Veldinfo** | Hoe ver rond je het tabblad Gebieden kijkt | {{link:settings/field-info-distance}} |
| **Bandenlijst bij aankondigen** | Alle banden of alleen HF | {{link:settings/band-list}} |
| **Taal** | Een van acht, of de browser volgen | {{link:settings/language}} |
| **Privacy** | Privacypagina, statistieken, alles wissen | {{link:settings/privacy-settings}} |
| **Als app installeren** | Op dit toestel installeren | {{link:start/install-android}} |
| Onderaan | Versie, updates, wat is er nieuw, wizard opnieuw | {{link:settings/version-and-updates}} |

:::caution[Alleen op dit toestel]
Alles wat je hier invult, blijft in de browser van dit toestel. Gebruik je Diana ook op een ander toestel? Vul het daar opnieuw in. Diana heeft geen account om ze te koppelen. Zie {{link:help/data-and-limits}}.
:::
'''}},
# ------------------------------------------------------------------
{'sec': 'settings', 'slug': 'your-station', 'order': 2,
'en': {'title': 'Your station', 'desc': 'Callsign, portable callsign and locator, and how to read the position line.', 'body': '''
**Settings** › **Your station**. Who you are and roughly where you are.

| Field | What to fill in | What Diana does with it |
|---|---|---|
| **Callsign** | Your normal callsign, for example `ON3VZ`. | Used as the spotter, and decides which country Diana proposes. |
| **Portable callsign** | What you use in the field, for example `ON3VZ/P`. | Filled in as the activator when you spot yourself or announce. |
| **Maidenhead locator** | Six characters, for example `JO21EE`. | Your starting point while there is no GPS: for the map, the distances and the lines to spots. |

*"No valid locator (e.g. JO21EE)"* means a typing error: two letters, two digits, two letters.

## Taking the locator from GPS

1. Stand where you want the locator for, outside if possible.
2. Tap **Take from GPS**.
3. Diana fills in the locator from your current position.

## The position line

Under the locator a line says how good your last position was, for example *"Last position: ±8 m · 2 min ago"*.

| You read | What it means | What to do |
|---|---|---|
| ±10 m or better | Satellites. Fine. | Nothing. |
| about ±50 to 100 m | Usually wifi, indoors. | Try outside. |
| *"Too coarse to say whether you are inside an area"* | Not good enough for inside-or-outside. | Go outside with open sky. |
| Stays coarse outside too | The site may only use an approximate location. | Check the location setting of your phone: {{link:help/location-problems}}. |
| *"No GPS position on this device yet"* | Location not allowed, or not asked yet. | Allow location, or rely on your locator. |

:::note
There is no setting for where the map opens. It always opens where you are, otherwise at your locator, otherwise in your callsign’s country.
:::
'''},
'nl': {'title': 'Jouw station', 'desc': 'Roepnaam, portable roepnaam en locator, en hoe je de positieregel leest.', 'body': '''
**Instellingen** › **Jouw station**. Wie je bent en ongeveer waar je zit.

| Veld | Wat je invult | Wat Diana ermee doet |
|---|---|---|
| **Roepnaam** | Je gewone roepnaam, bijvoorbeeld `ON3VZ`. | Gebruikt als spotter, en bepaalt welk land Diana voorstelt. |
| **Portable roepnaam** | Wat je in het veld gebruikt, bijvoorbeeld `ON3VZ/P`. | Ingevuld als activator wanneer je jezelf meldt of aankondigt. |
| **Maidenhead-locator** | Zes tekens, bijvoorbeeld `JO21EE`. | Je vertrekpunt zolang er geen gps is: voor de kaart, de afstanden en de lijnen naar spots. |

*"Geen geldige locator (bv. JO21EE)"* betekent een tikfout: twee letters, twee cijfers, twee letters.

## De locator uit gps overnemen

1. Ga staan waar je de locator voor wil, liefst buiten.
2. Tik op **Uit GPS overnemen**.
3. Diana vult de locator in vanaf je huidige positie.

## De positieregel

Onder de locator staat hoe goed je laatste positie was, bijvoorbeeld *"Laatste positie: ±8 m · 2 min geleden"*.

| Je leest | Wat het betekent | Wat je doet |
|---|---|---|
| ±10 m of beter | Satellieten. Prima. | Niets. |
| ongeveer ±50 tot 100 m | Meestal wifi, binnenshuis. | Probeer buiten. |
| *"Te grof om te zeggen of je binnen een gebied staat"* | Niet goed genoeg voor binnen of buiten. | Ga naar buiten met vrije hemel. |
| Blijft ook buiten grof | De site mag waarschijnlijk alleen een benaderde locatie gebruiken. | Kijk de locatie-instelling van je gsm na: {{link:help/location-problems}}. |
| *"Nog geen GPS-positie op dit toestel"* | Locatie niet toegestaan, of nog niet gevraagd. | Sta locatie toe, of werk met je locator. |

:::note
Er is geen instelling voor waar de kaart opent. Ze opent altijd waar je bent, anders bij je locator, anders in het land van je roepnaam.
:::
'''}},
# ------------------------------------------------------------------
{'sec': 'settings', 'slug': 'your-country', 'order': 3,
'en': {'title': 'Your country', 'desc': 'Which country Diana loads in detail, and how it differs from the spots filter.', 'body': '''
**Settings** › **Your country**. One choice for everything: which country Diana loads with its real boundaries, and which spots and agenda entries your country button shows. Of other countries Diana always shows points only.

## The two parts

| Part | What it does |
|---|---|
| **Country** | The country loaded in detail. In the list it says **With boundaries** or **Points only**. |
| **Show** | Your country or **Worldwide**. The filter for the Spots screen, the same switch as on that screen. |

Under the list Diana says what it has for that country, for example *"ONFF, 947 areas with boundaries loaded"* or *"For OKFF there are no boundaries, only points on the map"*.

## When to change it

- **Going abroad**: choose the country you visit. If Diana has its boundaries, the areas appear in full there. See {{link:travel/abroad}}.
- **Interested in a reference across the border**: tap its blue dot and use **Show [country] in detail**; that does the same as changing it here.

## Step by step

1. Tap **Settings** at the bottom right.
2. Open the list under **Your country** and choose the country.
3. The change is immediate. Read the line under the list to see what was loaded.
4. Want the spots worldwide or only of that country? Choose it under **Show**.

:::note
Choosing another country never changes **Show**. And the other way round: switching the spots filter does not load another country.
:::

Why a reference is an area or a dot: {{link:map/points-and-areas}}.
'''},
'nl': {'title': 'Jouw land', 'desc': 'Welk land Diana in detail laadt, en hoe dat verschilt van de spotfilter.', 'body': '''
**Instellingen** › **Jouw land**. Eén keuze voor alles: van welk land Diana de echte grenzen inlaadt, en welke spots en agenda-items je landknop toont. Van andere landen toont Diana altijd alleen de punten.

## De twee delen

| Deel | Wat het doet |
|---|---|
| **Land** | Het land dat in detail geladen wordt. In de lijst staat **Met grenzen** of **Alleen punten**. |
| **Tonen** | Jouw land of **Wereldwijd**. De filter voor het scherm Spots, dezelfde schakelaar als op dat scherm. |

Onder de lijst zegt Diana wat ze voor dat land heeft, bijvoorbeeld *"ONFF, 947 gebieden met grenzen ingeladen"* of *"Voor OKFF zijn er geen grenzen, alleen punten op de kaart"*.

## Wanneer aanpassen

- **Naar het buitenland**: kies het land dat je bezoekt. Heeft Diana de grenzen, dan verschijnen de gebieden daar volledig. Zie {{link:travel/abroad}}.
- **Interesse in een referentie over de grens**: tik haar blauwe bolletje aan en gebruik **Toon [land] in detail**; dat doet hetzelfde als het hier aanpassen.

## Stap voor stap

1. Tik rechtsonder op **Instellingen**.
2. Open de lijst onder **Jouw land** en kies het land.
3. De wijziging gaat meteen in. Lees de regel onder de lijst om te zien wat er geladen werd.
4. Wil je de spots wereldwijd of alleen van dat land? Kies het onder **Tonen**.

:::note
Een ander land kiezen verandert **Tonen** nooit. En omgekeerd: de spotfilter omzetten laadt geen ander land in.
:::

Waarom een referentie een vlak of een bolletje is: {{link:map/points-and-areas}}.
'''}},
# ------------------------------------------------------------------
{'sec': 'settings', 'slug': 'quick-words', 'order': 4,
'en': {'title': 'Quick words on a spot', 'desc': 'Five words you add to a spot’s remark with one tap.', 'body': '''
**Settings** › **Quick words on a spot**. Five words you can add to the remark of a spot with one tap, so you do not have to type in the field.

## Setting them

1. Fill in up to five boxes, each with one word or a short phrase.
2. An empty box simply gives no button.
3. When you spot yourself, they appear as buttons under the remark. See {{link:spots/spot-yourself}}.

## Ideas

Fill in what fits your station: a mode, your power, the antenna, a short status. Keep them short: a remark has at most 100 characters.

:::caution
No thank-yous or band requests: a spot goes to the DX cluster, where that is noise.
:::
'''},
'nl': {'title': 'Snelknoppen bij een spot', 'desc': 'Vijf woorden die je met één tik aan de opmerking van een spot hangt.', 'body': '''
**Instellingen** › **Snelknoppen bij een spot**. Vijf woorden die je met één tik aan de opmerking van een spot hangt, zodat je in het veld niet hoeft te typen.

## Instellen

1. Vul tot vijf vakjes in, elk met één woord of een korte uitdrukking.
2. Een leeg vakje geeft gewoon geen knop.
3. Als je jezelf spot, verschijnen ze als knoppen onder de opmerking. Zie {{link:spots/spot-yourself}}.

## Ideeën

Vul in wat bij jouw station past: een mode, je vermogen, de antenne, een korte status. Hou ze kort: een opmerking heeft hoogstens 100 tekens.

:::caution
Geen bedankjes of bandverzoeken: een spot gaat naar het DX-cluster, waar dat ruis is.
:::
'''}},
# ------------------------------------------------------------------
{'sec': 'settings', 'slug': 'field-info-distance', 'order': 5,
'en': {'title': 'Field info distance', 'desc': 'How far around you the Areas tab looks.', 'body': '''
**Settings** › **Field info**. How far around your position the **Areas** tab of Field info looks: **10, 25, 50 or 100 km**.

| Choose | When |
|---|---|
| **10 km** | Many areas close together, as in Flanders. A short, clear list. |
| **25 km** | A good middle way for most places. |
| **50 km** | Fewer areas around, or you are willing to drive. |
| **100 km** | The countryside, or abroad with few references. |

The list shows at most a hundred lines at once; **Show more** gives the rest. See {{link:field-info/areas-nearby}}.
'''},
'nl': {'title': 'Afstand voor Veldinfo', 'desc': 'Hoe ver rond je het tabblad Gebieden kijkt.', 'body': '''
**Instellingen** › **Veldinfo**. Hoe ver rond je positie het tabblad **Gebieden** van Veldinfo kijkt: **10, 25, 50 of 100 km**.

| Kies | Wanneer |
|---|---|
| **10 km** | Veel gebieden dicht bij elkaar, zoals in Vlaanderen. Een korte, overzichtelijke lijst. |
| **25 km** | Een goede middenweg voor de meeste plaatsen. |
| **50 km** | Minder gebieden in de buurt, of je wil best wat rijden. |
| **100 km** | Op het platteland, of in het buitenland met weinig referenties. |

De lijst toont hoogstens honderd regels tegelijk; **Toon meer** geeft de rest. Zie {{link:field-info/areas-nearby}}.
'''}},
# ------------------------------------------------------------------
{'sec': 'settings', 'slug': 'band-list', 'order': 6,
'en': {'title': 'Band list when announcing', 'desc': 'All bands or HF only in the band list of the announce form.', 'body': '''
**Settings** › **Band list when announcing**. Which bands the list on the announce screen offers.

| Choice | Bands |
|---|---|
| **All bands** | 160 m to 23 cm. |
| **HF only** | 80, 40, 30, 20, 15 and 10 m. |

Nearly every activation happens on the HF bands. With **HF only**, the list stays short and you scroll less on your phone. Work VHF or UHF too? Choose **All bands**.

See {{link:spots/announce}}.
'''},
'nl': {'title': 'Bandenlijst bij aankondigen', 'desc': 'Alle banden of alleen HF in de bandenlijst van het aankondigingsformulier.', 'body': '''
**Instellingen** › **Bandenlijst bij aankondigen**. Welke banden de lijst op het aankondigingsscherm toont.

| Keuze | Banden |
|---|---|
| **Alle banden** | 160 m tot 23 cm. |
| **Alleen HF** | 80, 40, 30, 20, 15 en 10 m. |

Bijna elke activatie gebeurt op de HF-banden. Met **Alleen HF** blijft de lijst kort en scroll je minder op je gsm. Werk je ook VHF of UHF? Kies dan **Alle banden**.

Zie {{link:spots/announce}}.
'''}},
# ------------------------------------------------------------------
{'sec': 'settings', 'slug': 'language', 'order': 7,
'en': {'title': 'Language', 'desc': 'Choose the language of the app.', 'body': '''
**Settings** › **Language**. Diana speaks English, Dutch, French, German, Danish, Italian, Spanish and Portuguese.

- Choose one of the eight, or **Follow the browser** to take the language of your browser.
- Without a choice, Diana starts in English.
- You can also switch the language under **≡** on the map, or in the first step of the wizard.

Everything switches at once. Area names are never translated: they are official names and belong in your log exactly as published.

:::note
"What’s new" (the release notes) is available in Dutch and English only.
:::
'''},
'nl': {'title': 'Taal', 'desc': 'De taal van de app kiezen.', 'body': '''
**Instellingen** › **Taal**. Diana spreekt Engels, Nederlands, Frans, Duits, Deens, Italiaans, Spaans en Portugees.

- Kies een van de acht, of **Volg de browser** om de taal van je browser over te nemen.
- Zonder keuze start Diana in het Engels.
- Je kan de taal ook wisselen onder **≡** op de kaart, of in de eerste stap van de wizard.

Alles schakelt meteen om. Namen van gebieden worden nooit vertaald: het zijn officiële namen die precies zo in je log horen.

:::note
"Wat is er nieuw" (de versie-informatie) bestaat alleen in het Nederlands en het Engels.
:::
'''}},
# ------------------------------------------------------------------
{'sec': 'settings', 'slug': 'privacy-settings', 'order': 8,
'en': {'title': 'Privacy and statistics', 'desc': 'The privacy page, your statistics choice and clearing everything.', 'body': '''
**Settings** › **Privacy**. What Diana keeps, what it sends, and your choice about anonymous statistics.

## What you find here

- **Open the privacy page**: which services Diana talks to and why. Summary in {{link:start/privacy}}.
- **Anonymous statistics**: **Yes, I’ll help** or **No, rather not**. Change it whenever you like.
- **Clear everything on this device**: removes everything Diana stored here.

## Changing your statistics choice

1. Tap **Settings** › **Privacy**.
2. Tap **Yes, I’ll help** or **No, rather not**.
3. You see *"Saved."*. That is all.

:::tip[Why yes helps]
Statistics are counted with Umami: no cookies, no profile, nothing that identifies you. For the volunteers behind Diana it is the only way to know the app is used and which screens matter. Diana works exactly the same either way.
:::

## Clearing everything

1. Tap **Clear everything on this device**.
2. Diana asks for confirmation: this removes your callsign, settings, offline map tiles and your statistics choice.
3. Confirm. Diana starts again at the welcome screen.

Use this when you pass on your device, or want to start over.
'''},
'nl': {'title': 'Privacy en statistieken', 'desc': 'De privacypagina, je keuze over statistieken en alles wissen.', 'body': '''
**Instellingen** › **Privacy**. Wat Diana bewaart, wat ze verstuurt, en jouw keuze over anonieme statistieken.

## Wat je hier vindt

- **Open de privacypagina**: met welke diensten Diana praat en waarom. Samenvatting in {{link:start/privacy}}.
- **Anonieme statistieken**: **Ja, ik help mee** of **Nee, liever niet**. Pas het aan wanneer je wil.
- **Wis alles op dit toestel**: verwijdert alles wat Diana hier bewaarde.

## Je keuze over statistieken aanpassen

1. Tik op **Instellingen** › **Privacy**.
2. Tik op **Ja, ik help mee** of **Nee, liever niet**.
3. Je ziet *"Opgeslagen."*. Meer is het niet.

:::tip[Waarom ja helpt]
Statistieken worden geteld met Umami: geen cookies, geen profiel, niets dat jou herkenbaar maakt. Voor de vrijwilligers achter Diana is het de enige manier om te weten dat de app gebruikt wordt en welke schermen ertoe doen. Diana werkt hoe dan ook precies hetzelfde.
:::

## Alles wissen

1. Tik op **Wis alles op dit toestel**.
2. Diana vraagt om te bevestigen: dit verwijdert je roepnaam, instellingen, offline kaarttegels en je keuze over statistieken.
3. Bevestig. Diana begint opnieuw bij het welkomstscherm.

Gebruik dit als je je toestel doorgeeft, of opnieuw wil beginnen.
'''}},
# ------------------------------------------------------------------
{'sec': 'settings', 'slug': 'version-and-updates', 'order': 9,
'en': {'title': 'Version and updates', 'desc': 'Reading the version line, checking for updates and running the wizard again.', 'body': '''
At the very bottom of **Settings**: which version you have, how fresh the data is, and whether there is something new.

## Reading the version line

`v2.2.12 · 6757ec3 · 14/11/2026`

| Part | Meaning |
|---|---|
| `v2.2.12` | The version of the app. |
| `6757ec3` | A code for this exact build of the app. |
| `14/11/2026` | The date of that release. |

The code only changes when the app itself changes, not when the nightly refresh brings new data. The **data line** under it says how fresh the map data is.

## The buttons

- **Check for updates**: Diana looks whether a new version is ready and loads it.
- **What’s new**: what every version brought, newest on top.
- **Run the setup wizard again**: the wizard starts from your current settings. At the end it offers the tour again.

:::tip[Someone asks which version you have?]
Read out the version line. That is exactly what is needed to help you.
:::

More about updates that do not seem to arrive: {{link:help/updates}}.
'''},
'nl': {'title': 'Versie en updates', 'desc': 'De versieregel lezen, op updates controleren en de wizard opnieuw doorlopen.', 'body': '''
Helemaal onderaan **Instellingen**: welke versie je hebt, hoe vers de gegevens zijn, en of er iets nieuws is.

## De versieregel lezen

`v2.2.12 · 6757ec3 · 14/11/2026`

| Deel | Betekenis |
|---|---|
| `v2.2.12` | De versie van de app. |
| `6757ec3` | Een code voor precies deze bouw van de app. |
| `14/11/2026` | De datum van die versie. |

De code verandert alleen als de app zelf verandert, niet als de nachtelijke verversing nieuwe gegevens brengt. De **gegevensregel** eronder zegt hoe vers de kaartgegevens zijn.

## De knoppen

- **Op updates controleren**: Diana kijkt of er een nieuwe versie klaarstaat en laadt ze.
- **Wat is er nieuw**: wat elke versie bracht, de nieuwste bovenaan.
- **Opstartwizard opnieuw doorlopen**: de wizard start vanaf je huidige instellingen. Op het einde krijg je de rondleiding opnieuw aangeboden.

:::tip[Iemand vraagt welke versie je hebt?]
Lees de versieregel voor. Dat is precies wat nodig is om je te helpen.
:::

Meer over updates die niet lijken door te komen: {{link:help/updates}}.
'''}},
]
