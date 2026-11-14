T = {
'field-info/overview': {'title': 'Infos terrain', 'desc': 'Tout sur l’endroit où vous êtes, en trois onglets.', 'body': '''
**Infos terrain** concerne l’endroit où vous vous trouvez. L’écran a trois onglets :

| Onglet | Ce qu’il montre |
|---|---|
| **Sites** | Les références WWFF autour de vous. Voir {{link:field-info/areas-nearby}}. |
| **Position** | Où vous êtes en termes radio : heure, locator, zones. Voir {{link:field-info/location}}. |
| **Conditions** | La météo spatiale et ce qu’elle signifie pour les bandes. Voir {{link:field-info/conditions-space-weather}} et {{link:field-info/conditions-bands}}. |

## Ouvrir Infos terrain

1. Touchez **Infos terrain** dans la barre du bas (le cercle avec un point).
2. Touchez l’onglet voulu en haut : **Sites**, **Position** ou **Conditions**.
3. Sous le titre, vérifiez d’où part Diana : *« depuis votre position GPS »* ou *« depuis votre locator JN18EU »*.

:::caution[Pas de position ?]
Si Diana indique qu’elle ne sait pas encore où vous êtes, autorisez la localisation (voir {{link:start/welcome-screen}}) ou saisissez votre locator dans **Réglages** › **Votre station**. Avec seulement un locator, Diana part du centre de ce carré, ce qui peut être à quelques kilomètres près.
:::
'''},
'field-info/areas-nearby': {'title': 'Sites à proximité', 'desc': 'Les références WWFF autour de vous, triées comme vous le voulez.', 'body': '''
L’onglet **Sites** liste les références WWFF autour de votre position, dans la distance choisie dans les Réglages (10, 25, 50 ou 100 km). Les références de l’autre côté de la frontière y figurent aussi.

{{img:phone-field-areas|Infos terrain, onglet Sites, avec des références près d’Anvers triées par distance}}

## Une ligne par référence

| Ce que vous voyez | Signification |
|---|---|
| Référence et nom | Par exemple `ONFF-0842 · Boshoek`. |
| Distance et direction | À vol d’oiseau depuis vous, par exemple `1.5 km · 62°`. |
| Nombre de QSO | Combien de contacts ont été faits depuis là, selon l’annuaire WWFF. |
| Dernière activité | La date de la dernière activation. |
| *aucune date d’activation connue* | L’annuaire connaît la référence mais pas de date. |
| *absent de l’annuaire WWFF* | Diana connaît la zone, mais l’annuaire n’a rien dessus. Cela ne veut pas dire qu’elle n’a jamais été activée. |

## Trier : quel ordre choisir ?

| Bouton | Quand l’utiliser |
|---|---|
| **Distance** | Les plus proches d’abord. Quand vous voulez vous installer vite. |
| **Dernière activité** | Les zones restées le plus longtemps sans activité d’abord. C’est là qu’un pile-up est le plus probable. |
| **Nombre de QSO** | Les zones les moins contactées d’abord. Quand vous voulez offrir une nouvelle aux chasseurs. |

## Ouvrir une zone

1. Touchez une ligne.
2. La carte s’ouvre, zoomée sur cette zone, avec son panneau et sa limite.
3. Plus de cent zones à proximité ? Touchez **Afficher plus** en bas.

## Modifier la distance

**Réglages** › **Infos terrain** › 10, 25, 50 ou 100 km. Voir {{link:settings/field-info-distance}}.

:::note
Le nombre de QSO et les dates viennent de l’annuaire WWFF, mis à jour chaque nuit. Là où l’annuaire n’a rien, l’écran le dit, plutôt que d’affirmer « jamais activée ».
:::
'''},
'field-info/location': {'title': 'La position en termes radio', 'desc': 'Heure, locator, position et zones de l’endroit où vous êtes.', 'body': '''
L’onglet **Position** donne tout ce qu’il vous faut sur votre propre emplacement pendant un QSO ou pour votre log. Diana le calcule sur l’appareil lui-même ; cela fonctionne donc aussi sans réseau.

{{img:phone-field-location|Infos terrain, onglet Position, avec heure UTC et locale, locator, précision et zones}}

| Case | Comment la lire |
|---|---|
| **Heure** | UTC et votre heure locale avec fuseau horaire. Votre log est toujours en UTC. |
| **Locator** | Votre locator Maidenhead en six caractères (`JO21FD`) et en huit (`JO21FD70`). En QSO, on donne généralement les six. |
| **Position** | En degrés décimaux et en degrés, minutes et secondes, avec la précision en mètres. |
| **Zones** | Votre zone CQ, votre zone UIT et votre région UIT. La Belgique est en CQ 14, UIT 27, région 1 ; la France métropolitaine aussi en CQ 14, UIT 27. |
| *limite proche : aussi …* | Vous êtes près d’une limite de zone, ou votre position est incertaine. Les deux numéros sont alors possibles. |
| **WWFF la plus proche** | Les références les plus proches, partout dans le monde, à vol d’oiseau. |

:::note[D’où viennent les zones]
Les zones CQ et UIT proviennent d’un jeu de données public, simplifié à environ 3 km. C’est pourquoi, près d’une limite, la case cite aussi la zone voisine.
:::
'''},
'field-info/conditions-space-weather': {'title': 'Conditions : météo spatiale', 'label': 'Météo spatiale', 'desc': 'Le cadran Kp, le SFI, l’indice A et les taches solaires, et ce qu’ils signifient.', 'body': '''
L’onglet **Conditions** commence par la météo spatiale du jour : un cadran avec l’**indice Kp** et trois nombres en dessous.

{{img:phone-field-conditions|Infos terrain, onglet Conditions, avec le cadran Kp sur 2, calme, et les barres des bandes}}

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

La source est la NOAA SWPC. Ce que cela signifie par bande : {{link:field-info/conditions-bands}}.
'''},
'field-info/conditions-bands': {'title': 'Conditions : les bandes', 'label': 'Les barres des bandes', 'desc': 'Comment lire la barre de couleurs de chaque bande au fil de la journée.', 'body': '''
Sous la météo spatiale, l’onglet **Conditions** affiche une barre de couleurs par bande : 80, 40, 20, 15 et 10 m.

## Lire la barre d’une bande

1. Chaque barre est **une bande**. À côté de la bande figure son usage, par exemple *« NVIS et EU »*.
2. La barre va de gauche à droite sur cinq moments de la journée : **matin, midi, après-midi, soir et nuit**. Diana les calcule à partir du lever et du coucher du soleil à votre position.
3. La **couleur** est l’attente : vert c’est bon, jaune moyen, rouge faible.
4. Le fin **trait** vertical, c’est **maintenant**. À droite figure ce qui vaut maintenant, par exemple *« maint. : bon »*.

## Ce que signifient les étiquettes

| Étiquette | Portée |
|---|---|
| **NVIS** | Proche, jusqu’à environ 400 km. Idéal pour être contacté dans votre propre pays. |
| **EU** | En Europe. |
| **DX** | Plus loin, hors d’Europe. |

| Bande | Étiquette dans Diana |
|---|---|
| 80 m | NVIS, EU la nuit |
| 40 m | NVIS et EU |
| 20 m | EU et DX |
| 15 m | DX |
| 10 m | DX |

:::caution[Une indication, pas une promesse]
Les barres sont une estimation approximative de Diana elle-même, fondée sur le SFI, le Kp, la saison et l’heure à votre position. Ce n’est pas une prévision de la NOAA. Une bande affichée comme « faible » peut tout de même être ouverte : écoutez toujours un instant.
:::

:::tip[Exemple sur le terrain]
Kp 2, calme, SFI 91, le soir dans les Ardennes : le 40 m est sur bon et c’est votre meilleure chance pour la Belgique et l’Europe. Le 15 m est sur faible le soir ; inutile de commencer par là.
:::

Sans position, Diana affiche quand même les barres, mais sans le trait de maintenant.
'''},
}
