PAGES = [
# ------------------------------------------------------------------
{'sec': 'help', 'slug': 'location-problems', 'order': 1,
'en': {'title': 'Location problems', 'desc': 'No position, or a position that stays rough: what to check, per device.', 'body': '''
Diana always asks for the most precise position your device can give. Whether a site gets the exact position or a deliberately blurred one is a setting of your phone or browser, not of Diana.

## First: try outside

Indoors, wifi alone often gives about ±100 m. Go outside, with open sky above you, wait ten seconds and tap **Map** in the bottom bar. Often that is enough.

## Still rough or no position? Check the setting

**Android with Chrome**

1. Open the **Settings** app of your phone.
2. Go to **Apps** › **Chrome** › **Permissions** › **Location**.
3. Choose **Allow only while using the app** and switch on **Use precise location**.
4. Also check the site itself: in Chrome, tap the icon left of the address bar › **Permissions** › **Location**: allowed.

**iPhone or iPad with Safari**

1. Open the **Settings** app.
2. Go to **Privacy & Security** › **Location Services** › **Safari Websites**.
3. Choose **While Using the App** and switch on **Precise Location**.

**iPhone or iPad with another browser** (for example Chrome)

1. Open the **Settings** app.
2. Go to **Privacy & Security** › **Location Services** › your browser.
3. Choose **While Using the App** and switch on **Precise Location**.

**Computer**

Click the lock icon next to the address bar and allow **Location** for this site. A laptop gets its position from wifi and is rarely better than about ±50 m.

## "Location is blocked for this site"

You (or someone) said no earlier. Diana cannot ask again: only you can allow it, in the browser or phone settings above. Then reload Diana.

## Without location

Diana works without location too. Fill in your locator under **Settings** › **Your station**. Distances and lines then start from the centre of your locator square. Only *am I inside the area* really needs a precise position.

See also {{link:map/am-i-inside}}.
'''},
'nl': {'title': 'Problemen met locatie', 'desc': 'Geen positie, of een positie die grof blijft: wat je nakijkt, per toestel.', 'body': '''
Diana vraagt altijd de nauwkeurigste positie die je toestel kan geven. Of een site de exacte positie krijgt of een bewust vervaagde, is een instelling van je gsm of browser, niet van Diana.

## Eerst: probeer buiten

Binnenshuis geeft wifi alleen vaak zo’n ±100 m. Ga naar buiten, met vrije hemel boven je, wacht tien seconden en tik onderaan op **Kaart**. Vaak volstaat dat.

## Nog altijd grof of geen positie? Kijk de instelling na

**Android met Chrome**

1. Open de app **Instellingen** van je gsm.
2. Ga naar **Apps** › **Chrome** › **Rechten** › **Locatie**.
3. Kies **Alleen toestaan bij gebruik van app** en zet **Exacte locatie gebruiken** aan.
4. Kijk ook bij de site zelf: tik in Chrome op het icoon links van de adresbalk › **Rechten** › **Locatie**: toegestaan.

**iPhone of iPad met Safari**

1. Open de app **Instellingen**.
2. Ga naar **Privacy en beveiliging** › **Locatievoorzieningen** › **Safari-websites**.
3. Kies **Bij gebruik van app** en zet **Exacte locatie** aan.

**iPhone of iPad met een andere browser** (bijvoorbeeld Chrome)

1. Open de app **Instellingen**.
2. Ga naar **Privacy en beveiliging** › **Locatievoorzieningen** › je browser.
3. Kies **Bij gebruik van app** en zet **Exacte locatie** aan.

**Computer**

Klik op het slotje naast de adresbalk en sta **Locatie** toe voor deze site. Een laptop haalt zijn positie uit wifi en is zelden beter dan zo’n ±50 m.

## "Locatie is geblokkeerd voor deze site"

Jij (of iemand anders) zei eerder nee. Diana kan het niet opnieuw vragen: alleen jij kan het toestaan, in de browser- of gsm-instellingen hierboven. Laad Diana daarna opnieuw.

## Zonder locatie

Diana werkt ook zonder locatie. Vul je locator in bij **Instellingen** › **Jouw station**. Afstanden en lijnen vertrekken dan vanaf het midden van je locatorvak. Alleen *sta ik in het gebied* heeft echt een exacte positie nodig.

Zie ook {{link:map/am-i-inside}}.
'''}},
# ------------------------------------------------------------------
{'sec': 'help', 'slug': 'scripts-blocked', 'order': 2,
'en': {'title': 'Stuck on the start screen', 'desc': 'Script blockers and strict browsers: what Diana needs, and nothing more.', 'body': '''
Diana is a web app: without JavaScript nothing runs. If a blocker stops the scripts, Diana stays on the start screen. After a while a box appears there saying so.

## Solving it

1. Allow scripts for **diana-onff.github.io** only. Not `github.io` and not `github.com`: Diana needs neither.
2. **Reload the page**: **F5** or **Ctrl+R** (Mac: **Cmd+R**). On a phone, pull the page down or tap reload. Without reloading, the old block stays, even after you clicked "Trust".
3. Still stuck? A second extension may block too (an ad blocker, a privacy extension). Switch them off one at a time for this site.
4. Diana starts but the map stays empty? Allow `blob:` workers for diana-onff.github.io (see below).

## What Diana loads

**Scripts**: all from diana-onff.github.io itself.

| File | What it is |
|---|---|
| `vendor/maplibre-gl.js` | MapLibre, the map library. A copy on Diana’s own site, not from a CDN. |
| `js/*.js` | Diana’s own code. |
| `sw.js` | The service worker that keeps Diana working offline. |

No inline scripts and no `eval`. One exception, only with your consent: if you said yes to statistics, the Umami script from `cloud.umami.is`.

**Map worker**: MapLibre draws the map in a background worker started from a `blob:` address. A blocker that refuses `blob:` workers lets Diana start but leaves the map blank.

**Data**:

| Host | Why |
|---|---|
| `tiles.openfreemap.org` | Map tiles and label fonts |
| `spots.wwff.co` | Live spots and agenda |
| `diana-spotline.diana-onff.workers.dev` | Only when you send a spot or announcement |
| `raw.githubusercontent.com` | Space weather for Conditions |
| `cloud.umami.is` | Only if you said yes to statistics |

Your position is never sent anywhere.
'''},
'nl': {'title': 'Vast op het startscherm', 'desc': 'Scriptblokkers en strenge browsers: wat Diana nodig heeft, en niets meer.', 'body': '''
Diana is een web-app: zonder JavaScript draait er niets. Houdt een blokker de scripts tegen, dan blijft Diana op het startscherm. Na een tijdje verschijnt daar een vak dat dat zegt.

## Zo los je het op

1. Sta scripts toe voor **diana-onff.github.io**, en alleen daarvoor. Niet `github.io` en niet `github.com`: die heeft Diana niet nodig.
2. **Laad de pagina opnieuw**: **F5** of **Ctrl+R** (Mac: **Cmd+R**). Op een gsm trek je de pagina naar beneden of tik je op herladen. Zonder herladen blijft de oude blokkering staan, ook als je al op "Vertrouwen" klikte.
3. Nog vast? Misschien blokkeert een tweede extensie (een advertentieblokker, een privacy-extensie). Zet ze voor deze site een voor een uit.
4. Diana start maar de kaart blijft leeg? Sta `blob:`-workers toe voor diana-onff.github.io (zie hieronder).

## Wat Diana laadt

**Scripts**: allemaal van diana-onff.github.io zelf.

| Bestand | Wat het is |
|---|---|
| `vendor/maplibre-gl.js` | MapLibre, de kaartbibliotheek. Een kopie op Diana’s eigen site, niet van een CDN. |
| `js/*.js` | Diana’s eigen code. |
| `sw.js` | De service worker die Diana offline laat werken. |

Geen inline scripts en geen `eval`. Eén uitzondering, alleen met jouw toestemming: als je ja zei tegen statistieken, het Umami-script van `cloud.umami.is`.

**Kaartworker**: MapLibre tekent de kaart in een achtergrondworker die start vanaf een `blob:`-adres. Een blokker die `blob:`-workers weigert, laat Diana starten maar houdt de kaart leeg.

**Gegevens**:

| Adres | Waarom |
|---|---|
| `tiles.openfreemap.org` | Kaarttegels en lettertypes van de labels |
| `spots.wwff.co` | Live spots en agenda |
| `diana-spotline.diana-onff.workers.dev` | Alleen als je een spot of aankondiging verstuurt |
| `raw.githubusercontent.com` | Ruimteweer voor Condities |
| `cloud.umami.is` | Alleen als je ja zei tegen statistieken |

Je positie wordt nooit ergens naartoe gestuurd.
'''}},
# ------------------------------------------------------------------
{'sec': 'help', 'slug': 'updates', 'order': 3,
'en': {'title': 'Updates', 'desc': 'How Diana updates itself, and what to do if a new version does not show.', 'body': '''
Diana updates itself. You never have to download anything.

## How it works

- **The data** (references, QSO counts, boundaries) is refreshed every night. Diana fetches it fresh on every start, and falls back to the copy on your phone when the signal is weak.
- **The app itself**: when you open Diana with signal, it checks for a new version. A new version is only announced when there really is one.

## A new version does not show?

1. Make sure you have signal.
2. Open **Settings** and tap **Check for updates** at the bottom.
3. Compare the version line with the one in **What’s new**. See {{link:settings/version-and-updates}}.
4. Still the old version? Close Diana completely (swipe it away from your recent apps) and open it again.

:::note
Releases of the app are listed in **What’s new**, newest on top, in Dutch and English.
:::
'''},
'nl': {'title': 'Updates', 'desc': 'Hoe Diana zichzelf bijwerkt, en wat je doet als een nieuwe versie niet verschijnt.', 'body': '''
Diana werkt zichzelf bij. Je hoeft nooit iets te downloaden.

## Hoe het werkt

- **De gegevens** (referenties, QSO-aantallen, grenzen) worden elke nacht ververst. Diana haalt ze bij elke start vers op, en valt terug op de kopie op je gsm als het bereik zwak is.
- **De app zelf**: als je Diana met bereik opent, kijkt ze of er een nieuwe versie is. Een nieuwe versie wordt alleen gemeld als er echt een is.

## Een nieuwe versie verschijnt niet?

1. Zorg dat je bereik hebt.
2. Open **Instellingen** en tik onderaan op **Op updates controleren**.
3. Vergelijk de versieregel met die in **Wat is er nieuw**. Zie {{link:settings/version-and-updates}}.
4. Nog altijd de oude versie? Sluit Diana helemaal af (veeg ze weg uit je recente apps) en open ze opnieuw.

:::note
De versies van de app staan in **Wat is er nieuw**, de nieuwste bovenaan, in het Nederlands en het Engels.
:::
'''}},
# ------------------------------------------------------------------
{'sec': 'help', 'slug': 'data-and-limits', 'order': 4,
'en': {'title': 'Your data and the limits', 'desc': 'What stays on your device, why nothing syncs, and what Diana cannot do.', 'body': '''
## Everything stays on one device, in one browser

Your callsigns, locator, country, quick words, language, statistics choice and the PINs of your announcements live in the local storage of that one browser. Nothing syncs.

- Use Diana on your phone and on your laptop? Set it up on both. There is no account to link them.
- **Clearing the browser data** (history, cookies and site data), using a **private window**, or **removing the installed app** clears these settings. Diana then starts again at the welcome screen.

:::caution[Your announcement PINs]
They are in that same storage. Clear the browser and they are gone. Write important PINs down somewhere else too.
:::

## What Diana cannot do

- **Live data depends on others.** Spots and the agenda come from WWFF Spotline. If it is down, the Spots screen says so. The band conditions come from NOAA; the tab says how old they are.
- **Boundaries exist only where a file was supplied**: today five countries. Elsewhere references are points, and Diana cannot tell whether you are inside. See {{link:map/points-and-areas}}.
- **Not every reserve has full details.** Many have only a name and reference. That is a gap in the source data.
- **Diana does not log** and does not upload logs. That stays with your own logging program and WWFF.

## Data usage

The boundaries and activation figures come from the WWFF programmes, WDPA, government sources and WWFF Spotline, and remain their owners’ data. See {{link:about/data-sources}}.
'''},
'nl': {'title': 'Je gegevens en de grenzen', 'desc': 'Wat op je toestel blijft, waarom niets synchroniseert, en wat Diana niet kan.', 'body': '''
## Alles blijft op één toestel, in één browser

Je roepnamen, locator, land, snelknoppen, taal, keuze over statistieken en de pins van je aankondigingen staan in de lokale opslag van die ene browser. Er synchroniseert niets.

- Gebruik je Diana op je gsm en op je laptop? Stel ze op beide in. Er is geen account om ze te koppelen.
- **Browsergegevens wissen** (geschiedenis, cookies en sitegegevens), een **privévenster** gebruiken, of **de geïnstalleerde app verwijderen** wist deze instellingen. Diana begint dan opnieuw bij het welkomstscherm.

:::caution[De pins van je aankondigingen]
Die staan in dezelfde opslag. Wis je de browser, dan zijn ze weg. Schrijf belangrijke pins ook ergens anders op.
:::

## Wat Diana niet kan

- **Live gegevens hangen af van anderen.** Spots en de agenda komen van WWFF Spotline. Ligt die plat, dan zegt het scherm Spots dat. De bandcondities komen van NOAA; het tabblad zegt hoe oud ze zijn.
- **Grenzen bestaan alleen waar een bestand aangeleverd werd**: vandaag vijf landen. Elders zijn referenties punten, en kan Diana niet zeggen of je erin staat. Zie {{link:map/points-and-areas}}.
- **Niet elk reservaat heeft alle details.** Veel hebben alleen een naam en referentie. Dat is een gat in de brongegevens.
- **Diana logt niet** en laadt geen logs op. Dat blijft bij je eigen logprogramma en WWFF.

## Gebruik van de gegevens

De grenzen en activatiecijfers komen van de WWFF-programma’s, WDPA, overheidsbronnen en WWFF Spotline, en blijven gegevens van hun eigenaars. Zie {{link:about/data-sources}}.
'''}},
# ------------------------------------------------------------------
{'sec': 'help', 'slug': 'faq', 'order': 5,
'en': {'title': 'Frequently asked questions', 'desc': 'Short answers to the questions that come up most.', 'body': '''
## Does Diana cost anything?

No. Diana is free, without ads and without an account.

## Is Diana an official WWFF app?

No. Diana is a volunteer project that supports the WWFF hobby. It uses the public services of WWFF, such as Spotline and the directory.

## Does Diana send my position anywhere?

No. Your position is used only on your own screen. A spot sends your callsign, frequency, mode, reference and remark, never your position. See {{link:start/privacy}}.

## Does Diana work without signal?

Yes, with the last data it loaded: the map you already viewed, the references, Field info Location and the band plan. Live spots and sending a spot need signal.

## Why is my reference a point and not an area?

Because Diana has no boundary for it, or because it lies in another country than the one you loaded. See {{link:map/points-and-areas}}.

## Can I log in Diana?

No. Diana helps before and during the activation. Your log stays in your logging program. Under **Rules** Diana shows the right file name.

## My settings are gone. What happened?

The browser data was cleared, the app was removed, or you used a private window. See {{link:help/data-and-limits}}.

## Can my national programme get boundaries too?

Yes. The national coordinator sends the area file (KMZ) to the Diana team. More in {{link:about/about-diana}}.

## I found a mistake. Where do I report it?

Contact details are on the privacy page in the app (**Settings** › **Privacy**). Mention your version line: {{link:settings/version-and-updates}}.
'''},
'nl': {'title': 'Veelgestelde vragen', 'desc': 'Korte antwoorden op de vragen die het vaakst terugkomen.', 'body': '''
## Kost Diana iets?

Nee. Diana is gratis, zonder reclame en zonder account.

## Is Diana een officiële WWFF-app?

Nee. Diana is een vrijwilligersproject dat de WWFF-hobby ondersteunt. Ze gebruikt de openbare diensten van WWFF, zoals Spotline en de directory.

## Stuurt Diana mijn positie ergens naartoe?

Nee. Je positie wordt alleen op je eigen scherm gebruikt. Een spot stuurt je roepnaam, frequentie, mode, referentie en opmerking, nooit je positie. Zie {{link:start/privacy}}.

## Werkt Diana zonder bereik?

Ja, met de laatst geladen gegevens: de kaart die je al bekeek, de referenties, Veldinfo Locatie en het bandplan. Live spots en een spot versturen hebben bereik nodig.

## Waarom is mijn referentie een punt en geen vlak?

Omdat Diana er geen grens voor heeft, of omdat ze in een ander land ligt dan het land dat je inlaadde. Zie {{link:map/points-and-areas}}.

## Kan ik in Diana loggen?

Nee. Diana helpt voor en tijdens de activatie. Je log blijft in je logprogramma. Onder **Regels** toont Diana de juiste bestandsnaam.

## Mijn instellingen zijn weg. Wat is er gebeurd?

De browsergegevens werden gewist, de app werd verwijderd, of je gebruikte een privévenster. Zie {{link:help/data-and-limits}}.

## Kan mijn nationale programma ook grenzen krijgen?

Ja. De nationale coördinator stuurt het gebiedsbestand (KMZ) naar het Diana-team. Meer in {{link:about/about-diana}}.

## Ik vond een fout. Waar meld ik die?

De contactgegevens staan op de privacypagina in de app (**Instellingen** › **Privacy**). Vermeld je versieregel: {{link:settings/version-and-updates}}.
'''}},
]
