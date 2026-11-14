T = {
'field-info/overview': {'title': 'Info de campo', 'desc': 'Tudo sobre o local onde estás, em três separadores.', 'body': '''
A **Info de campo** é sobre o local onde estás. Tem três separadores:

| Separador | O que mostra |
|---|---|
| **Áreas** | As referências WWFF à tua volta. Vê {{link:field-info/areas-nearby}}. |
| **Localização** | Onde estás em termos de rádio: hora, locator, zonas. Vê {{link:field-info/location}}. |
| **Condições** | Meteorologia espacial e o que significa para as bandas. Vê {{link:field-info/conditions-space-weather}} e {{link:field-info/conditions-bands}}. |

## Abrir a Info de campo

1. Toca em **Info de campo** na barra de baixo (o círculo com um ponto).
2. Toca no separador que queres, em cima: **Áreas**, **Localização** ou **Condições**.
3. Debaixo do título, confirma de onde o Diana parte: *"a partir da sua posição GPS"* ou *"a partir do seu locator IN51RQ"*.

:::caution[Sem posição?]
Se o Diana disser que ainda não sabe onde estás, permite a localização (vê {{link:start/welcome-screen}}) ou preenche o teu locator em **Definições** › **A tua estação**. Só com um locator, o Diana trabalha a partir do centro desse quadrado, que pode estar a alguns quilómetros.
:::
'''},
'field-info/areas-nearby': {'title': 'Áreas por perto', 'desc': 'As referências WWFF à tua volta, ordenadas como quiseres.', 'body': '''
O separador **Áreas** lista as referências WWFF à volta da tua posição, dentro da distância que escolheste nas Definições (10, 25, 50 ou 100 km). As referências do outro lado da fronteira também aparecem.

{{img:phone-field-areas|Info de campo, separador Áreas, com referências perto de Antuérpia ordenadas por distância}}

## Uma linha por referência

| O que vês | Significado |
|---|---|
| Referência e nome | Por exemplo `ONFF-0842 · Boshoek`. |
| Distância e direção | Em linha reta a partir de ti, por exemplo `1.5 km · 62°`. |
| Número de QSO | Quantos contactos foram feitos a partir de lá, segundo o diretório WWFF. |
| Última atividade | A data da última ativação. |
| *sem data de ativação conhecida* | O diretório tem a referência, mas não uma data. |
| *não consta do diretório WWFF* | O Diana conhece a área, mas o diretório não tem nada sobre ela. Isso não quer dizer que nunca tenha sido ativada. |

## Ordenar: que ordem escolher?

| Botão | Quando usar |
|---|---|
| **Distância** | As mais próximas primeiro. Quando queres montar a estação depressa. |
| **Última atividade** | As áreas que estão há mais tempo fora do ar primeiro. É aí que um pile-up é mais provável. |
| **Número de QSO** | As áreas menos trabalhadas primeiro. Quando queres dar aos caçadores uma nova. |

## Abrir uma área

1. Toca numa linha.
2. O mapa abre, aproximado nessa área, com o seu painel e limite.
3. Mais de cem áreas por perto? Toca em **Mostrar mais** em baixo.

## Mudar a distância

**Definições** › **Info de campo** › 10, 25, 50 ou 100 km. Vê {{link:settings/field-info-distance}}.

:::note
O número de QSO e as datas vêm do diretório WWFF, atualizado todas as noites. Onde o diretório não tem nada, o ecrã diz isso, em vez de lhe chamar "nunca ativada".
:::
'''},
'field-info/location': {'title': 'Localização em termos de rádio', 'desc': 'Hora, locator, posição e zonas do local onde estás.', 'body': '''
O separador **Localização** dá tudo o que precisas sobre o teu próprio local durante um QSO ou no teu log. O Diana calcula-o no próprio dispositivo, por isso também funciona sem rede.

{{img:phone-field-location|Info de campo, separador Localização, com hora UTC e local, locator, precisão e zonas}}

| Caixa | Como ler |
|---|---|
| **Hora** | UTC e a tua hora local com fuso horário. O teu log é sempre em UTC. |
| **Locator** | O teu locator Maidenhead em seis caracteres (`JO21FD`) e em oito (`JO21FD70`). Num QSO normalmente dás os seis. |
| **Posição** | Em graus decimais e em graus, minutos e segundos, com a precisão em metros. |
| **Zonas** | A tua zona CQ, zona ITU e região ITU. A Bélgica é CQ 14, ITU 27, região 1; Portugal continental é CQ 14, ITU 37. |
| *limite perto: também …* | Estás perto de um limite de zona, ou a tua posição é incerta. Os dois números são então possíveis. |
| **WWFF mais próxima** | As referências mais próximas, em qualquer parte do mundo, em linha reta. |

:::note[De onde vêm as zonas]
As zonas CQ e ITU vêm de um conjunto de dados público, simplificado para cerca de 3 km. É por isso que perto de um limite a caixa também indica a zona vizinha.
:::
'''},
'field-info/conditions-space-weather': {'title': 'Condições: meteorologia espacial', 'label': 'Meteorologia espacial', 'desc': 'O mostrador Kp, o SFI, o índice A e as manchas solares, e o que significam.', 'body': '''
O separador **Condições** começa com a meteorologia espacial de hoje: um mostrador com o **índice Kp** e três números por baixo.

{{img:phone-field-conditions|Info de campo, separador Condições, com o mostrador Kp em 2, calma, e as barras das bandas}}

## O mostrador Kp

O Kp mede o quão agitado está o campo magnético da Terra, numa escala de 0 a 9. Quanto mais baixo, melhor para as bandas mais altas. O Diana mostra o valor oficial de três horas da NOAA, e ao lado uma estimativa dos últimos minutos.

| Kp | Palavra no Diana | O que significa |
|---|---|---|
| 0 a 2 | calma | Sem efeito. Condições normais. |
| 3 | instável | Ligeiramente agitado. Normalmente ainda sem efeito notório. |
| 4 | ativa | 20, 15 e 10 m descem um nível. |
| 5 e 6 | tempestade G1, G2 | Tempestade fraca: 20, 15 e 10 m pior. Os 80 e 40 m quase não sentem. |
| 7 a 9 | tempestade G3 a G5 | Tempestade forte: todas as bandas pior, as altas mais do que todas. |

:::note
O Kp é um valor mundial, não uma medição na tua posição.
:::

## Os três números

| Número | O que te diz |
|---|---|
| **SFI** | Fluxo solar. Quanto mais alto, melhor abrem as bandas altas. Perto de 70 é baixo, acima de 150 é alto. |
| **A** | Quão agitado esteve o campo magnético ao longo do dia todo. Baixo é bom. |
| **Manchas solares** | Acompanham o SFI: mais manchas, mais hipóteses de DX nas bandas altas. |

O SFI, o A e as manchas solares são valores diários; o Diana diz de que dia são.

## Que idade têm os números?

Debaixo do mostrador diz quando os números foram atualizados, por exemplo *"Atualizado às 14:37 (há 12 min)"*. O Diana tenta obtê-los duas vezes por hora, mas na prática pode haver algumas horas entre duas atualizações.

- Com mais de **oito horas**: a mensagem fica laranja.
- Valor Kp com mais de **doze horas**: o Diana diz isso à parte.

A fonte é a NOAA SWPC. O que significa por banda: {{link:field-info/conditions-bands}}.
'''},
'field-info/conditions-bands': {'title': 'Condições: as bandas', 'label': 'As barras das bandas', 'desc': 'Como ler a barra de cores de cada banda ao longo do dia.', 'body': '''
Debaixo da meteorologia espacial, o separador **Condições** mostra uma barra de cores por banda: 80, 40, 20, 15 e 10 m.

## Ler a barra de uma banda

1. Cada barra é **uma banda**. Ao lado da banda diz para que serve, por exemplo *"NVIS e EU"*.
2. A barra vai da esquerda para a direita por cinco partes do dia: **manhã, meio-dia, tarde, anoitecer e noite**. O Diana calcula-as a partir do nascer e do pôr do sol na tua posição.
3. A **cor** é a expectativa: verde é boa, amarelo razoável, vermelho fraca.
4. O fino **traço** vertical é **agora**. À direita diz o que vale agora, por exemplo *"agora: boa"*.

## O que significam as etiquetas

| Etiqueta | Alcance |
|---|---|
| **NVIS** | Perto, até cerca de 400 km. Ideal para seres contactado dentro do teu país. |
| **EU** | Dentro da Europa. |
| **DX** | Mais longe, fora da Europa. |

| Banda | Etiqueta no Diana |
|---|---|
| 80 m | NVIS, EU à noite |
| 40 m | NVIS e EU |
| 20 m | EU e DX |
| 15 m | DX |
| 10 m | DX |

:::caution[Uma indicação, não uma promessa]
As barras são uma estimativa aproximada do próprio Diana, com base no SFI, no Kp, na estação do ano e na hora do dia na tua posição. Não é uma previsão da NOAA. Uma banda marcada como "fraca" pode estar aberta na mesma: escuta sempre um momento.
:::

:::tip[Exemplo no terreno]
Kp 2, calma, SFI 91, ao anoitecer nas Ardenas: os 40 m estão em boa e são a tua melhor hipótese para a Bélgica e a Europa. Os 15 m estão em fraca ao anoitecer; não vale a pena começar por aí.
:::

Sem posição, o Diana mostra na mesma as barras, mas sem o traço do agora.
'''},
}
