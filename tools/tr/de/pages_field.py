T = {
'field-info/overview': {'title': 'Feldinfo', 'desc': 'Alles über den Ort, an dem du stehst, in drei Reitern.', 'body': '''
**Feldinfo** handelt von dem Ort, an dem du stehst. Sie hat drei Reiter:

| Reiter | Was er zeigt |
|---|---|
| **Gebiete** | Die WWFF-Referenzen um dich herum. Siehe {{link:field-info/areas-nearby}}. |
| **Standort** | Wo du in Funkbegriffen stehst: Zeit, Locator, Zonen. Siehe {{link:field-info/location}}. |
| **Bedingungen** | Weltraumwetter und was es für die Bänder bedeutet. Siehe {{link:field-info/conditions-space-weather}} und {{link:field-info/conditions-bands}}. |

## Feldinfo öffnen

1. Tippe unten auf **Feldinfo** (der Kreis mit einem Punkt).
2. Tippe oben auf den gewünschten Reiter: **Gebiete**, **Standort** oder **Bedingungen**.
3. Prüfe unter dem Titel, wovon Diana ausgeht: *„ab deiner GPS-Position“* oder *„ab deinem Locator JO31AB“*.

:::caution[Keine Position?]
Steht da, dass Diana noch nicht weiß, wo du bist, dann erlaube den Standort (siehe {{link:start/welcome-screen}}) oder trage deinen Locator unter **Einstellungen** › **Ihre Station** ein. Mit nur einem Locator rechnet Diana ab der Mitte dieses Feldes, und das kann ein paar Kilometer daneben liegen.
:::
'''},
'field-info/areas-nearby': {'title': 'Gebiete in der Nähe', 'desc': 'Die WWFF-Referenzen um dich herum, sortiert, wie du willst.', 'body': '''
Der Reiter **Gebiete** listet die WWFF-Referenzen um deine Position auf, innerhalb der Entfernung, die du in den Einstellungen gewählt hast (10, 25, 50 oder 100 km). Referenzen jenseits der Grenze sind auch dabei.

{{img:phone-field-areas|Feldinfo, Reiter Gebiete, mit Referenzen bei Antwerpen nach Entfernung sortiert}}

## Eine Zeile pro Referenz

| Was du siehst | Bedeutung |
|---|---|
| Referenz und Name | Zum Beispiel `ONFF-0842 · Boshoek`. |
| Entfernung und Richtung | In Luftlinie von dir, zum Beispiel `1.5 km · 62°`. |
| Anzahl QSOs | Wie viele Verbindungen laut WWFF-Verzeichnis von dort gemacht wurden. |
| Zuletzt aktiv | Das Datum der letzten Aktivierung. |
| *kein Aktivierungsdatum bekannt* | Das Verzeichnis kennt die Referenz, aber kein Datum. |
| *nicht im WWFF-Verzeichnis* | Diana kennt das Gebiet, aber das Verzeichnis hat nichts dazu. Das heißt nicht, dass es nie aktiviert wurde. |

## Sortieren: welche Reihenfolge wählen?

| Schaltfläche | Wann sinnvoll |
|---|---|
| **Entfernung** | Das nächste zuerst. Wenn du schnell aufbauen willst. |
| **Zuletzt aktiv** | Die Gebiete, die am längsten nicht in der Luft waren, zuerst. Dort ist ein Pile-up am wahrscheinlichsten. |
| **Anzahl QSOs** | Die am wenigsten gearbeiteten Gebiete zuerst. Wenn du den Jägern ein neues geben willst. |

## Ein Gebiet öffnen

1. Tippe auf eine Zeile.
2. Die Karte öffnet sich, auf dieses Gebiet gezoomt, mit seinem Fenster und seiner Grenze.
3. Mehr als hundert Gebiete in der Nähe? Tippe unten auf **weitere anzeigen**.

## Die Entfernung ändern

**Einstellungen** › **Feldinfo** › 10, 25, 50 oder 100 km. Siehe {{link:settings/field-info-distance}}.

:::note
Die Anzahl QSOs und die Daten kommen aus dem WWFF-Verzeichnis, jede Nacht aktualisiert. Wo das Verzeichnis nichts hat, sagt der Bildschirm das, statt „nie aktiviert“ zu behaupten.
:::
'''},
'field-info/location': {'title': 'Standort in Funkbegriffen', 'desc': 'Zeit, Locator, Position und Zonen des Ortes, an dem du stehst.', 'body': '''
Der Reiter **Standort** gibt dir alles, was du über deinen eigenen Platz während eines QSOs oder für dein Log brauchst. Diana berechnet es auf deinem Gerät selbst, also klappt es auch ohne Empfang.

{{img:phone-field-location|Feldinfo, Reiter Standort, mit UTC und Ortszeit, Locator, Genauigkeit und Zonen}}

| Feld | Wie du es liest |
|---|---|
| **Zeit** | UTC und deine Ortszeit mit Zeitzone. Dein Log ist immer in UTC. |
| **Locator** | Dein Maidenhead-Locator mit sechs Zeichen (`JO21FD`) und mit acht (`JO21FD70`). Im QSO gibst du meist die sechs. |
| **Position** | In Dezimalgrad und in Grad, Minuten und Sekunden, mit der Genauigkeit in Metern. |
| **Zonen** | Deine CQ-Zone, ITU-Zone und ITU-Region. Belgien ist CQ 14, ITU 27, Region 1; Deutschland ebenfalls CQ 14, ITU 28. |
| *Grenze in der Nähe: auch …* | Du bist nah an einer Zonengrenze, oder deine Position ist unsicher. Dann sind beide Nummern möglich. |
| **Nächste WWFF** | Die nächsten Referenzen, überall auf der Welt, in Luftlinie. |

:::note[Woher die Zonen kommen]
Die CQ- und ITU-Zonen stammen aus einem öffentlichen Datensatz, vereinfacht auf etwa 3 km. Deshalb nennt das Feld nahe einer Grenze auch die Nachbarzone.
:::
'''},
'field-info/conditions-space-weather': {'title': 'Bedingungen: Weltraumwetter', 'label': 'Weltraumwetter', 'desc': 'Die Kp-Anzeige, SFI, A-Index und Sonnenflecken, und was sie bedeuten.', 'body': '''
Der Reiter **Bedingungen** beginnt mit dem heutigen Weltraumwetter: eine Anzeige mit dem **Kp-Index** und drei Zahlen darunter.

{{img:phone-field-conditions|Feldinfo, Reiter Bedingungen, mit der Kp-Anzeige auf 2, ruhig, und den Bandbalken}}

## Die Kp-Anzeige

Kp misst, wie unruhig das Erdmagnetfeld ist, auf einer Skala von 0 bis 9. Je niedriger, desto besser für die höheren Bänder. Diana zeigt den offiziellen Dreistundenwert von NOAA, und daneben eine Schätzung der letzten Minuten.

| Kp | Wort in Diana | Was es bedeutet |
|---|---|---|
| 0 bis 2 | ruhig | Kein Einfluss. Normale Bedingungen. |
| 3 | unruhig | Leicht unruhig. Meist noch kein spürbarer Effekt. |
| 4 | aktiv | 20, 15 und 10 m gehen eine Stufe zurück. |
| 5 und 6 | Sturm G1, G2 | Kleiner Sturm: 20, 15 und 10 m schlechter. 80 und 40 m merken kaum etwas. |
| 7 bis 9 | Sturm G3 bis G5 | Starker Sturm: alle Bänder schlechter, die hohen am meisten. |

:::note
Kp ist ein weltweiter Wert, keine Messung an deinem Standort.
:::

## Die drei Zahlen

| Zahl | Was sie dir sagt |
|---|---|
| **SFI** | Solarer Flux. Je höher, desto besser öffnen die hohen Bänder. Um 70 ist niedrig, über 150 ist hoch. |
| **A** | Wie unruhig das Magnetfeld über den ganzen Tag war. Niedrig ist gut. |
| **Sonnenflecken** | Geht mit dem SFI einher: mehr Sonnenflecken, mehr Chancen auf DX auf den hohen Bändern. |

SFI, A und Sonnenflecken sind Tageswerte; Diana sagt, von welchem Tag sie stammen.

## Wie alt sind die Zahlen?

Unter der Anzeige steht, wann die Zahlen aktualisiert wurden, zum Beispiel *„Aktualisiert um 14:37 (vor 12 Min.)“*. Diana versucht sie zweimal pro Stunde zu holen, aber in der Praxis können zwischen zwei Aktualisierungen ein paar Stunden liegen.

- Älter als **acht Stunden**: die Meldung wird orange.
- Kp-Wert älter als **zwölf Stunden**: Diana sagt das gesondert.

Die Quelle ist NOAA SWPC. Was es pro Band bedeutet: {{link:field-info/conditions-bands}}.
'''},
'field-info/conditions-bands': {'title': 'Bedingungen: die Bänder', 'label': 'Die Bandbalken', 'desc': 'Wie du den Farbbalken jedes Bandes über den Tag liest.', 'body': '''
Unter dem Weltraumwetter zeigt der Reiter **Bedingungen** einen Farbbalken pro Band: 80, 40, 20, 15 und 10 m.

## Einen Bandbalken lesen

1. Jeder Balken ist **ein Band**. Neben dem Band steht, wofür es gut ist, zum Beispiel *„NVIS und EU“*.
2. Der Balken läuft von links nach rechts über fünf Tageszeiten: **Morgen, Mittag, Nachmittag, Abend und Nacht**. Diana berechnet sie aus Sonnenaufgang und Sonnenuntergang an deinem Standort.
3. Die **Farbe** ist die Erwartung: grün ist gut, gelb mäßig, rot schlecht.
4. Der dünne senkrechte **Strich** ist **jetzt**. Rechts steht, was jetzt gilt, zum Beispiel *„jetzt: gut“*.

## Was die Beschriftungen bedeuten

| Beschriftung | Reichweite |
|---|---|
| **NVIS** | In der Nähe, bis etwa 400 km. Ideal, um im eigenen Land gearbeitet zu werden. |
| **EU** | Innerhalb Europas. |
| **DX** | Weiter weg, außerhalb Europas. |

| Band | Beschriftung in Diana |
|---|---|
| 80 m | NVIS, EU nachts |
| 40 m | NVIS und EU |
| 20 m | EU und DX |
| 15 m | DX |
| 10 m | DX |

:::caution[Ein Richtwert, kein Versprechen]
Die Balken sind Dianas eigene grobe Schätzung, auf Basis von SFI, Kp, Jahreszeit und Tageszeit an deinem Standort. Es ist keine NOAA-Vorhersage. Ein Band, das als „schlecht“ angezeigt wird, kann trotzdem offen sein: hör immer kurz hinein.
:::

:::tip[Beispiel im Gelände]
Kp 2, ruhig, SFI 91, abends in den Ardennen: 40 m steht auf gut und ist deine beste Chance für Belgien und Europa. 15 m steht abends auf schlecht; dort brauchst du nicht anzufangen.
:::

Ohne Position zeigt Diana die Balken trotzdem, aber ohne den Strich für jetzt.
'''},
}
