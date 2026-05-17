import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error

from src.exponential_smoothing import modelo as es
from src.exponential_smoothing import plots as grafico 


def executar_exponential_smoothing(df):

    modelo = es.modelo(df)
    test, forecast = es.validacao_modelo(modelo, df)
    grafico.plotar_validacao(df, test, forecast)


    previsao = es.previsao_intervalo_confianca(modelo, df)
    grafico.plotar_previsao_2026(previsao)

    print(previsao)
    
    modelo_ajustado = modelo.fit() # O teste ljung Box necessita de um modelo ajustado
    ljung_box = es.test_Ljung_Box(modelo_ajustado)
    
    print(ljung_box)

    return previsao




