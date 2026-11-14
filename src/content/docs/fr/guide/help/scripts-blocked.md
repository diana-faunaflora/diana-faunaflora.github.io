---
title: "Bloqué sur l’écran de démarrage"
description: "Bloqueurs de scripts et navigateurs stricts : ce dont Diana a besoin, et rien de plus."
sidebar:
  order: 2
---

Diana est une application web : sans JavaScript, rien ne fonctionne. Si un bloqueur arrête les scripts, Diana reste sur l’écran de démarrage. Au bout d’un moment, une boîte y apparaît pour le dire.

## Résoudre le problème

1. Autorisez les scripts uniquement pour **diana-onff.github.io**. Ni `github.io` ni `github.com` : Diana n’a besoin d’aucun des deux.
2. **Rechargez la page** : **F5** ou **Ctrl+R** (Mac : **Cmd+R**). Sur un téléphone, tirez la page vers le bas ou touchez recharger. Sans rechargement, l’ancien blocage reste, même après avoir cliqué sur « Faire confiance ».
3. Toujours bloqué ? Une deuxième extension peut aussi bloquer (un bloqueur de publicité, une extension de confidentialité). Désactivez-les une par une pour ce site.
4. Diana démarre mais la carte reste vide ? Autorisez les workers `blob:` pour diana-onff.github.io (voir ci-dessous).

## Ce que charge Diana

**Scripts** : tous depuis diana-onff.github.io lui-même.

| Fichier | Ce que c’est |
|---|---|
| `vendor/maplibre-gl.js` | MapLibre, la bibliothèque cartographique. Une copie sur le site de Diana, pas depuis un CDN. |
| `js/*.js` | Le code de Diana. |
| `sw.js` | Le service worker qui permet à Diana de fonctionner hors ligne. |

Pas de scripts en ligne et pas d’`eval`. Une exception, uniquement avec votre accord : si vous avez dit oui aux statistiques, le script Umami de `cloud.umami.is`.

**Worker de la carte** : MapLibre dessine la carte dans un worker en arrière-plan lancé depuis une adresse `blob:`. Un bloqueur qui refuse les workers `blob:` laisse Diana démarrer mais laisse la carte vide.

**Données** :

| Hôte | Pourquoi |
|---|---|
| `tiles.openfreemap.org` | Tuiles de carte et polices des étiquettes |
| `spots.wwff.co` | Spots en direct et agenda |
| `diana-spotline.diana-onff.workers.dev` | Seulement quand vous envoyez un spot ou une annonce |
| `raw.githubusercontent.com` | Météo spatiale pour Conditions |
| `cloud.umami.is` | Seulement si vous avez dit oui aux statistiques |

Votre position n’est jamais envoyée nulle part.
