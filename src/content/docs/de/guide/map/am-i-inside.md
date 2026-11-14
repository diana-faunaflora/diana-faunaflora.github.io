---
title: "Stehe ich im Gebiet?"
description: "Wie Diana dir sagt, ob du drin stehst, und wie du die Genauigkeit liest."
sidebar:
  order: 6
---

Eine Infokarte unten auf der Karte beantwortet die Frage, die jeder Aktivierer hat: **stehe ich im Schutzgebiet?**

## Was die Infokarte sagt

- **In einem Gebiet**: in welchem, und die Entfernung zur nächsten Grenze.
- **In mehreren gleichzeitig** (wenn Gebiete überlappen): wie viele, und das Fenster des kleinsten öffnet sich. Siehe [Überlappende Gebiete](/de/guide/map/overlapping-areas/).
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
Geh nach draußen, mit freiem Himmel über dir, und warte ein paar Sekunden. Bleibt sie grob bei mehr als etwa 75 m? Dann darf die Seite vielleicht nur einen ungefähren Standort verwenden. Ein Hinweis schlägt dann vor, die Standorteinstellung zu prüfen: siehe [Probleme mit dem Standort](/de/guide/help/location-problems/).
:::

## Zwei Fallen, auf die Diana achtet

- **Drinnen** kommt eine WLAN-Position oft innerhalb einer Sekunde und behauptet ±20 m. So genau hält sich die WLAN-Datenbank selbst, nicht die echte Genauigkeit. Diana antwortet, hört aber den Rest der zwölf Sekunden weiter zu und korrigiert die Antwort bei Bedarf.
- **Smartphones, die mehr behaupten, als sie können.** Diana vergleicht die Messungen der letzten 45 Sekunden. Ein einzelner Ausreißer wird ignoriert. Widersprechen sich die Messungen, sagt die Antwort *„Messungen widersprechen einander“*. Gehen zählt nicht als Streuung.

:::caution
Diana kann das nur für Gebiete **mit** Grenze beantworten. Bei einem gestrichelten Ring oder einem blauen Punkt geht es nicht. Siehe [Punkte und Flächen](/de/guide/map/points-and-areas/).
:::
