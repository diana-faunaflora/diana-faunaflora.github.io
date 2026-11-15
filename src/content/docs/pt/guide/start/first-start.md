---
title: "O ecrã de arranque"
description: "O que vês enquanto Diana arranca, e o que fazer se ficar parado no ecrã de arranque."
sidebar:
  order: 5
---

Sempre que Diana arranca, vês primeiro o ecrã de arranque: um desenho de uma ativação, um sinal de rádio a percorrê-lo, uma linha de progresso e o número da versão. Entretanto Diana lê os dados das referências e prepara o mapa.

O ecrã de arranque desaparece sozinho assim que o mapa está desenhado, e no máximo ao fim de nove segundos.

## Diana precisa de scripts

Diana é uma aplicação web: tudo o que faz corre como JavaScript no teu navegador. Se o navegador ou uma extensão bloquear scripts, nada consegue arrancar e ficas no ecrã de arranque.

Passado algum tempo aparece no ecrã de arranque uma caixa a dizer exatamente isso. Então:

1. Permite scripts apenas para **diana-onff.github.io**. Não para `github.io` nem para `github.com`: Diana não precisa de nenhum deles.
2. **Recarrega a página.** Num computador carrega em **F5** ou **Ctrl+R** (Mac: **Cmd+R**). No telemóvel, puxa a página para baixo ou toca no botão de recarregar do navegador.
3. Continua parado? Talvez outra extensão também esteja a bloquear, como um bloqueador de anúncios. Desativa-as uma a uma para este site.

:::caution[Recarregar é essencial]
A maioria dos bloqueadores só aplica uma regra nova a uma página carregada de novo. Sem recarregar, o bloqueio antigo mantém-se, mesmo depois de clicares em "Confiar".
:::

Todos os scripts vêm do próprio endereço de Diana. Nada é carregado de outros sites, exceto o script das estatísticas, e só se disseres que sim. Detalhes em [Parado no ecrã de arranque](/pt/guide/help/scripts-blocked/).

## A primeiríssima vez

Num dispositivo que nunca abriu Diana, seguem-se ao ecrã de arranque duas coisas curtas: o [Ecrã de boas-vindas](/pt/guide/start/welcome-screen/) e [O assistente inicial](/pt/guide/start/setup-wizard/).
