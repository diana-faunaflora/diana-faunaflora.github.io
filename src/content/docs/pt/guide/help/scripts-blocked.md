---
title: "Parado no ecrã de arranque"
description: "Bloqueadores de scripts e navegadores restritos: o que Diana precisa, e nada mais."
sidebar:
  order: 2
---

Diana é uma aplicação web: sem JavaScript nada corre. Se um bloqueador parar os scripts, Diana fica no ecrã de arranque. Passado algum tempo aparece aí uma caixa a dizer isso.

## Resolver

1. Permite scripts apenas para **diana-onff.github.io**. Não `github.io` nem `github.com`: Diana não precisa de nenhum deles.
2. **Recarrega a página**: **F5** ou **Ctrl+R** (Mac: **Cmd+R**). No telemóvel, puxa a página para baixo ou toca em recarregar. Sem recarregar, o bloqueio antigo mantém-se, mesmo depois de clicares em "Confiar".
3. Continua parado? Pode haver uma segunda extensão a bloquear (um bloqueador de anúncios, uma extensão de privacidade). Desativa-as uma a uma para este site.
4. Diana arranca mas o mapa fica vazio? Permite workers `blob:` para diana-onff.github.io (ver abaixo).

## O que Diana carrega

**Scripts**: todos do próprio diana-onff.github.io.

| Ficheiro | O que é |
|---|---|
| `vendor/maplibre-gl.js` | MapLibre, a biblioteca de mapas. Uma cópia no site de Diana, não de uma CDN. |
| `js/*.js` | O código de Diana. |
| `sw.js` | O service worker que mantém Diana a funcionar offline. |

Sem scripts inline e sem `eval`. Uma exceção, só com o teu consentimento: se disseste sim às estatísticas, o script do Umami de `cloud.umami.is`.

**Worker do mapa**: o MapLibre desenha o mapa num worker em segundo plano lançado a partir de um endereço `blob:`. Um bloqueador que recuse workers `blob:` deixa Diana arrancar mas deixa o mapa em branco.

**Dados**:

| Servidor | Para quê |
|---|---|
| `tiles.openfreemap.org` | Mosaicos do mapa e tipos de letra das etiquetas |
| `spots.wwff.co` | Spots em direto e agenda |
| `diana-spotline.diana-onff.workers.dev` | Só quando envias um spot ou anúncio |
| `raw.githubusercontent.com` | Meteorologia espacial para Condições |
| `cloud.umami.is` | Só se disseste sim às estatísticas |

A tua posição nunca é enviada para lado nenhum.
