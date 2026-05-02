import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.metrics import mean_absolute_error, mean_squared_error

plt.style.use('grayscale') #Definindo globalmente o stilos dos plots 

def plotar_graficos_serie (df):
    
    #Criando uma figura com três linhas e uma coluna para plotar os três graficos em um só 
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12,12))

    #PLotando o gráfico com base no gênero 
    df[['F', 'M', 'CVLI']].plot(kind='line', ax=ax1)
    ax1.set_title = ('Quantidade')  
    ax1.set_xlabel(None)
    ax1.set_ylabel = ('Número de Casos')
    
    #PLotando o gráfico proporção por Genero 
    df_percetual = df[['F', 'M']].div(df['CVLI'], axis=0) * 100 
    df_percetual.plot(kind='area', stacked=True, ax=ax2)
    ax2.set_title = ('Proporção')
    ax2.set_xlabel(None)
    ax2.set_ylabel = ('Porcentagem por gênero')

    
    #PLotando o gráfico das valores observados na série
    df_cvli = df['CVLI'].plot(kind='line', ax=ax3)
    ax3.set_title = ('Homicidios no Estado do Ceará')
    ax3.set_xlabel(None)
    ax3.set_ylabel = ('Meses')

    #Ajustando lyout
    plt.tight_layout()
    plt.show()

def plotar_validacao(test, forecast, df):
   
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

    pd.concat([test, forecast], axis=1).plot(ax=ax1)
    ax1.set_title("Validação: [2024 - 2025]")
    ax1.set_xlabel(None)
    ax1.legend(["Histórico", "Previsão"]) # Garante que a legenda apareça corretamente

    pd.concat([df['CVLI'], forecast], axis=1).plot(ax=ax2, linewidth=1)
    ax2.set_title("Visão Geral: Histórico vs Previsão")
    ax2.set_xlabel(None)
    ax2.legend(["Histórico (CVLI)", "Previsão"])

    plt.tight_layout()
    plt.show()


def decomposicao_aditivo(df):

    decomposicao_serie = seasonal_decompose(df['CVLI'], model='addmuitive', period=12)
    figure = decomposicao_serie.plot()
    figure.set_size_inches((12, 12))
    plt.tight_layout()
    plt.show()

def decomposicao_multplicativo(df):
    
    decomposicao_serie = seasonal_decompose(df['CVLI'], model='multiplicative', period=12)
    figure = decomposicao_serie.plot()
    figure.set_size_inches((12, 12))
    plt.tight_layout()
    plt.show()

def tabela_comparacao(test, forecast):
    comparativo = test.to_frame()
    comparativo['Previsao'] = forecast['CVLI']
    comparativo['Erro_Absoluto'] = (comparativo['CVLI'] - comparativo['Previsao']).abs()
    comparativo['Acerto_%'] = 100 - (comparativo['Erro_Absoluto'] / comparativo['CVLI'] * 100)
    print(comparativo)

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

