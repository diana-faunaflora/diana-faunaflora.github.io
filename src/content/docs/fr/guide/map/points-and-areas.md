---
title: "Points et zones"
description: "Pourquoi une référence est une zone verte et une autre un point bleu, et comment changer cela."
sidebar:
  order: 2
---

Sur la carte, une référence WWFF apparaît de l’une de trois façons. Laquelle dépend de ce que Diana sait d’elle, et du pays que vous avez choisi.

| Ce que vous voyez | Ce que cela signifie | Diana peut-elle dire si vous êtes dedans ? |
|---|---|---|
| **Zone verte** | Une référence avec sa vraie limite, dans le pays choisi. | Oui |
| **Anneau pointillé avec un point orange** | Une référence de votre pays sans limite. Seulement un emplacement approximatif. | Non |
| **Point bleu** | Une référence dans un autre pays. Rapprochés, ils forment un cercle numéroté. | Non |

## Pourquoi une zone ?

Une zone a besoin d’un fichier de limites. Diana dispose aujourd’hui de ces fichiers pour **cinq pays** : la Belgique (ONFF), les Pays-Bas (PAFF), l’Allemagne (DLFF), le Danemark (OZFF) et le Portugal (CTFF), et d’autres s’ajoutent régulièrement. Ce sont les coordinateurs nationaux WWFF qui les fournissent.

Diana charge les limites d’**un seul pays à la fois** : celui que vous avez choisi dans les Réglages. La carte reste ainsi rapide sur un téléphone.

## Pourquoi un point ?

- La référence se trouve dans un pays pour lequel Diana n’a **pas de fichier de limites**. Diana ne connaît alors que la position indiquée dans l’annuaire WWFF.
- Ou le pays **a** des limites dans Diana, mais **ce n’est pas le pays que vous avez choisi**. Il apparaît alors aussi comme un point, jusqu’à ce que vous chargiez ce pays.

## Pourquoi un anneau pointillé ?

Dans un pays avec limites, quelques références n’ont pas de limite dans le fichier, par exemple des zones d’outre-mer des Pays-Bas. Elles apparaissent comme un anneau pointillé à l’emplacement approximatif.

## Vous obtenez toujours les détails

Quoi que vous voyiez, **touchez-le** : un panneau s’ouvre avec tout ce que Diana sait. Pour un point bleu, ce sont la référence, le pays et le nom, le locator et les zones, la direction et la distance depuis vous, le nombre de QSO ou **ATNO** si elle n’a jamais été activée, et un lien vers plus d’informations. Voir [Infos sur une zone](/fr/guide/map/area-panel/).

## Quand et comment changer

Quand vous partez dans un autre pays, ou voulez voir la vraie limite d’une référence qui est maintenant un point :

**Depuis le panneau (le plus rapide)**

1. Touchez le point bleu.
2. Si Diana possède les limites de ce pays, le panneau le dit et affiche un bouton **Afficher [pays] en détail**.
3. Touchez-le. Diana charge ce pays et rouvre la même référence, maintenant avec sa limite.

**Depuis les Réglages**

1. Touchez **Réglages** en bas à droite.
2. Sous **Votre pays**, choisissez le pays. Les pays marqués **Avec limites** obtiennent leurs zones ; **Points uniquement** reste en points.
3. Le changement est immédiat. Sous le menu, Diana indique ce qu’elle a chargé, par exemple *« PAFF, 281 zones avec limites chargées »*.

Votre filtre de spots (votre pays ou Mondial) ne change pas quand vous choisissez un autre pays. Plus d’informations dans [Votre pays](/fr/guide/settings/your-country/).

:::note[Une nouvelle réserve d’abord comme point]
Les références existantes proviennent de l’annuaire WWFF, chaque nuit. Les limites viennent d’un fichier publié par l’équipe Diana. Une toute nouvelle réserve peut donc apparaître d’abord comme un point et recevoir son contour plus tard.
:::
