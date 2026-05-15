import pandas as pd 
from prophet import Prophet
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

from prophet.diagnostics import cross_validation, performance_metrics

def preparar_df(df):
    df_prophet = df[['CVLI']].copy().reset_index()
    df_prophet = df_prophet.rename(columns={'MES': 'ds', 'CVLI': 'y'})
    return df_prophet
#Tem que modificar as colunas pois o prophet só reconhece ds e y 


def treinando_modelo(df_prophet): 
    # Divisão treino/teste
    train = df_prophet[df_prophet['ds'] < '2024-01-01']
    test  = df_prophet[df_prophet['ds'] >= '2024-01-01']
    
    # Treinar só com dados de treino
    m = Prophet(
        seasonality_mode='multiplicative',
        interval_width=0.95,
        weekly_seasonality=False,
        daily_seasonality=False,
        changepoint_prior_scale=0.15,
       #changepoint_prior_scale=0.5 aplicando com intervalo é 2021 para frente 
    )
    m.add_country_holidays(country_name='BR') #Adicionando feriados do Brasil 
    m.fit(train)

    return m, test

def modelo_final(df_prophet): 
    
    m = Prophet(
        seasonality_mode='multiplicative',
        interval_width=0.95,
        weekly_seasonality=False,
        daily_seasonality=False,
        changepoint_prior_scale=0.15, 

    )
    m.add_country_holidays(country_name='BR') 
    
    m.fit(df_prophet)

    return m

def validacao_modelo(modelo, test):
    
    future = modelo.make_future_dataframe(periods=len(test), freq='MS')
    
    forecast_test = modelo.predict(future)

    return forecast_test

def metricas(test, forecast_test):

    # Métricas
    real = test['y'].values
    previsto = forecast_test.set_index('ds').loc[test['ds'], 'yhat'].values

    mae  = mean_absolute_error(real, previsto)
    rmse = np.sqrt(mean_squared_error(real, previsto))
    mape = np.mean(np.abs((real - previsto) / real)) * 100

    print(f"MAE:  {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"MAPE: {mape:.2f}%")
    print(f"Acurácia: {100 - mape:.2f}%")


def previsao_2026(forecast):
    

    previsao_2026 = forecast[
        (forecast['ds'] >= '2026-04-01') & 
        (forecast['ds'] <= '2026-12-01')
    ][['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

    previsao_2026 = previsao_2026.copy()
    previsao_2026['yhat']  = previsao_2026['yhat'].astype(int)
    previsao_2026['yhat_lower'] = previsao_2026['yhat_lower'].astype(int)
    previsao_2026['yhat_upper'] = previsao_2026['yhat_upper'].astype(int)

    return previsao_2026



def aplicando_cross_validation(modelo_final): 

    df_cv = cross_validation(modelo_final, initial='730 days', period='180 days', horizon='365 days')
    df_p = performance_metrics(df_cv)
    print(df_p.head())