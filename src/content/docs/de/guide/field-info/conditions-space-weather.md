---
title: "Bedingungen: Weltraumwetter"
description: "Die Kp-Anzeige, SFI, A-Index und Sonnenflecken, und was sie bedeuten."
sidebar:
  order: 4
  label: "Weltraumwetter"
---

Der Reiter **Bedingungen** beginnt mit dem heutigen Weltraumwetter: eine Anzeige mit dem **Kp-Index** und drei Zahlen darunter.

![Feldinfo, Reiter Bedingungen, mit der Kp-Anzeige auf 2, ruhig, und den Bandbalken](../../../../../assets/screens/phone-field-conditions.webp)

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

Die Quelle ist NOAA SWPC. Was es pro Band bedeutet: [Die Bandbalken](/de/guide/field-info/conditions-bands/).
