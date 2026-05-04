from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
import pandas as pd 
import pmdarima as pm 
import numpy as np 
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
from src import plots as grafico 
from sklearn.metrics import mean_absolute_error, mean_squared_error
from statsmodels.stats.diagnostic import acorr_ljungbox



def testar_estacionariedade(serie):
    #CALCULANDO O DICKEY FULLER 

    resultado = adfuller(serie) 
    
    print('Estatistica ADF: ', resultado[0]) #Quanto mais negativo mais estácionário é a série
    print('p-valor: ', resultado[1]) # > 0.05 então a série não é tecnicamente estácionária (Existe tencia de queda ou subida)

    if (resultado[1] > 0.05):
        print('Serie não é estácionaria')
    else:
        print('Série é estacionária')

    #Como a serie é não estácionária, então foi aplicado a diferenciação para tornara a série estácionária  

#|-------- Modelo Sarima ------------------|
def treinar_modelo(serie):

    modelo = pm.auto_arima(
                            serie.values,
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

    return modelo 

def validar_modelo_sarima(modelo, df):

    train = df['CVLI'].loc['2014-01-01':'2023-12-01']
    test = df['CVLI'].loc['2024-01-01':]

    #Treinando o modelo
    modelo.fit(train)

    #Criando as previsões (Validação)
    forecast = modelo.predict(n_periods=len(test)).astype(int)

    #Gerando um dataframe com os valore previstos
    forecast = pd.DataFrame(forecast, index=test.index, columns=['CVLI'])

    return test, forecast 

def previsao_modelo(modelo, df):

    serie_completa = df['CVLI']

    modelo.fit(serie_completa)

    previsao_2026 = modelo.predict(n_periods=9).astype(int)
    
    indice_2026 = pd.date_range(start='2026-04-01', periods=9, freq='MS')

    df_2026 = pd.DataFrame(previsao_2026, index=indice_2026, columns=['CVLI'])

    return df_2026

def  test_Ljung_Box(modelo): 

    residuos = modelo.resid()
    resultado_lb = acorr_ljungbox(residuos, lags=[10], return_df=True)

    return resultado_lb

def calculando_metricas(test, forecast):
    # MAE: Média de erro absoluto 
    mae = mean_absolute_error(test, forecast)

    # RMSE: Penaliza erros maiores 
    rmse = np.sqrt(mean_squared_error(test, forecast))

    # MAPE: Erro percentual
    mape = np.mean(np.abs((test - forecast['CVLI']) / test)) * 100

    print(f"Erro Médio Absoluto (MAE): {mae:.2f} crimes")
    print(f"Raiz do Erro Quadrático Médio (RMSE): {rmse:.2f} crimes")
    print(f"Erro Percentual Médio (MAPE): {mape:.2f}%")
