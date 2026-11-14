---
title: "Privacidade"
description: "O que o Diana sabe, o que não sabe, e porquê."
sidebar:
  order: 9
---

O Diana foi feito para que os teus dados fiquem contigo. Esta página resume a página de privacidade da aplicação (**Definições** › **Privacidade** › **Abrir a página de privacidade**).

## Em resumo

- O teu indicativo, locator e definições ficam no navegador deste dispositivo. Nada é enviado para lado nenhum.
- A tua posição GPS é usada apenas no ecrã à tua frente. Nunca é enviada para lado nenhum.
- Fazer o teu spot envia o teu indicativo, frequência, modo e referência para o WWFF Spotline, nunca a tua posição.
- Com a tua permissão em separado, o Diana pode contar uma visita anónima. Nada é contado sem o teu sim, e podes mudar de ideias a qualquer momento nas Definições.
- O Diana não usa cookies de publicidade nem cria um perfil teu.

## O que fica neste dispositivo

O teu indicativo, indicativo portátil, locator, e definições como bandas, a distância da Info de campo, palavras rápidas e idioma, juntamente com a tua escolha sobre estatísticas e se já viste o ecrã de boas-vindas. O Diana guarda também uma cópia offline dos mosaicos do mapa e da própria aplicação, para continuar a funcionar sem rede. Isso é a cache normal do navegador, não dados pessoais.

## Serviços com que o Diana fala

| Serviço | Para quê |
|---|---|
| WWFF Spotline (`spots.wwff.co`) | Spots em direto e a agenda. Recebe o teu indicativo, frequência, modo, referência e observação quando fazes o teu spot. Nunca a tua posição. |
| OpenFreeMap (`tiles.openfreemap.org`) | Os mosaicos do mapa, feitos com dados do OpenStreetMap. Sem cookies. |
| O relé do Diana (um Cloudflare Worker) | Passa o teu spot ou anúncio ao Spotline. Conta pedidos por endereço IP com hash para evitar abusos, nunca regista o teu indicativo, posição ou observação. |
| Umami (`cloud.umami.is`) | Conta uma visita anónima, só com a tua permissão. Sem cookies, sem dados pessoais. |

## O que um spot próprio envia

Exatamente isto, e mais nada: o indicativo do ativador, o indicativo do spotter, a frequência, o modo, a referência e uma observação opcional que tu próprio escreveste. Nunca a tua posição.

## Apagar tudo

**Definições** › **Privacidade** › **Limpar tudo neste dispositivo** remove tudo o que o Diana guardou neste dispositivo: o teu indicativo, definições, mosaicos offline do mapa e a tua escolha sobre estatísticas. O Diana recomeça então no ecrã de boas-vindas.

## Os teus direitos e contacto

Como o Diana guarda as tuas definições pessoais apenas no teu próprio dispositivo, consultá-las, corrigi-las ou apagá-las é tão simples como abrir as Definições. Para qualquer questão sobre as estatísticas anónimas, ou uma reclamação, a página de privacidade da aplicação indica o endereço de contacto.
