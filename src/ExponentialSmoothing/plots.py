import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error



def plotar_validacao(df, test, forecast): 


    fig, ax = plt.subplots(figsize=(14, 6))

    # Série histórica completa (treino)
    train = df['2014-01-01':'2024-03-01']
    ax.plot(train.index, train['CVLI'], label='Treino', color='steelblue', linewidth=2)

    # Valores reais do período de teste
    ax.plot(test.index, test['CVLI'], label='Real (Teste)', color='green', linewidth=2, marker='o', markersize=4)

    # Previsão
    ax.plot(test.index, forecast, label='Previsão', color='red', linewidth=2, linestyle='--', marker='x', markersize=5)

    # Linha divisória treino/teste
    ax.axvline(pd.Timestamp('2024-04-01'), color='gray', linestyle=':', linewidth=1.5, label='Início do Teste')

    # Métricas no gráfico
    mae  = mean_absolute_error(test['CVLI'], forecast)
    mape = np.mean(np.abs((test['CVLI'] - forecast) / test['CVLI'])) * 100
    
    ax.set_title(f'Suavização Exponencial — Teste vs Previsão\nMAE: {mae:.1f}  |  MAPE: {mape:.1f}%', fontsize=14, fontweight='bold')

    ax.set_xlabel('Data')
    ax.set_ylabel('CVLI')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()