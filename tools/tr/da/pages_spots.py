T = {
'spots/on-air': {'title': 'Hvem er i luften', 'desc': 'Spots-skærmen: live WWFF-spots, ATNO, retning og afstand.', 'body': '''
Tryk på **Spots** i bjælken nederst. Skærmen **Spots & agenda** viser, hvem der er i luften fra et WWFF-område lige nu. Listen kommer live fra WWFF Spotline og opdateres hvert 30. sekund.

{{img:phone-spots-world|Spots-skærmen, fanen Aktiv nu, Globalt, med en liste over stationer}}

## Én linje pr. station

| Hvad du ser | Betydning |
|---|---|
| Kaldesignal | Aktivatoren, fx `F5MQU/P`. |
| Antal QSO'er | Hvor mange forbindelser der tidligere er kørt fra den reference ifølge WWFF-fortegnelsen. |
| **ATNO** i rødt | *All Time New One*: referencen er aldrig blevet aktiveret. Jægerens favorit. |
| Frekvens, mode, reference | Fx `10112 kHz · CW · FFF-4038`. |
| Minutter | Hvor længe siden spottet kom ind. |
| Retning og afstand | Fra dig, fx `191° · 440 km`. |

## Dit land eller globalt

Under fanerne vælger du **dit land** (fx OZFF) eller **Globalt**. Diana husker valget og holder det i takt med den samme indstilling i Indstillinger. Hvilket land knappen står for, følger din landeindstilling: indtil du vælger et, tager Diana det ud fra dit kaldesignal (OZ… giver OZFF, ON… ONFF, DL… DLFF).

## Åbn et spot

1. Tryk på en linje.
2. Kortet åbner, zoomet ind på det område, med et panel: frekvens og mode, reservatet, locatoren dér og din, bemærkningen, antal QSO'er, Mere info og et kompas med retningen.
3. **← Tilbage til Spots**, eller Androids tilbage-knap, bringer dig tilbage til listen.
4. **×** eller at stryge nedad lukker kun panelet og beholder kortet.

:::note[Kan Spotline ikke nås?]
Så siger skærmen det, i stedet for at vise gamle spots uden advarsel.
:::
'''},
'spots/agenda': {'title': 'Agendaen', 'desc': 'Annoncerede aktiveringer: hvem planlægger hvad, og hvornår.', 'body': '''
Tryk på fanen **Agenda** på skærmen **Spots**. Du ser alle annoncerede aktiveringer, med reference, bånd og modes, og dato og tid i UTC.

{{img:phone-agenda|Fanen Agenda med annoncerede aktiveringer}}

## Sådan læser du agendaen

- **I gang nu**: en orange prik og *"i gang til …"*.
- **Kommer senere**: gråt, med dato og starttid.
- **ATNO** i rødt: referencen er aldrig blevet aktiveret.

Dit valg mellem **dit land** og **Globalt** gælder også her.

## Åbn en annoncering

Tryk på en linje. Kortet åbner ved det område med bånd og mode, reservatet, locatoren, bemærkningen og retningen. **← Tilbage til Spots** bringer dig tilbage.

## Annoncér selv

Tryk på **+ Bebud** øverst i agendaen. Se {{link:spots/announce}}.

:::tip[Også på kortet]
Annonceringer står på kortet som en hvid prik med orange ring, med en orange stiplet linje fra dig. Se {{link:map/reading-the-map}}.
:::
'''},
'spots/spot-yourself': {'title': 'Spot dig selv', 'desc': 'Fortæl jægerne, at du er i luften, via WWFF Spotline.', 'body': '''
I luften og klar? Spot dig selv, så jægerne kan finde dig. Spottet går til WWFF Spotline og derfra videre til DX-clusteret.

{{img:phone-spot-yourself|Meld-skærmen med reference, kaldesignaler, frekvens, mode og bemærkning}}

## Trin for trin

1. Tryk på **Meld** i bjælken nederst, eller på **Spot dig selv her** i panelet for et område.
2. Tjek **referencen**. Står du i et område, eller kom du fra et panel, har Diana allerede udfyldt den og siger, hvor den kom fra.
3. Dine **kaldesignaler** kommer fra Indstillinger: det portable kaldesignal som aktivator, dit normale kaldesignal som spotter.
4. Udfyld **frekvensen** i kHz, fx `7144`, og vælg **mode**.
5. Valgfrit: en kort **bemærkning**, op til 100 tegn. Tryk på et af dine **hurtige ord** for at tilføje det med ét tryk.
6. Tryk på **Tjek**. Spotline ser på dit spot uden at placere det, og fortæller dig, hvad den mener.
7. Godkendt? Tryk på **Send spot**. Du får en bekræftelse med nummeret på dit spot.

## Hvorfor først Tjek, så Send?

Hver forespørgsel til Spotline går fra et budget, som alle brugere deler. *Tjek* sikrer, at et spot er i orden, før det koster en rigtig afsendelse. Ændrer du noget efter tjekket, lukker *Send* igen: godkendelsen gjaldt spottet, som det så ud dengang.

## Hvad Diana tjekker for dig

- Formatet på **kaldesignalet**, intervallet for **frekvensen** og længden af **bemærkningen**, ligesom Spotline.
- **Båndplanen**: en advarsel, når din mode ikke passer til segmentet for din frekvens.
- **Referencen**, mod Dianas egen liste. Det svarer med det samme, også uden dækning.

:::caution[Hvad der ikke hører hjemme i en bemærkning]
Ingen tak og ingen ønsker om bånd. Hvert spot går til DX-clusteret, hvor det bare er støj. Spotline filtrerer også upassende sprog.
:::

## Når noget går galt

- **Trykket to gange på en dårlig forbindelse?** Diana siger, at spottet allerede var der. Intet placeres to gange.
- **Afviser Spotline?** Du får Spotlines egen forklaring.
- **Virker afsendelse slet ikke?** Diana tilbyder **Send på den gamle måde**: spottet går til Spotlines egen formular i en ny fane. Du ser selv deres svar, men Diana kan ikke bekræfte det.

Ikke i luften endnu, kun ved at planlægge? Brug agendaen: {{link:spots/announce}}.
'''},
'spots/announce': {'title': 'Annoncér en aktivering', 'desc': 'Sæt en planlagt aktivering i WWFF-agendaen, og gem din PIN-kode.', 'body': '''
Planlægger du en aktivering? Annoncér den, så jægerne er klar. Annonceringen går til WWFF-agendaen på Spotline.

{{img:phone-announce|Bebud-skærmen med kaldesignaler, reference, start og slut, bånd og modes}}

## Tre veje ind

- **Agenda** i bjælken nederst.
- **+ Bebud** på fanen Agenda på Spots-skærmen.
- **Annoncér en aktivering** i panelet for et område: så er referencen allerede udfyldt.

## Trin for trin

1. Tjek **aktivatorens kaldesignal** og **dit eget kaldesignal**. En anden må gerne annoncere for en aktivator.
2. Udfyld **WWFF-referencen**, fx `OZFF-0012`.
3. Vælg **start** og **slut**. Du vælger dem efter uret på din egen enhed; Diana regner dem om til UTC, før de forlader din enhed.
4. Valgfrit: sæt kryds ved **bånd** og **modes** (flere er muligt, fx *40 m, 20 m · CW, SSB*) og tilføj en bemærkning.
5. Tryk på **Tjek**, og når den er godkendt, på **Send bebudelse**.
6. **Skriv din PIN-kode ned.**

:::danger[Gem din PIN-kode]
PIN-koden er den eneste måde at ændre eller aflyse denne annoncering senere, på Spotlines eget websted. Diana kan ikke gøre det for dig, og en mistet PIN-kode kan ikke gendannes. Derfor fører Diana under formularen en liste over alt, hvad du har annonceret fra denne enhed (reference, dato, PIN). Tryk på **✕** for at fjerne en linje. Den liste findes kun på denne enhed.
:::

## Begrænsninger

- Højst **én måned** frem, og slut ikke før start. Spotline bruger de samme regler.
- Højst **16 annonceringer om dagen** fra én enhed via Diana, for at beskytte det fælles budget. Normalt brug ligger langt under.
- Der er ingen "gammel måde" for annonceringer. Virker det ikke, så prøv igen senere.

Hvilke bånd listen tilbyder (alle, eller kun HF), er en indstilling: {{link:settings/band-list}}.
'''},
}
