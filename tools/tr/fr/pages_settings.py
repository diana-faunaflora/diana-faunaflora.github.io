T = {
'settings/overview': {'title': 'Réglages', 'desc': 'Comment ouvrir les Réglages, et à quoi sert chaque partie.', 'body': '''
Tout ce que vous avez configuré dans l’assistant, et un peu plus, se trouve dans les **Réglages**.

{{img:phone-settings|L’écran Réglages avec Votre station et Votre pays}}

## Ouvrir les Réglages

1. Touchez **Réglages** dans la barre du bas (la roue dentée, tout à droite).
2. Faites défiler jusqu’à la partie à modifier.
3. Modifiez-la. Tout est enregistré immédiatement : il n’y a pas de bouton d’enregistrement. Vous voyez brièvement *« Enregistré sur cet appareil »*.

## Ce qu’ils contiennent

| Partie | Ce que vous réglez | Page |
|---|---|---|
| **Votre station** | Indicatif, indicatif portable, locator | {{link:settings/your-station}} |
| **Votre pays** | Le pays chargé en détail, et le filtre des spots | {{link:settings/your-country}} |
| **Mots rapides pour un spot** | Cinq mots à ajouter d’un toucher | {{link:settings/quick-words}} |
| **Infos terrain** | Jusqu’où regarde l’onglet Sites autour de vous | {{link:settings/field-info-distance}} |
| **Liste des bandes à l’annonce** | Toutes les bandes ou HF uniquement | {{link:settings/band-list}} |
| **Langue** | Une parmi huit, ou suivre le navigateur | {{link:settings/language}} |
| **Confidentialité** | Page de confidentialité, statistiques, tout effacer | {{link:settings/privacy-settings}} |
| **Installer comme application** | Installer sur cet appareil | {{link:start/install-android}} |
| Tout en bas | Version, mises à jour, nouveautés, relancer l’assistant | {{link:settings/version-and-updates}} |

:::caution[Uniquement sur cet appareil]
Tout ce que vous saisissez ici reste dans le navigateur de cet appareil. Vous utilisez aussi Diana sur un autre appareil ? Saisissez-le là aussi. Diana n’a pas de compte pour les relier. Voir {{link:help/data-and-limits}}.
:::
'''},
'settings/your-station': {'title': 'Votre station', 'desc': 'Indicatif, indicatif portable et locator, et comment lire la ligne de position.', 'body': '''
**Réglages** › **Votre station**. Qui vous êtes, et à peu près où vous êtes.

| Champ | Quoi saisir | Ce qu’en fait Diana |
|---|---|---|
| **Indicatif** | Votre indicatif habituel, par exemple `F4ABC`. | Utilisé comme spotter, et détermine le pays que Diana propose. |
| **Indicatif portable** | Celui que vous utilisez sur le terrain, par exemple `F4ABC/P`. | Rempli comme activateur quand vous vous annoncez ou annoncez une activation. |
| **Locator Maidenhead** | Six caractères, par exemple `JN18EU`. | Votre point de départ tant qu’il n’y a pas de GPS : pour la carte, les distances et les lignes vers les spots. |

*« Locator non valide (ex. JO21EE) »* signifie une faute de frappe : deux lettres, deux chiffres, deux lettres.

## Prendre le locator depuis le GPS

1. Placez-vous là où vous voulez le locator, de préférence dehors.
2. Touchez **Depuis le GPS**.
3. Diana remplit le locator à partir de votre position actuelle.

## La ligne de position

Sous le locator, une ligne indique la qualité de votre dernière position, par exemple *« Dernière position : ±8 m · il y a 2 min »*.

| Vous lisez | Ce que cela signifie | Que faire |
|---|---|---|
| ±10 m ou mieux | Satellites. Parfait. | Rien. |
| environ ±50 à 100 m | Généralement le wifi, à l’intérieur. | Essayez dehors. |
| Trop grossière pour dire si vous êtes dans une zone | Pas assez pour dedans ou dehors. | Sortez, sous un ciel dégagé. |
| Reste grossière même dehors | Le site n’a peut-être droit qu’à une position approximative. | Vérifiez le réglage de localisation du téléphone : {{link:help/location-problems}}. |
| *« Pas encore de position GPS sur cet appareil. »* | Localisation non autorisée, ou pas encore demandée. | Autorisez la localisation, ou fiez-vous à votre locator. |

:::note
Il n’y a pas de réglage pour l’endroit où s’ouvre la carte. Elle s’ouvre toujours là où vous êtes, sinon sur votre locator, sinon dans le pays de votre indicatif.
:::
'''},
'settings/your-country': {'title': 'Votre pays', 'desc': 'Le pays que Diana charge en détail, et en quoi il diffère du filtre des spots.', 'body': '''
**Réglages** › **Votre pays**. Un seul choix pour tout : le pays que Diana charge avec ses vraies limites, et les spots et entrées d’agenda qu’affiche le bouton de votre pays. Pour les autres pays, Diana n’affiche toujours que des points.

## Les deux parties

| Partie | Ce qu’elle fait |
|---|---|
| **Pays** | Le pays chargé en détail. La liste indique **Avec limites** ou **Points uniquement**. |
| **Afficher** | Votre pays ou **Mondial**. Le filtre de l’écran Spots, le même interrupteur que sur cet écran. |

Sous la liste, Diana indique ce qu’elle a pour ce pays, par exemple *« ONFF, 947 zones avec limites chargées »*, ou qu’il n’y a pas de limites pour l’OKFF, seulement des points sur la carte.

## Quand le modifier

- **Vous partez à l’étranger** : choisissez le pays que vous visitez. Si Diana a ses limites, les zones y apparaissent entièrement. Voir {{link:travel/abroad}}.
- **Une référence de l’autre côté de la frontière vous intéresse** : touchez son point bleu et utilisez **Afficher [pays] en détail** ; cela revient au même que de le changer ici.

## Étape par étape

1. Touchez **Réglages** en bas à droite.
2. Ouvrez la liste sous **Votre pays** et choisissez le pays.
3. Le changement est immédiat. Lisez la ligne sous la liste pour voir ce qui a été chargé.
4. Vous voulez les spots du monde entier ou seulement de ce pays ? Choisissez-le sous **Afficher**.

:::note
Choisir un autre pays ne modifie jamais **Afficher**. Et inversement : changer le filtre des spots ne charge pas un autre pays.
:::

Pourquoi une référence est une zone ou un point : {{link:map/points-and-areas}}.
'''},
'settings/quick-words': {'title': 'Mots rapides pour un spot', 'desc': 'Cinq mots à ajouter à la remarque d’un spot d’un seul toucher.', 'body': '''
**Réglages** › **Mots rapides pour un spot**. Cinq mots que vous pouvez ajouter à la remarque d’un spot d’un seul toucher, pour ne pas devoir taper sur le terrain.

## Les configurer

1. Remplissez jusqu’à cinq cases, chacune avec un mot ou une courte expression.
2. Une case vide ne donne simplement pas de bouton.
3. Quand vous vous annoncez, ils apparaissent comme boutons sous la remarque. Voir {{link:spots/spot-yourself}}.

## Idées

Mettez ce qui correspond à votre station : un mode, votre puissance, l’antenne, un court statut. Restez bref : une remarque fait au maximum 100 caractères.

:::caution
Pas de remerciements ni de demandes de bande : un spot part vers le DX cluster, où c’est du bruit.
:::
'''},
'settings/field-info-distance': {'title': 'Distance d’Infos terrain', 'desc': 'Jusqu’où regarde l’onglet Sites autour de vous.', 'body': '''
**Réglages** › **Infos terrain**. Jusqu’où l’onglet **Sites** d’Infos terrain regarde autour de votre position : **10, 25, 50 ou 100 km**.

| Choisissez | Quand |
|---|---|
| **10 km** | Beaucoup de zones proches les unes des autres, comme en Flandre. Une liste courte et claire. |
| **25 km** | Un bon compromis dans la plupart des endroits. |
| **50 km** | Moins de zones autour, ou vous êtes prêt à rouler. |
| **100 km** | La campagne, ou l’étranger avec peu de références. |

La liste affiche au maximum cent lignes à la fois ; **Afficher plus** donne le reste. Voir {{link:field-info/areas-nearby}}.
'''},
'settings/band-list': {'title': 'Liste des bandes à l’annonce', 'desc': 'Toutes les bandes ou HF uniquement dans la liste du formulaire d’annonce.', 'body': '''
**Réglages** › **Liste des bandes à l’annonce**. Les bandes que propose la liste de l’écran d’annonce.

| Choix | Bandes |
|---|---|
| **Toutes les bandes** | De 160 m à 23 cm. |
| **HF uniquement** | 80, 40, 30, 20, 15 et 10 m. |

Presque toutes les activations se font sur les bandes HF. Avec **HF uniquement**, la liste reste courte et vous faites moins défiler sur votre téléphone. Vous trafiquez aussi en VHF ou UHF ? Choisissez **Toutes les bandes**.

Voir {{link:spots/announce}}.
'''},
'settings/language': {'title': 'Langue', 'desc': 'Choisir la langue de l’application.', 'body': '''
**Réglages** › **Langue**. Diana parle anglais, néerlandais, français, allemand, danois, italien, espagnol et portugais.

- Choisissez l’une des huit, ou **Suivre le navigateur** pour prendre la langue de votre navigateur.
- Sans choix, Diana démarre en anglais.
- Vous pouvez aussi changer de langue via **≡** sur la carte, ou à la première étape de l’assistant.

Tout change immédiatement. Les noms des zones ne sont jamais traduits : ce sont des noms officiels, qui vont dans votre log exactement comme ils sont publiés.

:::note
Les « Nouveautés » (notes de version) n’existent qu’en néerlandais et en anglais.
:::
'''},
'settings/privacy-settings': {'title': 'Confidentialité et statistiques', 'desc': 'La page de confidentialité, votre choix sur les statistiques et tout effacer.', 'body': '''
**Réglages** › **Confidentialité**. Ce que Diana conserve, ce qu’elle envoie, et votre choix concernant les statistiques anonymes.

## Ce que vous trouvez ici

- **Ouvrir la page confidentialité** : avec quels services Diana communique et pourquoi. Résumé dans {{link:start/privacy}}.
- **Statistiques anonymes** : **Oui, je participe** ou **Non, plutôt pas**. Modifiable quand vous voulez.
- **Tout effacer sur cet appareil** : supprime tout ce que Diana a enregistré ici.

## Modifier votre choix sur les statistiques

1. Touchez **Réglages** › **Confidentialité**.
2. Touchez **Oui, je participe** ou **Non, plutôt pas**.
3. Vous voyez *« Enregistré. »*. C’est tout.

:::tip[Pourquoi un oui aide]
Les statistiques sont comptées avec Umami : pas de cookies, pas de profil, rien qui vous identifie. Pour les bénévoles derrière Diana, c’est le seul moyen de savoir que l’application est utilisée et quels écrans comptent. Diana fonctionne exactement de la même façon dans les deux cas.
:::

## Tout effacer

1. Touchez **Tout effacer sur cet appareil**.
2. Diana demande confirmation : cela supprime votre indicatif, vos réglages, les tuiles hors ligne et votre choix sur les statistiques.
3. Confirmez. Diana recommence à l’écran d’accueil.

Utilisez-le quand vous donnez votre appareil, ou voulez repartir de zéro.
'''},
'settings/version-and-updates': {'title': 'Version et mises à jour', 'desc': 'Lire la ligne de version, rechercher des mises à jour et relancer l’assistant.', 'body': '''
Tout en bas des **Réglages** : la version que vous avez, la fraîcheur des données, et s’il y a du nouveau.

## Lire la ligne de version

`v2.2.12 · 6757ec3 · 14/11/2026`

| Partie | Signification |
|---|---|
| `v2.2.12` | La version de l’application. |
| `6757ec3` | Un code pour cette compilation précise de l’application. |
| `14/11/2026` | La date de cette version. |

Le code ne change que lorsque l’application elle-même change, pas quand la mise à jour nocturne apporte de nouvelles données. La **ligne des données** en dessous indique la fraîcheur des données de la carte.

## Les boutons

- **Rechercher des mises à jour** : Diana regarde si une nouvelle version est prête et la charge.
- **Nouveautés** : ce que chaque version a apporté, la plus récente en haut.
- **Relancer l’assistant de démarrage** : l’assistant part de vos réglages actuels. À la fin, il propose de nouveau la visite.

:::tip[Quelqu’un vous demande votre version ?]
Lisez la ligne de version. C’est exactement ce qu’il faut pour vous aider.
:::

Plus d’informations sur les mises à jour qui semblent ne pas arriver : {{link:help/updates}}.
'''},
}
