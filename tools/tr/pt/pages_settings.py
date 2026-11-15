T = {
'settings/overview': {'title': 'Definições', 'desc': 'Como abrir as Definições, e para que serve cada parte.', 'body': '''
Tudo o que configuraste no assistente, e um pouco mais, está em **Definições**.

{{img:phone-settings|O ecrã Definições com A tua estação e O seu país}}

## Abrir as Definições

1. Toca em **Definições** na barra de baixo (a roda dentada, totalmente à direita).
2. Desce até à parte que queres mudar.
3. Muda-a. Tudo é guardado de imediato: não há botão de guardar. Vês por instantes *"Guardado neste dispositivo"*.

## O que contém

| Parte | O que defines | Página |
|---|---|---|
| **A tua estação** | Indicativo, indicativo portátil, locator | {{link:settings/your-station}} |
| **O seu país** | Que país é carregado em detalhe, e o filtro de spots | {{link:settings/your-country}} |
| **Palavras rápidas para um spot** | Cinco palavras para juntar com um toque | {{link:settings/quick-words}} |
| **Info de campo** | Até onde o separador Áreas olha à tua volta | {{link:settings/field-info-distance}} |
| **Lista de bandas ao anunciar** | Todas as bandas ou apenas HF | {{link:settings/band-list}} |
| **Idioma** | Um de oito, ou seguir o navegador | {{link:settings/language}} |
| **Privacidade** | Página de privacidade, estatísticas, limpar tudo | {{link:settings/privacy-settings}} |
| **Instalar como aplicação** | Instalar neste dispositivo | {{link:start/install-android}} |
| No fundo | Versão, atualizações, novidades, repetir o assistente | {{link:settings/version-and-updates}} |

:::caution[Só neste dispositivo]
Tudo o que preenches aqui fica no navegador deste dispositivo. Usas Diana também noutro dispositivo? Preenche lá outra vez. Diana não tem conta para os ligar. Vê {{link:help/data-and-limits}}.
:::
'''},
'settings/your-station': {'title': 'A tua estação', 'desc': 'Indicativo, indicativo portátil e locator, e como ler a linha da posição.', 'body': '''
**Definições** › **A tua estação**. Quem és e mais ou menos onde estás.

| Campo | O que preencher | O que Diana faz com ele |
|---|---|---|
| **Indicativo** | O teu indicativo normal, por exemplo `CT1ABC`. | Usado como spotter, e decide que país Diana propõe. |
| **Indicativo portátil** | O que usas no terreno, por exemplo `CT1ABC/P`. | Preenchido como ativador quando fazes o teu spot ou anuncias. |
| **Locator Maidenhead** | Seis caracteres, por exemplo `IN51RQ`. | O teu ponto de partida enquanto não houver GPS: para o mapa, as distâncias e as linhas até aos spots. |

*"Locator inválido (ex.: JO21EE)"* significa um erro de escrita: duas letras, dois algarismos, duas letras.

## Obter o locator do GPS

1. Põe-te no sítio para o qual queres o locator, de preferência ao ar livre.
2. Toca em **Obter do GPS**.
3. Diana preenche o locator a partir da tua posição atual.

## A linha da posição

Debaixo do locator, uma linha diz quão boa foi a tua última posição, por exemplo *"Última posição: ±8 m · há 2 min"*.

| Lês | O que significa | O que fazer |
|---|---|---|
| ±10 m ou melhor | Satélites. Está bem. | Nada. |
| cerca de ±50 a 100 m | Normalmente wifi, dentro de casa. | Tenta lá fora. |
| Demasiado grosseira para dizer se estás dentro de uma área | Não chega para dentro ou fora. | Vai para fora, com céu aberto. |
| Continua grosseira mesmo lá fora | Talvez o site só possa usar uma localização aproximada. | Verifica a definição de localização do telemóvel: {{link:help/location-problems}}. |
| *"Ainda não há posição GPS neste dispositivo."* | Localização não permitida, ou ainda não pedida. | Permite a localização, ou confia no teu locator. |

:::note
Não há nenhuma definição para o sítio onde o mapa abre. Abre sempre onde estás, senão no teu locator, senão no país do teu indicativo.
:::
'''},
'settings/your-country': {'title': 'O teu país', 'desc': 'Que país Diana carrega em detalhe, e em que difere do filtro de spots.', 'body': '''
**Definições** › **O seu país**. Uma escolha para tudo: que país Diana carrega com os seus limites reais, e que spots e entradas da agenda o botão do teu país mostra. Dos outros países, Diana mostra sempre apenas pontos.

## As duas partes

| Parte | O que faz |
|---|---|
| **País** | O país carregado em detalhe. Na lista diz **Com fronteiras** ou **Apenas pontos**. |
| **Mostrar** | O teu país ou **Mundial**. O filtro do ecrã Spots, o mesmo interruptor que nesse ecrã. |

Debaixo da lista, Diana diz o que tem para esse país, por exemplo *"CTFF, … áreas com fronteiras carregadas"*, ou que para a OKFF não há fronteiras, apenas pontos no mapa.

## Quando mudar

- **Vais ao estrangeiro**: escolhe o país que vais visitar. Se Diana tiver os seus limites, as áreas aparecem lá por inteiro. Vê {{link:travel/abroad}}.
- **Interessa-te uma referência do outro lado da fronteira**: toca no seu ponto azul e usa **Mostrar [país] em detalhe**; isso faz o mesmo que mudar aqui.

## Passo a passo

1. Toca em **Definições** no canto inferior direito.
2. Abre a lista em **O seu país** e escolhe o país.
3. A mudança é imediata. Lê a linha debaixo da lista para ver o que foi carregado.
4. Queres os spots do mundo inteiro ou só desse país? Escolhe em **Mostrar**.

:::note
Escolher outro país nunca muda **Mostrar**. E ao contrário: mudar o filtro de spots não carrega outro país.
:::

Porque é que uma referência é uma área ou um ponto: {{link:map/points-and-areas}}.
'''},
'settings/quick-words': {'title': 'Palavras rápidas para um spot', 'desc': 'Cinco palavras que juntas à observação de um spot com um toque.', 'body': '''
**Definições** › **Palavras rápidas para um spot**. Cinco palavras que podes juntar à observação de um spot com um toque, para não teres de escrever no terreno.

## Configurar

1. Preenche até cinco caixas, cada uma com uma palavra ou uma expressão curta.
2. Uma caixa vazia simplesmente não dá botão.
3. Quando fazes o teu spot, aparecem como botões debaixo da observação. Vê {{link:spots/spot-yourself}}.

## Ideias

Preenche o que se adapta à tua estação: um modo, a tua potência, a antena, um estado curto. Mantém-nas curtas: uma observação tem no máximo 100 caracteres.

:::caution
Nada de agradecimentos nem de pedidos de banda: um spot vai para o DX cluster, onde isso é ruído.
:::
'''},
'settings/field-info-distance': {'title': 'Distância da Info de campo', 'desc': 'Até onde o separador Áreas olha à tua volta.', 'body': '''
**Definições** › **Info de campo**. Até onde o separador **Áreas** da Info de campo olha à volta da tua posição: **10, 25, 50 ou 100 km**.

| Escolhe | Quando |
|---|---|
| **10 km** | Muitas áreas juntas, como na Flandres. Uma lista curta e clara. |
| **25 km** | Um bom meio-termo para a maioria dos sítios. |
| **50 km** | Menos áreas à volta, ou estás disposto a conduzir. |
| **100 km** | O campo, ou o estrangeiro com poucas referências. |

A lista mostra no máximo cem linhas de cada vez; **Mostrar mais** dá o resto. Vê {{link:field-info/areas-nearby}}.
'''},
'settings/band-list': {'title': 'Lista de bandas ao anunciar', 'desc': 'Todas as bandas ou apenas HF na lista de bandas do formulário de anúncio.', 'body': '''
**Definições** › **Lista de bandas ao anunciar**. Que bandas a lista do ecrã de anúncio oferece.

| Escolha | Bandas |
|---|---|
| **Todas as bandas** | 160 m a 23 cm. |
| **Apenas HF** | 80, 40, 30, 20, 15 e 10 m. |

Quase todas as ativações acontecem nas bandas de HF. Com **Apenas HF**, a lista fica curta e fazes menos deslocamento no telemóvel. Também trabalhas VHF ou UHF? Escolhe **Todas as bandas**.

Vê {{link:spots/announce}}.
'''},
'settings/language': {'title': 'Idioma', 'desc': 'Escolher o idioma da aplicação.', 'body': '''
**Definições** › **Idioma**. Diana fala inglês, neerlandês, francês, alemão, dinamarquês, italiano, espanhol e português.

- Escolhe um dos oito, ou **Seguir o navegador** para usar o idioma do teu navegador.
- Sem escolha feita, Diana arranca em inglês.
- Também podes mudar o idioma em **≡** no mapa, ou no primeiro passo do assistente.

Tudo muda de imediato. Os nomes das áreas nunca são traduzidos: são nomes oficiais e entram no teu log exatamente como foram publicados.

:::note
As "Novidades" (as notas das versões) só existem em neerlandês e inglês.
:::
'''},
'settings/privacy-settings': {'title': 'Privacidade e estatísticas', 'desc': 'A página de privacidade, a tua escolha sobre estatísticas e limpar tudo.', 'body': '''
**Definições** › **Privacidade**. O que Diana guarda, o que envia, e a tua escolha sobre estatísticas anónimas.

## O que encontras aqui

- **Abrir a página de privacidade**: com que serviços Diana fala e porquê. Resumo em {{link:start/privacy}}.
- **Estatísticas anónimas**: **Sim, ajudo com gosto** ou **Não, prefiro que não**. Muda quando quiseres.
- **Limpar tudo neste dispositivo**: remove tudo o que Diana guardou aqui.

## Mudar a tua escolha sobre estatísticas

1. Toca em **Definições** › **Privacidade**.
2. Toca em **Sim, ajudo com gosto** ou **Não, prefiro que não**.
3. Vês *"Guardado."*. É tudo.

:::tip[Porque é que o sim ajuda]
As estatísticas são contadas com o Umami: sem cookies, sem perfil, nada que te identifique. Para os voluntários por trás de Diana é a única forma de saber que a aplicação é usada e que ecrãs importam. Diana funciona exatamente da mesma forma em ambos os casos.
:::

## Limpar tudo

1. Toca em **Limpar tudo neste dispositivo**.
2. Diana pede confirmação: isto remove o teu indicativo, definições, mosaicos offline do mapa e a tua escolha sobre estatísticas.
3. Confirma. Diana recomeça no ecrã de boas-vindas.

Usa isto quando passas o teu dispositivo a outra pessoa, ou queres começar de novo.
'''},
'settings/version-and-updates': {'title': 'Versão e atualizações', 'desc': 'Ler a linha da versão, procurar atualizações e repetir o assistente.', 'body': '''
Mesmo no fundo das **Definições**: que versão tens, quão frescos estão os dados, e se há alguma novidade.

## Ler a linha da versão

`v2.2.12 · 6757ec3 · 14/11/2026`

| Parte | Significado |
|---|---|
| `v2.2.12` | A versão da aplicação. |
| `6757ec3` | Um código para esta compilação exata da aplicação. |
| `14/11/2026` | A data dessa versão. |

O código só muda quando a própria aplicação muda, não quando a atualização noturna traz dados novos. A **linha dos dados** por baixo diz quão frescos estão os dados do mapa.

## Os botões

- **Procurar atualizações**: Diana vê se há uma versão nova pronta e carrega-a.
- **Novidades**: o que cada versão trouxe, a mais recente no topo.
- **Repetir o assistente inicial**: o assistente começa a partir das tuas definições atuais. No fim, volta a oferecer a visita.

:::tip[Alguém pergunta que versão tens?]
Lê em voz alta a linha da versão. É exatamente isso que é preciso para te ajudar.
:::

Mais sobre atualizações que parecem não chegar: {{link:help/updates}}.
'''},
}
