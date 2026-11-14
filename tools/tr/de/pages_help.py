T = {
'help/location-problems': {'title': 'Probleme mit dem Standort', 'desc': 'Keine Position, oder eine Position, die grob bleibt: was du pro Gerät prüfst.', 'body': '''
Diana fragt immer nach der genauesten Position, die dein Gerät liefern kann. Ob eine Seite die genaue oder eine absichtlich unscharfe Position bekommt, ist eine Einstellung deines Smartphones oder Browsers, nicht von Diana.

## Zuerst: draußen versuchen

Drinnen liefert WLAN allein oft etwa ±100 m. Geh nach draußen, mit freiem Himmel über dir, warte zehn Sekunden und tippe unten auf **Karte**. Oft reicht das schon.

## Immer noch grob oder keine Position? Prüfe die Einstellung

**Android mit Chrome**

1. Öffne die App **Einstellungen** deines Smartphones.
2. Geh zu **Apps** › **Chrome** › **Berechtigungen** › **Standort**.
3. Wähle **Nur während der Nutzung der App zulassen** und schalte **Genauen Standort verwenden** ein.
4. Prüfe auch die Seite selbst: in Chrome tippst du auf das Symbol links der Adressleiste › **Berechtigungen** › **Standort**: zugelassen.

**iPhone oder iPad mit Safari**

1. Öffne die App **Einstellungen**.
2. Geh zu **Datenschutz & Sicherheit** › **Ortungsdienste** › **Safari-Websites**.
3. Wähle **Beim Verwenden der App** und schalte **Genauer Standort** ein.

**iPhone oder iPad mit einem anderen Browser** (zum Beispiel Chrome)

1. Öffne die App **Einstellungen**.
2. Geh zu **Datenschutz & Sicherheit** › **Ortungsdienste** › dein Browser.
3. Wähle **Beim Verwenden der App** und schalte **Genauer Standort** ein.

**Computer**

Klicke auf das Schlosssymbol neben der Adressleiste und erlaube **Standort** für diese Seite. Ein Laptop bekommt seine Position aus dem WLAN und ist selten besser als etwa ±50 m.

## „Standort ist für diese Seite blockiert“

Du (oder jemand anderes) hast früher Nein gesagt. Diana kann nicht noch einmal fragen: nur du kannst es erlauben, in den Browser- oder Smartphone-Einstellungen oben. Lade Diana danach neu.

## Ohne Standort

Diana funktioniert auch ohne Standort. Trag deinen Locator unter **Einstellungen** › **Ihre Station** ein. Entfernungen und Linien gehen dann von der Mitte deines Locator-Feldes aus. Nur *stehe ich im Gebiet* braucht wirklich eine genaue Position.

Siehe auch {{link:map/am-i-inside}}.
'''},
'help/scripts-blocked': {'title': 'Hängt auf dem Startbildschirm', 'desc': 'Skriptblocker und strenge Browser: was Diana braucht, und nicht mehr.', 'body': '''
Diana ist eine Web-App: ohne JavaScript läuft nichts. Hält ein Blocker die Skripte an, bleibt Diana auf dem Startbildschirm. Nach einer Weile erscheint dort ein Kasten, der das sagt.

## Lösen

1. Erlaube Skripte nur für **diana-onff.github.io**. Nicht `github.io` und nicht `github.com`: beides braucht Diana nicht.
2. **Lade die Seite neu**: **F5** oder **Strg+R** (Mac: **Cmd+R**). Auf dem Smartphone ziehst du die Seite nach unten oder tippst auf Neu laden. Ohne Neuladen bleibt die alte Sperre, auch wenn du schon auf „Vertrauen“ geklickt hast.
3. Hängt es immer noch? Vielleicht blockiert eine zweite Erweiterung mit (ein Werbeblocker, eine Datenschutz-Erweiterung). Schalte sie für diese Seite nacheinander aus.
4. Diana startet, aber die Karte bleibt leer? Erlaube `blob:`-Worker für diana-onff.github.io (siehe unten).

## Was Diana lädt

**Skripte**: alle von diana-onff.github.io selbst.

| Datei | Was es ist |
|---|---|
| `vendor/maplibre-gl.js` | MapLibre, die Kartenbibliothek. Eine Kopie auf Dianas eigener Seite, nicht von einem CDN. |
| `js/*.js` | Dianas eigener Code. |
| `sw.js` | Der Service Worker, der Diana offline am Laufen hält. |

Keine Inline-Skripte und kein `eval`. Eine Ausnahme, nur mit deiner Zustimmung: wenn du Ja zur Statistik gesagt hast, das Umami-Skript von `cloud.umami.is`.

**Karten-Worker**: MapLibre zeichnet die Karte in einem Hintergrund-Worker, der von einer `blob:`-Adresse gestartet wird. Ein Blocker, der `blob:`-Worker verweigert, lässt Diana starten, aber die Karte bleibt leer.

**Daten**:

| Host | Wozu |
|---|---|
| `tiles.openfreemap.org` | Kartenkacheln und Schriften der Beschriftung |
| `spots.wwff.co` | Live-Spots und Agenda |
| `diana-spotline.diana-onff.workers.dev` | Nur wenn du einen Spot oder eine Ankündigung sendest |
| `raw.githubusercontent.com` | Weltraumwetter für Bedingungen |
| `cloud.umami.is` | Nur wenn du Ja zur Statistik gesagt hast |

Deine Position wird nie irgendwohin geschickt.
'''},
'help/updates': {'title': 'Updates', 'desc': 'Wie Diana sich selbst aktualisiert, und was zu tun ist, wenn eine neue Version nicht erscheint.', 'body': '''
Diana aktualisiert sich selbst. Du musst nie etwas herunterladen.

## Wie es funktioniert

- **Die Daten** (Referenzen, Anzahl QSOs, Grenzen) werden jede Nacht aktualisiert. Diana holt sie bei jedem Start frisch und nimmt bei schwachem Empfang die Kopie auf deinem Smartphone.
- **Die App selbst**: wenn du Diana mit Empfang öffnest, schaut sie nach einer neuen Version. Eine neue Version wird nur gemeldet, wenn es wirklich eine gibt.

## Eine neue Version erscheint nicht?

1. Sorg dafür, dass du Empfang hast.
2. Öffne **Einstellungen** und tippe unten auf **Nach Updates suchen**.
3. Vergleiche die Versionszeile mit der in **Was ist neu**. Siehe {{link:settings/version-and-updates}}.
4. Immer noch die alte Version? Schließe Diana ganz (wische sie aus den zuletzt verwendeten Apps weg) und öffne sie erneut.

:::note
Die Versionen der App stehen in **Was ist neu**, die neueste oben, auf Niederländisch und Englisch.
:::
'''},
'help/data-and-limits': {'title': 'Deine Daten und die Grenzen', 'desc': 'Was auf deinem Gerät bleibt, warum nichts synchronisiert wird, und was Diana nicht kann.', 'body': '''
## Alles bleibt auf einem Gerät, in einem Browser

Deine Rufzeichen, Locator, Land, Schnellwörter, Sprache, Statistik-Wahl und die PINs deiner Ankündigungen liegen im lokalen Speicher dieses einen Browsers. Nichts wird synchronisiert.

- Nutzt du Diana auf dem Smartphone und auf dem Laptop? Richte sie auf beiden ein. Es gibt kein Konto, um sie zu verbinden.
- **Browserdaten löschen** (Verlauf, Cookies und Websitedaten), ein **privates Fenster** oder **die installierte App entfernen** löscht diese Einstellungen. Diana beginnt dann wieder beim Willkommensbildschirm.

:::caution[Die PINs deiner Ankündigungen]
Sie liegen im selben Speicher. Browser löschen, und sie sind weg. Schreib wichtige PINs auch woanders auf.
:::

## Was Diana nicht kann

- **Live-Daten hängen von anderen ab.** Spots und Agenda kommen von WWFF Spotline. Ist es nicht erreichbar, sagt der Spots-Bildschirm das. Die Ausbreitungsbedingungen kommen von NOAA; der Reiter sagt, wie alt sie sind.
- **Grenzen gibt es nur, wo eine Datei geliefert wurde**: heute fünf Länder. Anderswo sind Referenzen Punkte, und Diana kann nicht sagen, ob du drin stehst. Siehe {{link:map/points-and-areas}}.
- **Nicht jedes Schutzgebiet hat vollständige Angaben.** Viele haben nur einen Namen und eine Referenz. Das ist eine Lücke in den Quelldaten.
- **Diana loggt nicht** und lädt keine Logs hoch. Das bleibt bei deinem eigenen Logprogramm und bei WWFF.

## Nutzung der Daten

Die Grenzen und Aktivierungszahlen kommen von den WWFF-Programmen, der WDPA, Behördenquellen und WWFF Spotline, und bleiben Daten ihrer Eigentümer. Siehe {{link:about/data-sources}}.
'''},
'help/faq': {'title': 'Häufige Fragen', 'desc': 'Kurze Antworten auf die Fragen, die am häufigsten kommen.', 'body': '''
## Kostet Diana etwas?

Nein. Diana ist kostenlos, ohne Werbung und ohne Konto.

## Ist Diana eine offizielle WWFF-App?

Nein. Diana ist ein ehrenamtliches Projekt, das das WWFF-Hobby unterstützt. Es nutzt die öffentlichen Dienste von WWFF, wie Spotline und das Verzeichnis.

## Schickt Diana meine Position irgendwohin?

Nein. Deine Position wird nur auf deinem eigenen Bildschirm verwendet. Ein Spot sendet dein Rufzeichen, Frequenz, Betriebsart, Referenz und Bemerkung, nie deine Position. Siehe {{link:start/privacy}}.

## Funktioniert Diana ohne Empfang?

Ja, mit den zuletzt geladenen Daten: die Karte, die du schon angesehen hast, die Referenzen, Feldinfo Standort und der Bandplan. Live-Spots und das Senden eines Spots brauchen Empfang.

## Warum ist meine Referenz ein Punkt und keine Fläche?

Weil Diana keine Grenze dafür hat, oder weil sie in einem anderen Land liegt als dem, das du geladen hast. Siehe {{link:map/points-and-areas}}.

## Kann ich in Diana loggen?

Nein. Diana hilft vor und während der Aktivierung. Dein Log bleibt in deinem Logprogramm. Unter **Regeln** zeigt Diana den richtigen Dateinamen.

## Meine Einstellungen sind weg. Was ist passiert?

Die Browserdaten wurden gelöscht, die App wurde entfernt, oder du hast ein privates Fenster benutzt. Siehe {{link:help/data-and-limits}}.

## Kann mein nationales Programm auch Grenzen bekommen?

Ja. Der nationale Koordinator schickt die Gebietsdatei (KMZ) an das Diana-Team. Mehr unter {{link:about/about-diana}}.

## Ich habe einen Fehler gefunden. Wo melde ich ihn?

Die Kontaktdaten stehen auf der Datenschutzseite in der App (**Einstellungen** › **Datenschutz**). Nenne deine Versionszeile: {{link:settings/version-and-updates}}.
'''},
}
