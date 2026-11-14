T = {
'settings/overview': {'title': 'Ajustes', 'desc': 'Cómo abrir Ajustes, y para qué sirve cada parte.', 'body': '''
Todo lo que configuraste en el asistente, y algo más, está en **Ajustes**.

{{img:phone-settings|La pantalla Ajustes con Tu estación y Tu país}}

## Abrir Ajustes

1. Toca **Ajustes** en la barra de abajo (la rueda dentada, del todo a la derecha).
2. Desplázate hasta la parte que quieras cambiar.
3. Cámbiala. Todo se guarda al momento: no hay botón de guardar. Ves un instante *"Guardado en este dispositivo"*.

## Qué contiene

| Parte | Qué ajustas | Página |
|---|---|---|
| **Tu estación** | Indicativo, indicativo portátil, locator | {{link:settings/your-station}} |
| **Tu país** | Qué país se carga en detalle, y el filtro de spots | {{link:settings/your-country}} |
| **Palabras rápidas para un spot** | Cinco palabras para añadir con un toque | {{link:settings/quick-words}} |
| **Info de campo** | Hasta dónde mira la pestaña Áreas a tu alrededor | {{link:settings/field-info-distance}} |
| **Lista de bandas al anunciar** | Todas las bandas o solo HF | {{link:settings/band-list}} |
| **Idioma** | Uno de ocho, o seguir el navegador | {{link:settings/language}} |
| **Privacidad** | Página de privacidad, estadísticas, borrar todo | {{link:settings/privacy-settings}} |
| **Instalar como aplicación** | Instalar en este dispositivo | {{link:start/install-android}} |
| Al final | Versión, actualizaciones, novedades, repetir el asistente | {{link:settings/version-and-updates}} |

:::caution[Solo en este dispositivo]
Todo lo que introduces aquí se queda en el navegador de este dispositivo. ¿Usas Diana también en otro dispositivo? Introdúcelo allí también. Diana no tiene cuenta para vincularlos. Consulta {{link:help/data-and-limits}}.
:::
'''},
'settings/your-station': {'title': 'Tu estación', 'desc': 'Indicativo, indicativo portátil y locator, y cómo leer la línea de posición.', 'body': '''
**Ajustes** › **Tu estación**. Quién eres y, más o menos, dónde estás.

| Campo | Qué poner | Qué hace Diana con él |
|---|---|---|
| **Indicativo** | Tu indicativo habitual, por ejemplo `EA4ABC`. | Se usa como spotter, y decide qué país propone Diana. |
| **Indicativo portátil** | El que usas en el campo, por ejemplo `EA4ABC/P`. | Se rellena como activador cuando te spoteas o anuncias. |
| **Locator Maidenhead** | Seis caracteres, por ejemplo `IN80DK`. | Tu punto de partida mientras no haya GPS: para el mapa, las distancias y las líneas hacia los spots. |

*"Locator no válido (ej. JO21EE)"* significa un error al teclear: dos letras, dos cifras, dos letras.

## Tomar el locator del GPS

1. Ponte donde quieras el locator, mejor al aire libre.
2. Toca **Tomar del GPS**.
3. Diana rellena el locator con tu posición actual.

## La línea de posición

Bajo el locator, una línea dice lo buena que fue tu última posición, por ejemplo *"Última posición: ±8 m · hace 2 min"*.

| Lees | Qué significa | Qué hacer |
|---|---|---|
| ±10 m o mejor | Satélites. Bien. | Nada. |
| unos ±50 a 100 m | Normalmente wifi, en interiores. | Prueba fuera. |
| Demasiado imprecisa para saber si estás en un área | No basta para dentro o fuera. | Sal, con cielo despejado. |
| Sigue imprecisa también fuera | Quizá el sitio solo pueda usar una ubicación aproximada. | Revisa el ajuste de ubicación del móvil: {{link:help/location-problems}}. |
| *"Todavía no hay posición GPS en este dispositivo."* | Ubicación no permitida, o aún no se ha pedido. | Permite la ubicación, o confía en tu locator. |

:::note
No hay ningún ajuste para dónde se abre el mapa. Siempre se abre donde estás; si no, en tu locator; si no, en el país de tu indicativo.
:::
'''},
'settings/your-country': {'title': 'Tu país', 'desc': 'Qué país carga Diana en detalle, y en qué se diferencia del filtro de spots.', 'body': '''
**Ajustes** › **Tu país**. Una sola elección para todo: qué país carga Diana con sus límites reales, y qué spots y entradas de agenda muestra el botón de tu país. De los demás países, Diana siempre muestra solo puntos.

## Las dos partes

| Parte | Qué hace |
|---|---|
| **País** | El país que se carga en detalle. En la lista pone **Con límites** o **Solo puntos**. |
| **Mostrar** | Tu país o **Mundial**. El filtro de la pantalla Spots, el mismo interruptor que en esa pantalla. |

Bajo la lista, Diana dice lo que tiene para ese país, por ejemplo *"ONFF, 947 áreas con límites cargadas"*, o que para el OKFF no hay límites, solo puntos en el mapa.

## Cuándo cambiarlo

- **Te vas al extranjero**: elige el país que visitas. Si Diana tiene sus límites, allí las áreas aparecen completas. Consulta {{link:travel/abroad}}.
- **Te interesa una referencia al otro lado de la frontera**: toca su punto azul y usa **Mostrar [país] en detalle**; hace lo mismo que cambiarlo aquí.

## Paso a paso

1. Toca **Ajustes** abajo a la derecha.
2. Abre la lista en **Tu país** y elige el país.
3. El cambio es inmediato. Lee la línea bajo la lista para ver qué se ha cargado.
4. ¿Quieres los spots de todo el mundo o solo de ese país? Elígelo en **Mostrar**.

:::note
Elegir otro país nunca cambia **Mostrar**. Y al revés: cambiar el filtro de spots no carga otro país.
:::

Por qué una referencia es un área o un punto: {{link:map/points-and-areas}}.
'''},
'settings/quick-words': {'title': 'Palabras rápidas para un spot', 'desc': 'Cinco palabras que añades a la observación de un spot con un toque.', 'body': '''
**Ajustes** › **Palabras rápidas para un spot**. Cinco palabras que puedes añadir a la observación de un spot con un toque, para no tener que escribir en el campo.

## Configurarlas

1. Rellena hasta cinco casillas, cada una con una palabra o una frase corta.
2. Una casilla vacía simplemente no da botón.
3. Cuando te spoteas, aparecen como botones bajo la observación. Consulta {{link:spots/spot-yourself}}.

## Ideas

Pon lo que encaje con tu estación: un modo, tu potencia, la antena, un estado breve. Que sean cortas: una observación tiene como máximo 100 caracteres.

:::caution
Nada de agradecimientos ni de peticiones de banda: un spot va al DX cluster, donde eso es ruido.
:::
'''},
'settings/field-info-distance': {'title': 'Distancia de Info de campo', 'desc': 'Hasta dónde mira la pestaña Áreas a tu alrededor.', 'body': '''
**Ajustes** › **Info de campo**. Hasta dónde mira la pestaña **Áreas** de Info de campo alrededor de tu posición: **10, 25, 50 o 100 km**.

| Elige | Cuándo |
|---|---|
| **10 km** | Muchas áreas juntas, como en Flandes. Una lista corta y clara. |
| **25 km** | Un buen término medio para la mayoría de los sitios. |
| **50 km** | Menos áreas alrededor, o no te importa conducir. |
| **100 km** | El campo, o el extranjero con pocas referencias. |

La lista muestra como mucho cien líneas a la vez; **Mostrar más** da el resto. Consulta {{link:field-info/areas-nearby}}.
'''},
'settings/band-list': {'title': 'Lista de bandas al anunciar', 'desc': 'Todas las bandas o solo HF en la lista del formulario de anuncio.', 'body': '''
**Ajustes** › **Lista de bandas al anunciar**. Qué bandas ofrece la lista de la pantalla de anuncio.

| Opción | Bandas |
|---|---|
| **Todas las bandas** | De 160 m a 23 cm. |
| **Solo HF** | 80, 40, 30, 20, 15 y 10 m. |

Casi todas las activaciones son en las bandas de HF. Con **Solo HF** la lista es corta y te desplazas menos en el móvil. ¿También trabajas VHF o UHF? Elige **Todas las bandas**.

Consulta {{link:spots/announce}}.
'''},
'settings/language': {'title': 'Idioma', 'desc': 'Elegir el idioma de la app.', 'body': '''
**Ajustes** › **Idioma**. Diana habla inglés, neerlandés, francés, alemán, danés, italiano, español y portugués.

- Elige uno de los ocho, o **Seguir el navegador** para usar el idioma de tu navegador.
- Sin elegir nada, Diana arranca en inglés.
- También puedes cambiar el idioma en **≡** en el mapa, o en el primer paso del asistente.

Todo cambia al momento. Los nombres de las áreas nunca se traducen: son nombres oficiales y van en tu log tal como se publican.

:::note
Las "Novedades" (las notas de versión) solo existen en neerlandés e inglés.
:::
'''},
'settings/privacy-settings': {'title': 'Privacidad y estadísticas', 'desc': 'La página de privacidad, tu elección sobre estadísticas y borrarlo todo.', 'body': '''
**Ajustes** › **Privacidad**. Qué guarda Diana, qué envía, y tu elección sobre estadísticas anónimas.

## Qué encuentras aquí

- **Abrir la página de privacidad**: con qué servicios habla Diana y por qué. Resumen en {{link:start/privacy}}.
- **Estadísticas anónimas**: **Sí, ayudo con gusto** o **No, prefiero que no**. Cámbialo cuando quieras.
- **Borrar todo en este dispositivo**: elimina todo lo que Diana ha guardado aquí.

## Cambiar tu elección sobre estadísticas

1. Toca **Ajustes** › **Privacidad**.
2. Toca **Sí, ayudo con gusto** o **No, prefiero que no**.
3. Ves *"Guardado."*. Eso es todo.

:::tip[Por qué ayuda un sí]
Las estadísticas se cuentan con Umami: sin cookies, sin perfil, nada que te identifique. Para los voluntarios que hay detrás de Diana es la única forma de saber que la app se usa y qué pantallas importan. Diana funciona exactamente igual en ambos casos.
:::

## Borrarlo todo

1. Toca **Borrar todo en este dispositivo**.
2. Diana pide confirmación: esto elimina tu indicativo, tus ajustes, las teselas sin conexión y tu elección sobre estadísticas.
3. Confirma. Diana vuelve a la pantalla de bienvenida.

Úsalo cuando des tu dispositivo a otra persona, o quieras empezar de cero.
'''},
'settings/version-and-updates': {'title': 'Versión y actualizaciones', 'desc': 'Leer la línea de versión, buscar actualizaciones y repetir el asistente.', 'body': '''
Al final de **Ajustes**: qué versión tienes, lo recientes que son los datos, y si hay algo nuevo.

## Leer la línea de versión

`v2.2.12 · 6757ec3 · 14/11/2026`

| Parte | Significado |
|---|---|
| `v2.2.12` | La versión de la app. |
| `6757ec3` | Un código para esta compilación exacta de la app. |
| `14/11/2026` | La fecha de esa versión. |

El código solo cambia cuando cambia la propia app, no cuando la actualización nocturna trae datos nuevos. La **línea de datos** de debajo dice lo recientes que son los datos del mapa.

## Los botones

- **Buscar actualizaciones**: Diana mira si hay una versión nueva lista y la carga.
- **Novedades**: lo que trajo cada versión, la más reciente arriba.
- **Repetir el asistente de inicio**: el asistente parte de tus ajustes actuales. Al final vuelve a ofrecer el recorrido.

:::tip[¿Alguien te pregunta qué versión tienes?]
Lee en voz alta la línea de versión. Es exactamente lo que hace falta para ayudarte.
:::

Más sobre actualizaciones que parecen no llegar: {{link:help/updates}}.
'''},
}
