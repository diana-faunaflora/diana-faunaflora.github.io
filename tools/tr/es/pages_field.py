T = {
'field-info/overview': {'title': 'Info de campo', 'desc': 'Todo sobre el lugar donde estás, en tres pestañas.', 'body': '''
**Info de campo** trata del lugar donde estás. Tiene tres pestañas:

| Pestaña | Qué muestra |
|---|---|
| **Áreas** | Las referencias WWFF a tu alrededor. Consulta {{link:field-info/areas-nearby}}. |
| **Ubicación** | Dónde estás en términos de radio: hora, locator, zonas. Consulta {{link:field-info/location}}. |
| **Condiciones** | El clima espacial y lo que significa para las bandas. Consulta {{link:field-info/conditions-space-weather}} y {{link:field-info/conditions-bands}}. |

## Abrir Info de campo

1. Toca **Info de campo** en la barra de abajo (el círculo con un punto).
2. Toca arriba la pestaña que quieras: **Áreas**, **Ubicación** o **Condiciones**.
3. Bajo el título, comprueba desde dónde parte Diana: *"desde tu posición GPS"* o *"desde tu localizador IN80DK"*.

:::caution[¿Sin posición?]
Si Diana dice que todavía no sabe dónde estás, permite la ubicación (consulta {{link:start/welcome-screen}}) o introduce tu locator en **Ajustes** › **Tu estación**. Solo con un locator, Diana calcula desde el centro de ese cuadro, que puede estar a unos kilómetros.
:::
'''},
'field-info/areas-nearby': {'title': 'Áreas cercanas', 'desc': 'Las referencias WWFF a tu alrededor, ordenadas como quieras.', 'body': '''
La pestaña **Áreas** lista las referencias WWFF alrededor de tu posición, dentro de la distancia que elegiste en Ajustes (10, 25, 50 o 100 km). También aparecen las referencias al otro lado de la frontera.

{{img:phone-field-areas|Info de campo, pestaña Áreas, con referencias cerca de Amberes ordenadas por distancia}}

## Una línea por referencia

| Lo que ves | Significado |
|---|---|
| Referencia y nombre | Por ejemplo `ONFF-0842 · Boshoek`. |
| Distancia y rumbo | En línea recta desde ti, por ejemplo `1.5 km · 62°`. |
| Número de QSO | Cuántos contactos se han hecho desde allí, según el directorio WWFF. |
| Última actividad | La fecha de la última activación. |
| *sin fecha de activación conocida* | El directorio tiene la referencia, pero no una fecha. |
| *no figura en el directorio WWFF* | Diana conoce el área, pero el directorio no tiene nada. Eso no significa que nunca se haya activado. |

## Ordenar: ¿qué orden elegir?

| Botón | Cuándo usarlo |
|---|---|
| **Distancia** | Las más cercanas primero. Cuando quieres montar rápido. |
| **Última actividad** | Las áreas que llevan más tiempo sin salir al aire, primero. Ahí es más probable un pile-up. |
| **Número de QSO** | Las áreas menos trabajadas primero. Cuando quieres dar a los cazadores una nueva. |

## Abrir un área

1. Toca una línea.
2. Se abre el mapa, acercado a esa área, con su panel y su límite.
3. ¿Más de cien áreas cerca? Toca **Mostrar más** abajo.

## Cambiar la distancia

**Ajustes** › **Info de campo** › 10, 25, 50 o 100 km. Consulta {{link:settings/field-info-distance}}.

:::note
El número de QSO y las fechas vienen del directorio WWFF, actualizado cada noche. Donde el directorio no tiene nada, la pantalla lo dice, en vez de llamarla "nunca activada".
:::
'''},
'field-info/location': {'title': 'La ubicación en términos de radio', 'desc': 'Hora, locator, posición y zonas del lugar donde estás.', 'body': '''
La pestaña **Ubicación** te da todo lo que necesitas sobre tu propio sitio durante un QSO o para tu log. Diana lo calcula en el propio dispositivo, así que también funciona sin cobertura.

{{img:phone-field-location|Info de campo, pestaña Ubicación, con hora UTC y local, locator, precisión y zonas}}

| Casilla | Cómo leerla |
|---|---|
| **Hora** | UTC y tu hora local con zona horaria. Tu log siempre va en UTC. |
| **Locator** | Tu locator Maidenhead con seis caracteres (`JO21FD`) y con ocho (`JO21FD70`). En un QSO normalmente se dan los seis. |
| **Posición** | En grados decimales y en grados, minutos y segundos, con la precisión en metros. |
| **Zonas** | Tu zona CQ, zona ITU y región ITU. Bélgica es CQ 14, ITU 27, región 1; la España peninsular es CQ 14, ITU 37. |
| *límite cercano: también …* | Estás cerca de un límite de zona, o tu posición es incierta. Entonces son posibles los dos números. |
| **WWFF más cercanas** | Las referencias más cercanas, en cualquier parte del mundo, en línea recta. |

:::note[De dónde salen las zonas]
Las zonas CQ e ITU vienen de un conjunto de datos público, simplificado a unos 3 km. Por eso, cerca de un límite, la casilla menciona también la zona vecina.
:::
'''},
'field-info/conditions-space-weather': {'title': 'Condiciones: clima espacial', 'label': 'Clima espacial', 'desc': 'El indicador Kp, el SFI, el índice A y las manchas solares, y qué significan.', 'body': '''
La pestaña **Condiciones** empieza con el clima espacial de hoy: un indicador con el **índice Kp** y tres números debajo.

{{img:phone-field-conditions|Info de campo, pestaña Condiciones, con el indicador Kp en 2, tranquila, y las barras de las bandas}}

## El indicador Kp

El Kp mide lo agitado que está el campo magnético terrestre, en una escala de 0 a 9. Cuanto más bajo, mejor para las bandas altas. Diana muestra el valor oficial de tres horas de la NOAA, y al lado una estimación de los últimos minutos.

| Kp | Palabra en Diana | Qué significa |
|---|---|---|
| de 0 a 2 | tranquila | Sin efecto. Condiciones normales. |
| 3 | inestable | Algo agitado. Normalmente aún sin efecto notable. |
| 4 | activa | 20, 15 y 10 m bajan un escalón. |
| 5 y 6 | tormenta G1, G2 | Tormenta menor: 20, 15 y 10 m empeoran. 80 y 40 m apenas lo notan. |
| de 7 a 9 | tormenta de G3 a G5 | Tormenta fuerte: todas las bandas empeoran, sobre todo las altas. |

:::note
El Kp es un valor mundial, no una medida en tu posición.
:::

## Los tres números

| Número | Qué te dice |
|---|---|
| **SFI** | Flujo solar. Cuanto más alto, mejor se abren las bandas altas. Hacia 70 es bajo, por encima de 150 es alto. |
| **A** | Lo agitado que ha estado el campo magnético durante todo el día. Bajo es bueno. |
| **Manchas solares** | Van con el SFI: más manchas, más posibilidades de DX en las bandas altas. |

El SFI, el A y las manchas solares son valores diarios; Diana dice de qué día son.

## ¿Qué antigüedad tienen los datos?

Bajo el indicador pone cuándo se actualizaron los datos, por ejemplo *"Actualizado a las 14:37 (hace 12 min)"*. Diana intenta obtenerlos dos veces por hora, pero en la práctica puede haber unas horas entre dos actualizaciones.

- Más de **ocho horas**: el mensaje se vuelve naranja.
- Valor Kp de más de **doce horas**: Diana lo indica aparte.

La fuente es NOAA SWPC. Qué significa por banda: {{link:field-info/conditions-bands}}.
'''},
'field-info/conditions-bands': {'title': 'Condiciones: las bandas', 'label': 'Las barras de bandas', 'desc': 'Cómo leer la barra de colores de cada banda a lo largo del día.', 'body': '''
Bajo el clima espacial, la pestaña **Condiciones** muestra una barra de colores por banda: 80, 40, 20, 15 y 10 m.

## Leer la barra de una banda

1. Cada barra es **una banda**. Junto a la banda pone para qué sirve, por ejemplo *"NVIS y EU"*.
2. La barra va de izquierda a derecha por cinco partes del día: **mañana, mediodía, tarde, anochecer y noche**. Diana las calcula a partir de la salida y la puesta del sol en tu posición.
3. El **color** es la expectativa: verde es buena, amarillo regular, rojo mala.
4. La fina **raya** vertical es **ahora**. A la derecha pone lo que vale ahora, por ejemplo *"ahora: buena"*.

## Qué significan las etiquetas

| Etiqueta | Alcance |
|---|---|
| **NVIS** | Cerca, hasta unos 400 km. Ideal para que te trabajen dentro de tu propio país. |
| **EU** | Dentro de Europa. |
| **DX** | Más lejos, fuera de Europa. |

| Banda | Etiqueta en Diana |
|---|---|
| 80 m | NVIS, EU de noche |
| 40 m | NVIS y EU |
| 20 m | EU y DX |
| 15 m | DX |
| 10 m | DX |

:::caution[Una indicación, no una promesa]
Las barras son una estimación aproximada de la propia Diana, basada en el SFI, el Kp, la estación del año y la hora del día en tu posición. No es un pronóstico de la NOAA. Una banda marcada como "mala" puede estar abierta igualmente: escucha siempre un momento.
:::

:::tip[Ejemplo en el campo]
Kp 2, tranquila, SFI 91, al anochecer en las Ardenas: los 40 m están en buena y son tu mejor opción para Bélgica y Europa. Los 15 m están en mala al anochecer; no hace falta empezar por ahí.
:::

Sin posición, Diana sigue mostrando las barras, pero sin la raya de ahora.
'''},
}
