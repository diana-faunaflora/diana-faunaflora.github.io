T = {
'map/map-screen': {'title': 'O ecrã do mapa', 'desc': 'O ecrã principal do Diana: os botões em cima e a barra em baixo.', 'body': '''
O mapa é o ecrã principal do Diana. Tudo o resto começa aqui.

{{img:phone-map|O mapa do Diana à volta de Antuérpia, com áreas verdes, um spot e linhas}}

## A barra em baixo

Da esquerda para a direita: **Mapa**, **Spots**, **Spot**, **Agenda**, **Info de campo**, **Regras** e **Definições**. Toca num para abrir esse ecrã.

:::tip[Voltar à tua posição]
Toca em **Mapa** na barra de baixo a qualquer momento: o mapa centra-se de novo onde estás, e o zoom fica como está. O Diana faz uma nova medição GPS se a última tiver mais de dois minutos ou for menos precisa do que 30 m. Sem GPS, centra-se no teu locator das Definições, e avisa disso.
:::

## Os botões em cima

| Botão | O que faz |
|---|---|
| **⌕** | Pesquisar por nome ou número de referência. Vê {{link:map/search}}. |
| **◐** | Estilo do mapa: Liberty, Positron, Bright ou Dark. |
| **≡** | Camadas e idioma. Vê {{link:map/layers-and-styles}}. |

No canto superior esquerdo, uma linha diz quantas referências estão carregadas, por exemplo *"947 referências WWFF · 1 sem limite"*.

## Navegar

- **Arrasta** com um dedo para mover o mapa.
- **Afasta ou junta** dois dedos para aproximar ou afastar, ou usa **+** e **−** à direita.
- **Toca** numa área, num ponto ou num spot para abrir o seu painel. Vê {{link:map/area-panel}}.

## O que estou a ver?

As cores, pontos e linhas são explicados em {{link:map/reading-the-map}}. Porque é que uma referência é uma área e outra só um ponto é explicado em {{link:map/points-and-areas}}.
'''},
'map/points-and-areas': {'title': 'Pontos e áreas', 'desc': 'Porque é que uma referência é uma área verde e outra um ponto azul, e como mudar isso.', 'body': '''
No mapa, uma referência WWFF aparece de uma de três formas. Qual delas depende do que o Diana sabe sobre ela, e do país que escolheste.

| O que vês | O que significa | O Diana consegue dizer se estás dentro? |
|---|---|---|
| **Área verde** | Uma referência com o seu limite real, no país que escolheste. | Sim |
| **Anel tracejado com um ponto laranja** | Uma referência do teu país sem limite. Apenas um local aproximado. | Não |
| **Ponto azul** | Uma referência noutro país. Quando estão juntas, formam um círculo com um número. | Não |

## Porquê uma área?

Uma área precisa de um ficheiro de limites. Hoje o Diana tem esses ficheiros para **cinco países**: Bélgica (ONFF), Países Baixos (PAFF), Alemanha (DLFF), Dinamarca (OZFF) e Portugal (CTFF), e estão sempre a juntar-se mais. São os coordenadores nacionais WWFF que os fornecem.

O Diana carrega os limites de **um país de cada vez**: o que escolheste nas Definições. Assim o mapa mantém-se rápido no telemóvel.

## Porquê um ponto?

- A referência fica num país para o qual o Diana **não tem ficheiro de limites**. Nesse caso o Diana só conhece a posição do diretório WWFF.
- Ou o país **tem** limites no Diana, mas **não é o país que escolheste**. Então também aparece como ponto, até carregares esse país.

## Porquê um anel tracejado?

Dentro de um país com limites, algumas referências não têm limite no ficheiro, por exemplo áreas ultramarinas dos Países Baixos. Aparecem como um anel tracejado no local aproximado.

## Os detalhes tens sempre

Seja o que for que vês, **toca-lhe**: abre-se um painel com tudo o que o Diana sabe. Para um ponto azul isso é a referência, o país e o nome, o locator e as zonas, a direção e a distância a partir de ti, o número de QSO ou **ATNO** quando nunca foi ativada, e uma ligação para mais informação. Vê {{link:map/area-panel}}.

## Quando e como mudar

Quando vais para outro país, ou queres ver o limite real de uma referência que agora é um ponto:

**A partir do painel (mais rápido)**

1. Toca no ponto azul.
2. Se o Diana tiver os limites desse país, o painel diz isso e mostra um botão **Mostrar [país] em detalhe**.
3. Toca nele. O Diana carrega esse país e volta a abrir a mesma referência, agora com o seu limite.

**A partir das Definições**

1. Toca em **Definições** no canto inferior direito.
2. Em **O seu país**, escolhe o país. Os países marcados **Com fronteiras** recebem as suas áreas; **Apenas pontos** fica em pontos.
3. A mudança é imediata. Debaixo do menu, o Diana diz o que carregou, por exemplo *"PAFF, 281 áreas com fronteiras carregadas"*.

O teu filtro de spots (o teu país ou Mundial) não muda quando escolhes outro país. Mais em {{link:settings/your-country}}.

:::note[Uma reserva nova primeiro como ponto]
Que referências existem vem do diretório WWFF, todas as noites. Os limites vêm de um ficheiro que a equipa do Diana publica. Por isso uma reserva novinha pode aparecer primeiro como ponto e receber o contorno mais tarde.
:::
'''},
'map/reading-the-map': {'title': 'Ler o mapa', 'desc': 'O que significa cada cor, ponto e linha no mapa.', 'body': '''
Tudo no mapa tem um significado. Esta é a legenda.

{{img:map-legend|Mapa à volta de Antuérpia e Roosendaal com áreas verdes, aglomerados azuis, uma linha verde pontilhada e uma linha laranja tracejada}}

## Áreas e referências

| O que vês | Significado |
|---|---|
| Área verde com um número | Uma referência com o seu limite real, no teu país. O número é a referência, por exemplo `ONFF-0602`. |
| Contorno laranja | A área em que acabaste de tocar. |
| Anel tracejado com um ponto laranja | Uma referência do teu país sem limite: um local aproximado. |
| Ponto azul | Uma referência noutro país. |
| Círculo azul com um número | Vários pontos azuis juntos. Toca para aproximar; separa-se. |
| Linha cinzenta | Uma fronteira de país no mapa de base. |

A partir do nível de zoom 11, cada ponto recebe a sua referência como etiqueta.

## Spots e anúncios

| O que vês | Significado |
|---|---|
| Ícone de antena verde a pulsar | Uma estação no ar agora, com indicativo, frequência e modo ao lado. |
| **Linha verde pontilhada** | De ti até uma estação que está no ar agora. |
| Spot esbatido | Um spot com mais de 30 minutos. |
| Ponto branco com anel laranja | Uma ativação anunciada da agenda. |
| **Linha laranja tracejada** | De ti até uma ativação anunciada, com indicativo e hora. |
| A tua posição | Um marcador. Quando a tua posição é menos precisa do que cerca de 10 m, um anel tracejado mostra a margem. |

:::tip[Demasiadas linhas?]
Desliga-as em **≡** › **Linhas até aos spots**. O Diana lembra-se da escolha. **⤢ Ver todos os spots** enquadra todos os spots e a tua própria posição de uma vez.
:::

Porque é que algumas referências são áreas e outras pontos: {{link:map/points-and-areas}}.
'''},
'map/area-panel': {'title': 'Detalhes da área', 'desc': 'Toca numa área ou ponto: o painel com tudo o que o Diana sabe, e fazer spot a partir daí.', 'body': '''
Toca numa área, num ponto ou num spot no mapa. Sobe um painel de baixo com tudo o que o Diana sabe sobre essa referência. O Diana mostra apenas o que sabe mesmo: nunca uma caixa vazia.

{{img:phone-area-panel|Painel de ONFF-0685 Hobokense Polder com área, gestor, designação, categoria IUCN e locator}}

## O que está no painel

Para uma **área com limite**:

- Referência, região e nome.
- O que o ficheiro da área traz: **área** em hectares, **gerido por**, **designação**, **categoria IUCN**, **designada desde**. Nem todas as reservas têm tudo isto; é uma lacuna nos dados de origem, não algo que o Diana esconda.
- O **número de QSO** e a **última ativação**, do diretório WWFF.
- O **locator**, a **zona CQ**, a **zona ITU** e a **região ITU**.
- **Mais info**: o site da reserva, quando o diretório WWFF tem um. Abre no teu navegador, por isso o Diana e o mapa ficam onde estavam.

Para uma **referência sem limite** (anel tracejado): o mesmo painel sem os números da área, e uma nota a dizer que o Diana não consegue saber se estás dentro.

Para um **ponto azul** noutro país: referência, país e nome, locator e zonas, **A partir de ti** (direção e distância), o número de QSO ou **ATNO** a vermelho quando nunca foi ativada, e Mais info.

## Fazer spot ou anunciar a partir do painel

Em baixo, em cada painel, há dois botões:

- **Faz o teu spot aqui** abre o formulário de spot com a referência já preenchida. Vê {{link:spots/spot-yourself}}.
- **Anunciar uma ativação** abre o formulário da agenda com a referência preenchida. Vê {{link:spots/announce}}.

## Fechar o painel

Desliza o painel **para baixo**, ou toca em **×**. O mapa fica onde está. No telemóvel, só se vê um painel de baixo de cada vez.
'''},
'map/overlapping-areas': {'title': 'Áreas sobrepostas', 'desc': 'Quando as referências ficam umas sobre as outras, e como alternar entre elas.', 'body': '''
Às vezes as referências sobrepõem-se: uma reserva pequena fica muitas vezes dentro de uma área natural maior. Nesse pedaço de terreno, estás em todas ao mesmo tempo.

## Como o Diana mostra isso

O Diana desenha sempre a área **mais pequena** por cima, para que lhe possas tocar. Um toque abre a área mais pequena debaixo do teu dedo: toca dentro da reserva para a reserva, e no terreno à volta para a área maior.

## Mudar para a outra área

1. Toca no mapa dentro da reserva. Abre-se o painel da área **mais pequena**.
2. Desce no painel até **"Este ponto também está dentro destas referências"**. As outras áreas estão aí como botões, com nome e tamanho.
3. Toca num botão. O painel mostra agora essa área, com o seu próprio limite a laranja.
4. Voltar? Esse painel tem um botão para a área de onde vieste.

## Com a tua posição GPS

Se estiveres em várias áreas ao mesmo tempo, o cartão em baixo no mapa diz isso, por exemplo *"Estás dentro de 2 referências"*, com a distância ao limite mais próximo. O Diana abre então o painel da área mais pequena, com as outras como botões.

:::tip[O que isto significa para a tua ativação]
Se estás em todas essas áreas, as regras WWFF permitem ativá-las em conjunto. Lê as regras no Diana em **Regras**, ou o texto oficial em wwff.co. Vê {{link:rules/wwff-rules}}.
:::

:::caution[Não para referências sem limite]
Um anel tracejado é só um local aproximado. Aí o Diana não consegue saber se estás dentro, e por isso também não pode mostrar sobreposição.
:::
'''},
'map/am-i-inside': {'title': 'Estou dentro da área?', 'desc': 'Como o Diana te diz se estás dentro, e como ler a precisão.', 'body': '''
Um cartão em baixo no mapa responde à pergunta que todo o ativador faz: **estou dentro da reserva?**

## O que o cartão diz

- **Dentro de uma área**: qual, e a distância ao limite mais próximo.
- **Dentro de várias ao mesmo tempo** (quando as áreas se sobrepõem): quantas, e abre-se o painel da mais pequena. Vê {{link:map/overlapping-areas}}.
- **Fora**: a área mais próxima e a que distância fica.

Cada resposta termina com a qualidade da tua posição, por exemplo *"posição ±6 m"*.

:::note[Áreas feitas de várias parcelas]
Algumas referências são compostas por parcelas separadas. O painel diz então quantas. Toda a tua estação tem de estar dentro de uma delas.
:::

## Porque demora alguns segundos

Um telemóvel que acabou de acordar o GPS responde primeiro com base no wifi e nas antenas de rede, e essa posição pode estar a centenas de metros. Por isso o Diana continua à escuta enquanto a precisão melhora, e mostra o que tem até ali: *"A afinar… ±380 m"*. Responde assim que a posição for suficientemente boa, ou ao fim de doze segundos com a melhor que conseguiu. Se ainda for grosseira, a resposta diz isso.

## Ler a precisão

| Precisão | O que normalmente significa |
|---|---|
| ±10 m ou melhor | Satélites. Fiável, também perto de um limite. |
| ±20 a 50 m | Razoável. Cuidado perto de um limite. |
| ±100 m ou pior | Wifi ou antenas de rede, muitas vezes dentro de casa. Não chega para ter certeza. |

Quando a margem é maior do que cerca de 10 m, é desenhado um **anel tracejado** à volta do teu marcador com exatamente esse raio. Um anel apertado significa satélites; um anel que cobre o quarteirão inteiro significa que a resposta veio do wifi.

:::tip[Obter uma posição melhor]
Vai lá para fora, com céu aberto por cima, e espera uns segundos. Continua grosseira, acima de cerca de 75 m? Então talvez o site só possa usar uma localização aproximada. Aparece então um aviso a sugerir que verifiques a definição de localização: vê {{link:help/location-problems}}.
:::

## Duas armadilhas que o Diana vigia

- **Dentro de casa**, uma posição por wifi chega muitas vezes num segundo a dizer ±20 m. É a precisão que a base de dados de wifi julga ter, não a precisão real. O Diana responde, mas continua à escuta o resto dos doze segundos e corrige a resposta se for preciso.
- **Telemóveis que prometem mais do que conseguem.** O Diana compara as leituras dos últimos 45 segundos. Uma leitura isolada e disparatada é ignorada. Se as leituras se contradizem, a resposta diz *"leituras contraditórias"*. Andar não conta como dispersão.

:::caution
O Diana só consegue responder a isto para áreas **com** limite. Para um anel tracejado ou um ponto azul não consegue. Vê {{link:map/points-and-areas}}.
:::
'''},
'map/layers-and-styles': {'title': 'Camadas e estilo do mapa', 'desc': 'Ligar e desligar partes do mapa, e escolher um estilo de mapa.', 'body': '''
## Camadas (≡)

Toca em **≡** no canto superior direito do mapa. Podes ligar e desligar o seguinte:

| Camada | O que mostra |
|---|---|
| **Zonas de referência** | As áreas verdes do teu país. |
| **Números de referência** | As etiquetas como `ONFF-0602`. |
| **Sem limite (ponto)** | Os anéis tracejados das referências sem limite. |
| **Spots no mapa** | Spots em direto e anúncios. Vêm do WWFF Spotline e atualizam a cada 30 segundos. |
| **Linhas até aos spots** | As linhas verdes pontilhadas e laranja tracejadas a partir de ti. |
| **Outras zonas WWFF** | Os pontos azuis do resto do mundo. |

No mesmo menu estão **⤢ Ver todos os spots** e os botões de idioma. O Diana lembra-se das tuas escolhas.

## Estilo do mapa (◐)

Toca em **◐** para outro mapa de base:

- **Liberty**: o padrão, com cores de terreno.
- **Positron**: muito claro e calmo, bom com sol forte.
- **Bright**: mais cor e mais detalhe.
- **Dark**: escuro, descansa os olhos à noite.

:::tip
No terreno, com sol forte, o **Positron** é muitas vezes o mais fácil de ler.
:::
'''},
'map/search': {'title': 'Pesquisar', 'desc': 'Encontrar uma referência pelo nome ou número, em qualquer parte do mundo.', 'body': '''
Toca em **⌕** no topo do mapa e escreve.

- **Um nome**, por exemplo `Kalmthoutse Heide`.
- **Uma referência completa**, por exemplo `ONFF-0012` ou `CTFF-0012`.
- **Só um número**, por exemplo `0012`. Nesse caso o Diana procura apenas no teu próprio país.

Todas as referências WWFF do mundo podem ser encontradas. Os resultados do país carregado aparecem primeiro. Toca num resultado: o mapa aproxima-se dele e abre o seu painel.

:::tip
A pesquisa também funciona offline: a lista de referências está no teu dispositivo.
:::
'''},
}
