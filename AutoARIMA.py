from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
import pandas as pd 
import pmdarima as pm 
import numpy as np 
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
import plotar_graficos as grafico 
from sklearn.metrics import mean_absolute_error, mean_squared_error
from statsmodels.stats.diagnostic import acorr_ljungbox


#Carregando a base de Dados 
df = pd.read_csv("Dados\Serie_homicidios_Ceara_2014-2025.csv", sep=";")

# |----------Pré-Processamento dos Dados --------------------|

#Convertendo Coluna de Data em datatime (%y-%m-%d)
df["MES"] = pd.to_datetime(df["MES"], format="%m/%Y")

#Transformando o 'MES' no indice
df.index = df['MES']
del df['MES']
#print(df)

# |------------ Análise Exploratória e Decomposição da Série Temporal ---------------|

#Plotando os graficos iniciais 
grafico.plotar_graficos_serie(df)

#Decomposição da Série temporal (Aditiva)
grafico.decomposicao_aditivo(df)

#CALCULANDO O DICKEY FULLER 
#Saber se os dado têm uma média e  uma variância constantes 
resultado = adfuller(df['CVLI'])

print('Estatistica ADF: ', resultado[0]) #Quanto mais negativo mais estácionário é a série

print('p-valor: ', resultado[1]) # > 0.05 então a série não é tecnicamente estácionária (Existe tencia de queda ou subida)

print("Tornando a série estacionária")

#Como a serie é não estácionária, então foi aplicado a diferenciação para tornara a série estácionária  
# Garantindo a estacionaridade da Série -------|
df_diff = df['CVLI'].diff().dropna()  #Aplicando a diferenciação 
resultado_adf = adfuller(df_diff)

print('Estatistica ADF: ', resultado_adf[0]) #Quanto mais negativo mais estácionário é a série

print('p-valor: ', resultado_adf[1]) # > 0.05 então a série não é tecnicamente estácionária (Existe tencia de queda ou subida)



# |-----------------Implementando auto-arima -------------------------------------| 
# Identificando os parâmetros mais otimizados para o modelo
modelo = pm.auto_arima(
                        df['CVLI'].values,
                        start_p = 1, 
                        max_p = 6, 
                        start_q = 1, 
                        max_q = 6, 
                        m = 12, 
                        seasonal = True, 
                        d = 1, 
                        D = 1, 
                        trace = True, 
                        error_action='ignore', 
                        suppress_warnings = True, 
                        stepwise = True 
)

 #Não itera sobre todas as combinações possiveis do Arima 
print(modelo)
#ARIMA(p, d,, q)
'''
    ARIMA(1,1,0)(2,1,0)[12] 

    p -> O número de lags que foram/devem ser excluídos no modelo
    d -> O número de vezes que as obsrvações serão diferenciadas 
    q -> O tamanho de uma janela de média móvel. (Ordem de média movel)

'''

modelo.plot_diagnostics() 
plt.tight_layout()
plt.show()



# |--------------- Validação -----------------------|

train = df['CVLI'].loc['2014-01-01':'2023-12-01']
test = df['CVLI'].loc['2024-01-01':]

#Treinando o modelo
modelo.fit(train)

#Criando as previsões (Validação)
forecast = modelo.predict(n_periods=24).astype(int)

#Gerando um dataframe com os valore previstos
forecast = pd.DataFrame(forecast, index=test.index, columns=['CVLI'])
print(forecast)

#validaçãp
grafico.plotar_validacao(test, forecast, df)

#Metircas (MAE, RMSE, MAPE)
grafico.calculando_metricas(test, forecast)

# Criando a tabela de comparação
# grafico.tabela_comparacao(test, forecast)


# |-------- Teste Ljung-Box--------------------------|

# 1. Extrair os resíduos do modelo que você treinou
residuos = modelo.resid()

# 2. Executar o teste de Ljung-Box
# O parâmetro 'lags' costuma ser 10 ou 20 para séries mensais
resultado_lb = acorr_ljungbox(residuos, lags=[10], return_df=True)

print(resultado_lb)



# |------------------ Realizando as Previsões --------------------------------|




