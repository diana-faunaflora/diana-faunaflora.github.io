T = {
'map/map-screen': {'title': 'La pantalla del mapa', 'desc': 'La pantalla principal de Diana: los botones de arriba y la barra de abajo.', 'body': '''
El mapa es la pantalla principal de Diana. Todo lo demás empieza aquí.

{{img:phone-map|El mapa de Diana alrededor de Amberes, con áreas verdes, un spot y líneas}}

## La barra de abajo

De izquierda a derecha: **Mapa**, **Spots**, **Spot**, **Agenda**, **Info de campo**, **Reglas** y **Ajustes**. Toca uno para abrir esa pantalla.

:::tip[Volver a tu posición]
Toca **Mapa** en la barra de abajo en cualquier momento: el mapa vuelve a centrarse donde estás, y el zoom se queda como está. Diana toma una nueva medida GPS si la última tiene más de dos minutos o es menos precisa que 30 m. Sin GPS, se centra en tu locator de Ajustes, y lo dice.
:::

## Los botones de arriba

| Botón | Qué hace |
|---|---|
| **⌕** | Buscar por nombre o número de referencia. Consulta {{link:map/search}}. |
| **◐** | Estilo del mapa: Liberty, Positron, Bright o Dark. |
| **≡** | Capas e idioma. Consulta {{link:map/layers-and-styles}}. |

Arriba a la izquierda, una línea indica cuántas referencias hay cargadas, por ejemplo *"947 referencias WWFF · 1 sin límite"*.

## Moverse

- **Arrastra** con un dedo para mover el mapa.
- **Pellizca** con dos dedos para acercar o alejar, o usa **+** y **−** a la derecha.
- **Toca** un área, un punto o un spot para abrir su panel. Consulta {{link:map/area-panel}}.

## ¿Qué estoy viendo?

Los colores, puntos y líneas se explican en {{link:map/reading-the-map}}. Por qué una referencia es un área y otra solo un punto se explica en {{link:map/points-and-areas}}.
'''},
'map/points-and-areas': {'title': 'Puntos y áreas', 'desc': 'Por qué una referencia es un área verde y otra un punto azul, y cómo cambiarlo.', 'body': '''
En el mapa, una referencia WWFF aparece de una de tres maneras. Cuál depende de lo que Diana sabe de ella, y del país que hayas elegido.

| Lo que ves | Qué significa | ¿Puede Diana decir si estás dentro? |
|---|---|---|
| **Área verde** | Una referencia con su límite real, en el país elegido. | Sí |
| **Anillo discontinuo con un punto naranja** | Una referencia de tu país sin límite. Solo un lugar aproximado. | No |
| **Punto azul** | Una referencia de otro país. Juntos forman un círculo con un número. | No |

## ¿Por qué un área?

Un área necesita un archivo de límites. Hoy Diana tiene esos archivos para **cinco países**: Bélgica (ONFF), Países Bajos (PAFF), Alemania (DLFF), Dinamarca (OZFF) y Portugal (CTFF), y siguen llegando más. Los facilitan los coordinadores nacionales WWFF.

Diana carga los límites de **un país cada vez**: el que has elegido en Ajustes. Así el mapa sigue siendo rápido en el móvil.

## ¿Por qué un punto?

- La referencia está en un país para el que Diana **no tiene archivo de límites**. Entonces Diana solo conoce la posición del directorio WWFF.
- O el país **sí tiene** límites en Diana, pero **no es el país que has elegido**. Entonces también aparece como punto, hasta que cargues ese país.

## ¿Por qué un anillo discontinuo?

Dentro de un país con límites, algunas referencias no tienen límite en el archivo, por ejemplo territorios de ultramar de los Países Bajos. Aparecen como un anillo discontinuo en el lugar aproximado.

## Los detalles los tienes siempre

Veas lo que veas, **tócalo**: se abre un panel con todo lo que Diana sabe. Para un punto azul son la referencia, el país y el nombre, el locator y las zonas, el rumbo y la distancia desde ti, el número de QSO o **ATNO** si nunca se ha activado, y un enlace a más información. Consulta {{link:map/area-panel}}.

## Cuándo y cómo cambiarlo

Cuando vas a otro país, o quieres ver el límite real de una referencia que ahora es un punto:

**Desde el panel (lo más rápido)**

1. Toca el punto azul.
2. Si Diana tiene los límites de ese país, el panel lo dice y muestra un botón **Mostrar [país] en detalle**.
3. Tócalo. Diana carga ese país y vuelve a abrir la misma referencia, ahora con su límite.

**Desde Ajustes**

1. Toca **Ajustes** abajo a la derecha.
2. En **Tu país**, elige el país. Los países marcados **Con límites** reciben sus áreas; **Solo puntos** se queda en puntos.
3. El cambio es inmediato. Bajo el menú, Diana dice lo que ha cargado, por ejemplo *"PAFF, 281 áreas con límites cargadas"*.

Tu filtro de spots (tu país o Mundial) no cambia al elegir otro país. Más en {{link:settings/your-country}}.

:::note[Una reserva nueva, primero como punto]
Qué referencias existen viene del directorio WWFF, cada noche. Los límites vienen de un archivo que publica el equipo de Diana. Por eso una reserva recién creada puede aparecer primero como punto y recibir su contorno más tarde.
:::
'''},
'map/reading-the-map': {'title': 'Leer el mapa', 'desc': 'Qué significa cada color, punto y línea del mapa.', 'body': '''
Todo en el mapa tiene un significado. Esta es la leyenda.

{{img:map-legend|Mapa alrededor de Amberes y Roosendaal con áreas verdes, grupos azules, una línea verde punteada y una línea naranja discontinua}}

## Áreas y referencias

| Lo que ves | Significado |
|---|---|
| Área verde con un número | Una referencia con su límite real, en tu país. El número es la referencia, por ejemplo `ONFF-0602`. |
| Contorno naranja | El área que acabas de tocar. |
| Anillo discontinuo con un punto naranja | Una referencia de tu país sin límite: un lugar aproximado. |
| Punto azul | Una referencia de otro país. |
| Círculo azul con un número | Varios puntos azules juntos. Tócalo para acercar; se separa. |
| Línea gris | Una frontera en el mapa base. |

A partir del nivel de zoom 11, cada punto recibe su referencia como etiqueta.

## Spots y anuncios

| Lo que ves | Significado |
|---|---|
| Icono de antena verde que late | Una estación en el aire ahora, con indicativo, frecuencia y modo al lado. |
| **Línea verde punteada** | De ti a una estación que está en el aire ahora. |
| Spot difuminado | Un spot de hace más de 30 minutos. |
| Punto blanco con anillo naranja | Una activación anunciada en la agenda. |
| **Línea naranja discontinua** | De ti a una activación anunciada, con indicativo y hora. |
| Tu posición | Un marcador. Cuando tu posición es menos precisa que unos 10 m, un anillo discontinuo muestra el margen. |

:::tip[¿Demasiadas líneas?]
Desactívalas en **≡** › **Líneas hacia los spots**. Diana recuerda la elección. **⤢ Ver todos los spots** encuadra todos los spots y tu propia posición de una vez.
:::

Por qué algunas referencias son áreas y otras puntos: {{link:map/points-and-areas}}.
'''},
'map/area-panel': {'title': 'Detalles del área', 'desc': 'Toca un área o un punto: el panel con todo lo que Diana sabe, y spotearte desde ahí.', 'body': '''
Toca un área, un punto o un spot en el mapa. Desde abajo sube un panel con todo lo que Diana sabe de esa referencia. Diana solo muestra lo que de verdad sabe: nunca una casilla vacía.

{{img:phone-area-panel|Panel de ONFF-0685 Hobokense Polder con superficie, gestor, designación, categoría UICN y locator}}

## Qué hay en el panel

Para un **área con límite**:

- Referencia, región y nombre.
- Lo que contiene el archivo del área: **superficie** en hectáreas, **gestor**, **designación**, **categoría UICN**, **designado desde**. No todas las reservas lo tienen todo; es una laguna de los datos de origen, no algo que Diana oculte.
- El **número de QSO** y la **última activación**, del directorio WWFF.
- El **locator**, la **zona CQ**, la **zona ITU** y la **región ITU**.
- **Más info**: la web de la reserva, cuando el directorio WWFF tiene una. Se abre en tu navegador, así que Diana y el mapa se quedan donde estaban.

Para una **referencia sin límite** (anillo discontinuo): el mismo panel sin los datos del área, y una nota de que Diana no puede saber si estás dentro.

Para un **punto azul** de otro país: referencia, país y nombre, locator y zonas, **Desde ti** (rumbo y distancia), el número de QSO o **ATNO** en rojo si nunca se ha activado, y Más info.

## Spotearte o anunciar desde el panel

Abajo en cada panel hay dos botones:

- **Spotéate aquí** abre el formulario del spot con la referencia ya rellenada. Consulta {{link:spots/spot-yourself}}.
- **Anunciar una activación** abre el formulario de la agenda con la referencia rellenada. Consulta {{link:spots/announce}}.

## Cerrar el panel

Desliza el panel **hacia abajo**, o toca **×**. El mapa se queda donde está. En el móvil solo se ve un panel inferior a la vez.
'''},
'map/overlapping-areas': {'title': 'Áreas superpuestas', 'desc': 'Cuando las referencias se superponen, y cómo cambiar entre ellas.', 'body': '''
A veces las referencias se superponen: una reserva pequeña suele estar dentro de un área natural mayor. En ese trozo de terreno estás en todas a la vez.

## Cómo lo muestra Diana

Diana dibuja siempre el área **más pequeña** encima, para que puedas tocarla. Un toque abre el área más pequeña bajo tu dedo: toca dentro de la reserva para la reserva, y en el terreno de alrededor para el área mayor.

## Cambiar a la otra área

1. Toca el mapa dentro de la reserva. Se abre el panel del área **más pequeña**.
2. Desplázate por el panel hasta **"Este punto también está dentro de estas referencias"**. Las demás áreas aparecen ahí como botones, con nombre y tamaño.
3. Toca un botón. El panel muestra ahora esa área, con su propio límite en naranja.
4. ¿Volver? Ese panel tiene un botón hacia el área de la que venías.

## Con tu posición GPS

Si estás en varias áreas a la vez, la tarjeta de abajo del mapa lo dice, por ejemplo *"Estás en 2 zonas"*, con la distancia al límite más cercano. Diana abre entonces el panel del área más pequeña, con las demás como botones.

:::tip[Qué significa para tu activación]
Si estás en todas esas áreas, las reglas WWFF te permiten activarlas juntas. Lee las reglas en Diana en **Reglas**, o el texto oficial en wwff.co. Consulta {{link:rules/wwff-rules}}.
:::

:::caution[No para referencias sin límite]
Un anillo discontinuo es solo un lugar aproximado. Ahí Diana no puede saber si estás dentro, y por tanto tampoco mostrar superposiciones.
:::
'''},
'map/am-i-inside': {'title': '¿Estoy dentro del área?', 'desc': 'Cómo te dice Diana si estás dentro, y cómo leer la precisión.', 'body': '''
Una tarjeta abajo en el mapa responde la pregunta de todo activador: **¿estoy dentro de la reserva?**

## Qué dice la tarjeta

- **Dentro de un área**: cuál, y la distancia al límite más cercano.
- **Dentro de varias a la vez** (cuando las áreas se superponen): cuántas, y se abre el panel de la más pequeña. Consulta {{link:map/overlapping-areas}}.
- **Fuera**: el área más cercana y a qué distancia está.

Cada respuesta termina con lo buena que era tu posición, por ejemplo *"posición ±6 m"*.

:::note[Áreas formadas por varias parcelas]
Algunas referencias constan de parcelas separadas. El panel indica entonces cuántas. Toda tu estación debe estar dentro de una de ellas.
:::

## Por qué tarda unos segundos

Un móvil que acaba de despertar su GPS responde primero con el wifi y las antenas de telefonía, y esa posición puede fallar por cientos de metros. Por eso Diana sigue escuchando mientras la precisión mejora, y muestra lo que tiene hasta ese momento: *"Afinando… ±380 m"*. Responde en cuanto la posición es lo bastante buena, o a los doce segundos con la mejor que haya obtenido. Si sigue siendo imprecisa, la respuesta lo dice.

## Leer la precisión

| Precisión | Qué suele significar |
|---|---|
| ±10 m o mejor | Satélites. Fiable, también cerca de un límite. |
| de ±20 a 50 m | Aceptable. Cuidado cerca de un límite. |
| ±100 m o peor | Wifi o antenas de telefonía, a menudo en interiores. No basta para estar seguro. |

Cuando el margen supera unos 10 m, se dibuja un **anillo discontinuo** alrededor de tu marcador con exactamente ese radio. Un anillo ajustado significa satélites; un anillo que cubre toda la manzana significa que la respuesta vino del wifi.

:::tip[Conseguir una posición mejor]
Sal al exterior, con el cielo despejado, y espera unos segundos. ¿Sigue imprecisa, por encima de unos 75 m? Quizá el sitio solo pueda usar una ubicación aproximada. Aparece entonces un aviso que sugiere revisar el ajuste de ubicación: consulta {{link:help/location-problems}}.
:::

## Dos trampas que Diana vigila

- **En interiores**, una posición por wifi llega a menudo en un segundo diciendo ±20 m. Es la precisión que la base de datos de wifi cree tener, no la real. Diana responde, pero sigue escuchando el resto de los doce segundos y corrige la respuesta si hace falta.
- **Móviles que prometen más de lo que pueden.** Diana compara las lecturas de los últimos 45 segundos. Una lectura suelta disparatada se ignora. Si las lecturas se contradicen, la respuesta dice *"lecturas contradictorias"*. Caminar no cuenta como dispersión.

:::caution
Diana solo puede responder esto para áreas **con** límite. Para un anillo discontinuo o un punto azul no puede. Consulta {{link:map/points-and-areas}}.
:::
'''},
'map/layers-and-styles': {'title': 'Capas y estilo del mapa', 'desc': 'Activar y desactivar partes del mapa, y elegir un estilo.', 'body': '''
## Capas (≡)

Toca **≡** arriba a la derecha del mapa. Puedes activar y desactivar:

| Capa | Qué muestra |
|---|---|
| **Zonas** | Las áreas verdes de tu país. |
| **Números de referencia** | Las etiquetas como `ONFF-0602`. |
| **Sin límite (punto)** | Los anillos discontinuos de las referencias sin límite. |
| **Spots en el mapa** | Spots en directo y anuncios. Vienen de WWFF Spotline y se actualizan cada 30 segundos. |
| **Líneas hacia los spots** | Las líneas verdes punteadas y naranjas discontinuas desde ti. |
| **Otras zonas WWFF** | Los puntos azules del resto del mundo. |

En el mismo menú están **⤢ Ver todos los spots** y los botones de idioma. Diana recuerda tus elecciones.

## Estilo del mapa (◐)

Toca **◐** para otro mapa base:

- **Liberty**: el predeterminado, con colores del terreno.
- **Positron**: muy claro y tranquilo, bueno a pleno sol.
- **Bright**: más color y detalle.
- **Dark**: oscuro, descansa la vista de noche.

:::tip
En el campo, a pleno sol, **Positron** suele ser el más fácil de leer.
:::
'''},
'map/search': {'title': 'Buscar', 'desc': 'Encontrar una referencia por nombre o número, en cualquier parte del mundo.', 'body': '''
Toca **⌕** en la parte superior del mapa y escribe.

- **Un nombre**, por ejemplo `Kalmthoutse Heide`.
- **Una referencia completa**, por ejemplo `ONFF-0012` o `DLFF-0210`.
- **Solo un número**, por ejemplo `0012`. Entonces Diana busca solo en tu propio país.

Se puede encontrar cualquier referencia WWFF del mundo. Los resultados del país cargado salen primero. Toca un resultado: el mapa se acerca y abre su panel.

:::tip
La búsqueda también funciona sin conexión: la lista de referencias está en tu dispositivo.
:::
'''},
}
