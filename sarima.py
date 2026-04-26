import pandas as pd
import numpy as np
import matplotlib.pyplot as  plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.api import ExponentialSmoothing
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.stats.diagnostic import acorr_ljungbox
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error

dataFrame = pd.read_csv('Dados\Serie_homicidios_Ceara_2014-2025.csv', sep=';')

dataFrame.drop(columns=['M'], inplace=True)
dataFrame.drop(columns=['F'], inplace=True)

#Divindo dados para treino
train_size = int(len(dataFrame) * 0.8)
train, test = dataFrame.iloc[:train_size], dataFrame.iloc[train_size:]

# Passando apenas a série numérica
modelo = SARIMAX(train['CVLI'].astype(float),
                order=(1, 1, 1),
                seasonal_order=(1, 1, 1, 12))

#Resultado treino
resultado = modelo.fit()

#Previsão 
previsao = resultado.forecast(steps=len(test))

resultado.resid.plot(title='Residuos de Modelo', figsize=(14, 7))

plt.show()

print(acorr_ljungbox(resultado.resid, lags=[10]))


plot_acf(resultado.resid, lags=20)
plt.show()

plt.figure(figsize=(14, 7))
plt.plot(previsao, label='Previsao', linestyle='--')

MAE  = mean_absolute_error(test['CVLI'], previsao)
MAPE = mean_absolute_percentage_error(test['CVLI'], previsao) * 100 

print(f"Erro Médio Absoluto (MAE): {MAE:.2f} homicídios")
print(f"Erro Percentual (MAPE): {MAPE:.2f}%")

plt.figure(figsize=(14, 7))
plt.plot(train.index, train['CVLI'], label='Treino', color='blue')
plt.plot(test.index, test['CVLI'], label='Teste', color='green')
plt.plot(test.index, previsao, label='Previsão (SARIMAX)', color='Red', linestyle='--')
plt.title('Compração dados Reais com Previsão SARIMAX')

plt.legend()
plt.xlabel('DATA')
plt.ylabel('Quantidade de Ocorrências')

plt.show()


df_previsao = pd.DataFrame({
    'Meses Projetados': previsao.index, 
    'Estimativa_CVLI': previsao.values.round(0)
})

print(df_previsao)