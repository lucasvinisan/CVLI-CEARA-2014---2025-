# Previsão de CVLI - Ceará (2026-2027)

## 📁 Estrutura do Projeto

| Arquivo | Descrição |
|---------|-----------|
|Dashboard | Análise Descritiva dos CVLI ocorridos no Ceará (2014 - 2025) |
|Dados | Base de Dados utilizada para o estudo |
| Img | Imagens dos plots dos modelos para análise|
| `Exponential_Smoothing.py` | Análise exploratória + Modelo Holt-Winters |
| `SARIMA.py` | Modelo SARIMA |


- Distribuição dos Homicidios Ceará (2014 - 2015) 

![Homcidios_Ceara](img/Homicidios_ceara(2014-2024).jpeg)

- Decomposição da serie Temporal
![Serie_Temporal](img/Serie_Temporal.jpeg)


## 📊 Resultados

| Modelo                |  MAPE  |  MAE  | LB_STAT(Lag 10) | LB_pVALUE     |
|-----------------------|--------|-------|-----------------|---------------|
| Exponential Smoothing | 6.72%  | 17.81 |  9.280059 | 0.505747  | 
| SARIMA                | 13.84% | 37.71 | 5.687021  | 0.840837  |

✅ O Exponential Smoothing apresentou melhor performance para este problema.

O modelo Exponential Smoothing apresentou MAPE de 6.72%, com erro médio de ~18 homicidios a cada mês. Por outro lado, o modelo SARIMA mostrou-se inferior, apresentando um MAPE de 13.84 e um erro médio de ~38 homcídios por mês. Portanto, o modelo Exponential Smoothing foi o que apresentou o melhor desempenho no estudo, com acuracia maior e uma melhor aderência aos dados.

## ▶️ Como reproduzir
