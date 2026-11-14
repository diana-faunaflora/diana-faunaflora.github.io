T = {
'map/map-screen': {'title': 'Der Kartenbildschirm', 'desc': 'Der Hauptbildschirm von Diana: die Schaltflächen oben und die Leiste unten.', 'body': '''
Die Karte ist der Hauptbildschirm von Diana. Alles andere beginnt hier.

{{img:phone-map|Die Karte von Diana rund um Antwerpen, mit grünen Gebieten, einem Spot und Linien}}

## Die Leiste unten

Von links nach rechts: **Karte**, **Spots**, **Melden**, **Agenda**, **Feldinfo**, **Regeln** und **Einstellungen**. Tippe auf einen Eintrag, um diesen Bildschirm zu öffnen.

:::tip[Zurück zu deiner eigenen Position]
Tippe jederzeit unten auf **Karte**: die Karte zentriert sich wieder auf deinen Standort, der Zoom bleibt, wie er ist. Diana misst die GPS-Position neu, wenn die letzte älter als zwei Minuten oder ungenauer als 30 m war. Ohne GPS zentriert sie auf deinen Locator aus den Einstellungen und sagt das auch.
:::

## Die Schaltflächen oben

| Schaltfläche | Was sie tut |
|---|---|
| **⌕** | Nach Name oder Referenznummer suchen. Siehe {{link:map/search}}. |
| **◐** | Kartenstil: Liberty, Positron, Bright oder Dark. |
| **≡** | Ebenen und Sprache. Siehe {{link:map/layers-and-styles}}. |

Oben links steht eine Zeile, wie viele Referenzen geladen sind, zum Beispiel *„947 WWFF-Gebiete · 1 ohne Grenze“*.

## Bewegen

- **Ziehe** mit einem Finger, um die Karte zu verschieben.
- **Spreize oder kneife** mit zwei Fingern zum Zoomen, oder nimm **+** und **−** rechts.
- **Tippe** auf ein Gebiet, einen Punkt oder einen Spot, um sein Fenster zu öffnen. Siehe {{link:map/area-panel}}.

## Was sehe ich?

Die Farben, Punkte und Linien erklärt {{link:map/reading-the-map}}. Warum eine Referenz eine Fläche ist und eine andere nur ein Punkt, erklärt {{link:map/points-and-areas}}.
'''},
'map/points-and-areas': {'title': 'Punkte und Flächen', 'desc': 'Warum eine Referenz eine grüne Fläche ist und eine andere ein blauer Punkt, und wie du das änderst.', 'body': '''
Auf der Karte erscheint eine WWFF-Referenz auf eine von drei Arten. Welche, hängt davon ab, was Diana über sie weiß, und von dem Land, das du gewählt hast.

| Was du siehst | Was es bedeutet | Kann Diana sagen, ob du drin stehst? |
|---|---|---|
| **Grüne Fläche** | Eine Referenz mit ihrer echten Grenze, im gewählten Land. | Ja |
| **Gestrichelter Ring mit orangem Punkt** | Eine Referenz deines Landes ohne Grenze. Nur ein ungefährer Ort. | Nein |
| **Blauer Punkt** | Eine Referenz in einem anderen Land. Dicht beieinander bilden sie einen Kreis mit Zahl. | Nein |

## Warum eine Fläche?

Eine Fläche braucht eine Grenzdatei. Diana hat solche Dateien heute für **fünf Länder**: Belgien (ONFF), die Niederlande (PAFF), Deutschland (DLFF), Dänemark (OZFF) und Portugal (CTFF), und es kommen laufend weitere hinzu. Die nationalen WWFF-Koordinatoren liefern sie.

Diana lädt die Grenzen von **jeweils einem Land**: dem, das du in den Einstellungen gewählt hast. So bleibt die Karte auf dem Smartphone schnell.

## Warum ein Punkt?

- Die Referenz liegt in einem Land, für das Diana **keine Grenzdatei** hat. Dann kennt Diana nur die Position aus dem WWFF-Verzeichnis.
- Oder das Land **hat** Grenzen in Diana, ist aber **nicht das Land, das du gewählt hast**. Dann erscheint es ebenfalls als Punkt, bis du dieses Land lädst.

## Warum ein gestrichelter Ring?

Innerhalb eines Landes mit Grenzen haben einige Referenzen keine Grenze in der Datei, zum Beispiel Überseegebiete der Niederlande. Sie erscheinen als gestrichelter Ring am ungefähren Ort.

## Die Details bekommst du immer

Egal, was du siehst: **tippe darauf**. Ein Fenster öffnet sich mit allem, was Diana weiß. Bei einem blauen Punkt sind das Referenz, Land und Name, Locator und Zonen, Richtung und Entfernung von dir, die Anzahl QSOs oder **ATNO**, wenn sie noch nie aktiviert wurde, und ein Link zu mehr Informationen. Siehe {{link:map/area-panel}}.

## Wann und wie du es änderst

Wenn du in ein anderes Land fährst, oder die echte Grenze einer Referenz sehen willst, die jetzt ein Punkt ist:

**Aus dem Fenster (am schnellsten)**

1. Tippe auf den blauen Punkt.
2. Hat Diana die Grenzen dieses Landes, sagt das Fenster es und zeigt die Schaltfläche **[Land] im Detail zeigen**.
3. Tippe darauf. Diana lädt dieses Land und öffnet dieselbe Referenz erneut, jetzt mit ihrer Grenze.

**Aus den Einstellungen**

1. Tippe unten rechts auf **Einstellungen**.
2. Wähle unter **Ihr Land** das Land. Länder mit **Mit Grenzen** bekommen ihre Flächen; **Nur Punkte** bleibt bei Punkten.
3. Die Änderung gilt sofort. Unter dem Menü sagt Diana, was geladen wurde, zum Beispiel *„PAFF, 281 Gebiete mit Grenzen geladen“*.

Dein Spotfilter (dein Land oder Weltweit) ändert sich nicht, wenn du ein anderes Land wählst. Mehr unter {{link:settings/your-country}}.

:::note[Ein neues Schutzgebiet zuerst als Punkt]
Welche Referenzen es gibt, kommt jede Nacht aus dem WWFF-Verzeichnis. Die Grenzen kommen aus einer Datei, die das Diana-Team veröffentlicht. Ein ganz neues Schutzgebiet kann deshalb zuerst als Punkt erscheinen und seinen Umriss später bekommen.
:::
'''},
'map/reading-the-map': {'title': 'Die Karte lesen', 'desc': 'Was jede Farbe, jeder Punkt und jede Linie auf der Karte bedeutet.', 'body': '''
Alles auf der Karte hat eine Bedeutung. Das ist die Legende.

{{img:map-legend|Karte rund um Antwerpen und Roosendaal mit grünen Gebieten, blauen Clustern, einer grünen gepunkteten und einer orangen gestrichelten Linie}}

## Gebiete und Referenzen

| Was du siehst | Bedeutung |
|---|---|
| Grüne Fläche mit Nummer | Eine Referenz mit ihrer echten Grenze, in deinem Land. Die Nummer ist die Referenz, zum Beispiel `ONFF-0602`. |
| Orange Umrandung | Das Gebiet, das du gerade angetippt hast. |
| Gestrichelter Ring mit orangem Punkt | Eine Referenz deines Landes ohne Grenze: ein ungefährer Ort. |
| Blauer Punkt | Eine Referenz in einem anderen Land. |
| Blauer Kreis mit Zahl | Mehrere blaue Punkte dicht beieinander. Tippe darauf zum Hineinzoomen; er teilt sich auf. |
| Graue Linie | Eine Landesgrenze auf der Grundkarte. |

Ab Zoomstufe 11 bekommt jeder Punkt seine Referenz als Beschriftung.

## Spots und Ankündigungen

| Was du siehst | Bedeutung |
|---|---|
| Grün pulsierendes Antennensymbol | Eine Station, die jetzt QRV ist, mit Rufzeichen, Frequenz und Betriebsart daneben. |
| **Grüne gepunktete Linie** | Von dir zu einer Station, die jetzt QRV ist. |
| Verblasster Spot | Ein Spot, der älter als 30 Minuten ist. |
| Weißer Punkt mit orangem Ring | Eine angekündigte Aktivierung aus der Agenda. |
| **Orange gestrichelte Linie** | Von dir zu einer angekündigten Aktivierung, beschriftet mit Rufzeichen und Uhrzeit. |
| Deine Position | Ein Marker. Ist deine Position ungenauer als etwa 10 m, zeigt ein gestrichelter Ring die Unsicherheit. |

:::tip[Zu viele Linien?]
Schalte sie aus unter **≡** › **Linien zu den Spots**. Diana merkt sich die Wahl. **⤢ Alle Spots einpassen** zeigt alle Spots und deine eigene Position auf einmal.
:::

Warum manche Referenzen Flächen sind und andere Punkte: {{link:map/points-and-areas}}.
'''},
'map/area-panel': {'title': 'Infos zu einem Gebiet', 'desc': 'Tippe ein Gebiet oder einen Punkt an: das Fenster mit allem, was Diana weiß, und von dort spotten.', 'body': '''
Tippe auf der Karte ein Gebiet, einen Punkt oder einen Spot an. Von unten gleitet ein Fenster hoch, mit allem, was Diana über diese Referenz weiß. Diana zeigt nur, was sie wirklich weiß: nie ein leeres Feld.

{{img:phone-area-panel|Fenster von ONFF-0685 Hobokense Polder mit Fläche, Verwaltung, Ausweisung, IUCN-Kategorie und Locator}}

## Was im Fenster steht

Für ein **Gebiet mit Grenze**:

- Referenz, Region und Name.
- Was die Gebietsdatei enthält: **Fläche** in Hektar, **Verwaltung**, **Ausweisung**, **IUCN-Kategorie**, **Ausgewiesen seit**. Nicht jedes Schutzgebiet hat alle Angaben; das ist eine Lücke in den Quelldaten, nicht etwas, das Diana versteckt.
- Die **Anzahl QSOs** und die **letzte Aktivierung**, aus dem WWFF-Verzeichnis.
- Der **Locator**, die **CQ-Zone**, die **ITU-Zone** und die **ITU-Region**.
- **Mehr Infos**: die Website des Schutzgebiets, wenn das WWFF-Verzeichnis eine hat. Sie öffnet sich in deinem Browser, Diana und die Karte bleiben, wo sie waren.

Für eine **Referenz ohne Grenze** (gestrichelter Ring): dasselbe Fenster ohne die Flächenangaben, und ein Hinweis, dass Diana nicht sagen kann, ob du drin stehst.

Für einen **blauen Punkt** in einem anderen Land: Referenz, Land und Name, Locator und Zonen, **Von dir** (Richtung und Entfernung), die Anzahl QSOs oder **ATNO** in Rot, wenn sie noch nie aktiviert wurde, und Mehr Infos.

## Aus dem Fenster spotten oder ankündigen

Unten in jedem Fenster stehen zwei Schaltflächen:

- **Hier selbst spotten** öffnet das Spot-Formular mit der Referenz schon ausgefüllt. Siehe {{link:spots/spot-yourself}}.
- **Aktivierung ankündigen** öffnet das Agenda-Formular mit der Referenz schon ausgefüllt. Siehe {{link:spots/announce}}.

## Das Fenster schließen

Wische das Fenster **nach unten**, oder tippe auf **×**. Die Karte bleibt, wo sie ist. Auf dem Smartphone ist immer nur ein unteres Fenster sichtbar.
'''},
'map/overlapping-areas': {'title': 'Überlappende Gebiete', 'desc': 'Wenn Referenzen übereinander liegen, und wie du zwischen ihnen wechselst.', 'body': '''
Referenzen überlappen sich manchmal: ein kleines Schutzgebiet liegt oft innerhalb eines größeren Naturgebiets. Stehst du auf diesem Stück Boden, bist du in allen gleichzeitig.

## Wie Diana das zeigt

Diana zeichnet immer das **kleinste** Gebiet obenauf, damit du es antippen kannst. Ein Tippen öffnet das kleinste Gebiet unter deinem Finger: tippe in das Schutzgebiet für das Schutzgebiet, und in das Land drumherum für das größere Gebiet.

## Zum anderen Gebiet wechseln

1. Tippe auf die Karte innerhalb des Schutzgebiets. Das Fenster des **kleinsten** Gebiets öffnet sich.
2. Scrolle im Fenster nach unten zu **„Dieser Punkt liegt auch in diesen Referenzen“**. Die anderen Gebiete stehen dort als Schaltflächen, mit Name und Größe.
3. Tippe auf eine Schaltfläche. Das Fenster zeigt jetzt dieses Gebiet, mit seiner eigenen Grenze in Orange.
4. Zurück? Dieses Fenster hat eine Schaltfläche zu dem Gebiet, von dem du kamst.

## Mit deiner GPS-Position

Stehst du in mehreren Gebieten gleichzeitig, sagt das die Infokarte unten auf der Karte, zum Beispiel *„Sie stehen in 2 Gebieten“*, mit der Entfernung zur nächsten Grenze. Diana öffnet dann das Fenster des kleinsten Gebiets, mit den anderen als Schaltflächen.

:::tip[Was das für deine Aktivierung bedeutet]
Stehst du in all diesen Gebieten, erlauben dir die WWFF-Regeln, sie zusammen zu aktivieren. Lies die Regeln in Diana unter **Regeln**, oder den offiziellen Text auf wwff.co. Siehe {{link:rules/wwff-rules}}.
:::

:::caution[Nicht für Referenzen ohne Grenze]
Ein gestrichelter Ring ist nur ein ungefährer Ort. Dort kann Diana nicht sagen, ob du drin stehst, und also auch keine Überlappung zeigen.
:::
'''},
'map/am-i-inside': {'title': 'Stehe ich im Gebiet?', 'desc': 'Wie Diana dir sagt, ob du drin stehst, und wie du die Genauigkeit liest.', 'body': '''
Eine Infokarte unten auf der Karte beantwortet die Frage, die jeder Aktivierer hat: **stehe ich im Schutzgebiet?**

## Was die Infokarte sagt

- **In einem Gebiet**: in welchem, und die Entfernung zur nächsten Grenze.
- **In mehreren gleichzeitig** (wenn Gebiete überlappen): wie viele, und das Fenster des kleinsten öffnet sich. Siehe {{link:map/overlapping-areas}}.
- **Draußen**: das nächste Gebiet und wie weit es weg ist.

Jede Antwort endet damit, wie gut deine Position war, zum Beispiel *„Position ±6 m“*.

:::note[Gebiete aus mehreren Teilflächen]
Manche Referenzen bestehen aus getrennten Teilflächen. Das Fenster sagt dann, wie viele. Deine ganze Station muss in einer davon stehen.
:::

## Warum es ein paar Sekunden dauert

Ein Smartphone, das sein GPS gerade erst geweckt hat, antwortet zuerst aus WLAN und Funkmasten, und diese Position kann Hunderte Meter daneben liegen. Deshalb hört Diana weiter zu, während die Genauigkeit besser wird, und zeigt, was sie bisher hat: *„Wird genauer… ±380 m“*. Sie antwortet, sobald die Position gut genug ist, oder nach zwölf Sekunden mit der besten, die sie bekommen hat. Ist die dann noch grob, sagt die Antwort das.

## Die Genauigkeit lesen

| Genauigkeit | Was das meist bedeutet |
|---|---|
| ±10 m oder besser | Satelliten. Zuverlässig, auch nah an einer Grenze. |
| ±20 bis 50 m | Brauchbar. Vorsicht nah an einer Grenze. |
| ±100 m oder schlechter | WLAN oder Funkmasten, oft drinnen. Nicht gut genug, um sicher zu sein. |

Ist die Unsicherheit größer als etwa 10 m, wird ein **gestrichelter Ring** um deinen Marker gezeichnet, mit genau diesem Radius. Ein enger Ring heißt Satelliten; ein Ring über den ganzen Block heißt, die Antwort kam aus dem WLAN.

:::tip[Eine bessere Position bekommen]
Geh nach draußen, mit freiem Himmel über dir, und warte ein paar Sekunden. Bleibt sie grob bei mehr als etwa 75 m? Dann darf die Seite vielleicht nur einen ungefähren Standort verwenden. Ein Hinweis schlägt dann vor, die Standorteinstellung zu prüfen: siehe {{link:help/location-problems}}.
:::

## Zwei Fallen, auf die Diana achtet

- **Drinnen** kommt eine WLAN-Position oft innerhalb einer Sekunde und behauptet ±20 m. So genau hält sich die WLAN-Datenbank selbst, nicht die echte Genauigkeit. Diana antwortet, hört aber den Rest der zwölf Sekunden weiter zu und korrigiert die Antwort bei Bedarf.
- **Smartphones, die mehr behaupten, als sie können.** Diana vergleicht die Messungen der letzten 45 Sekunden. Ein einzelner Ausreißer wird ignoriert. Widersprechen sich die Messungen, sagt die Antwort *„Messungen widersprechen einander“*. Gehen zählt nicht als Streuung.

:::caution
Diana kann das nur für Gebiete **mit** Grenze beantworten. Bei einem gestrichelten Ring oder einem blauen Punkt geht es nicht. Siehe {{link:map/points-and-areas}}.
:::
'''},
'map/layers-and-styles': {'title': 'Ebenen und Kartenstil', 'desc': 'Teile der Karte ein- und ausschalten, und einen Kartenstil wählen.', 'body': '''
## Ebenen (≡)

Tippe oben rechts auf der Karte auf **≡**. Das kannst du ein- und ausschalten:

| Ebene | Was sie zeigt |
|---|---|
| **Schutzgebiete** | Die grünen Gebiete deines Landes. |
| **Referenznummern** | Die Beschriftungen wie `ONFF-0602`. |
| **Ohne Grenze (Punkt)** | Die gestrichelten Ringe von Referenzen ohne Grenze. |
| **Spots auf der Karte** | Live-Spots und Ankündigungen. Sie kommen von WWFF Spotline und werden alle 30 Sekunden aktualisiert. |
| **Linien zu den Spots** | Die grünen gepunkteten und orangen gestrichelten Linien von dir aus. |
| **Andere WWFF-Gebiete** | Die blauen Punkte im Rest der Welt. |

Im selben Menü stehen **⤢ Alle Spots einpassen** und die Sprachschaltflächen. Diana merkt sich deine Wahl.

## Kartenstil (◐)

Tippe auf **◐** für eine andere Grundkarte:

- **Liberty**: der Standard, mit Geländefarben.
- **Positron**: sehr hell und ruhig, gut bei starker Sonne.
- **Bright**: mehr Farbe und Details.
- **Dark**: dunkel, schont nachts die Augen.

:::tip
Im Gelände, bei starker Sonne, ist **Positron** oft am besten zu lesen.
:::
'''},
'map/search': {'title': 'Suchen', 'desc': 'Eine Referenz nach Name oder Nummer finden, überall auf der Welt.', 'body': '''
Tippe oben auf der Karte auf **⌕** und tippe los.

- **Einen Namen**, zum Beispiel `Kalmthoutse Heide`.
- **Eine vollständige Referenz**, zum Beispiel `ONFF-0012` oder `DLFF-0210`.
- **Nur eine Nummer**, zum Beispiel `0012`. Dann sucht Diana nur in deinem eigenen Land.

Jede WWFF-Referenz weltweit ist auffindbar. Treffer aus dem geladenen Land stehen zuerst. Tippe auf einen Treffer: die Karte zoomt dorthin und öffnet sein Fenster.

:::tip
Die Suche funktioniert auch offline: die Liste der Referenzen liegt auf deinem Gerät.
:::
'''},
}
