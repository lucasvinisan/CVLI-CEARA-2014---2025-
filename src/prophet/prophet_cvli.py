import pandas as pd 
from prophet import Prophet
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

from src.prophet import modelo as md
from src.prophet import plots as grafico


def executar_prophet(df):
    
    new_df = md.preparar_df(df) #Apenas modificando as colunas para implementar o prophet 

    new_df = new_df[(new_df['ds'] <= '2017-01-01') | (new_df['ds'] >= '2020-01-01') ] 
    #Le em consideração esse cenário e sem ele 

    #validação
    modelo, test = md.treinando_modelo(new_df) # Treinando modelo com dados de teste
    forecast_validacao = md.validacao_modelo(modelo, test)

    md.metricas(test, forecast_validacao)
    fig = modelo.plot(forecast_validacao)
    plt.show()

    #Modelo Final 
    modelo_final = md.modelo_final(new_df)

    future = modelo_final.make_future_dataframe(periods=9, freq='MS')  # gera datas futuras
    forecast_2026 = modelo_final.predict(future)

    previsao = md.previsao_2026(forecast_2026)

    grafico.plotar_previsao_2026(previsao)

    md.aplicando_cross_validation(modelo_final)

    return previsao 



'''

Verificar vario modelos

    from prophet.diagnostics import cross_validation, performance_metrics

    for cps in [0.10, 0.15, 0.20, 0.25, 0.30]:
        m = Prophet(
            seasonality_mode='multiplicative',
           interval_width=0.95,
           changepoint_prior_scale=cps,
            weekly_seasonality=False,
            daily_seasonality=False
        )
        m.fit(new_df)  # usa o dataframe completo
        df_cv = cross_validation(m, initial='1095 days', period='180 days', horizon='48 days')
       df_p = performance_metrics(df_cv)
       print(f"cps={cps:.2f} | MAPE={df_p['mape'].mean():.4f} | Coverage={df_p['coverage'].mean():.3f}")
    
  '''