T = {
'spots/on-air': {'title': 'Wer ist QRV', 'desc': 'Der Spots-Bildschirm: Live-WWFF-Spots, ATNO, Richtung und Entfernung.', 'body': '''
Tippe unten auf **Spots**. Der Bildschirm **Spots & Agenda** zeigt, wer gerade aus einem WWFF-Gebiet QRV ist. Die Liste kommt live von WWFF Spotline und wird alle 30 Sekunden aktualisiert.

{{img:phone-spots-world|Der Spots-Bildschirm, Reiter Jetzt aktiv, Weltweit, mit einer Liste von Stationen}}

## Eine Zeile pro Station

| Was du siehst | Bedeutung |
|---|---|
| Rufzeichen | Der Aktivierer, zum Beispiel `F5MQU/P`. |
| Anzahl QSOs | Wie viele Verbindungen laut WWFF-Verzeichnis schon aus dieser Referenz gemacht wurden. |
| **ATNO** in Rot | *All Time New One*: diese Referenz wurde noch nie aktiviert. Der Liebling jedes Jägers. |
| Frequenz, Betriebsart, Referenz | Zum Beispiel `10112 kHz · CW · FFF-4038`. |
| Minuten | Wie lange der Spot her ist. |
| Richtung und Entfernung | Von dir aus, zum Beispiel `191° · 440 km`. |

## Dein Land oder weltweit

Unter den Reitern wählst du **dein Land** (zum Beispiel DLFF) oder **Weltweit**. Diana merkt sich die Wahl und hält sie im Gleichschritt mit derselben Einstellung in den Einstellungen. Für welches Land die Schaltfläche steht, folgt deiner Ländereinstellung: solange du keines gewählt hast, nimmt Diana es aus deinem Rufzeichen (ON… ergibt ONFF, PA… PAFF, DL… DLFF).

## Einen Spot öffnen

1. Tippe auf eine Zeile.
2. Die Karte öffnet sich, auf dieses Gebiet gezoomt, mit einem Fenster: Frequenz und Betriebsart, das Schutzgebiet, der Locator dort und deiner, die Bemerkung, die Anzahl QSOs, Mehr Infos und ein Kompass mit der Richtung.
3. **← Zurück zu Spots**, oder die Zurück-Taste von Android, bringt dich zur Liste zurück.
4. **×** oder Wischen nach unten schließt nur das Fenster und behält die Karte.

:::note[Spotline nicht erreichbar?]
Dann sagt der Bildschirm das, statt ohne Hinweis alte Spots zu zeigen.
:::
'''},
'spots/agenda': {'title': 'Die Agenda', 'desc': 'Angekündigte Aktivierungen: wer was plant, und wann.', 'body': '''
Tippe auf dem Bildschirm **Spots** auf den Reiter **Agenda**. Du siehst jede angekündigte Aktivierung, mit Referenz, Bändern und Betriebsarten, und Datum und Uhrzeit in UTC.

{{img:phone-agenda|Der Reiter Agenda mit angekündigten Aktivierungen}}

## Die Agenda lesen

- **Läuft jetzt**: ein oranger Punkt und *„läuft bis …“*.
- **Kommt noch**: grau, mit Datum und Startzeit.
- **ATNO** in Rot: die Referenz wurde noch nie aktiviert.

Deine Wahl zwischen **deinem Land** und **Weltweit** gilt auch hier.

## Eine Ankündigung öffnen

Tippe auf eine Zeile. Die Karte öffnet sich bei diesem Gebiet mit Band und Betriebsart, dem Schutzgebiet, dem Locator, der Bemerkung und der Richtung. **← Zurück zu Spots** bringt dich zurück.

## Selbst ankündigen

Tippe oben in der Agenda auf **+ Ankündigen**. Siehe {{link:spots/announce}}.

:::tip[Auch auf der Karte]
Ankündigungen stehen auf der Karte als weißer Punkt mit orangem Ring, mit einer orangen gestrichelten Linie von dir aus. Siehe {{link:map/reading-the-map}}.
:::
'''},
'spots/spot-yourself': {'title': 'Selbst spotten', 'desc': 'Den Jägern sagen, dass du QRV bist, über WWFF Spotline.', 'body': '''
QRV und bereit? Spotte dich selbst, damit die Jäger dich finden. Der Spot geht an WWFF Spotline und von dort in den DX-Cluster.

{{img:phone-spot-yourself|Der Melden-Bildschirm mit Referenz, Rufzeichen, Frequenz, Betriebsart und Bemerkung}}

## Schritt für Schritt

1. Tippe unten auf **Melden**, oder im Fenster eines Gebiets auf **Hier selbst spotten**.
2. Prüfe die **Referenz**. Stehst du in einem Gebiet, oder kommst du aus einem Fenster, hat Diana sie schon ausgefüllt und sagt, woher sie stammt.
3. Deine **Rufzeichen** kommen aus den Einstellungen: das Portable-Rufzeichen als Aktivierer, dein normales Rufzeichen als Spotter.
4. Trage die **Frequenz** in kHz ein, zum Beispiel `7144`, und wähle die **Betriebsart**.
5. Optional: eine kurze **Bemerkung**, bis zu 100 Zeichen. Tippe auf eines deiner **Schnellwörter**, um es mit einem Tippen hinzuzufügen.
6. Tippe auf **Prüfen**. Spotline sieht sich deinen Spot an, ohne ihn zu setzen, und sagt dir, was es davon hält.
7. Akzeptiert? Tippe auf **Spot senden**. Du bekommst eine Bestätigung mit der Nummer deines Spots.

## Warum erst Prüfen, dann Senden?

Jede Anfrage an Spotline geht von einem Budget ab, das sich alle Nutzer teilen. *Prüfen* sorgt dafür, dass ein Spot stimmt, bevor er ein echtes Senden kostet. Änderst du nach dem Prüfen etwas, schließt *Senden* wieder: die Freigabe galt für den Spot, wie er da war.

## Was Diana für dich prüft

- Das Format des **Rufzeichens**, den Bereich der **Frequenz** und die Länge der **Bemerkung**, genau wie Spotline.
- Den **Bandplan**: eine Warnung, wenn deine Betriebsart nicht zum Segment deiner Frequenz passt.
- Die **Referenz**, gegen Dianas eigene Liste. Das antwortet sofort, auch ohne Empfang.

:::caution[Was nicht in eine Bemerkung gehört]
Kein Dankeschön und keine Bandwünsche. Jeder Spot geht in den DX-Cluster, wo so etwas nur Rauschen ist. Spotline filtert außerdem unangemessene Sprache.
:::

## Wenn etwas schiefgeht

- **Bei schlechter Verbindung zweimal gedrückt?** Diana sagt, dass der Spot schon da war. Nichts wird doppelt gesetzt.
- **Spotline lehnt ab?** Du bekommst die Erklärung von Spotline selbst.
- **Senden geht gar nicht?** Diana bietet **Auf die alte Art senden** an: der Spot geht in einem neuen Tab an das eigene Formular von Spotline. Deren Antwort siehst du selbst, aber Diana kann sie nicht bestätigen.

Noch nicht QRV, nur am Planen? Nimm die Agenda: {{link:spots/announce}}.
'''},
'spots/announce': {'title': 'Eine Aktivierung ankündigen', 'desc': 'Eine geplante Aktivierung in die WWFF-Agenda eintragen, und deine PIN aufbewahren.', 'body': '''
Planst du eine Aktivierung? Kündige sie an, damit die Jäger bereit sind. Die Ankündigung geht in die WWFF-Agenda auf Spotline.

{{img:phone-announce|Der Ankündigen-Bildschirm mit Rufzeichen, Referenz, Beginn und Ende, Bändern und Betriebsarten}}

## Drei Wege hinein

- **Agenda** in der Leiste unten.
- **+ Ankündigen** im Reiter Agenda des Spots-Bildschirms.
- **Aktivierung ankündigen** im Fenster eines Gebiets: die Referenz ist dann schon ausgefüllt.

## Schritt für Schritt

1. Prüfe das **Rufzeichen des Aktivierers** und **dein eigenes Rufzeichen**. Jemand anderes darf für einen Aktivierer ankündigen.
2. Trage die **WWFF-Referenz** ein, zum Beispiel `DLFF-0210`.
3. Wähle **Beginn** und **Ende**. Du wählst sie nach der Uhr deines eigenen Geräts; Diana rechnet sie in UTC um, bevor sie dein Gerät verlassen.
4. Optional: kreuze die **Bänder** und **Betriebsarten** an (mehrere sind möglich, zum Beispiel *40 m, 20 m · CW, SSB*) und füge eine Bemerkung hinzu.
5. Tippe auf **Prüfen**, und wenn es akzeptiert ist, auf **Ankündigung senden**.
6. **Schreib dir deine PIN auf.**

:::danger[Bewahre deine PIN auf]
Die PIN ist der einzige Weg, diese Ankündigung später auf der Seite von Spotline zu ändern oder zu streichen. Diana kann das nicht für dich tun, und eine verlorene PIN lässt sich nicht wiederherstellen. Deshalb führt Diana unter dem Formular eine Liste von allem, was du von diesem Gerät angekündigt hast (Referenz, Datum, PIN). Tippe auf **✕**, um eine Zeile zu entfernen. Diese Liste gibt es nur auf diesem Gerät.
:::

## Grenzen

- Höchstens **einen Monat** im Voraus, und das Ende nicht vor dem Beginn. Spotline wendet dieselben Regeln an.
- Höchstens **16 Ankündigungen pro Tag** von einem Gerät über Diana, um das gemeinsame Budget zu schützen. Normale Nutzung bleibt weit darunter.
- Für Ankündigungen gibt es keine „alte Art“. Klappt es nicht, versuch es später noch einmal.

Welche Bänder die Liste anbietet (alle, oder nur KW), ist eine Einstellung: {{link:settings/band-list}}.
'''},
}
