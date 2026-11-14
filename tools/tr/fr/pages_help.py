T = {
'help/location-problems': {'title': 'Problèmes de position', 'desc': 'Pas de position, ou une position qui reste grossière : quoi vérifier, appareil par appareil.', 'body': '''
Diana demande toujours la position la plus précise que votre appareil peut fournir. Qu’un site reçoive la position exacte ou une position volontairement floue est un réglage de votre téléphone ou de votre navigateur, pas de Diana.

## D’abord : essayez dehors

À l’intérieur, le wifi seul donne souvent environ ±100 m. Sortez, avec le ciel dégagé au-dessus de vous, attendez dix secondes et touchez **Carte** dans la barre du bas. Souvent, cela suffit.

## Toujours grossière ou pas de position ? Vérifiez le réglage

**Android avec Chrome**

1. Ouvrez l’application **Paramètres** du téléphone.
2. Allez dans **Applications** › **Chrome** › **Autorisations** › **Position**.
3. Choisissez **Autoriser seulement si l’appli est en cours d’utilisation** et activez **Utiliser la position exacte**.
4. Vérifiez aussi le site lui-même : dans Chrome, touchez l’icône à gauche de la barre d’adresse › **Autorisations** › **Position** : autorisée.

**iPhone ou iPad avec Safari**

1. Ouvrez l’application **Réglages**.
2. Allez dans **Confidentialité et sécurité** › **Service de localisation** › **Sites web Safari**.
3. Choisissez **Lorsque l’app est active** et activez **Position exacte**.

**iPhone ou iPad avec un autre navigateur** (par exemple Chrome)

1. Ouvrez l’application **Réglages**.
2. Allez dans **Confidentialité et sécurité** › **Service de localisation** › votre navigateur.
3. Choisissez **Lorsque l’app est active** et activez **Position exacte**.

**Ordinateur**

Cliquez sur l’icône du cadenas à côté de la barre d’adresse et autorisez la **Position** pour ce site. Un ordinateur portable obtient sa position du wifi et fait rarement mieux qu’environ ±50 m.

## « La position est bloquée pour ce site »

Vous (ou quelqu’un) avez refusé auparavant. Diana ne peut pas redemander : vous seul pouvez l’autoriser, dans les réglages du navigateur ou du téléphone ci-dessus. Rechargez ensuite Diana.

## Sans position

Diana fonctionne aussi sans position. Saisissez votre locator dans **Réglages** › **Votre station**. Les distances et les lignes partent alors du centre de votre carré locator. Seul *suis-je dans la zone* a vraiment besoin d’une position précise.

Voir aussi {{link:map/am-i-inside}}.
'''},
'help/scripts-blocked': {'title': 'Bloqué sur l’écran de démarrage', 'desc': 'Bloqueurs de scripts et navigateurs stricts : ce dont Diana a besoin, et rien de plus.', 'body': '''
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
'''},
'help/updates': {'title': 'Mises à jour', 'desc': 'Comment Diana se met à jour toute seule, et que faire si une nouvelle version n’apparaît pas.', 'body': '''
Diana se met à jour toute seule. Vous n’avez jamais rien à télécharger.

## Comment ça marche

- **Les données** (références, nombre de QSO, limites) sont mises à jour chaque nuit. Diana les récupère fraîches à chaque démarrage, et utilise la copie de votre téléphone quand le réseau est faible.
- **L’application elle-même** : quand vous ouvrez Diana avec du réseau, elle vérifie s’il existe une nouvelle version. Une nouvelle version n’est annoncée que lorsqu’il y en a vraiment une.

## Une nouvelle version n’apparaît pas ?

1. Assurez-vous d’avoir du réseau.
2. Ouvrez les **Réglages** et touchez **Rechercher des mises à jour** tout en bas.
3. Comparez la ligne de version avec celle des **Nouveautés**. Voir {{link:settings/version-and-updates}}.
4. Toujours l’ancienne version ? Fermez complètement Diana (balayez-la hors des applications récentes) et rouvrez-la.

:::note
Les versions de l’application figurent dans les **Nouveautés**, la plus récente en haut, en néerlandais et en anglais.
:::
'''},
'help/data-and-limits': {'title': 'Vos données et les limites', 'desc': 'Ce qui reste sur votre appareil, pourquoi rien n’est synchronisé, et ce que Diana ne peut pas faire.', 'body': '''
## Tout reste sur un appareil, dans un navigateur

Vos indicatifs, locator, pays, mots rapides, langue, choix sur les statistiques et les codes PIN de vos annonces sont dans le stockage local de ce seul navigateur. Rien n’est synchronisé.

- Vous utilisez Diana sur votre téléphone et sur votre portable ? Configurez-la sur les deux. Il n’y a pas de compte pour les relier.
- **Effacer les données du navigateur** (historique, cookies et données de sites), utiliser une **fenêtre privée** ou **supprimer l’application installée** efface ces réglages. Diana recommence alors à l’écran d’accueil.

:::caution[Les codes PIN de vos annonces]
Ils sont dans ce même stockage. Effacez le navigateur et ils disparaissent. Notez aussi les codes PIN importants ailleurs.
:::

## Ce que Diana ne peut pas faire

- **Les données en direct dépendent d’autres services.** Les spots et l’agenda viennent de WWFF Spotline. S’il est indisponible, l’écran Spots le dit. Les conditions de propagation viennent de la NOAA ; l’onglet indique leur âge.
- **Les limites n’existent que là où un fichier a été fourni** : aujourd’hui cinq pays. Ailleurs, les références sont des points, et Diana ne peut pas dire si vous êtes dedans. Voir {{link:map/points-and-areas}}.
- **Toutes les réserves n’ont pas d’informations complètes.** Beaucoup n’ont qu’un nom et une référence. C’est une lacune des données sources.
- **Diana ne tient pas de log** et n’envoie pas de logs. Cela reste le rôle de votre logiciel de log et du WWFF.

## Utilisation des données

Les limites et les chiffres d’activation proviennent des programmes WWFF, de la WDPA, de sources publiques et de WWFF Spotline, et restent les données de leurs propriétaires. Voir {{link:about/data-sources}}.
'''},
'help/faq': {'title': 'Questions fréquentes', 'desc': 'Des réponses courtes aux questions les plus fréquentes.', 'body': '''
## Diana est-elle payante ?

Non. Diana est gratuite, sans publicité et sans compte.

## Diana est-elle une application officielle du WWFF ?

Non. Diana est un projet bénévole qui soutient le hobby WWFF. Elle utilise les services publics du WWFF, comme Spotline et l’annuaire.

## Diana envoie-t-elle ma position quelque part ?

Non. Votre position n’est utilisée que sur votre propre écran. Un spot envoie votre indicatif, fréquence, mode, référence et remarque, jamais votre position. Voir {{link:start/privacy}}.

## Diana fonctionne-t-elle sans réseau ?

Oui, avec les dernières données chargées : la carte déjà consultée, les références, Infos terrain Position et le plan de bandes. Les spots en direct et l’envoi d’un spot nécessitent du réseau.

## Pourquoi ma référence est-elle un point et pas une zone ?

Parce que Diana n’a pas de limite pour elle, ou parce qu’elle se trouve dans un autre pays que celui que vous avez chargé. Voir {{link:map/points-and-areas}}.

## Puis-je tenir mon log dans Diana ?

Non. Diana aide avant et pendant l’activation. Votre log reste dans votre logiciel de log. Sous **Règles**, Diana montre le bon nom de fichier.

## Mes réglages ont disparu. Que s’est-il passé ?

Les données du navigateur ont été effacées, l’application a été supprimée, ou vous avez utilisé une fenêtre privée. Voir {{link:help/data-and-limits}}.

## Mon programme national peut-il aussi avoir ses limites ?

Oui. Le coordinateur national envoie le fichier des zones (KMZ) à l’équipe Diana. Plus d’informations dans {{link:about/about-diana}}.

## J’ai trouvé une erreur. Où la signaler ?

Les coordonnées figurent sur la page de confidentialité de l’application (**Réglages** › **Confidentialité**). Indiquez votre ligne de version : {{link:settings/version-and-updates}}.
'''},
}
