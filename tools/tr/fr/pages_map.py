T = {
'map/map-screen': {'title': 'L’écran de la carte', 'desc': 'L’écran principal de Diana : les boutons du haut et la barre du bas.', 'body': '''
La carte est l’écran principal de Diana. Tout le reste part d’ici.

{{img:phone-map|La carte de Diana autour d’Anvers, avec des zones vertes, un spot et des lignes}}

## La barre du bas

De gauche à droite : **Carte**, **Spots**, **Spoter**, **Agenda**, **Infos terrain**, **Règles** et **Réglages**. Touchez-en un pour ouvrir cet écran.

:::tip[Revenir à votre position]
Touchez **Carte** dans la barre du bas à tout moment : la carte se recentre sur l’endroit où vous êtes, et le zoom reste tel quel. Diana refait une mesure GPS si la dernière date de plus de deux minutes ou est moins précise que 30 m. Sans GPS, elle se centre sur votre locator des Réglages, et le dit.
:::

## Les boutons du haut

| Bouton | Ce qu’il fait |
|---|---|
| **⌕** | Rechercher par nom ou numéro de référence. Voir {{link:map/search}}. |
| **◐** | Style de carte : Liberty, Positron, Bright ou Dark. |
| **≡** | Calques et langue. Voir {{link:map/layers-and-styles}}. |

En haut à gauche, une ligne indique combien de références sont chargées, par exemple *« 947 références WWFF · 1 sans limite »*.

## Se déplacer

- **Faites glisser** un doigt pour déplacer la carte.
- **Pincez** avec deux doigts pour zoomer ou dézoomer, ou utilisez **+** et **−** à droite.
- **Touchez** une zone, un point ou un spot pour ouvrir son panneau. Voir {{link:map/area-panel}}.

## Qu’est-ce que je vois ?

Les couleurs, points et lignes sont expliqués dans {{link:map/reading-the-map}}. Pourquoi une référence est une zone et une autre seulement un point est expliqué dans {{link:map/points-and-areas}}.
'''},
'map/points-and-areas': {'title': 'Points et zones', 'desc': 'Pourquoi une référence est une zone verte et une autre un point bleu, et comment changer cela.', 'body': '''
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

Quoi que vous voyiez, **touchez-le** : un panneau s’ouvre avec tout ce que Diana sait. Pour un point bleu, ce sont la référence, le pays et le nom, le locator et les zones, la direction et la distance depuis vous, le nombre de QSO ou **ATNO** si elle n’a jamais été activée, et un lien vers plus d’informations. Voir {{link:map/area-panel}}.

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

Votre filtre de spots (votre pays ou Mondial) ne change pas quand vous choisissez un autre pays. Plus d’informations dans {{link:settings/your-country}}.

:::note[Une nouvelle réserve d’abord comme point]
Les références existantes proviennent de l’annuaire WWFF, chaque nuit. Les limites viennent d’un fichier publié par l’équipe Diana. Une toute nouvelle réserve peut donc apparaître d’abord comme un point et recevoir son contour plus tard.
:::
'''},
'map/reading-the-map': {'title': 'Lire la carte', 'desc': 'Ce que signifie chaque couleur, point et ligne sur la carte.', 'body': '''
Tout sur la carte a un sens. Voici la légende.

{{img:map-legend|Carte autour d’Anvers et de Roosendaal avec des zones vertes, des groupes bleus, une ligne verte pointillée et une ligne orange tiretée}}

## Zones et références

| Ce que vous voyez | Signification |
|---|---|
| Zone verte avec un numéro | Une référence avec sa vraie limite, dans votre pays. Le numéro est la référence, par exemple `ONFF-0602`. |
| Contour orange | La zone que vous venez de toucher. |
| Anneau pointillé avec un point orange | Une référence de votre pays sans limite : un emplacement approximatif. |
| Point bleu | Une référence dans un autre pays. |
| Cercle bleu avec un numéro | Plusieurs points bleus rapprochés. Touchez-le pour zoomer ; il se divise. |
| Ligne grise | Une frontière nationale sur le fond de carte. |

À partir du niveau de zoom 11, chaque point reçoit sa référence comme étiquette.

## Spots et annonces

| Ce que vous voyez | Signification |
|---|---|
| Icône d’antenne verte qui pulse | Une station en l’air maintenant, avec indicatif, fréquence et mode à côté. |
| **Ligne verte pointillée** | De vous vers une station en l’air maintenant. |
| Spot estompé | Un spot de plus de 30 minutes. |
| Point blanc avec anneau orange | Une activation annoncée dans l’agenda. |
| **Ligne orange tiretée** | De vous vers une activation annoncée, avec indicatif et heure. |
| Votre position | Un marqueur. Quand votre position est moins précise qu’environ 10 m, un anneau pointillé montre la marge. |

:::tip[Trop de lignes ?]
Désactivez-les via **≡** › **Lignes vers les spots**. Diana retient ce choix. **⤢ Afficher tous les spots** cadre tous les spots et votre propre position d’un coup.
:::

Pourquoi certaines références sont des zones et d’autres des points : {{link:map/points-and-areas}}.
'''},
'map/area-panel': {'title': 'Infos sur une zone', 'desc': 'Touchez une zone ou un point : le panneau avec tout ce que Diana sait, et s’annoncer depuis là.', 'body': '''
Touchez une zone, un point ou un spot sur la carte. Un panneau monte du bas avec tout ce que Diana sait de cette référence. Diana n’affiche que ce qu’elle sait vraiment : jamais une case vide.

{{img:phone-area-panel|Panneau de ONFF-0685 Hobokense Polder avec superficie, gestionnaire, désignation, catégorie UICN et locator}}

## Ce que contient le panneau

Pour une **zone avec limite** :

- La référence, la région et le nom.
- Ce que contient le fichier de la zone : **superficie** en hectares, **gestionnaire**, **désignation**, **catégorie UICN**, **désigné depuis**. Toutes les réserves n’ont pas tout ; c’est une lacune des données sources, pas quelque chose que Diana cache.
- Le **nombre de QSO** et la **dernière activation**, d’après l’annuaire WWFF.
- Le **locator**, la **zone CQ**, la **zone UIT** et la **région UIT**.
- **Plus d’infos** : le site de la réserve, quand l’annuaire WWFF en a un. Il s’ouvre dans votre navigateur ; Diana et la carte restent où elles étaient.

Pour une **référence sans limite** (anneau pointillé) : le même panneau sans les chiffres de la zone, et une note indiquant que Diana ne peut pas dire si vous êtes dedans.

Pour un **point bleu** dans un autre pays : référence, pays et nom, locator et zones, **Depuis vous** (direction et distance), le nombre de QSO ou **ATNO** en rouge si elle n’a jamais été activée, et Plus d’infos.

## S’annoncer ou annoncer depuis le panneau

En bas de chaque panneau se trouvent deux boutons :

- **Annoncez-vous ici** ouvre le formulaire de spot avec la référence déjà remplie. Voir {{link:spots/spot-yourself}}.
- **Annoncer une activation** ouvre le formulaire de l’agenda avec la référence remplie. Voir {{link:spots/announce}}.

## Fermer le panneau

Faites glisser le panneau **vers le bas**, ou touchez **×**. La carte reste où elle est. Sur un téléphone, un seul panneau du bas est visible à la fois.
'''},
'map/overlapping-areas': {'title': 'Zones qui se chevauchent', 'desc': 'Quand des références se superposent, et comment passer de l’une à l’autre.', 'body': '''
Les références se chevauchent parfois : une petite réserve se trouve souvent à l’intérieur d’une zone naturelle plus grande. Sur ce bout de terrain, vous êtes dans toutes à la fois.

## Comment Diana l’affiche

Diana dessine toujours la zone **la plus petite** au-dessus, pour que vous puissiez la toucher. Un toucher ouvre la plus petite zone sous votre doigt : touchez dans la réserve pour la réserve, et dans le terrain autour pour la zone plus grande.

## Passer à l’autre zone

1. Touchez la carte à l’intérieur de la réserve. Le panneau de la zone **la plus petite** s’ouvre.
2. Faites défiler le panneau jusqu’à **« Ce point est aussi situé dans ces références »**. Les autres zones y figurent comme boutons, avec nom et taille.
3. Touchez un bouton. Le panneau affiche maintenant cette zone, avec sa propre limite en orange.
4. Pour revenir ? Ce panneau a un bouton vers la zone d’où vous venez.

## Avec votre position GPS

Si vous êtes dans plusieurs zones à la fois, la carte d’information en bas de la carte le dit, par exemple *« Vous êtes dans 2 zones »*, avec la distance jusqu’à la limite la plus proche. Diana ouvre alors le panneau de la plus petite zone, avec les autres comme boutons.

:::tip[Ce que cela signifie pour votre activation]
Si vous êtes dans toutes ces zones, les règles WWFF vous permettent de les activer ensemble. Lisez les règles dans Diana sous **Règles**, ou le texte officiel sur wwff.co. Voir {{link:rules/wwff-rules}}.
:::

:::caution[Pas pour les références sans limite]
Un anneau pointillé n’est qu’un emplacement approximatif. Diana ne peut pas y dire si vous êtes dedans, ni donc montrer de chevauchement.
:::
'''},
'map/am-i-inside': {'title': 'Suis-je dans la zone ?', 'desc': 'Comment Diana vous dit si vous êtes dedans, et comment lire la précision.', 'body': '''
Une carte d’information en bas de la carte répond à la question que se pose tout activateur : **suis-je dans la réserve ?**

## Ce que dit la carte d’information

- **Dans une zone** : laquelle, et la distance jusqu’à la limite la plus proche.
- **Dans plusieurs à la fois** (quand des zones se chevauchent) : combien, et le panneau de la plus petite s’ouvre. Voir {{link:map/overlapping-areas}}.
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
Sortez, avec le ciel dégagé au-dessus de vous, et attendez quelques secondes. Elle reste grossière, au-delà d’environ 75 m ? Le site n’a peut-être droit qu’à une position approximative. Un bandeau propose alors de vérifier le réglage de localisation : voir {{link:help/location-problems}}.
:::

## Deux pièges que Diana surveille

- **À l’intérieur**, une position wifi arrive souvent en une seconde en annonçant ±20 m. C’est la précision que la base de données wifi s’attribue, pas la précision réelle. Diana répond, mais continue d’écouter le reste des douze secondes et corrige la réponse si nécessaire.
- **Les téléphones qui promettent plus qu’ils ne peuvent.** Diana compare les relevés des 45 dernières secondes. Un relevé isolé et aberrant est ignoré. Si les relevés se contredisent, la réponse indique *« relevés contradictoires »*. Marcher ne compte pas comme dispersion.

:::caution
Diana ne peut répondre que pour les zones **avec** limite. Pour un anneau pointillé ou un point bleu, elle ne le peut pas. Voir {{link:map/points-and-areas}}.
:::
'''},
'map/layers-and-styles': {'title': 'Calques et style de carte', 'desc': 'Afficher ou masquer des parties de la carte, et choisir un style de carte.', 'body': '''
## Calques (≡)

Touchez **≡** en haut à droite de la carte. Vous pouvez afficher ou masquer :

| Calque | Ce qu’il montre |
|---|---|
| **Zones** | Les zones vertes de votre pays. |
| **Numéros de référence** | Les étiquettes comme `ONFF-0602`. |
| **Sans limite (point)** | Les anneaux pointillés des références sans limite. |
| **Spots sur la carte** | Les spots en direct et les annonces. Ils viennent de WWFF Spotline et se mettent à jour toutes les 30 secondes. |
| **Lignes vers les spots** | Les lignes vertes pointillées et orange tiretées depuis vous. |
| **Autres zones WWFF** | Les points bleus du reste du monde. |

Le même menu contient **⤢ Afficher tous les spots** et les boutons de langue. Diana retient vos choix.

## Style de carte (◐)

Touchez **◐** pour un autre fond de carte :

- **Liberty** : le style par défaut, avec les couleurs du terrain.
- **Positron** : très clair et calme, bien en plein soleil.
- **Bright** : plus de couleurs et de détails.
- **Dark** : sombre, reposant pour les yeux la nuit.

:::tip
Sur le terrain, en plein soleil, **Positron** est souvent le plus lisible.
:::
'''},
'map/search': {'title': 'Rechercher', 'desc': 'Trouver une référence par nom ou numéro, partout dans le monde.', 'body': '''
Touchez **⌕** en haut de la carte et tapez.

- **Un nom**, par exemple `Kalmthoutse Heide`.
- **Une référence complète**, par exemple `ONFF-0012` ou `FFF-4038`.
- **Seulement un numéro**, par exemple `0012`. Diana ne cherche alors que dans votre propre pays.

Toutes les références WWFF du monde peuvent être trouvées. Les résultats du pays chargé apparaissent en premier. Touchez un résultat : la carte zoome dessus et ouvre son panneau.

:::tip
La recherche fonctionne aussi hors ligne : la liste des références est sur votre appareil.
:::
'''},
}
