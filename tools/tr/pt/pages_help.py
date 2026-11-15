T = {
'help/location-problems': {'title': 'Problemas de localização', 'desc': 'Sem posição, ou uma posição que continua grosseira: o que verificar, por dispositivo.', 'body': '''
Diana pede sempre a posição mais exata que o teu dispositivo consegue dar. Se um site recebe a posição exata ou uma propositadamente desfocada é uma definição do teu telemóvel ou navegador, não de Diana.

## Primeiro: tenta lá fora

Dentro de casa, o wifi sozinho dá muitas vezes cerca de ±100 m. Vai lá para fora, com céu aberto por cima, espera dez segundos e toca em **Mapa** na barra de baixo. Muitas vezes isso chega.

## Continua grosseira ou sem posição? Verifica a definição

**Android com Chrome**

1. Abre a aplicação **Definições** do telemóvel.
2. Vai a **Apps** › **Chrome** › **Autorizações** › **Localização**.
3. Escolhe **Permitir apenas durante a utilização da app** e ativa **Usar localização exata**.
4. Verifica também o próprio site: no Chrome, toca no ícone à esquerda da barra de endereço › **Autorizações** › **Localização**: permitida.

**iPhone ou iPad com Safari**

1. Abre a aplicação **Definições**.
2. Vai a **Privacidade e segurança** › **Serviços de localização** › **Sites do Safari**.
3. Escolhe **Durante a utilização da app** e ativa **Localização exata**.

**iPhone ou iPad com outro navegador** (por exemplo Chrome)

1. Abre a aplicação **Definições**.
2. Vai a **Privacidade e segurança** › **Serviços de localização** › o teu navegador.
3. Escolhe **Durante a utilização da app** e ativa **Localização exata**.

**Computador**

Clica no ícone do cadeado ao lado da barra de endereço e permite **Localização** para este site. Um portátil obtém a posição do wifi e raramente é melhor do que cerca de ±50 m.

## "A localização está bloqueada para este site"

Tu (ou alguém) disseste que não anteriormente. Diana não pode voltar a perguntar: só tu podes permitir, nas definições do navegador ou do telemóvel acima. Depois recarrega Diana.

## Sem localização

Diana também funciona sem localização. Preenche o teu locator em **Definições** › **A tua estação**. As distâncias e linhas partem então do centro do quadrado do teu locator. Só o *estou dentro da área* precisa mesmo de uma posição exata.

Vê também {{link:map/am-i-inside}}.
'''},
'help/scripts-blocked': {'title': 'Parado no ecrã de arranque', 'desc': 'Bloqueadores de scripts e navegadores restritos: o que Diana precisa, e nada mais.', 'body': '''
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
'''},
'help/updates': {'title': 'Atualizações', 'desc': 'Como Diana se atualiza sozinho, e o que fazer se uma versão nova não aparecer.', 'body': '''
Diana atualiza-se sozinho. Nunca tens de transferir nada.

## Como funciona

- **Os dados** (referências, número de QSO, limites) são atualizados todas as noites. Diana vai buscá-los frescos em cada arranque, e usa a cópia do teu telemóvel quando a rede é fraca.
- **A própria aplicação**: quando abres Diana com rede, verifica se há uma versão nova. Uma versão nova só é anunciada quando existe mesmo.

## Uma versão nova não aparece?

1. Garante que tens rede.
2. Abre as **Definições** e toca em **Procurar atualizações** no fundo.
3. Compara a linha da versão com a das **Novidades**. Vê {{link:settings/version-and-updates}}.
4. Continua a versão antiga? Fecha Diana por completo (desliza-a para fora das aplicações recentes) e volta a abri-la.

:::note
As versões da aplicação estão nas **Novidades**, a mais recente no topo, em neerlandês e inglês.
:::
'''},
'help/data-and-limits': {'title': 'Os teus dados e os limites', 'desc': 'O que fica no teu dispositivo, porque nada sincroniza, e o que Diana não consegue fazer.', 'body': '''
## Tudo fica num dispositivo, num navegador

Os teus indicativos, locator, país, palavras rápidas, idioma, escolha sobre estatísticas e os PIN dos teus anúncios ficam no armazenamento local desse único navegador. Nada sincroniza.

- Usas Diana no telemóvel e no portátil? Configura-o nos dois. Não há conta para os ligar.
- **Apagar os dados do navegador** (histórico, cookies e dados de sites), usar uma **janela privada** ou **remover a aplicação instalada** apaga estas definições. Diana recomeça então no ecrã de boas-vindas.

:::caution[Os PIN dos teus anúncios]
Estão nesse mesmo armazenamento. Apaga o navegador e desaparecem. Aponta os PIN importantes também noutro sítio.
:::

## O que Diana não consegue fazer

- **Os dados em direto dependem de outros.** Os spots e a agenda vêm do WWFF Spotline. Se estiver em baixo, o ecrã Spots diz isso. As condições de propagação vêm da NOAA; o separador diz que idade têm.
- **Só há limites onde foi fornecido um ficheiro**: hoje cinco países. Noutros sítios as referências são pontos, e Diana não consegue dizer se estás dentro. Vê {{link:map/points-and-areas}}.
- **Nem todas as reservas têm detalhes completos.** Muitas têm só um nome e uma referência. É uma lacuna nos dados de origem.
- **Diana não faz log** nem carrega logs. Isso fica com o teu próprio programa de log e com o WWFF.

## Utilização dos dados

Os limites e os números de ativações vêm dos programas WWFF, da WDPA, de fontes governamentais e do WWFF Spotline, e continuam a ser dados dos seus proprietários. Vê {{link:about/data-sources}}.
'''},
'help/faq': {'title': 'Perguntas frequentes', 'desc': 'Respostas curtas às perguntas que surgem mais vezes.', 'body': '''
## Diana custa alguma coisa?

Não. Diana é gratuita, sem publicidade e sem conta.

## Diana é uma aplicação oficial do WWFF?

Não. Diana é um projeto de voluntários que apoia o hobby WWFF. Usa os serviços públicos do WWFF, como o Spotline e o diretório.

## Diana envia a minha posição para algum lado?

Não. A tua posição é usada apenas no teu próprio ecrã. Um spot envia o teu indicativo, frequência, modo, referência e observação, nunca a tua posição. Vê {{link:start/privacy}}.

## Diana funciona sem rede?

Sim, com os últimos dados carregados: o mapa que já viste, as referências, a Localização da Info de campo e o plano de bandas. Os spots em direto e o envio de um spot precisam de rede.

## Porque é que a minha referência é um ponto e não uma área?

Porque Diana não tem limite para ela, ou porque fica noutro país que não o que carregaste. Vê {{link:map/points-and-areas}}.

## Posso fazer log em Diana?

Não. Diana ajuda antes e durante a ativação. O teu log fica no teu programa de log. Em **Regras**, Diana mostra o nome de ficheiro certo.

## As minhas definições desapareceram. O que aconteceu?

Os dados do navegador foram apagados, a aplicação foi removida, ou usaste uma janela privada. Vê {{link:help/data-and-limits}}.

## O meu programa nacional também pode ter limites?

Sim. O coordenador nacional envia o ficheiro das áreas (KMZ) à equipa de Diana. Mais em {{link:about/about-diana}}.

## Encontrei um erro. Onde o comunico?

Os contactos estão na página de privacidade da aplicação (**Definições** › **Privacidade**). Indica a tua linha da versão: {{link:settings/version-and-updates}}.
'''},
}
