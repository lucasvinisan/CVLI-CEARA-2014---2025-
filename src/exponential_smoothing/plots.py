import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error

#Definindo globalmente o style dos plots 
plt.style.use('grayscale') 

def plotar_validacao(df, test, forecast): 


    fig, ax1 = plt.subplots(figsize=(12, 8))

    # Série histórica completa (treino)
    train = df['2014-01-01':'2023-12-01']
    test_series = test['CVLI']

    
    ax1.plot(train.index, train['CVLI'], label='Treino', linewidth=1)

    # Valores reais do período de teste
    ax1.plot(test_series.index, test_series, label='Real (Teste)', color='black', linewidth=1, marker='o', markersize=4)

    # Previsão
    ax1.plot(test_series.index, forecast, label='Previsão', linewidth=1, linestyle='--',  color='red', marker='x', markersize=4)

    # Linha divisória treino/teste
    ax1.axvline(pd.Timestamp('2024-01-01'), linestyle=':', linewidth=1.5, label='Início do Teste')
    
    
    # MAE: Média de erro absoluto 
    mae = mean_absolute_error(test_series, forecast)

    # RMSE: Penaliza erros maiores 
    rmse = np.sqrt(mean_squared_error(test_series, forecast))

    # MAPE: Erro percentual
    mape = np.mean(np.abs((test_series - forecast) / test_series)) * 100

    ax1.set_title(f'Exponential Smoothing — Teste vs Previsão\nMAE: {mae:.1f}  |  MAPE: {mape:.1f}% | RMSE: {rmse:.1f}%', fontsize=14, fontweight='bold')

    ax1.set_ylabel('Ocorrências CVLI')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

