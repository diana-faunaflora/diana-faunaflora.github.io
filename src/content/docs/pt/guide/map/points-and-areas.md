---
title: "Pontos e áreas"
description: "Porque é que uma referência é uma área verde e outra um ponto azul, e como mudar isso."
sidebar:
  order: 2
---

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

Seja o que for que vês, **toca-lhe**: abre-se um painel com tudo o que o Diana sabe. Para um ponto azul isso é a referência, o país e o nome, o locator e as zonas, a direção e a distância a partir de ti, o número de QSO ou **ATNO** quando nunca foi ativada, e uma ligação para mais informação. Vê [Detalhes da área](/pt/guide/map/area-panel/).

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

O teu filtro de spots (o teu país ou Mundial) não muda quando escolhes outro país. Mais em [O teu país](/pt/guide/settings/your-country/).

:::note[Uma reserva nova primeiro como ponto]
Que referências existem vem do diretório WWFF, todas as noites. Os limites vêm de um ficheiro que a equipa do Diana publica. Por isso uma reserva novinha pode aparecer primeiro como ponto e receber o contorno mais tarde.
:::
