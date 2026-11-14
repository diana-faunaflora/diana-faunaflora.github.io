---
title: "Der Startbildschirm"
description: "Was du siehst, während Diana startet, und was zu tun ist, wenn sie auf dem Startbildschirm hängen bleibt."
sidebar:
  order: 5
---

Bei jedem Start siehst du zuerst den Startbildschirm: eine Zeichnung einer Aktivierung, ein Funksignal, das darüber läuft, einen Fortschrittsbalken und die Versionsnummer. Währenddessen liest Diana die Referenzdaten und bereitet die Karte vor.

Der Startbildschirm verschwindet von selbst, sobald die Karte gezeichnet ist, spätestens nach neun Sekunden.

## Diana braucht Skripte

Diana ist eine Web-App: alles, was sie tut, läuft als JavaScript in deinem Browser. Blockiert dein Browser oder eine Erweiterung Skripte, kann nichts starten und du bleibst auf dem Startbildschirm.

Nach einer Weile erscheint auf dem Startbildschirm ein Kasten, der genau das sagt. Dann:

1. Erlaube Skripte nur für **diana-onff.github.io**. Nicht für `github.io` oder `github.com`: beides braucht Diana nicht.
2. **Lade die Seite neu.** Am Computer drückst du **F5** oder **Strg+R** (Mac: **Cmd+R**). Auf dem Smartphone ziehst du die Seite nach unten oder tippst auf die Neu-laden-Schaltfläche des Browsers.
3. Hängt es immer noch? Dann blockiert vielleicht eine andere Erweiterung mit, zum Beispiel ein Werbeblocker. Schalte sie für diese Seite nacheinander aus.

:::caution[Neu laden ist entscheidend]
Die meisten Blocker wenden eine neue Regel erst auf eine neu geladene Seite an. Ohne Neuladen bleibt die alte Sperre bestehen, auch wenn du schon auf „Vertrauen“ geklickt hast.
:::

Alle Skripte kommen von Dianas eigener Adresse. Von anderen Seiten wird nichts geladen, außer dem Statistik-Skript, und das nur, wenn du zustimmst. Details unter [Hängt auf dem Startbildschirm](/de/guide/help/scripts-blocked/).

## Beim allerersten Mal

Auf einem Gerät, das Diana noch nie geöffnet hat, folgen nach dem Startbildschirm zwei kurze Dinge: der [Willkommensbildschirm](/de/guide/start/welcome-screen/) und [Der Startassistent](/de/guide/start/setup-wizard/).
