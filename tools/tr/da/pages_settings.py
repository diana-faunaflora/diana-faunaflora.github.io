T = {
'settings/overview': {'title': 'Indstillinger', 'desc': 'Sådan åbner du Indstillinger, og hvad hver del er til.', 'body': '''
Alt, hvad du satte op i guiden, og lidt mere, findes under **Indstillinger**.

{{img:phone-settings|Indstillinger-skærmen med Din station og Dit land}}

## Åbn Indstillinger

1. Tryk på **Indstillinger** i bjælken nederst (tandhjulet, helt til højre).
2. Rul ned til den del, du vil ændre.
3. Ændr den. Alt gemmes med det samme: der er ingen gem-knap. Du ser kort *"Gemt på denne enhed"*.

## Hvad den indeholder

| Del | Hvad du indstiller | Side |
|---|---|---|
| **Din station** | Kaldesignal, portabelt kaldesignal, locator | {{link:settings/your-station}} |
| **Dit land** | Hvilket land der indlæses i detaljer, og spotfilteret | {{link:settings/your-country}} |
| **Hurtige ord til en spot** | Fem ord, du tilføjer med ét tryk | {{link:settings/quick-words}} |
| **Feltinfo** | Hvor langt omkring dig fanen Områder kigger | {{link:settings/field-info-distance}} |
| **Båndliste ved annoncering** | Alle bånd eller kun HF | {{link:settings/band-list}} |
| **Sprog** | Et af otte, eller følg browseren | {{link:settings/language}} |
| **Privatliv** | Privatlivsside, statistik, ryd alt | {{link:settings/privacy-settings}} |
| **Installer som app** | Installer på denne enhed | {{link:start/install-android}} |
| Helt nederst | Version, opdateringer, nyheder, kør guiden igen | {{link:settings/version-and-updates}} |

:::caution[Kun på denne enhed]
Alt, hvad du udfylder her, bliver i browseren på denne enhed. Bruger du også Diana på en anden enhed? Så udfyld det dér igen. Diana har ingen konto til at forbinde dem. Se {{link:help/data-and-limits}}.
:::
'''},
'settings/your-station': {'title': 'Din station', 'desc': 'Kaldesignal, portabelt kaldesignal og locator, og sådan læser du positionslinjen.', 'body': '''
**Indstillinger** › **Din station**. Hvem du er, og cirka hvor du er.

| Felt | Hvad du udfylder | Hvad Diana gør med det |
|---|---|---|
| **Kaldesignal** | Dit normale kaldesignal, fx `OZ1ABC`. | Bruges som spotter og afgør, hvilket land Diana foreslår. |
| **Portabelt kaldesignal** | Det, du bruger i felten, fx `OZ1ABC/P`. | Udfyldes som aktivator, når du spotter dig selv eller annoncerer. |
| **Maidenhead-locator** | Seks tegn, fx `JO55WM`. | Dit udgangspunkt, så længe der ikke er GPS: til kortet, afstandene og linjerne til spots. |

*"Ikke en gyldig locator (fx JO21EE)"* betyder en tastefejl: to bogstaver, to cifre, to bogstaver.

## Hent locatoren fra GPS

1. Stil dig dér, hvor du vil have locatoren for, helst udendørs.
2. Tryk på **Hent fra GPS**.
3. Diana udfylder locatoren ud fra din nuværende position.

## Positionslinjen

Under locatoren står en linje med, hvor god din seneste position var, fx *"Seneste position: ±8 m · for 2 min siden"*.

| Du læser | Hvad det betyder | Hvad du gør |
|---|---|---|
| ±10 m eller bedre | Satellitter. Fint. | Intet. |
| omkring ±50 til 100 m | Som regel wifi, indendørs. | Prøv udenfor. |
| For grov til at afgøre, om du står i et område | Ikke godt nok til inde eller ude. | Gå udenfor med åben himmel. |
| Forbliver grov også udenfor | Webstedet må måske kun bruge en omtrentlig placering. | Tjek placeringsindstillingen på din telefon: {{link:help/location-problems}}. |
| *"Endnu ingen GPS-position på denne enhed."* | Placering ikke tilladt, eller ikke spurgt endnu. | Tillad placering, eller brug din locator. |

:::note
Der er ingen indstilling for, hvor kortet åbner. Det åbner altid, hvor du er, ellers ved din locator, ellers i dit kaldesignals land.
:::
'''},
'settings/your-country': {'title': 'Dit land', 'desc': 'Hvilket land Diana indlæser i detaljer, og hvordan det adskiller sig fra spotfilteret.', 'body': '''
**Indstillinger** › **Dit land**. Ét valg for det hele: hvilket land Diana indlæser med dets rigtige grænser, og hvilke spots og agendaposter din landeknap viser. For andre lande viser Diana altid kun punkter.

## De to dele

| Del | Hvad den gør |
|---|---|
| **Land** | Det land, der indlæses i detaljer. I listen står **Med grænser** eller **Kun punkter**. |
| **Vis** | Dit land eller **Globalt**. Filteret på Spots-skærmen, den samme kontakt som på den skærm. |

Under listen siger Diana, hvad den har for det land, fx *"OZFF, … områder med grænser indlæst"*, eller at der ikke er grænser for OKFF, kun punkter på kortet.

## Hvornår du ændrer det

- **Du rejser til udlandet**: vælg det land, du besøger. Har Diana dets grænser, vises områderne dér i fuld form. Se {{link:travel/abroad}}.
- **Du er interesseret i en reference på den anden side af grænsen**: tryk på dens blå prik og brug **Vis [land] i detaljer**; det gør det samme som at ændre det her.

## Trin for trin

1. Tryk på **Indstillinger** nederst til højre.
2. Åbn listen under **Dit land** og vælg landet.
3. Ændringen sker med det samme. Læs linjen under listen for at se, hvad der blev indlæst.
4. Vil du have spots fra hele verden eller kun fra det land? Vælg det under **Vis**.

:::note
At vælge et andet land ændrer aldrig **Vis**. Og omvendt: at skifte spotfilteret indlæser ikke et andet land.
:::

Hvorfor en reference er et område eller en prik: {{link:map/points-and-areas}}.
'''},
'settings/quick-words': {'title': 'Hurtige ord til en spot', 'desc': 'Fem ord, du tilføjer til bemærkningen i et spot med ét tryk.', 'body': '''
**Indstillinger** › **Hurtige ord til en spot**. Fem ord, du kan tilføje til bemærkningen i et spot med ét tryk, så du ikke skal skrive i felten.

## Opsætning

1. Udfyld op til fem felter, hvert med ét ord eller en kort vending.
2. Et tomt felt giver simpelthen ingen knap.
3. Når du spotter dig selv, vises de som knapper under bemærkningen. Se {{link:spots/spot-yourself}}.

## Idéer

Udfyld det, der passer til din station: en mode, din effekt, antennen, en kort status. Hold dem korte: en bemærkning har højst 100 tegn.

:::caution
Ingen tak og ingen ønsker om bånd: et spot går til DX-clusteret, hvor det bare er støj.
:::
'''},
'settings/field-info-distance': {'title': 'Afstand for Feltinfo', 'desc': 'Hvor langt omkring dig fanen Områder kigger.', 'body': '''
**Indstillinger** › **Feltinfo**. Hvor langt omkring din position fanen **Områder** i Feltinfo kigger: **10, 25, 50 eller 100 km**.

| Vælg | Hvornår |
|---|---|
| **10 km** | Mange områder tæt sammen, som i Flandern. En kort, overskuelig liste. |
| **25 km** | En god mellemvej de fleste steder. |
| **50 km** | Færre områder omkring dig, eller du er villig til at køre. |
| **100 km** | På landet, eller i udlandet med få referencer. |

Listen viser højst hundrede linjer ad gangen; **Vis mere** giver resten. Se {{link:field-info/areas-nearby}}.
'''},
'settings/band-list': {'title': 'Båndliste ved annoncering', 'desc': 'Alle bånd eller kun HF i båndlisten i annonceringsformularen.', 'body': '''
**Indstillinger** › **Båndliste ved annoncering**. Hvilke bånd listen på annonceringsskærmen tilbyder.

| Valg | Bånd |
|---|---|
| **Alle bånd** | 160 m til 23 cm. |
| **Kun HF** | 80, 40, 30, 20, 15 og 10 m. |

Næsten alle aktiveringer foregår på HF-båndene. Med **Kun HF** bliver listen kort, og du skal scrolle mindre på telefonen. Kører du også VHF eller UHF? Vælg **Alle bånd**.

Se {{link:spots/announce}}.
'''},
'settings/language': {'title': 'Sprog', 'desc': 'Vælg appens sprog.', 'body': '''
**Indstillinger** › **Sprog**. Diana taler engelsk, hollandsk, fransk, tysk, dansk, italiensk, spansk og portugisisk.

- Vælg et af de otte, eller **Følg browseren** for at bruge din browsers sprog.
- Uden et valg starter Diana på engelsk.
- Du kan også skifte sprog under **≡** på kortet, eller i guidens første trin.

Alt skifter med det samme. Områdenavne oversættes aldrig: det er officielle navne, og de hører hjemme i din log præcis som de er udgivet.

:::note
"Nyheder" (udgivelsesnoterne) findes kun på hollandsk og engelsk.
:::
'''},
'settings/privacy-settings': {'title': 'Privatliv og statistik', 'desc': 'Privatlivssiden, dit valg om statistik og at rydde alt.', 'body': '''
**Indstillinger** › **Privatliv**. Hvad Diana gemmer, hvad den sender, og dit valg om anonym statistik.

## Hvad du finder her

- **Åbn privatlivssiden**: hvilke tjenester Diana taler med og hvorfor. Resumé i {{link:start/privacy}}.
- **Anonym statistik**: **Ja, jeg hjælper gerne** eller **Nej, hellere ikke**. Skift når som helst.
- **Ryd alt på denne enhed**: fjerner alt, hvad Diana har gemt her.

## Skift dit valg om statistik

1. Tryk på **Indstillinger** › **Privatliv**.
2. Tryk på **Ja, jeg hjælper gerne** eller **Nej, hellere ikke**.
3. Du ser *"Gemt."*. Det er det hele.

:::tip[Hvorfor et ja hjælper]
Statistikken tælles med Umami: ingen cookies, ingen profil, intet der identificerer dig. For de frivillige bag Diana er det den eneste måde at vide, at appen bliver brugt, og hvilke skærme der betyder noget. Diana virker præcis ens i begge tilfælde.
:::

## Ryd alt

1. Tryk på **Ryd alt på denne enhed**.
2. Diana beder om en bekræftelse: det fjerner dit kaldesignal, dine indstillinger, offline-kortfliser og dit valg om statistik.
3. Bekræft. Diana starter forfra ved velkomstskærmen.

Brug det, når du giver din enhed videre, eller vil starte forfra.
'''},
'settings/version-and-updates': {'title': 'Version og opdateringer', 'desc': 'Sådan læser du versionslinjen, søger efter opdateringer og kører guiden igen.', 'body': '''
Helt nederst i **Indstillinger**: hvilken version du har, hvor friske dataene er, og om der er noget nyt.

## Sådan læser du versionslinjen

`v2.2.12 · 6757ec3 · 14/11/2026`

| Del | Betydning |
|---|---|
| `v2.2.12` | Appens version. |
| `6757ec3` | En kode for netop dette build af appen. |
| `14/11/2026` | Datoen for den udgivelse. |

Koden ændrer sig kun, når selve appen ændrer sig, ikke når den natlige opdatering bringer nye data. **Datalinjen** under den siger, hvor friske kortdataene er.

## Knapperne

- **Søg efter opdateringer**: Diana ser efter, om en ny version er klar, og indlæser den.
- **Nyheder**: hvad hver version bragte, den nyeste øverst.
- **Kør opstartsguiden igen**: guiden starter fra dine nuværende indstillinger. Til sidst tilbyder den rundvisningen igen.

:::tip[Spørger nogen, hvilken version du har?]
Læs versionslinjen op. Det er præcis, hvad der skal til for at hjælpe dig.
:::

Mere om opdateringer, der ikke ser ud til at komme: {{link:help/updates}}.
'''},
}
