import pandas as pd 

df_sarima = pd.read_csv("outputs/previsao_sarima")
df_exponential_smoothing = pd.read_csv("outputs/previsao_exponential_smoothing")
df_prophet_modifcado= pd.read_csv("outputs/previsao_prophet")


print('Sarima')
print(df_sarima)
print(df_sarima['lower'].sum())
print(df_sarima['upper'].sum())




print('Exponential Smoothing')
print(df_exponential_smoothing)
print(df_exponential_smoothing['lower'].sum())
print(df_exponential_smoothing['upper'].sum())


print('Prophet')
print(df_prophet_modifcado)
print(df_prophet_modifcado['yhat'].sum())
print(df_prophet_modifcado['yhat_lower'].sum())
print(df_prophet_modifcado['yhat_upper'].sum())
