import pandas as pd 
from src import plots as grafico 
from src import modelo as ms


def executar_sarima(df):

    # |------------ Análise Exploratória e Decomposição da Série Temporal ---------------| 
    grafico.plotar_graficos_serie(df)

    #Decomposição da Série temporal (Aditiva)
    grafico.decomposicao_aditivo(df)

    serie = df['CVLI']

    ms.testar_estacionariedade(serie)

    #d = 1 e D = 1 aplico a suavisação da seie (Dois são 1 se a série for estacionária)
    # |-----------------Implementando auto-arima -------------------------------------| 
    modelo = ms.treinar_modelo(serie)

    grafico.modelo_diagnostico(modelo)

    test, forecast = ms.validar_modelo_sarima(modelo, df)

    print(forecast)
   
    #validaçãp
    grafico.plotar_validacao(test, forecast, df)

    #Metircas (MAE, RMSE, MAPE)
    ms.calculando_metricas(test, forecast)

    # Criando a tabela de comparação
    #grafico.tabela_comparacao(test, forecast)

    resultado_teste_lb = ms.test_Ljung_Box(modelo)
    print(resultado_teste_lb) 

    # |------------------ Realizando as Previsões --------------------------------|

    previsao = ms.previsao_modelo(modelo, df)

    print(previsao)
    



