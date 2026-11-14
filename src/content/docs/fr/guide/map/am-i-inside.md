---
title: "Suis-je dans la zone ?"
description: "Comment Diana vous dit si vous êtes dedans, et comment lire la précision."
sidebar:
  order: 6
---

Une carte d’information en bas de la carte répond à la question que se pose tout activateur : **suis-je dans la réserve ?**

## Ce que dit la carte d’information

- **Dans une zone** : laquelle, et la distance jusqu’à la limite la plus proche.
- **Dans plusieurs à la fois** (quand des zones se chevauchent) : combien, et le panneau de la plus petite s’ouvre. Voir [Zones qui se chevauchent](/fr/guide/map/overlapping-areas/).
- **En dehors** : la zone la plus proche et à quelle distance elle se trouve.

Chaque réponse se termine par la qualité de votre position, par exemple *« position ±6 m »*.

:::note[Zones composées de plusieurs parcelles]
Certaines références sont faites de parcelles séparées. Le panneau indique alors combien. Toute votre station doit se trouver dans l’une d’elles.
:::

## Pourquoi cela prend quelques secondes

Un téléphone qui vient de réveiller son GPS répond d’abord à partir du wifi et des antennes relais, et cette position peut être fausse de plusieurs centaines de mètres. Diana continue donc d’écouter pendant que la précision s’améliore, et affiche ce qu’elle a pour l’instant : *« Affinage… ±380 m »*. Elle répond dès que la position est assez bonne, ou après douze secondes avec la meilleure obtenue. Si celle-ci reste grossière, la réponse le dit.

## Lire la précision

| Précision | Ce que cela signifie généralement |
|---|---|
| ±10 m ou mieux | Satellites. Fiable, même près d’une limite. |
| ±20 à 50 m | Correct. Prudence près d’une limite. |
| ±100 m ou pire | Wifi ou antennes relais, souvent à l’intérieur. Pas assez pour être sûr. |

Quand la marge dépasse environ 10 m, un **anneau pointillé** est dessiné autour de votre marqueur avec exactement ce rayon. Un anneau serré signifie satellites ; un anneau qui couvre tout le pâté de maisons signifie que la réponse vient du wifi.

:::tip[Obtenir une meilleure position]
Sortez, avec le ciel dégagé au-dessus de vous, et attendez quelques secondes. Elle reste grossière, au-delà d’environ 75 m ? Le site n’a peut-être droit qu’à une position approximative. Un bandeau propose alors de vérifier le réglage de localisation : voir [Problèmes de position](/fr/guide/help/location-problems/).
:::

## Deux pièges que Diana surveille

- **À l’intérieur**, une position wifi arrive souvent en une seconde en annonçant ±20 m. C’est la précision que la base de données wifi s’attribue, pas la précision réelle. Diana répond, mais continue d’écouter le reste des douze secondes et corrige la réponse si nécessaire.
- **Les téléphones qui promettent plus qu’ils ne peuvent.** Diana compare les relevés des 45 dernières secondes. Un relevé isolé et aberrant est ignoré. Si les relevés se contredisent, la réponse indique *« relevés contradictoires »*. Marcher ne compte pas comme dispersion.

:::caution
Diana ne peut répondre que pour les zones **avec** limite. Pour un anneau pointillé ou un point bleu, elle ne le peut pas. Voir [Points et zones](/fr/guide/map/points-and-areas/).
:::
