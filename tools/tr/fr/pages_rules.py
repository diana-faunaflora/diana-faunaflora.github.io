T = {
'rules/wwff-rules': {'title': 'Les règles WWFF dans Diana', 'desc': 'La sélection de règles WWFF dans l’application, et le bon nom pour votre fichier de log.', 'body': '''
Touchez **Règles** dans la barre du bas. L’onglet **Règles** s’ouvre : une sélection des règles officielles WWFF qui comptent le plus sur le terrain, dans votre langue.

{{img:phone-rules|L’écran Règles avec les règles sur la zone de référence}}

## Ce qu’il contient

Les règles 3.5, 3.6, 4.4, 4.7, 6.8, 6.9 et 6.11 des WWFF Global Rules, en trois groupes :

- **La zone** : être à l’intérieur de la zone de référence, références qui en bordent ou en contiennent une autre, activer plusieurs références à la fois.
- **Les QSO** : règles sur les contacts eux-mêmes.
- **Les logs** : comment nommer et envoyer votre log.

Ce sont des règles WWFF ; elles s’appliquent donc aussi au FFF et à tout autre programme national.

:::note[Traductions]
Les textes dans les autres langues sont traduits par l’équipe Diana. C’est le texte anglais du WWFF qui fait foi. Chaque traduction renvoie au PDF officiel.
:::

## Le nom de votre fichier de log

La règle 6.8 impose un nom de fichier précis. Diana montre un exemple dont chaque partie est expliquée :

`ON3VZ@ONFF-0104 20261002.adi`

| Partie | Signification |
|---|---|
| `ON3VZ` | Votre indicatif. |
| `@` | Séparateur. |
| `ONFF-0104` | La référence. |
| (espace) | Un espace. |
| `20261002` | La date : année, mois, jour. |
| `.adi` | Un fichier de log ADIF. |

La règle 6.9 renvoie à la recherche officielle de logs du WWFF : [wwff.co/logsearch](https://wwff.co/logsearch/).

:::tip
Diana ne tient pas votre log. Elle vous aide avant et pendant l’activation ; votre log reste dans votre propre logiciel.
:::
'''},
'rules/band-plan': {'title': 'Le plan de bandes', 'desc': 'Où vous pouvez émettre sur chaque bande, avec les fréquences préférées WWFF.', 'body': '''
Sur l’écran **Règles**, touchez l’onglet **Plan de bandes**.

{{img:phone-bandplan|Le plan de bandes avec les segments CW, numérique et SSB du 80, 40 et 30 m}}

## Comment le lire

Pour chaque bande :

- Une **barre** avec les segments **CW**, **numérique** et **SSB**, avec leurs fréquences, par exemple *CW 3,500 à 3,570 MHz*.
- La fréquence **FT8**, signalée.
- Les **fréquences préférées WWFF**, mises en avant dans un encadré jaune, par exemple *SSB 7,144 · CW 7,024*.

## Pourquoi c’est important

Quand vous vous annoncez, Diana vérifie votre fréquence par rapport à ce plan de bandes et vous avertit si votre mode ne correspond pas au segment. Voir {{link:spots/spot-yourself}}.

:::tip
Un jour de forte activité, commencez près de la fréquence préférée WWFF : c’est là que les chasseurs écoutent en premier.
:::
'''},
}
