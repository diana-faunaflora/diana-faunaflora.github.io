---
title: "Confidentialité"
description: "Ce que Diana sait, ce qu’elle ne sait pas, et pourquoi."
sidebar:
  order: 9
---

Diana est conçue pour que vos données restent chez vous. Cette page résume la page de confidentialité de l’application (**Réglages** › **Confidentialité** › **Ouvrir la page confidentialité**).

## En bref

- Votre indicatif, votre locator et vos réglages restent dans le navigateur de cet appareil. Rien n’est envoyé nulle part.
- Votre position GPS n’est utilisée que sur l’écran devant vous. Elle n’est jamais envoyée nulle part.
- Vous annoncer envoie votre indicatif, votre fréquence, votre mode et la référence à WWFF Spotline, jamais votre position.
- Avec votre autorisation séparée, Diana peut compter une visite anonyme. Rien n’est compté sans votre oui, et vous pouvez changer d’avis à tout moment dans les Réglages.
- Diana ne pose aucun cookie publicitaire et ne crée aucun profil de vous.

## Ce qui reste sur cet appareil

Votre indicatif, votre indicatif portable, votre locator, et des réglages comme les bandes, la distance d’Infos terrain, les mots rapides et la langue, ainsi que votre choix concernant les statistiques et le fait d’avoir vu l’écran d’accueil. Diana garde aussi une copie hors ligne des tuiles de la carte et de l’application elle-même, pour continuer à fonctionner sans réseau. C’est du cache de navigateur ordinaire, pas des données personnelles.

## Les services avec lesquels Diana communique

| Service | Pourquoi |
|---|---|
| WWFF Spotline (`spots.wwff.co`) | Les spots en direct et l’agenda. Reçoit votre indicatif, fréquence, mode, référence et remarque quand vous vous annoncez. Jamais votre position. |
| OpenFreeMap (`tiles.openfreemap.org`) | Les tuiles de la carte, construites à partir des données OpenStreetMap. Pas de cookies. |
| Le relais Diana (un Cloudflare Worker) | Transmet votre spot ou votre annonce à Spotline. Compte les requêtes par adresse IP hachée contre les abus, n’enregistre jamais votre indicatif, votre position ou votre remarque. |
| Umami (`cloud.umami.is`) | Compte une visite anonyme, uniquement avec votre autorisation. Pas de cookies, pas de données personnelles. |

## Ce qu’envoie un spot de vous-même

Exactement ceci, et rien d’autre : l’indicatif de l’activateur, l’indicatif du spotter, la fréquence, le mode, la référence et une remarque facultative que vous avez tapée vous-même. Jamais votre position.

## Tout effacer

**Réglages** › **Confidentialité** › **Tout effacer sur cet appareil** supprime tout ce que Diana a enregistré sur cet appareil : votre indicatif, vos réglages, les tuiles hors ligne et votre choix concernant les statistiques. Diana recommence alors à l’écran d’accueil.

## Vos droits et contact

Comme Diana ne garde vos réglages personnels que sur votre propre appareil, les consulter, les corriger ou les supprimer est aussi simple qu’ouvrir les Réglages. Pour toute question sur les statistiques anonymes, ou pour une réclamation, la page de confidentialité de l’application donne l’adresse de contact. En Belgique, vous pouvez aussi vous adresser à l’Autorité de protection des données (autoriteprotectiondonnees.be) ; en France, à la CNIL (cnil.fr).
