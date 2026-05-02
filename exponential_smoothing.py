import pandas as pd
import numpy as np
import matplotlib.pyplot as  plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.api import ExponentialSmoothing
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.stats.diagnostic import acorr_ljungbox
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error


dataFrame = pd.read_csv('Dados/CVLI_CEARA.csv', sep=';')


dataFrame.drop(columns=['M'], inplace=True)
dataFrame.drop(columns=['F'], inplace=True)

plt.figure(figsize=(14, 7))
plt.plot(dataFrame['MES'], dataFrame['CVLI'])
plt.title('Homícidios no Ceará')
plt.xlabel('Meses')
plt.ylabel('Número de Mortes Ocorridas')

#Definindo o intervalo menor para os anos não ficarem sobrepostos
id = np.linspace(0, len(dataFrame) - 1, 5, dtype=int)

meses_selecionados = dataFrame['MES'].iloc[id]

plt.xticks(meses_selecionados, rotation=0)

plt.show()


#Criando uma decomposição de Séries temporais com modelo aditivo em um periodo de 12 meses 

decomposicao = seasonal_decompose(dataFrame['CVLI'], model='additive', period=12)


figura_serie = decomposicao.plot()
figura_serie.set_size_inches(12, 8)
plt.show()


#Utilizando o o modelo Exponetial Smoothing (Suavização Exponencial)
#É um modelo simples e de fácil implementação que atribui pesos maiores às observações mais recentes. 

modelo_suavizacao_exponencial = ExponentialSmoothing(
    dataFrame['CVLI'], 
    trend=None,
    seasonal='add',
    seasonal_periods=12
)


fit_modelo = modelo_suavizacao_exponencial.fit()


#Previsões futuras 
forecast = fit_modelo.forecast(24)

plt.figure(figsize=(14, 7))


#Verificando os residuos do modelo 
fit_modelo.resid.plot(title='Resíduos do Modelo', figsize=(14, 7))
plt.show()

print(acorr_ljungbox(fit_modelo.resid, lags=[10]))


plot_acf(fit_modelo.resid, lags=20)
plt.show()


plt.figure(figsize=(14, 7))
plt.plot(forecast, label='Previsão Homicidios', linestyle='--')

df_previsao_smoothing_exponential = pd.DataFrame({
    'Meses Projetados' : forecast.index, 
    'Estimativa': forecast.values.round(0)
})

print(df_previsao_smoothing_exponential)



#Crianod um modelo e definindo o tamanho do teste (24 meses)

tamanho_teste = 24
treino = dataFrame.iloc[:-tamanho_teste]
teste = dataFrame.iloc[-tamanho_teste:]


print(f"Treinando com dados até: {treino['MES'].iloc[-1]}")
print(f"Testando com dados de: {teste['MES'].iloc[0]} até {teste['MES'].iloc[-1]}")



#Criando o modelo 

modelo_validacao = ExponentialSmoothing(
    treino['CVLI'], 
    trend=None, 
    seasonal='add',
    seasonal_periods=24
).fit()


#Prevendo os valores para o periodo que foi separado para teste 

previsoes_teste = modelo_validacao.forecast(24)


MAE = mean_absolute_error(teste['CVLI'], previsoes_teste)
MAPE = mean_absolute_percentage_error(teste['CVLI'], previsoes_teste) * 100 

print(f"Erro médio absoluto (MAE): {MAE:.2f} homicidios")
print(f"Erro percentual (MAPE):  {MAPE:.2f}%")


plt.figure(figsize=(14, 7))
plt.plot(treino['MES'], treino['CVLI'], label='Treino (Histórico)')
plt.plot(teste['MES'], teste['CVLI'], label='Teste (Realidade)', color='green')
plt.plot(teste['MES'], previsoes_teste, label='Previsão do Modelo', color='red', linestyle='--')

plt.title('Validação do Modelo: Real vs Previsto')
plt.legend()

#Definindo o intervalo de 5 para exibir os dados
indices = np.linspace(0, len(dataFrame) - 1, 5, dtype=int)

ticks_selecionados = dataFrame['MES'].iloc[indices]

plt.xticks(ticks_selecionados, rotation=0)

#Rotacioando os dados na eixo x
plt.xticks(rotation=45)

plt.show()


df_previsao = pd.DataFrame({
    'Meses Projetado': forecast.index,
    'Estimativa_CVLI': forecast.values.round(0)
})

print(df_previsao)