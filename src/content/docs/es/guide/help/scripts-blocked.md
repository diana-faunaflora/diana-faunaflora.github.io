---
title: "Atascado en la pantalla de arranque"
description: "Bloqueadores de scripts y navegadores estrictos: lo que Diana necesita, y nada más."
sidebar:
  order: 2
---

Diana es una app web: sin JavaScript no funciona nada. Si un bloqueador detiene los scripts, Diana se queda en la pantalla de arranque. Al cabo de un rato aparece ahí un recuadro que lo dice.

## Solucionarlo

1. Permite los scripts solo para **diana-onff.github.io**. Ni `github.io` ni `github.com`: Diana no necesita ninguno.
2. **Recarga la página**: **F5** o **Ctrl+R** (Mac: **Cmd+R**). En el móvil, desliza la página hacia abajo o toca recargar. Sin recargar, el bloqueo antiguo sigue ahí, aunque ya hayas hecho clic en "Confiar".
3. ¿Sigue atascado? Puede que una segunda extensión también bloquee (un bloqueador de anuncios, una extensión de privacidad). Desactívalas una a una para este sitio.
4. ¿Diana arranca pero el mapa sigue vacío? Permite los workers `blob:` para diana-onff.github.io (ver abajo).

## Qué carga Diana

**Scripts**: todos desde el propio diana-onff.github.io.

| Archivo | Qué es |
|---|---|
| `vendor/maplibre-gl.js` | MapLibre, la biblioteca de mapas. Una copia en la web de Diana, no desde un CDN. |
| `js/*.js` | El código de Diana. |
| `sw.js` | El service worker que mantiene Diana funcionando sin conexión. |

Sin scripts en línea y sin `eval`. Una excepción, solo con tu consentimiento: si dijiste que sí a las estadísticas, el script de Umami de `cloud.umami.is`.

**Worker del mapa**: MapLibre dibuja el mapa en un worker en segundo plano iniciado desde una dirección `blob:`. Un bloqueador que rechace los workers `blob:` deja arrancar Diana, pero el mapa se queda en blanco.

**Datos**:

| Servidor | Para qué |
|---|---|
| `tiles.openfreemap.org` | Teselas del mapa y fuentes de las etiquetas |
| `spots.wwff.co` | Spots en directo y agenda |
| `diana-spotline.diana-onff.workers.dev` | Solo cuando envías un spot o un anuncio |
| `raw.githubusercontent.com` | Clima espacial para Condiciones |
| `cloud.umami.is` | Solo si dijiste que sí a las estadísticas |

Tu posición nunca se envía a ninguna parte.
