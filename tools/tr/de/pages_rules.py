T = {
'rules/wwff-rules': {'title': 'WWFF-Regeln in Diana', 'desc': 'Die Auswahl der WWFF-Regeln in der App, und der richtige Name für deine Logdatei.', 'body': '''
Tippe unten auf **Regeln**. Der Reiter **Regeln** öffnet sich: eine Auswahl aus den offiziellen WWFF-Regeln, die im Gelände am meisten zählen, in deiner Sprache.

{{img:phone-rules|Der Regeln-Bildschirm mit den Regeln zum Referenzgebiet}}

## Was drinsteht

Die Regeln 3.5, 3.6, 4.4, 4.7, 6.8, 6.9 und 6.11 der WWFF Global Rules, in drei Gruppen:

- **Das Gebiet**: im Referenzgebiet stehen, Referenzen, die an eine andere grenzen oder sie enthalten, mehrere gleichzeitig aktivieren.
- **QSOs**: Regeln zu den Verbindungen selbst.
- **Logs**: wie du dein Log benennst und hochlädst.

Es sind WWFF-Regeln, also gelten sie auch für DLFF und jedes andere nationale Programm.

:::note[Übersetzungen]
Die Texte in anderen Sprachen sind vom Diana-Team übersetzt. Es gilt der englische Text von WWFF. Jede Übersetzung verlinkt auf das offizielle PDF.
:::

## Der Name deiner Logdatei

Regel 6.8 verlangt einen festen Dateinamen. Diana zeigt ein Beispiel, bei dem jeder Teil beschriftet ist:

`ON3VZ@ONFF-0104 20261002.adi`

| Teil | Bedeutung |
|---|---|
| `ON3VZ` | Dein Rufzeichen. |
| `@` | Trennzeichen. |
| `ONFF-0104` | Die Referenz. |
| (Leerzeichen) | Ein Leerzeichen. |
| `20261002` | Das Datum: Jahr, Monat, Tag. |
| `.adi` | Eine ADIF-Logdatei. |

Regel 6.9 verweist auf die offizielle Logsuche von WWFF: [wwff.co/logsearch](https://wwff.co/logsearch/).

:::tip
Diana loggt nicht für dich. Sie hilft dir vor und während der Aktivierung; dein Log bleibt in deinem eigenen Logprogramm.
:::
'''},
'rules/band-plan': {'title': 'Der Bandplan', 'desc': 'Wo du pro Band senden darfst, mit den WWFF-Vorzugsfrequenzen.', 'body': '''
Tippe auf dem Bildschirm **Regeln** auf den Reiter **Bandplan**.

{{img:phone-bandplan|Der Bandplan mit den CW-, Digital- und SSB-Segmenten von 80, 40 und 30 m}}

## Ihn lesen

Für jedes Band:

- Ein **Balken** mit den Segmenten für **CW**, **Digital** und **SSB**, mit ihren Frequenzen, zum Beispiel *CW 3.500 bis 3.570 MHz*.
- Die **FT8**-Frequenz, markiert.
- Die **WWFF-Vorzugsfrequenzen**, in einem gelben Kasten hervorgehoben, zum Beispiel *SSB 7.144 · CW 7.024*.

## Warum das wichtig ist

Wenn du dich selbst spottest, prüft Diana deine Frequenz gegen diesen Bandplan und warnt dich, wenn deine Betriebsart nicht zum Segment passt. Siehe {{link:spots/spot-yourself}}.

:::tip
An einem vollen Aktivierungstag beginnst du am besten nahe der WWFF-Vorzugsfrequenz: dort hören die Jäger zuerst.
:::
'''},
}
