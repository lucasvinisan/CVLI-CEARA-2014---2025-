import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error

from src.ExponentialSmoothing import modelo as es
from src.ExponentialSmoothing import plots as grafico 


def executar_exponential_Smoothing(df):

    modelo = es.modelo(df)

    test, forecast = es.validacao_modelo(modelo, df)

    grafico.plotar_validacao(df, test, forecast)

    previsao = es.previsao(modelo, df)


    return previsao




