import pandas as pd
import numpy as np
import matplotlib.pyplot as  plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.api import ExponentialSmoothing
from statsmodels.tsa.api import SimpleExpSmoothing, Holt 

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.stats.diagnostic import acorr_ljungbox
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error



def modelo(df):

    #È necessário construir um novo modelo para validação 
    modelo_suavizacao_exponencial = ExponentialSmoothing(
        df['CVLI'], 
        trend='add',
        seasonal='add',
        seasonal_periods=12
    )

    return modelo_suavizacao_exponencial 

def validacao_modelo(modelo, df): 
    
    train = df['2014-01-01' : '2024-03-01']
    test = df['2024-04-01': ]


    modelo_treino = ExponentialSmoothing(
        train['CVLI'],
        trend='add',
        seasonal='add',
        seasonal_periods=12
    )


    #Trianando modelo
    Modelo_Treinado_validacao = modelo_treino.fit()

    #Fazendo previsão 
    previsao = Modelo_Treinado_validacao.forecast(len(test)).astype(int)

    
    return test, previsao


def previsao(modelo, df): 

    modelo_previsao = modelo.fit()

    previsao = modelo_previsao.forecast(9).astype(int)

    return previsao


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

