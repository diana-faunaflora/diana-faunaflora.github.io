---
title: "¿Estoy dentro del área?"
description: "Cómo te dice Diana si estás dentro, y cómo leer la precisión."
sidebar:
  order: 6
---

Una tarjeta abajo en el mapa responde la pregunta de todo activador: **¿estoy dentro de la reserva?**

## Qué dice la tarjeta

- **Dentro de un área**: cuál, y la distancia al límite más cercano.
- **Dentro de varias a la vez** (cuando las áreas se superponen): cuántas, y se abre el panel de la más pequeña. Consulta [Áreas superpuestas](/es/guide/map/overlapping-areas/).
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
Sal al exterior, con el cielo despejado, y espera unos segundos. ¿Sigue imprecisa, por encima de unos 75 m? Quizá el sitio solo pueda usar una ubicación aproximada. Aparece entonces un aviso que sugiere revisar el ajuste de ubicación: consulta [Problemas de ubicación](/es/guide/help/location-problems/).
:::

## Dos trampas que Diana vigila

- **En interiores**, una posición por wifi llega a menudo en un segundo diciendo ±20 m. Es la precisión que la base de datos de wifi cree tener, no la real. Diana responde, pero sigue escuchando el resto de los doce segundos y corrige la respuesta si hace falta.
- **Móviles que prometen más de lo que pueden.** Diana compara las lecturas de los últimos 45 segundos. Una lectura suelta disparatada se ignora. Si las lecturas se contradicen, la respuesta dice *"lecturas contradictorias"*. Caminar no cuenta como dispersión.

:::caution
Diana solo puede responder esto para áreas **con** límite. Para un anillo discontinuo o un punto azul no puede. Consulta [Puntos y áreas](/es/guide/map/points-and-areas/).
:::
