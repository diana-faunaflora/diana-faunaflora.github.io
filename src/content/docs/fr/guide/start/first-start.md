---
title: "L’écran de démarrage"
description: "Ce que vous voyez pendant le démarrage de Diana, et que faire si elle reste bloquée sur l’écran de démarrage."
sidebar:
  order: 5
---

À chaque démarrage, vous voyez d’abord l’écran de démarrage : un dessin d’une activation, un signal radio qui le traverse, une barre de progression et le numéro de version. Pendant ce temps, Diana lit les données des références et prépare la carte.

L’écran de démarrage disparaît tout seul dès que la carte est dessinée, et au plus tard après neuf secondes.

## Diana a besoin de scripts

Diana est une application web : tout ce qu’elle fait s’exécute en JavaScript dans votre navigateur. Si votre navigateur ou une extension bloque les scripts, rien ne peut démarrer et vous restez sur l’écran de démarrage.

Au bout d’un moment, une boîte apparaît sur l’écran de démarrage pour le dire. Alors :

1. Autorisez les scripts uniquement pour **diana-onff.github.io**. Pas pour `github.io` ni pour `github.com` : Diana n’a besoin d’aucun des deux.
2. **Rechargez la page.** Sur un ordinateur, appuyez sur **F5** ou **Ctrl+R** (Mac : **Cmd+R**). Sur un téléphone, tirez la page vers le bas ou touchez le bouton de rechargement du navigateur.
3. Toujours bloqué ? Une autre extension bloque peut-être aussi, comme un bloqueur de publicité. Désactivez-les une par une pour ce site.

:::caution[Recharger est indispensable]
La plupart des bloqueurs n’appliquent une nouvelle règle qu’à une page rechargée. Sans rechargement, l’ancien blocage reste en place, même après avoir cliqué sur « Faire confiance ».
:::

Tous les scripts viennent de l’adresse de Diana elle-même. Rien n’est chargé depuis d’autres sites, sauf le script de statistiques, et seulement si vous dites oui. Détails dans [Bloqué sur l’écran de démarrage](/fr/guide/help/scripts-blocked/).

## La toute première fois

Sur un appareil qui n’a jamais ouvert Diana, deux courtes étapes suivent l’écran de démarrage : [Écran d’accueil](/fr/guide/start/welcome-screen/) et [L’assistant de démarrage](/fr/guide/start/setup-wizard/).
