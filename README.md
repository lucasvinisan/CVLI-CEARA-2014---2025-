# Um Estudo Preditivo e Descritivo Sobre os CVLI Ocorridos no Estado do Ceará (2014 - 2025)

## 📄 Resumo
    
- **problema:** As altas taxas de crimes são um dos problemas mais graves enfrentados pelo estado do Ceará nos últimos anos. Por conta disso, decidi reaalizar  um estudo utlizando analise preditiva e descritiva sobre os CVLI, com  a finalidade de compreender o comportamento desses números nos últimos 12 anos no estado. 

- **Solução:** foi realizar um estudo descritivo sobre os dados acumulados dos CVLI (Crimes Violentos Letais e Intencionais) entre os anos de 2014 a 2025. Além disso, foi implmentado agoritmos preditivos com o intuito de projetar  cenários para os valores acumulados de CVLI nos anos de 2026 e 2027 no Ceará. 

- **Impacto:** O estudo identificou tendência de queda nos números de assassinatos no estado para os próximos anos, mas com números preocupantes que merecem atenção do poder público. 

## 📋 Introdução e Contextualização

- **Objetivo:** O principal objetivo do estudo era obter informações relevantes sobre os números de CVLI ocorridos no estado do Ceará. O número assassinatos ocorridos, a fim de obter insigts relevantes sobre essa temática relevante para a Segurança Pública do estado. 

- **Metodologia:** Na análise preditiva, as ferramentas utilizadas no estudo foram a linaguagem de programaçãO Python, a fim de implementar a analise exploratório e a construção dos modelos preditivos Holt-Winters e Sarima.  Para a análise descritiva foram utilizadas as ferramentas Tableau para construção e visualização do dashboard, o python para extração e tratamento dos dados e excel para visualização da base de dados.  

## 🎲 Coleta de Dados

- **Fonte:** Os dados foram coletados através do site da secretária de segurança pública do estado do Ceará. Adicionalmente, como as informações estavam completas e não continham dados faltantes, não foi necessário realizar tratamento de campos nulos ou de dados incompatíveis. As informações na base de dados está distribuída entre os meses de janeiro de 2014 a dezembro de 2025, totaizando 144 registros ao longo de 12 anos. Além dos indices totais, a base de dados detalha a distribuição de CVLI por gêneros (Feminino e Masculino).

## 📁 Estrutura do Projeto

| Arquivo | Descrição |
|---------|-----------|
|Dashboard | Análise Descritiva dos CVLI ocorridos no Ceará (2014 - 2025) |
|Dados | Base de Dados utilizada para o estudo |
| Img | Imagens dos plots dos modelos para análise|
| `Exponential_Smoothing.py` | Análise exploratória + Modelo Holt-Winters |
| `SARIMA.py` | Modelo SARIMA |


## 🔭  Análise Exploratório de Dados

### Distribuição dos Homicidios Ceará (2014 - 2015) 

![Homcidios_Ceara](img/Homicidios_ceara(2014-2024).jpeg)

A base de dados é composta por 144 registros representando todos os meses dos 12 anos utilizados para o estudo (2014 - 2025). 

### Decomposição da Série Temporal

![Serie_Temporal](img/Serie_Temporal.jpeg)

Séries Temporais são conjuntos de registros sobre uma variável, ordenado no tempo. O objetivo de utilizar analise de séries temporais é de identificar padrões não aleatórios na série, com o objetivo de fazer previsões futuras através de tomada de decisões. A decomposição da série poderá ajudar na identificação dos componentes que estão atuando sobre aquele conjunto de dados.

**CVLI - (Crimes Violentos Letais e Intencionais) estado do Ceará 2014***

- VARIAÇÃO: Os dados de CVLI iniciam com o patamar um pouco superior a 400 no ano de 2014, seguido de algumas oscilações. Posteriormente, observar-se uma redução drástica entre os meses finais de 2018 e iniciais de 2019. No final de 2017 foi observado o maior valor de CVLI da série no estado, onde em 2017 foi o ano com maior valor acumulado nesse retrato de 12 anos. Por outro lado, no ano de 2019 apresentou os menores valores mensais observados na série, onde os valores mensais giraram em torno de 200 CVLI.

- Volatilidade: Observa-se vários dados com fortes oscilações, com picos muitos acentuados e reduções drásticas em alguns períodos da série. Essas flutuações dos dados podem ter sido influenciadas por eventos externos como crises na segurança pública, conflitos entre facções criminosas por dominância de territórios para o tráfico de drogas e entre outros eventos externos.  

**Trend (Tendência)**

- Queda: A série inicia com valor de 400 CVLI no ano de 2014, seguida de uma queda suave até atingir seu menor valor no mês 35 (Fim do ano de 2015). Posteriormente, houve um aumento expressivo atingindo o seu pico no mês 45 (ano de 2017) o ano mais violento observado em todo o intervalo.
Nos anos seguintes houve queda acentuada nos números de CVLI até o mês 65 (Ano de 2019).   

- Estabilidade: Após o mês 80 (ano de 2020), a tendencia dos dados é queda suave e constante, sugerindo que políticas públicas de segurança ou condições externas (Fim de brigas entre facções por influência em território de tráfico de drogas) podem ter afetado os números de CVLI, onde os números de assassinatos estiveram sob relativo controle nos últimos anos da séries, sem novos picos explosivos observados.

**Seasonal (Sazonal):**

- Observa-se uma padrão sazonal claro nos homicídios do estado do Ceará ao longo dos anos. O primeiro período de aumento ocorre entre os meses de fevereiro e março, com expressivo aumento dos assassinatos, possivelmente influenciado por festividades como carnaval e o período de férias.

- O maior pico sazonal é observado entre os meses de Julho e Agosto, coincidindo com férias do meio do ano, período em que se registra as maiores altas nos crimes no estado. Em seguida, observa-se um período de estabilidade entre os meses de agosto e setembro, com poucas flutuações nos números. Por fim, após essa estabilidade há uma queda acentuada e contínua, que culmina em uma redução considerável atingindo seu ponto mais baixo no mês de dezembro

**Resid (Resíduo/Irregular/Restante):**

- Aleatoriedade: a maioria dos pontos concentra-se em torno de zero, sugerindo que o modelo de decomposição capturou bem os padrões (tendência e sazonalidade) da série. Os resíduos aparentam ser aleatórios, sem viés evidente.  

- Interpretação: Outliers (Pontos fora da curva) observa um outliers considerável no mês 72 (ano de 2020). Neste ano houve uma crise policial, onde delegacias foram fechadas e parte da força policial do estado cruzou os braços e não foram as ruas. Eventos extraordinários como esse não são capturados pelos componentes de tendência e sazonalidade.

## 📊 Resultados

| Modelo                |  MAPE  |  MAE  | LB_STAT(Lag 10) | LB_pVALUE     |
|-----------------------|--------|-------|-----------------|---------------|
| Exponential Smoothing | 6.72%  | 17.81 |  9.280059 | 0.505747  | 
| SARIMA                | 13.84% | 37.71 | 5.687021  | 0.840837  |

✅ O Exponential Smoothing apresentou melhor performance para este problema.

O modelo Exponential Smoothing apresentou MAPE de 6.72%, com erro médio de ~18 homicidios a cada mês. Por outro lado, o modelo SARIMA mostrou-se inferior, apresentando um MAPE de 13.84 e um erro médio de ~38 homcídios por mês. Portanto, o modelo Exponential Smoothing foi o que apresentou o melhor desempenho no estudo, com acuracia maior e uma melhor aderência aos dados.

## ▶️ Como reproduzir
