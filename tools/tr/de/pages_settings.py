T = {
'settings/overview': {'title': 'Einstellungen', 'desc': 'Wie du die Einstellungen öffnest, und wofür jeder Teil da ist.', 'body': '''
Alles, was du im Assistenten eingerichtet hast, und noch ein bisschen mehr, steht unter **Einstellungen**.

{{img:phone-settings|Der Einstellungen-Bildschirm mit Ihre Station und Ihr Land}}

## Einstellungen öffnen

1. Tippe unten auf **Einstellungen** (das Zahnrad, ganz rechts).
2. Scrolle zu dem Teil, den du ändern willst.
3. Ändere ihn. Alles wird sofort gespeichert: es gibt keine Speichern-Schaltfläche. Kurz erscheint *„Auf diesem Gerät gespeichert“*.

## Was drinsteht

| Teil | Was du einstellst | Seite |
|---|---|---|
| **Ihre Station** | Rufzeichen, Portable-Rufzeichen, Locator | {{link:settings/your-station}} |
| **Ihr Land** | Welches Land im Detail geladen wird, und der Spotfilter | {{link:settings/your-country}} |
| **Schnellwörter für einen Spot** | Fünf Wörter zum Hinzufügen mit einem Tippen | {{link:settings/quick-words}} |
| **Feldinfo** | Wie weit der Reiter Gebiete um dich herum schaut | {{link:settings/field-info-distance}} |
| **Bandliste beim Ankündigen** | Alle Bänder oder nur KW | {{link:settings/band-list}} |
| **Sprache** | Eine von acht, oder dem Browser folgen | {{link:settings/language}} |
| **Datenschutz** | Datenschutzseite, Statistik, alles löschen | {{link:settings/privacy-settings}} |
| **Als App installieren** | Auf diesem Gerät installieren | {{link:start/install-android}} |
| Ganz unten | Version, Updates, Was ist neu, Assistent erneut starten | {{link:settings/version-and-updates}} |

:::caution[Nur auf diesem Gerät]
Alles, was du hier eingibst, bleibt im Browser dieses Geräts. Nutzt du Diana auch auf einem anderen Gerät? Dann trag es dort noch einmal ein. Diana hat kein Konto, um Geräte zu verbinden. Siehe {{link:help/data-and-limits}}.
:::
'''},
'settings/your-station': {'title': 'Deine Station', 'desc': 'Rufzeichen, Portable-Rufzeichen und Locator, und wie du die Positionszeile liest.', 'body': '''
**Einstellungen** › **Ihre Station**. Wer du bist und ungefähr wo du bist.

| Feld | Was du einträgst | Was Diana damit macht |
|---|---|---|
| **Rufzeichen** | Dein normales Rufzeichen, zum Beispiel `DL1ABC`. | Wird als Spotter verwendet und bestimmt, welches Land Diana vorschlägt. |
| **Portable-Rufzeichen** | Was du im Gelände verwendest, zum Beispiel `DL1ABC/P`. | Wird als Aktivierer eingetragen, wenn du dich selbst spottest oder ankündigst. |
| **Maidenhead-Locator** | Sechs Zeichen, zum Beispiel `JO31AB`. | Dein Ausgangspunkt, solange es kein GPS gibt: für die Karte, die Entfernungen und die Linien zu den Spots. |

*„Kein gültiger Locator (z. B. JO21EE)“* heißt Tippfehler: zwei Buchstaben, zwei Ziffern, zwei Buchstaben.

## Den Locator aus dem GPS übernehmen

1. Stell dich dorthin, wofür du den Locator willst, möglichst draußen.
2. Tippe auf **Aus GPS übernehmen**.
3. Diana trägt den Locator aus deiner aktuellen Position ein.

## Die Positionszeile

Unter dem Locator sagt eine Zeile, wie gut deine letzte Position war, zum Beispiel *„Letzte Position: ±8 m · vor 2 Min.“*.

| Du liest | Was es bedeutet | Was tun |
|---|---|---|
| ±10 m oder besser | Satelliten. In Ordnung. | Nichts. |
| etwa ±50 bis 100 m | Meist WLAN, drinnen. | Draußen versuchen. |
| Zu grob, um zu sagen, ob du in einem Gebiet stehst | Nicht gut genug für drin oder draußen. | Nach draußen gehen, mit freiem Himmel. |
| Bleibt auch draußen grob | Die Seite darf vielleicht nur einen ungefähren Standort verwenden. | Die Standorteinstellung deines Smartphones prüfen: {{link:help/location-problems}}. |
| *„Noch keine GPS-Position auf diesem Gerät.“* | Standort nicht erlaubt, oder noch nicht gefragt. | Standort erlauben, oder auf deinen Locator setzen. |

:::note
Es gibt keine Einstellung dafür, wo die Karte startet. Sie öffnet immer dort, wo du bist, sonst bei deinem Locator, sonst im Land deines Rufzeichens.
:::
'''},
'settings/your-country': {'title': 'Dein Land', 'desc': 'Welches Land Diana im Detail lädt, und wie es sich vom Spotfilter unterscheidet.', 'body': '''
**Einstellungen** › **Ihr Land**. Eine Wahl für alles: welches Land Diana mit seinen echten Grenzen lädt, und welche Spots und Agendaeinträge deine Länderschaltfläche zeigt. Von anderen Ländern zeigt Diana immer nur Punkte.

## Die zwei Teile

| Teil | Was er tut |
|---|---|
| **Land** | Das Land, das im Detail geladen wird. In der Liste steht **Mit Grenzen** oder **Nur Punkte**. |
| **Anzeigen** | Dein Land oder **Weltweit**. Der Filter für den Spots-Bildschirm, derselbe Schalter wie auf diesem Bildschirm. |

Unter der Liste sagt Diana, was sie für dieses Land hat, zum Beispiel *„DLFF, … Gebiete mit Grenzen geladen“* oder dass es für OKFF keine Grenzen gibt, nur Punkte auf der Karte.

## Wann du es änderst

- **Du fährst ins Ausland**: wähle das Land, das du besuchst. Hat Diana seine Grenzen, erscheinen die Gebiete dort vollständig. Siehe {{link:travel/abroad}}.
- **Dich interessiert eine Referenz jenseits der Grenze**: tippe auf ihren blauen Punkt und nimm **[Land] im Detail zeigen**; das tut dasselbe wie eine Änderung hier.

## Schritt für Schritt

1. Tippe unten rechts auf **Einstellungen**.
2. Öffne die Liste unter **Ihr Land** und wähle das Land.
3. Die Änderung gilt sofort. Lies die Zeile unter der Liste, um zu sehen, was geladen wurde.
4. Spots weltweit oder nur aus diesem Land? Wähle es unter **Anzeigen**.

:::note
Ein anderes Land zu wählen ändert **Anzeigen** nie. Und umgekehrt: den Spotfilter umzuschalten lädt kein anderes Land.
:::

Warum eine Referenz eine Fläche oder ein Punkt ist: {{link:map/points-and-areas}}.
'''},
'settings/quick-words': {'title': 'Schnellwörter für einen Spot', 'desc': 'Fünf Wörter, die du mit einem Tippen zur Bemerkung eines Spots hinzufügst.', 'body': '''
**Einstellungen** › **Schnellwörter für einen Spot**. Fünf Wörter, die du mit einem Tippen zur Bemerkung eines Spots hinzufügen kannst, damit du im Gelände nicht tippen musst.

## Einrichten

1. Fülle bis zu fünf Felder aus, jedes mit einem Wort oder einem kurzen Ausdruck.
2. Ein leeres Feld ergibt einfach keine Taste.
3. Wenn du dich selbst spottest, erscheinen sie als Tasten unter der Bemerkung. Siehe {{link:spots/spot-yourself}}.

## Ideen

Trag ein, was zu deiner Station passt: eine Betriebsart, deine Leistung, die Antenne, einen kurzen Status. Halte sie kurz: eine Bemerkung hat höchstens 100 Zeichen.

:::caution
Kein Dankeschön und keine Bandwünsche: ein Spot geht in den DX-Cluster, wo so etwas nur Rauschen ist.
:::
'''},
'settings/field-info-distance': {'title': 'Entfernung für die Feldinfo', 'desc': 'Wie weit der Reiter Gebiete um dich herum schaut.', 'body': '''
**Einstellungen** › **Feldinfo**. Wie weit der Reiter **Gebiete** der Feldinfo um deine Position herum schaut: **10, 25, 50 oder 100 km**.

| Wähle | Wann |
|---|---|
| **10 km** | Viele Gebiete dicht beieinander, wie in Flandern. Eine kurze, übersichtliche Liste. |
| **25 km** | Ein guter Mittelweg für die meisten Orte. |
| **50 km** | Weniger Gebiete in der Umgebung, oder du fährst gern ein Stück. |
| **100 km** | Auf dem Land, oder im Ausland mit wenigen Referenzen. |

Die Liste zeigt höchstens hundert Zeilen auf einmal; **weitere anzeigen** gibt den Rest. Siehe {{link:field-info/areas-nearby}}.
'''},
'settings/band-list': {'title': 'Bandliste beim Ankündigen', 'desc': 'Alle Bänder oder nur KW in der Bandliste des Ankündigungsformulars.', 'body': '''
**Einstellungen** › **Bandliste beim Ankündigen**. Welche Bänder die Liste im Ankündigungsfenster anbietet.

| Wahl | Bänder |
|---|---|
| **Alle Bänder** | 160 m bis 23 cm. |
| **Nur KW** | 80, 40, 30, 20, 15 und 10 m. |

Fast jede Aktivierung findet auf den KW-Bändern statt. Mit **Nur KW** bleibt die Liste kurz und du scrollst auf dem Smartphone weniger. Arbeitest du auch auf UKW? Dann wähle **Alle Bänder**.

Siehe {{link:spots/announce}}.
'''},
'settings/language': {'title': 'Sprache', 'desc': 'Die Sprache der App wählen.', 'body': '''
**Einstellungen** › **Sprache**. Diana spricht Englisch, Niederländisch, Französisch, Deutsch, Dänisch, Italienisch, Spanisch und Portugiesisch.

- Wähle eine der acht, oder **Dem Browser folgen**, um die Sprache deines Browsers zu nehmen.
- Ohne Wahl startet Diana auf Englisch.
- Du kannst die Sprache auch unter **≡** auf der Karte wechseln, oder im ersten Schritt des Assistenten.

Alles wechselt sofort. Gebietsnamen werden nie übersetzt: es sind offizielle Namen, und sie gehören genau so in dein Log, wie sie veröffentlicht sind.

:::note
„Was ist neu“ (die Versionshinweise) gibt es nur auf Niederländisch und Englisch.
:::
'''},
'settings/privacy-settings': {'title': 'Datenschutz und Statistik', 'desc': 'Die Datenschutzseite, deine Statistik-Wahl und alles löschen.', 'body': '''
**Einstellungen** › **Datenschutz**. Was Diana speichert, was sie sendet, und deine Wahl zur anonymen Statistik.

## Was du hier findest

- **Datenschutzseite öffnen**: mit welchen Diensten Diana spricht und warum. Zusammenfassung unter {{link:start/privacy}}.
- **Anonyme Statistiken**: **Ja, ich helfe mit** oder **Nein, lieber nicht**. Jederzeit änderbar.
- **Alles auf diesem Gerät löschen**: entfernt alles, was Diana hier gespeichert hat.

## Deine Statistik-Wahl ändern

1. Tippe auf **Einstellungen** › **Datenschutz**.
2. Tippe auf **Ja, ich helfe mit** oder **Nein, lieber nicht**.
3. Du siehst *„Gespeichert.“*. Das war es.

:::tip[Warum ein Ja hilft]
Die Statistik wird mit Umami gezählt: keine Cookies, kein Profil, nichts, was dich identifiziert. Für die Ehrenamtlichen hinter Diana ist es der einzige Weg zu wissen, dass die App genutzt wird und welche Bildschirme wichtig sind. Diana funktioniert in beiden Fällen genau gleich.
:::

## Alles löschen

1. Tippe auf **Alles auf diesem Gerät löschen**.
2. Diana fragt nach einer Bestätigung: das entfernt dein Rufzeichen, deine Einstellungen, die Offline-Kartenkacheln und deine Statistik-Wahl.
3. Bestätige. Diana beginnt wieder beim Willkommensbildschirm.

Nutze das, wenn du dein Gerät weitergibst oder neu anfangen willst.
'''},
'settings/version-and-updates': {'title': 'Version und Updates', 'desc': 'Die Versionszeile lesen, nach Updates suchen und den Assistenten erneut starten.', 'body': '''
Ganz unten in den **Einstellungen**: welche Version du hast, wie frisch die Daten sind, und ob es etwas Neues gibt.

## Die Versionszeile lesen

`v2.2.12 · 6757ec3 · 14/11/2026`

| Teil | Bedeutung |
|---|---|
| `v2.2.12` | Die Version der App. |
| `6757ec3` | Ein Code für genau diesen Build der App. |
| `14/11/2026` | Das Datum dieser Version. |

Der Code ändert sich nur, wenn sich die App selbst ändert, nicht wenn die nächtliche Aktualisierung neue Daten bringt. Die **Datenzeile** darunter sagt, wie frisch die Kartendaten sind.

## Die Schaltflächen

- **Nach Updates suchen**: Diana schaut, ob eine neue Version bereitliegt, und lädt sie.
- **Was ist neu**: was jede Version gebracht hat, die neueste oben.
- **Startassistent erneut durchlaufen**: der Assistent startet mit deinen aktuellen Einstellungen. Am Ende bietet er den Rundgang noch einmal an.

:::tip[Jemand fragt, welche Version du hast?]
Lies die Versionszeile vor. Genau das braucht man, um dir zu helfen.
:::

Mehr zu Updates, die nicht anzukommen scheinen: {{link:help/updates}}.
'''},
}
