# Previsão de CVLI - Ceará (2014-2025)

## 📁 Estrutura do Projeto

| Arquivo | Descrição |
|---------|-----------|
| `01_EDA_Exponential_Smoothing.ipynb` | Análise exploratória + Modelo Holt-Winters |
| `02_SARIMA.ipynb` | Modelo SARIMA |

## 📊 Resultados

| Modelo                |  MAPE  |  MAE  | LB_STAT(Lag 10) | LB_pVALUE     |
|-----------------------|--------|-------|-----------------|---------------|
| Exponential Smoothing | 6.72%  | 17.81 |  9.280059 | 0.505747  | 
| SARIMA                | 13.84% | 37.71 | 5.687021  | 0.840837  |

✅ O Exponential Smoothing apresentou melhor performance para este problema.

## ▶️ Como reproduzir
