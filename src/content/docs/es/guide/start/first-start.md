---
title: "La pantalla de arranque"
description: "Qué ves mientras Diana arranca, y qué hacer si se queda en la pantalla de arranque."
sidebar:
  order: 5
---

Cada vez que Diana arranca, ves primero la pantalla de arranque: un dibujo de una activación, una señal de radio que la recorre, una barra de progreso y el número de versión. Mientras tanto, Diana lee los datos de las referencias y prepara el mapa.

La pantalla de arranque desaparece sola en cuanto el mapa está dibujado, y como mucho a los nueve segundos.

## Diana necesita scripts

Diana es una app web: todo lo que hace se ejecuta como JavaScript en tu navegador. Si el navegador o una extensión bloquea los scripts, nada puede arrancar y te quedas en la pantalla de arranque.

Al cabo de un rato aparece en la pantalla de arranque un recuadro que lo explica. Entonces:

1. Permite los scripts solo para **diana-onff.github.io**. No para `github.io` ni para `github.com`: Diana no necesita ninguno.
2. **Recarga la página.** En un ordenador pulsa **F5** o **Ctrl+R** (Mac: **Cmd+R**). En el móvil, desliza la página hacia abajo o toca el botón de recargar del navegador.
3. ¿Sigue sin funcionar? Quizá otra extensión también bloquee, como un bloqueador de anuncios. Desactívalas una a una para este sitio.

:::caution[Recargar es imprescindible]
La mayoría de los bloqueadores solo aplican una regla nueva a una página que se vuelve a cargar. Sin recargar, el bloqueo antiguo sigue ahí, aunque ya hayas hecho clic en "Confiar".
:::

Todos los scripts vienen de la propia dirección de Diana. No se carga nada de otros sitios, salvo el script de estadísticas, y solo si dices que sí. Detalles en [Atascado en la pantalla de arranque](/es/guide/help/scripts-blocked/).

## La primerísima vez

En un dispositivo que nunca ha abierto Diana, tras la pantalla de arranque vienen dos pasos cortos: la [Pantalla de bienvenida](/es/guide/start/welcome-screen/) y [El asistente de inicio](/es/guide/start/setup-wizard/).
