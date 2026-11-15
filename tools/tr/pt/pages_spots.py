T = {
'spots/on-air': {'title': 'Quem está no ar', 'desc': 'O ecrã Spots: spots WWFF em direto, ATNO, direção e distância.', 'body': '''
Toca em **Spots** na barra de baixo. O ecrã **Spots e agenda** mostra quem está no ar a partir de uma área WWFF neste momento. A lista vem em direto do WWFF Spotline e atualiza a cada 30 segundos.

{{img:phone-spots-world|O ecrã Spots, separador No ar, Mundial, com uma lista de estações}}

## Uma linha por estação

| O que vês | Significado |
|---|---|
| Indicativo | O ativador, por exemplo `F5MQU/P`. |
| Número de QSO | Quantos contactos já foram feitos a partir dessa referência, segundo o diretório WWFF. |
| **ATNO** a vermelho | *All Time New One*: esta referência nunca foi ativada. A preferida dos caçadores. |
| Frequência, modo, referência | Por exemplo `10112 kHz · CW · FFF-4038`. |
| Minutos | Há quanto tempo chegou o spot. |
| Direção e distância | A partir de ti, por exemplo `191° · 440 km`. |

## O teu país ou mundial

Debaixo dos separadores escolhes **o teu país** (por exemplo CTFF) ou **Mundial**. Diana lembra-se da escolha e mantém-na igual à mesma opção nas Definições. O país que o botão representa segue a tua definição de país: enquanto não escolheres nenhum, Diana tira-o do teu indicativo (CT… dá CTFF, ON… ONFF, DL… DLFF).

## Abrir um spot

1. Toca numa linha.
2. O mapa abre, aproximado nessa área, com um painel: frequência e modo, a reserva, o locator de lá e o teu, a observação, o número de QSO, Mais info e uma bússola com a direção.
3. **← Voltar a Spots**, ou o botão de voltar do Android, leva-te de volta à lista.
4. **×** ou deslizar para baixo fecha apenas o painel e mantém o mapa.

:::note[Spotline inacessível?]
Então o ecrã diz isso, em vez de mostrar spots antigos sem aviso.
:::
'''},
'spots/agenda': {'title': 'A agenda', 'desc': 'Ativações anunciadas: quem planeia o quê, e quando.', 'body': '''
No ecrã **Spots**, toca no separador **Agenda**. Vês todas as ativações anunciadas, com referência, bandas e modos, e data e hora em UTC.

{{img:phone-agenda|O separador Agenda com ativações anunciadas}}

## Ler a agenda

- **A decorrer agora**: um ponto laranja e *"em direto até …"*.
- **Ainda por vir**: a cinzento, com data e hora de início.
- **ATNO** a vermelho: a referência nunca foi ativada.

A tua escolha entre **o teu país** e **Mundial** também se aplica aqui.

## Abrir um anúncio

Toca numa linha. O mapa abre nessa área com banda e modo, a reserva, o locator, a observação e a direção. **← Voltar a Spots** leva-te de volta.

## Anunciar tu próprio

Toca em **+ Anunciar** no topo da agenda. Vê {{link:spots/announce}}.

:::tip[Também no mapa]
Os anúncios estão no mapa como um ponto branco com anel laranja, com uma linha laranja tracejada a partir de ti. Vê {{link:map/reading-the-map}}.
:::
'''},
'spots/spot-yourself': {'title': 'Faz o teu spot', 'desc': 'Avisa os caçadores de que estás no ar, através do WWFF Spotline.', 'body': '''
No ar e pronto? Faz o teu spot, para que os caçadores te encontrem. O spot vai para o WWFF Spotline e daí para o DX cluster.

{{img:phone-spot-yourself|O ecrã Spot com referência, indicativos, frequência, modo e observação}}

## Passo a passo

1. Toca em **Spot** na barra de baixo, ou em **Faz o teu spot aqui** no painel de uma área.
2. Confirma a **referência**. Se estás dentro de uma área, ou vieste de um painel, Diana já a preencheu e diz de onde veio.
3. Os teus **indicativos** vêm das Definições: o indicativo portátil como ativador, o teu indicativo normal como spotter.
4. Preenche a **frequência** em kHz, por exemplo `7144`, e escolhe o **modo**.
5. Opcional: uma **observação** curta, até 100 caracteres. Toca numa das tuas **palavras rápidas** para a juntar com um toque.
6. Toca em **Verificar**. O Spotline analisa o teu spot sem o publicar, e diz-te o que acha.
7. Foi aceite? Toca em **Enviar spot**. Recebes uma confirmação com o número do teu spot.

## Porquê primeiro Verificar, depois Enviar?

Cada pedido ao Spotline sai de um orçamento partilhado por todos os utilizadores. *Verificar* garante que um spot está certo antes de custar um envio real. Se mudares alguma coisa depois de verificar, *Enviar* volta a fechar: a aprovação era para o spot tal como estava.

## O que Diana verifica por ti

- O formato do **indicativo**, o intervalo da **frequência** e o tamanho da **observação**, tal como o Spotline.
- O **plano de bandas**: um aviso quando o teu modo não corresponde ao segmento da tua frequência.
- A **referência**, contra a lista de Diana. Isso responde de imediato, mesmo sem rede.

:::caution[O que não pertence a uma observação]
Nada de agradecimentos nem de pedidos de banda. Cada spot vai para o DX cluster, onde isso é ruído. O Spotline também filtra linguagem imprópria.
:::

## Quando algo corre mal

- **Carregaste duas vezes com má ligação?** Diana diz que o spot já lá estava. Nada é publicado duas vezes.
- **O Spotline recusa?** Recebes a explicação do próprio Spotline.
- **O envio não funciona de todo?** Diana oferece **Enviar à moda antiga**: o spot vai para o formulário do próprio Spotline num novo separador. Vês a resposta deles tu próprio, mas Diana não a consegue confirmar.

Ainda não estás no ar, só estás a planear? Usa a agenda: {{link:spots/announce}}.
'''},
'spots/announce': {'title': 'Anunciar uma ativação', 'desc': 'Colocar uma ativação planeada na agenda WWFF, e guardar o teu PIN.', 'body': '''
Estás a planear uma ativação? Anuncia-a, para que os caçadores estejam prontos. O anúncio vai para a agenda WWFF no Spotline.

{{img:phone-announce|O ecrã Anunciar com indicativos, referência, início e fim, bandas e modos}}

## Três formas de lá chegar

- **Agenda** na barra de baixo.
- **+ Anunciar** no separador Agenda do ecrã Spots.
- **Anunciar uma ativação** no painel de uma área: a referência fica logo preenchida.

## Passo a passo

1. Confirma o **indicativo do ativador** e **o teu próprio indicativo**. Outra pessoa pode anunciar por um ativador.
2. Preenche a **referência WWFF**, por exemplo `CTFF-0012`.
3. Escolhe o **início** e o **fim**. Escolhes pela hora do teu próprio dispositivo; Diana converte para UTC antes de saírem do teu dispositivo.
4. Opcional: marca as **bandas** e os **modos** (podes escolher vários, por exemplo *40 m, 20 m · CW, SSB*) e junta uma observação.
5. Toca em **Verificar** e, quando for aceite, em **Enviar anúncio**.
6. **Aponta o teu PIN.**

:::danger[Guarda o teu PIN]
O PIN é a única forma de alterar ou cancelar este anúncio mais tarde, no próprio site do Spotline. Diana não o pode fazer por ti, e um PIN perdido não se recupera. Por isso Diana guarda, debaixo do formulário, uma lista de tudo o que anunciaste a partir deste dispositivo (referência, data, PIN). Toca em **✕** para remover uma linha. Essa lista existe só neste dispositivo.
:::

## Limites

- No máximo **um mês** de antecedência, e o fim não pode ser antes do início. O Spotline aplica as mesmas regras.
- No máximo **16 anúncios por dia** a partir de um dispositivo através de Diana, para proteger o orçamento partilhado. O uso normal fica muito abaixo disso.
- Para anúncios não existe "moda antiga". Se não funcionar, tenta mais tarde.

Que bandas a lista oferece (todas, ou apenas HF) é uma definição: {{link:settings/band-list}}.
'''},
}
