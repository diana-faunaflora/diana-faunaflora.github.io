---
title: "Estou dentro da área?"
description: "Como Diana te diz se estás dentro, e como ler a precisão."
sidebar:
  order: 6
---

Um cartão em baixo no mapa responde à pergunta que todo o ativador faz: **estou dentro da reserva?**

## O que o cartão diz

- **Dentro de uma área**: qual, e a distância ao limite mais próximo.
- **Dentro de várias ao mesmo tempo** (quando as áreas se sobrepõem): quantas, e abre-se o painel da mais pequena. Vê [Áreas sobrepostas](/pt/guide/map/overlapping-areas/).
- **Fora**: a área mais próxima e a que distância fica.

Cada resposta termina com a qualidade da tua posição, por exemplo *"posição ±6 m"*.

:::note[Áreas feitas de várias parcelas]
Algumas referências são compostas por parcelas separadas. O painel diz então quantas. Toda a tua estação tem de estar dentro de uma delas.
:::

## Porque demora alguns segundos

Um telemóvel que acabou de acordar o GPS responde primeiro com base no wifi e nas antenas de rede, e essa posição pode estar a centenas de metros. Por isso Diana continua à escuta enquanto a precisão melhora, e mostra o que tem até ali: *"A afinar… ±380 m"*. Responde assim que a posição for suficientemente boa, ou ao fim de doze segundos com a melhor que conseguiu. Se ainda for grosseira, a resposta diz isso.

## Ler a precisão

| Precisão | O que normalmente significa |
|---|---|
| ±10 m ou melhor | Satélites. Fiável, também perto de um limite. |
| ±20 a 50 m | Razoável. Cuidado perto de um limite. |
| ±100 m ou pior | Wifi ou antenas de rede, muitas vezes dentro de casa. Não chega para ter certeza. |

Quando a margem é maior do que cerca de 10 m, é desenhado um **anel tracejado** à volta do teu marcador com exatamente esse raio. Um anel apertado significa satélites; um anel que cobre o quarteirão inteiro significa que a resposta veio do wifi.

:::tip[Obter uma posição melhor]
Vai lá para fora, com céu aberto por cima, e espera uns segundos. Continua grosseira, acima de cerca de 75 m? Então talvez o site só possa usar uma localização aproximada. Aparece então um aviso a sugerir que verifiques a definição de localização: vê [Problemas de localização](/pt/guide/help/location-problems/).
:::

## Duas armadilhas que Diana vigia

- **Dentro de casa**, uma posição por wifi chega muitas vezes num segundo a dizer ±20 m. É a precisão que a base de dados de wifi julga ter, não a precisão real. Diana responde, mas continua à escuta o resto dos doze segundos e corrige a resposta se for preciso.
- **Telemóveis que prometem mais do que conseguem.** Diana compara as leituras dos últimos 45 segundos. Uma leitura isolada e disparatada é ignorada. Se as leituras se contradizem, a resposta diz *"leituras contraditórias"*. Andar não conta como dispersão.

:::caution
Diana só consegue responder a isto para áreas **com** limite. Para um anel tracejado ou um ponto azul não consegue. Vê [Pontos e áreas](/pt/guide/map/points-and-areas/).
:::
