T = {
'spots/on-air': {'title': 'Qui est en l’air', 'desc': 'L’écran Spots : les spots WWFF en direct, ATNO, direction et distance.', 'body': '''
Touchez **Spots** dans la barre du bas. L’écran **Spots et agenda** montre qui est en l’air depuis une zone WWFF en ce moment. La liste arrive en direct de WWFF Spotline et se met à jour toutes les 30 secondes.

{{img:phone-spots-world|L’écran Spots, onglet En cours, Mondial, avec une liste de stations}}

## Une ligne par station

| Ce que vous voyez | Signification |
|---|---|
| Indicatif | L’activateur, par exemple `F5MQU/P`. |
| Nombre de QSO | Combien de contacts ont déjà été faits depuis cette référence, selon l’annuaire WWFF. |
| **ATNO** en rouge | *All Time New One* : cette référence n’a jamais été activée. La préférée des chasseurs. |
| Fréquence, mode, référence | Par exemple `10112 kHz · CW · FFF-4038`. |
| Minutes | Depuis combien de temps le spot est arrivé. |
| Direction et distance | Depuis vous, par exemple `191° · 440 km`. |

## Votre pays ou mondial

Sous les onglets, vous choisissez **votre pays** (par exemple FFF) ou **Mondial**. Diana retient ce choix et le garde aligné sur le même réglage dans les Réglages. Le pays que représente le bouton suit votre réglage de pays : tant que vous n’en avez pas choisi, Diana le déduit de votre indicatif (F… donne FFF, ON… ONFF, DL… DLFF).

## Ouvrir un spot

1. Touchez une ligne.
2. La carte s’ouvre, zoomée sur cette zone, avec un panneau : fréquence et mode, la réserve, le locator sur place et le vôtre, la remarque, le nombre de QSO, Plus d’infos et une boussole avec la direction.
3. **← Retour : Spots**, ou le bouton retour d’Android, vous ramène à la liste.
4. **×** ou glisser vers le bas ferme seulement le panneau et garde la carte.

:::note[Spotline injoignable ?]
L’écran le dit alors, plutôt que de montrer d’anciens spots sans avertissement.
:::
'''},
'spots/agenda': {'title': 'L’agenda', 'desc': 'Les activations annoncées : qui prévoit quoi, et quand.', 'body': '''
Sur l’écran **Spots**, touchez l’onglet **Agenda**. Vous voyez toutes les activations annoncées, avec référence, bandes et modes, et date et heure en UTC.

{{img:phone-agenda|L’onglet Agenda avec des activations annoncées}}

## Lire l’agenda

- **En cours** : un point orange et *« en direct jusqu’à … »*.
- **À venir** : en gris, avec la date et l’heure de début.
- **ATNO** en rouge : la référence n’a jamais été activée.

Votre choix entre **votre pays** et **Mondial** s’applique aussi ici.

## Ouvrir une annonce

Touchez une ligne. La carte s’ouvre sur cette zone avec la bande et le mode, la réserve, le locator, la remarque et la direction. **← Retour : Spots** vous ramène.

## Annoncer vous-même

Touchez **+ Annoncer** en haut de l’agenda. Voir {{link:spots/announce}}.

:::tip[Aussi sur la carte]
Les annonces figurent sur la carte sous forme de point blanc avec un anneau orange, avec une ligne orange tiretée depuis vous. Voir {{link:map/reading-the-map}}.
:::
'''},
'spots/spot-yourself': {'title': 'Vous annoncer (self-spot)', 'label': 'Vous annoncer', 'desc': 'Dire aux chasseurs que vous êtes en l’air, via WWFF Spotline.', 'body': '''
En l’air et prêt ? Annoncez-vous, pour que les chasseurs vous trouvent. Le spot part vers WWFF Spotline et de là vers le DX cluster.

{{img:phone-spot-yourself|L’écran Spoter avec référence, indicatifs, fréquence, mode et remarque}}

## Étape par étape

1. Touchez **Spoter** dans la barre du bas, ou **Annoncez-vous ici** dans le panneau d’une zone.
2. Vérifiez la **référence**. Si vous êtes dans une zone, ou venez d’un panneau, Diana l’a déjà remplie et dit d’où elle vient.
3. Vos **indicatifs** viennent des Réglages : l’indicatif portable comme activateur, votre indicatif habituel comme spotter.
4. Saisissez la **fréquence** en kHz, par exemple `7144`, et choisissez le **mode**.
5. Facultatif : une courte **remarque**, jusqu’à 100 caractères. Touchez un de vos **mots rapides** pour l’ajouter d’un toucher.
6. Touchez **Vérifier**. Spotline examine votre spot sans le publier, et vous dit ce qu’il en pense.
7. Accepté ? Touchez **Envoyer le spot**. Vous recevez une confirmation avec le numéro de votre spot.

## Pourquoi d’abord Vérifier, puis Envoyer ?

Chaque requête à Spotline est prise sur un budget partagé par tous les utilisateurs. *Vérifier* garantit qu’un spot est correct avant qu’il coûte un vrai envoi. Si vous modifiez quelque chose après la vérification, *Envoyer* se referme : l’accord portait sur le spot tel qu’il était alors.

## Ce que Diana vérifie pour vous

- Le format de l’**indicatif**, la plage de **fréquence** et la longueur de la **remarque**, comme Spotline.
- Le **plan de bandes** : un avertissement quand votre mode ne correspond pas au segment de votre fréquence.
- La **référence**, d’après la liste de Diana. La réponse est immédiate, même sans réseau.

:::caution[Ce qui n’a pas sa place dans une remarque]
Pas de remerciements ni de demandes de bande. Chaque spot part vers le DX cluster, où c’est du bruit. Spotline filtre aussi le langage inapproprié.
:::

## Quand quelque chose ne va pas

- **Appuyé deux fois sur une mauvaise connexion ?** Diana dit que le spot était déjà là. Rien n’est publié deux fois.
- **Spotline refuse ?** Vous recevez l’explication de Spotline lui-même.
- **L’envoi ne fonctionne pas du tout ?** Diana propose **Envoyer à l’ancienne manière** : le spot part vers le propre formulaire de Spotline dans un nouvel onglet. Vous voyez leur réponse vous-même, mais Diana ne peut pas la confirmer.

Pas encore en l’air, seulement en train de planifier ? Utilisez l’agenda : {{link:spots/announce}}.
'''},
'spots/announce': {'title': 'Annoncer une activation', 'desc': 'Inscrire une activation prévue dans l’agenda WWFF, et conserver votre code PIN.', 'body': '''
Vous prévoyez une activation ? Annoncez-la, pour que les chasseurs soient prêts. L’annonce part vers l’agenda WWFF sur Spotline.

{{img:phone-announce|L’écran Annoncer avec indicatifs, référence, début et fin, bandes et modes}}

## Trois façons d’y accéder

- **Agenda** dans la barre du bas.
- **+ Annoncer** dans l’onglet Agenda de l’écran Spots.
- **Annoncer une activation** dans le panneau d’une zone : la référence est alors déjà remplie.

## Étape par étape

1. Vérifiez l’**indicatif de l’activateur** et **votre propre indicatif**. Quelqu’un d’autre peut annoncer pour un activateur.
2. Saisissez la **référence WWFF**, par exemple `FFF-4038`.
3. Choisissez le **début** et la **fin**. Vous les choisissez sur l’horloge de votre propre appareil ; Diana les convertit en UTC avant qu’ils quittent votre appareil.
4. Facultatif : cochez les **bandes** et les **modes** (plusieurs possibles, par exemple *40 m, 20 m · CW, SSB*) et ajoutez une remarque.
5. Touchez **Vérifier** puis, une fois accepté, **Envoyer l’annonce**.
6. **Notez votre code PIN.**

:::danger[Conservez votre code PIN]
Le PIN est le seul moyen de modifier ou d’annuler cette annonce plus tard, sur le site de Spotline. Diana ne peut pas le faire à votre place, et un PIN perdu ne peut pas être récupéré. C’est pourquoi Diana garde sous le formulaire une liste de tout ce que vous avez annoncé depuis cet appareil (référence, date, PIN). Touchez **✕** pour supprimer une ligne. Cette liste n’existe que sur cet appareil.
:::

## Limites

- Au maximum **un mois** à l’avance, et la fin pas avant le début. Spotline applique les mêmes règles.
- Au maximum **16 annonces par jour** depuis un appareil via Diana, pour protéger le budget partagé. Un usage normal reste bien en dessous.
- Il n’y a pas d’« ancienne manière » pour les annonces. Si cela ne fonctionne pas, réessayez plus tard.

Les bandes proposées par la liste (toutes, ou HF uniquement) sont un réglage : {{link:settings/band-list}}.
'''},
}
