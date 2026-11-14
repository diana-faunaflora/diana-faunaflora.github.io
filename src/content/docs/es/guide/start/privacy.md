---
title: "Privacidad"
description: "Qué sabe Diana, qué no sabe, y por qué."
sidebar:
  order: 9
---

Diana está hecha para que tus datos se queden contigo. Esta página resume la página de privacidad de la app (**Ajustes** › **Privacidad** › **Abrir la página de privacidad**).

## En resumen

- Tu indicativo, tu locator y tus ajustes se quedan en el navegador de este dispositivo. No se envía nada a ninguna parte.
- Tu posición GPS solo se usa en la pantalla que tienes delante. Nunca se envía a ninguna parte.
- Spotearte envía tu indicativo, frecuencia, modo y referencia a WWFF Spotline, nunca tu posición.
- Con tu permiso aparte, Diana puede contar una visita anónima. Sin tu sí no se cuenta nada, y puedes cambiar de opinión en cualquier momento en Ajustes.
- Diana no usa cookies publicitarias ni crea un perfil tuyo.

## Qué se queda en este dispositivo

Tu indicativo, indicativo portátil, locator y ajustes como bandas, la distancia de Info de campo, palabras rápidas e idioma, junto con tu elección sobre estadísticas y si ya has visto la pantalla de bienvenida. Diana guarda además una copia sin conexión de las teselas del mapa y de la propia app, para seguir funcionando sin cobertura. Eso es caché normal del navegador, no datos personales.

## Servicios con los que habla Diana

| Servicio | Para qué |
|---|---|
| WWFF Spotline (`spots.wwff.co`) | Spots en directo y la agenda. Recibe tu indicativo, frecuencia, modo, referencia y observación cuando te spoteas. Nunca tu posición. |
| OpenFreeMap (`tiles.openfreemap.org`) | Las teselas del mapa, hechas con datos de OpenStreetMap. Sin cookies. |
| El relé de Diana (un Cloudflare Worker) | Pasa tu spot o anuncio a Spotline. Cuenta peticiones por dirección IP con hash contra abusos, nunca registra tu indicativo, posición ni observación. |
| Umami (`cloud.umami.is`) | Cuenta una visita anónima, solo con tu permiso. Sin cookies, sin datos personales. |

## Qué envía un spot propio

Exactamente esto, y nada más: el indicativo del activador, el indicativo del spotter, la frecuencia, el modo, la referencia y una observación opcional escrita por ti. Nunca tu posición.

## Borrarlo todo

**Ajustes** › **Privacidad** › **Borrar todo en este dispositivo** elimina todo lo que Diana ha guardado en este dispositivo: indicativo, ajustes, teselas sin conexión y tu elección sobre estadísticas. Diana vuelve entonces a la pantalla de bienvenida.

## Tus derechos y contacto

Como Diana guarda tus ajustes personales solo en tu propio dispositivo, consultarlos, corregirlos o borrarlos es tan sencillo como abrir Ajustes. Para cualquier cuestión sobre las estadísticas anónimas, o una reclamación, la página de privacidad de la app indica la dirección de contacto. En España puedes dirigirte también a la Agencia Española de Protección de Datos (aepd.es).
