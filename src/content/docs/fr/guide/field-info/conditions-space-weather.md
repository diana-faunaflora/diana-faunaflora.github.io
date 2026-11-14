---
title: "Conditions : météo spatiale"
description: "Le cadran Kp, le SFI, l’indice A et les taches solaires, et ce qu’ils signifient."
sidebar:
  order: 4
  label: "Météo spatiale"
---

L’onglet **Conditions** commence par la météo spatiale du jour : un cadran avec l’**indice Kp** et trois nombres en dessous.

![Infos terrain, onglet Conditions, avec le cadran Kp sur 2, calme, et les barres des bandes](../../../../../assets/screens/phone-field-conditions.webp)

## Le cadran Kp

Le Kp mesure l’agitation du champ magnétique terrestre, sur une échelle de 0 à 9. Plus il est bas, mieux c’est pour les bandes hautes. Diana affiche la valeur officielle sur trois heures de la NOAA, et à côté une estimation des dernières minutes.

| Kp | Mot dans Diana | Ce que cela signifie |
|---|---|---|
| 0 à 2 | calme | Aucun effet. Conditions normales. |
| 3 | agité | Légèrement agité. Généralement pas encore d’effet notable. |
| 4 | actif | 20, 15 et 10 m perdent un cran. |
| 5 et 6 | tempête G1, G2 | Tempête modérée : 20, 15 et 10 m moins bons. 80 et 40 m le remarquent à peine. |
| 7 à 9 | tempête G3 à G5 | Forte tempête : toutes les bandes moins bonnes, les hautes surtout. |

:::note
Le Kp est une valeur mondiale, pas une mesure à votre position.
:::

## Les trois nombres

| Nombre | Ce qu’il vous dit |
|---|---|
| **SFI** | Le flux solaire. Plus il est élevé, mieux s’ouvrent les bandes hautes. Vers 70 c’est bas, au-dessus de 150 c’est haut. |
| **A** | L’agitation du champ magnétique sur toute la journée. Bas, c’est bien. |
| **Taches solaires** | Vont de pair avec le SFI : plus de taches, plus de chances de DX sur les bandes hautes. |

Le SFI, l’indice A et les taches solaires sont des valeurs journalières ; Diana indique de quel jour elles datent.

## Quel âge ont les chiffres ?

Sous le cadran, il est indiqué quand les chiffres ont été mis à jour, par exemple *« Mis à jour à 14:37 (il y a 12 min) »*. Diana essaie de les récupérer deux fois par heure, mais en pratique il peut y avoir quelques heures entre deux mises à jour.

- Plus de **huit heures** : le message devient orange.
- Valeur Kp de plus de **douze heures** : Diana le signale à part.

La source est la NOAA SWPC. Ce que cela signifie par bande : [Les barres des bandes](/fr/guide/field-info/conditions-bands/).
