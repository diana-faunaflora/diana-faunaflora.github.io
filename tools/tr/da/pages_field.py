T = {
'field-info/overview': {'title': 'Feltinfo', 'desc': 'Alt om det sted, hvor du står, i tre faner.', 'body': '''
**Feltinfo** handler om det sted, hvor du står. Den har tre faner:

| Fane | Hvad den viser |
|---|---|
| **Områder** | WWFF-referencerne omkring dig. Se {{link:field-info/areas-nearby}}. |
| **Placering** | Hvor du er i radiotermer: tid, locator, zoner. Se {{link:field-info/location}}. |
| **Forhold** | Rumvejr og hvad det betyder for båndene. Se {{link:field-info/conditions-space-weather}} og {{link:field-info/conditions-bands}}. |

## Åbn Feltinfo

1. Tryk på **Feltinfo** i bjælken nederst (cirklen med en prik).
2. Tryk på den fane, du vil have, øverst: **Områder**, **Placering** eller **Forhold**.
3. Tjek under titlen, hvad Diana går ud fra: *"fra din GPS-position"* eller *"fra din locator JO55WM"*.

:::caution[Ingen position?]
Siger Diana, at den endnu ikke ved, hvor du er, så tillad placering (se {{link:start/welcome-screen}}) eller udfyld din locator under **Indstillinger** › **Din station**. Med kun en locator regner Diana fra midten af det felt, og det kan være et par kilometer ved siden af.
:::
'''},
'field-info/areas-nearby': {'title': 'Områder i nærheden', 'desc': 'WWFF-referencerne omkring dig, sorteret som du vil.', 'body': '''
Fanen **Områder** viser WWFF-referencerne omkring din position, inden for den afstand du har valgt i Indstillinger (10, 25, 50 eller 100 km). Referencer på den anden side af grænsen er også med.

{{img:phone-field-areas|Feltinfo, fanen Områder, med referencer nær Antwerpen sorteret efter afstand}}

## Én linje pr. reference

| Hvad du ser | Betydning |
|---|---|
| Reference og navn | Fx `ONFF-0842 · Boshoek`. |
| Afstand og retning | I lige linje fra dig, fx `1.5 km · 62°`. |
| Antal QSO'er | Hvor mange forbindelser der er kørt derfra ifølge WWFF-fortegnelsen. |
| Senest aktiv | Datoen for den seneste aktivering. |
| *ingen aktiveringsdato kendt* | Fortegnelsen har referencen, men ingen dato. |
| *ikke i WWFF-fortegnelsen* | Diana kender området, men fortegnelsen har intet om det. Det betyder ikke, at det aldrig er blevet aktiveret. |

## Sortering: hvilken rækkefølge skal du vælge?

| Knap | Hvornår |
|---|---|
| **Afstand** | De nærmeste først. Når du vil hurtigt i gang. |
| **Senest aktiv** | De områder, der har været længst tid ude af luften, først. Dér er et pile-up mest sandsynligt. |
| **Antal QSO'er** | De mindst kørte områder først. Når du vil give jægerne et nyt. |

## Åbn et område

1. Tryk på en linje.
2. Kortet åbner, zoomet ind på det område, med dets panel og grænse.
3. Mere end hundrede områder i nærheden? Tryk på **Vis mere** nederst.

## Ændr afstanden

**Indstillinger** › **Feltinfo** › 10, 25, 50 eller 100 km. Se {{link:settings/field-info-distance}}.

:::note
Antal QSO'er og datoerne kommer fra WWFF-fortegnelsen, opdateret hver nat. Hvor fortegnelsen intet har, siger skærmen det, i stedet for at kalde det "aldrig aktiveret".
:::
'''},
'field-info/location': {'title': 'Placering i radiotermer', 'desc': 'Tid, locator, position og zoner for det sted, hvor du står.', 'body': '''
Fanen **Placering** giver alt, hvad du har brug for om dit eget sted under en QSO eller i din log. Diana regner det ud på selve enheden, så det virker også uden dækning.

{{img:phone-field-location|Feltinfo, fanen Placering, med UTC og lokal tid, locator, nøjagtighed og zoner}}

| Felt | Sådan læser du det |
|---|---|
| **Tid** | UTC og din lokale tid med tidszone. Din log er altid i UTC. |
| **Locator** | Din Maidenhead-locator med seks tegn (`JO21FD`) og med otte (`JO21FD70`). I en QSO giver du normalt de seks. |
| **Position** | I decimalgrader og i grader, minutter og sekunder, med nøjagtigheden i meter. |
| **Zoner** | Din CQ-zone, ITU-zone og ITU-region. Belgien er CQ 14, ITU 27, region 1; Danmark er CQ 14, ITU 18. |
| *grænse tæt på: også …* | Du er tæt på en zonegrænse, eller din position er usikker. Begge numre er så mulige. |
| **Nærmeste WWFF** | De nærmeste referencer, hvor som helst i verden, i lige linje. |

:::note[Hvor zonerne kommer fra]
CQ- og ITU-zonerne kommer fra et offentligt datasæt, forenklet til omkring 3 km. Derfor nævner feltet nær en grænse også nabozonen.
:::
'''},
'field-info/conditions-space-weather': {'title': 'Forhold: rumvejr', 'label': 'Rumvejr', 'desc': 'Kp-viseren, SFI, A-indeks og solpletter, og hvad de betyder.', 'body': '''
Fanen **Forhold** starter med dagens rumvejr: en viser med **Kp-indekset** og tre tal under den.

{{img:phone-field-conditions|Feltinfo, fanen Forhold, med Kp-viseren på 2, roligt, og båndbjælkerne}}

## Kp-viseren

Kp måler, hvor uroligt Jordens magnetfelt er, på en skala fra 0 til 9. Jo lavere, jo bedre for de højere bånd. Diana viser den officielle tre-timers værdi fra NOAA, og ved siden af et skøn over de seneste minutter.

| Kp | Ord i Diana | Hvad det betyder |
|---|---|---|
| 0 til 2 | roligt | Ingen effekt. Normale forhold. |
| 3 | uroligt | Lidt uroligt. Som regel endnu ingen mærkbar effekt. |
| 4 | aktivt | 20, 15 og 10 m falder et trin. |
| 5 og 6 | storm G1, G2 | Mindre storm: 20, 15 og 10 m dårligere. 80 og 40 m mærker det næsten ikke. |
| 7 til 9 | storm G3 til G5 | Kraftig storm: alle bånd dårligere, de høje mest. |

:::note
Kp er en global værdi, ikke en måling på din position.
:::

## De tre tal

| Tal | Hvad det fortæller dig |
|---|---|
| **SFI** | Solflux. Jo højere, jo bedre åbner de høje bånd. Omkring 70 er lavt, over 150 er højt. |
| **A** | Hvor uroligt magnetfeltet har været hele dagen. Lavt er godt. |
| **Solpletter** | Følger SFI: flere solpletter, større chance for DX på de høje bånd. |

SFI, A og solpletter er dagsværdier; Diana siger, hvilken dag de er fra.

## Hvor gamle er tallene?

Under viseren står der, hvornår tallene blev opdateret, fx *"Opdateret kl. 14:37 (for 12 min siden)"*. Diana prøver at hente dem to gange i timen, men i praksis kan der gå et par timer mellem to opdateringer.

- Ældre end **otte timer**: beskeden bliver orange.
- Kp-værdi ældre end **tolv timer**: Diana siger det særskilt.

Kilden er NOAA SWPC. Hvad det betyder pr. bånd: {{link:field-info/conditions-bands}}.
'''},
'field-info/conditions-bands': {'title': 'Forhold: båndene', 'label': 'Båndbjælkerne', 'desc': 'Sådan læser du farvebjælken for hvert bånd hen over dagen.', 'body': '''
Under rumvejret viser fanen **Forhold** en farvebjælke pr. bånd: 80, 40, 20, 15 og 10 m.

## Sådan læser du en båndbjælke

1. Hver bjælke er **ét bånd**. Ved siden af båndet står, hvad det er godt til, fx *"NVIS og EU"*.
2. Bjælken løber fra venstre mod højre over fem dele af døgnet: **morgen, middag, eftermiddag, aften og nat**. Diana regner dem ud fra solopgang og solnedgang på din position.
3. **Farven** er forventningen: grøn er godt, gul middel, rød dårligt.
4. Den tynde lodrette **streg** er **nu**. Til højre står, hvad der gælder nu, fx *"nu: godt"*.

## Hvad etiketterne betyder

| Etiket | Rækkevidde |
|---|---|
| **NVIS** | Tæt på, op til omkring 400 km. Ideelt til at blive kørt inden for dit eget land. |
| **EU** | Inden for Europa. |
| **DX** | Længere væk, uden for Europa. |

| Bånd | Etiket i Diana |
|---|---|
| 80 m | NVIS, EU om natten |
| 40 m | NVIS og EU |
| 20 m | EU og DX |
| 15 m | DX |
| 10 m | DX |

:::caution[En indikation, ikke et løfte]
Bjælkerne er Dianas eget grove skøn, baseret på SFI, Kp, årstiden og tidspunktet på din position. Det er ikke en prognose fra NOAA. Et bånd, der vises som "dårligt", kan sagtens være åbent: lyt altid lige efter.
:::

:::tip[Eksempel i felten]
Kp 2, roligt, SFI 91, om aftenen i Ardennerne: 40 m står på godt og er din bedste chance for Belgien og Europa. 15 m står på dårligt om aftenen; dér behøver du ikke starte.
:::

Uden position viser Diana stadig bjælkerne, men uden stregen for nu.
'''},
}
