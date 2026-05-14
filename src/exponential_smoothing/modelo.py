import pandas as pd
import numpy as np
import matplotlib.pyplot as  plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.api import ExponentialSmoothing
from statsmodels.tsa.api import SimpleExpSmoothing, Holt 

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.stats.diagnostic import acorr_ljungbox
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error
from statsmodels.stats.diagnostic import acorr_ljungbox

def modelo(df):

    #É necessário construir um novo modelo para validação 
    modelo_suavizacao_exponencial = ExponentialSmoothing(
        df['CVLI'], 
        trend='additive',
        seasonal='additive',
        seasonal_periods=12
    )

    return modelo_suavizacao_exponencial 

def validacao_modelo(modelo, df): 
    
    train = df['2014-01-01' : '2023-12-01']
    test = df['2024-01-01': ]


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

def transformar_DataFrame(previsao): 

    datas = pd.date_range(start='2026-04', end='2026-12', freq='MS')
    previsao = previsao.values.flatten() #A previsão retorna uma matriz 2D por isso a função 

    df_cvli = pd.DataFrame({
    'MES': datas,
    'CVLI': previsao 
    })

    df_cvli['MES'] = df_cvli['MES'].dt.to_period('M') # para ficar melhor apresentavel 
    
    return df_cvli

def  test_Ljung_Box(modelo_ajustado): 

    residuos = modelo_ajustado.resid

    resultado_lb = acorr_ljungbox(residuos, lags=[10], return_df=True)

    return resultado_lb