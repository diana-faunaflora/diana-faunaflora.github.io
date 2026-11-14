T = {
'help/location-problems': {'title': 'Problemas de ubicación', 'desc': 'Sin posición, o una posición que sigue imprecisa: qué revisar, dispositivo por dispositivo.', 'body': '''
Diana siempre pide la posición más precisa que tu dispositivo puede dar. Que un sitio reciba la posición exacta o una difuminada a propósito es un ajuste de tu móvil o navegador, no de Diana.

## Primero: prueba fuera

En interiores, el wifi solo da a menudo unos ±100 m. Sal al exterior, con el cielo despejado, espera diez segundos y toca **Mapa** en la barra de abajo. Muchas veces basta con eso.

## ¿Sigue imprecisa o sin posición? Revisa el ajuste

**Android con Chrome**

1. Abre la app **Ajustes** del móvil.
2. Ve a **Aplicaciones** › **Chrome** › **Permisos** › **Ubicación**.
3. Elige **Permitir solo mientras se usa la aplicación** y activa **Usar ubicación precisa**.
4. Revisa también el propio sitio: en Chrome, toca el icono a la izquierda de la barra de direcciones › **Permisos** › **Ubicación**: permitida.

**iPhone o iPad con Safari**

1. Abre la app **Ajustes**.
2. Ve a **Privacidad y seguridad** › **Localización** › **Sitios web de Safari**.
3. Elige **Cuando se use la app** y activa **Ubicación exacta**.

**iPhone o iPad con otro navegador** (por ejemplo Chrome)

1. Abre la app **Ajustes**.
2. Ve a **Privacidad y seguridad** › **Localización** › tu navegador.
3. Elige **Cuando se use la app** y activa **Ubicación exacta**.

**Ordenador**

Haz clic en el icono del candado junto a la barra de direcciones y permite la **Ubicación** para este sitio. Un portátil obtiene su posición del wifi y rara vez es mejor que unos ±50 m.

## "La ubicación está bloqueada para este sitio"

Tú (o alguien) dijiste que no antes. Diana no puede volver a preguntar: solo tú puedes permitirla, en los ajustes del navegador o del móvil de arriba. Después recarga Diana.

## Sin ubicación

Diana también funciona sin ubicación. Introduce tu locator en **Ajustes** › **Tu estación**. Las distancias y líneas parten entonces del centro de tu cuadro locator. Solo *estoy dentro del área* necesita de verdad una posición precisa.

Consulta también {{link:map/am-i-inside}}.
'''},
'help/scripts-blocked': {'title': 'Atascado en la pantalla de arranque', 'desc': 'Bloqueadores de scripts y navegadores estrictos: lo que Diana necesita, y nada más.', 'body': '''
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
'''},
'help/updates': {'title': 'Actualizaciones', 'desc': 'Cómo se actualiza Diana sola, y qué hacer si no aparece una versión nueva.', 'body': '''
Diana se actualiza sola. Nunca tienes que descargar nada.

## Cómo funciona

- **Los datos** (referencias, número de QSO, límites) se actualizan cada noche. Diana los obtiene frescos en cada arranque, y usa la copia de tu móvil cuando la cobertura es débil.
- **La propia app**: cuando abres Diana con cobertura, comprueba si hay una versión nueva. Solo se anuncia una versión nueva cuando de verdad la hay.

## ¿No aparece una versión nueva?

1. Asegúrate de tener cobertura.
2. Abre **Ajustes** y toca **Buscar actualizaciones** abajo del todo.
3. Compara la línea de versión con la de **Novedades**. Consulta {{link:settings/version-and-updates}}.
4. ¿Sigue la versión antigua? Cierra Diana del todo (deslízala fuera de las apps recientes) y vuelve a abrirla.

:::note
Las versiones de la app están en **Novedades**, la más reciente arriba, en neerlandés e inglés.
:::
'''},
'help/data-and-limits': {'title': 'Tus datos y los límites', 'desc': 'Qué se queda en tu dispositivo, por qué nada se sincroniza, y qué no puede hacer Diana.', 'body': '''
## Todo se queda en un dispositivo, en un navegador

Tus indicativos, locator, país, palabras rápidas, idioma, elección sobre estadísticas y los PIN de tus anuncios están en el almacenamiento local de ese único navegador. Nada se sincroniza.

- ¿Usas Diana en el móvil y en el portátil? Configúrala en los dos. No hay cuenta para vincularlos.
- **Borrar los datos del navegador** (historial, cookies y datos de sitios), usar una **ventana privada** o **quitar la app instalada** borra estos ajustes. Diana vuelve entonces a la pantalla de bienvenida.

:::caution[Los PIN de tus anuncios]
Están en ese mismo almacenamiento. Borra el navegador y desaparecen. Apunta también en otro sitio los PIN importantes.
:::

## Lo que Diana no puede hacer

- **Los datos en directo dependen de otros.** Los spots y la agenda vienen de WWFF Spotline. Si no está disponible, la pantalla Spots lo dice. Las condiciones de propagación vienen de la NOAA; la pestaña dice su antigüedad.
- **Solo hay límites donde se ha entregado un archivo**: hoy cinco países. En otros sitios las referencias son puntos, y Diana no puede decir si estás dentro. Consulta {{link:map/points-and-areas}}.
- **No todas las reservas tienen datos completos.** Muchas solo tienen un nombre y una referencia. Es una laguna de los datos de origen.
- **Diana no lleva el log** ni sube logs. Eso sigue en manos de tu programa de log y del WWFF.

## Uso de los datos

Los límites y las cifras de activación vienen de los programas WWFF, la WDPA, fuentes públicas y WWFF Spotline, y siguen siendo datos de sus propietarios. Consulta {{link:about/data-sources}}.
'''},
'help/faq': {'title': 'Preguntas frecuentes', 'desc': 'Respuestas cortas a las preguntas más habituales.', 'body': '''
## ¿Diana cuesta algo?

No. Diana es gratuita, sin publicidad y sin cuenta.

## ¿Diana es una app oficial del WWFF?

No. Diana es un proyecto de voluntarios que apoya el hobby WWFF. Usa los servicios públicos del WWFF, como Spotline y el directorio.

## ¿Diana envía mi posición a algún sitio?

No. Tu posición solo se usa en tu propia pantalla. Un spot envía tu indicativo, frecuencia, modo, referencia y observación, nunca tu posición. Consulta {{link:start/privacy}}.

## ¿Diana funciona sin cobertura?

Sí, con los últimos datos cargados: el mapa que ya has visto, las referencias, Info de campo Ubicación y el plan de bandas. Los spots en directo y enviar un spot necesitan cobertura.

## ¿Por qué mi referencia es un punto y no un área?

Porque Diana no tiene un límite para ella, o porque está en un país distinto del que has cargado. Consulta {{link:map/points-and-areas}}.

## ¿Puedo llevar el log en Diana?

No. Diana ayuda antes y durante la activación. Tu log se queda en tu programa de log. En **Reglas**, Diana muestra el nombre de archivo correcto.

## Mis ajustes han desaparecido. ¿Qué ha pasado?

Se borraron los datos del navegador, se quitó la app, o usaste una ventana privada. Consulta {{link:help/data-and-limits}}.

## ¿Mi programa nacional también puede tener límites?

Sí. El coordinador nacional envía el archivo de áreas (KMZ) al equipo de Diana. Más en {{link:about/about-diana}}.

## He encontrado un error. ¿Dónde lo comunico?

Los datos de contacto están en la página de privacidad de la app (**Ajustes** › **Privacidad**). Indica tu línea de versión: {{link:settings/version-and-updates}}.
'''},
}
