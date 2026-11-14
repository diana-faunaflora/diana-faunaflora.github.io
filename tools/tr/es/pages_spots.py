T = {
'spots/on-air': {'title': 'Quién está en el aire', 'desc': 'La pantalla Spots: spots WWFF en directo, ATNO, rumbo y distancia.', 'body': '''
Toca **Spots** en la barra de abajo. La pantalla **Spots y agenda** muestra quién está en el aire desde un área WWFF ahora mismo. La lista llega en directo de WWFF Spotline y se actualiza cada 30 segundos.

{{img:phone-spots-world|La pantalla Spots, pestaña En el aire, Mundial, con una lista de estaciones}}

## Una línea por estación

| Lo que ves | Significado |
|---|---|
| Indicativo | El activador, por ejemplo `F5MQU/P`. |
| Número de QSO | Cuántos contactos se han hecho ya desde esa referencia, según el directorio WWFF. |
| **ATNO** en rojo | *All Time New One*: esta referencia nunca se ha activado. La favorita de los cazadores. |
| Frecuencia, modo, referencia | Por ejemplo `10112 kHz · CW · FFF-4038`. |
| Minutos | Hace cuánto llegó el spot. |
| Rumbo y distancia | Desde ti, por ejemplo `191° · 440 km`. |

## Tu país o mundial

Bajo las pestañas eliges **tu país** (por ejemplo EAFF) o **Mundial**. Diana recuerda la elección y la mantiene igual que el mismo ajuste en Ajustes. El país que representa el botón sigue tu ajuste de país: mientras no elijas uno, Diana lo deduce de tu indicativo (EA… da EAFF, ON… ONFF, DL… DLFF).

## Abrir un spot

1. Toca una línea.
2. Se abre el mapa, acercado a esa área, con un panel: frecuencia y modo, la reserva, el locator de allí y el tuyo, la observación, el número de QSO, Más info y una brújula con el rumbo.
3. **← Volver a Spots**, o el botón atrás de Android, te devuelve a la lista.
4. **×** o deslizar hacia abajo cierra solo el panel y mantiene el mapa.

:::note[¿Spotline no responde?]
Entonces la pantalla lo dice, en vez de mostrar spots antiguos sin avisar.
:::
'''},
'spots/agenda': {'title': 'La agenda', 'desc': 'Activaciones anunciadas: quién planea qué, y cuándo.', 'body': '''
En la pantalla **Spots**, toca la pestaña **Agenda**. Ves todas las activaciones anunciadas, con referencia, bandas y modos, y fecha y hora en UTC.

{{img:phone-agenda|La pestaña Agenda con activaciones anunciadas}}

## Leer la agenda

- **En curso ahora**: un punto naranja y *"en directo hasta …"*.
- **Por venir**: en gris, con fecha y hora de inicio.
- **ATNO** en rojo: la referencia nunca se ha activado.

Tu elección entre **tu país** y **Mundial** también vale aquí.

## Abrir un anuncio

Toca una línea. El mapa se abre en esa área con banda y modo, la reserva, el locator, la observación y el rumbo. **← Volver a Spots** te devuelve.

## Anunciar tú

Toca **+ Anunciar** arriba en la agenda. Consulta {{link:spots/announce}}.

:::tip[También en el mapa]
Los anuncios aparecen en el mapa como un punto blanco con un anillo naranja, con una línea naranja discontinua desde ti. Consulta {{link:map/reading-the-map}}.
:::
'''},
'spots/spot-yourself': {'title': 'Spotéate', 'desc': 'Avisa a los cazadores de que estás en el aire, a través de WWFF Spotline.', 'body': '''
¿En el aire y listo? Spotéate, para que los cazadores te encuentren. El spot va a WWFF Spotline y de ahí al DX cluster.

{{img:phone-spot-yourself|La pantalla Spot con referencia, indicativos, frecuencia, modo y observación}}

## Paso a paso

1. Toca **Spot** en la barra de abajo, o **Spotéate aquí** en el panel de un área.
2. Comprueba la **referencia**. Si estás dentro de un área, o vienes de un panel, Diana ya la ha rellenado y dice de dónde viene.
3. Tus **indicativos** vienen de Ajustes: el indicativo portátil como activador, tu indicativo habitual como spotter.
4. Introduce la **frecuencia** en kHz, por ejemplo `7144`, y elige el **modo**.
5. Opcional: una **observación** corta, hasta 100 caracteres. Toca una de tus **palabras rápidas** para añadirla con un toque.
6. Toca **Comprobar**. Spotline revisa tu spot sin publicarlo, y te dice lo que opina.
7. ¿Aceptado? Toca **Enviar spot**. Recibes una confirmación con el número de tu spot.

## ¿Por qué primero Comprobar y luego Enviar?

Cada petición a Spotline sale de un presupuesto que comparten todos los usuarios. *Comprobar* garantiza que un spot es correcto antes de que cueste un envío real. Si cambias algo después de comprobar, *Enviar* se vuelve a cerrar: el visto bueno era para el spot tal como estaba entonces.

## Qué comprueba Diana por ti

- El formato del **indicativo**, el rango de la **frecuencia** y la longitud de la **observación**, igual que Spotline.
- El **plan de bandas**: un aviso cuando tu modo no encaja con el segmento de tu frecuencia.
- La **referencia**, contra la lista de Diana. Responde al instante, incluso sin cobertura.

:::caution[Lo que no va en una observación]
Nada de agradecimientos ni de peticiones de banda. Cada spot va al DX cluster, donde eso es ruido. Spotline también filtra el lenguaje inapropiado.
:::

## Cuando algo falla

- **¿Pulsado dos veces con mala conexión?** Diana dice que el spot ya estaba. No se publica nada dos veces.
- **¿Spotline lo rechaza?** Recibes la explicación del propio Spotline.
- **¿El envío no funciona en absoluto?** Diana ofrece **Enviar a la manera antigua**: el spot va al formulario de Spotline en una pestaña nueva. Ves tú su respuesta, pero Diana no puede confirmarla.

¿Aún no estás en el aire, solo planeando? Usa la agenda: {{link:spots/announce}}.
'''},
'spots/announce': {'title': 'Anunciar una activación', 'desc': 'Poner una activación prevista en la agenda WWFF, y guardar tu PIN.', 'body': '''
¿Planeas una activación? Anúnciala, para que los cazadores estén preparados. El anuncio va a la agenda WWFF en Spotline.

{{img:phone-announce|La pantalla Anunciar con indicativos, referencia, inicio y fin, bandas y modos}}

## Tres formas de llegar

- **Agenda** en la barra de abajo.
- **+ Anunciar** en la pestaña Agenda de la pantalla Spots.
- **Anunciar una activación** en el panel de un área: la referencia ya viene rellenada.

## Paso a paso

1. Comprueba el **indicativo del activador** y **tu propio indicativo**. Otra persona puede anunciar por un activador.
2. Introduce la **referencia WWFF**, por ejemplo `ONFF-0104`.
3. Elige **inicio** y **fin**. Los eliges con el reloj de tu propio dispositivo; Diana los convierte a UTC antes de que salgan de tu dispositivo.
4. Opcional: marca las **bandas** y los **modos** (puedes elegir varios, por ejemplo *40 m, 20 m · CW, SSB*) y añade una observación.
5. Toca **Comprobar** y, cuando se acepte, **Enviar anuncio**.
6. **Apunta tu PIN.**

:::danger[Guarda tu PIN]
El PIN es la única forma de cambiar o cancelar este anuncio más tarde, en la propia web de Spotline. Diana no puede hacerlo por ti, y un PIN perdido no se recupera. Por eso Diana guarda bajo el formulario una lista de todo lo que has anunciado desde este dispositivo (referencia, fecha, PIN). Toca **✕** para quitar una línea. Esa lista solo existe en este dispositivo.
:::

## Límites

- Como mucho **un mes** de antelación, y el fin no antes del inicio. Spotline aplica las mismas reglas.
- Como mucho **16 anuncios al día** desde un dispositivo a través de Diana, para proteger el presupuesto compartido. El uso normal queda muy por debajo.
- Para los anuncios no hay "manera antigua". Si no funciona, inténtalo más tarde.

Qué bandas ofrece la lista (todas, o solo HF) es un ajuste: {{link:settings/band-list}}.
'''},
}
