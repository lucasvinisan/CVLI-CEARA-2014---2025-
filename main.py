from src.Sarima.sarima import executar_sarima
from src.ExponentialSmoothing.exponential_Smoothing import executar_exponential_Smoothing
import pandas as pd 

def executar():

    df = pd.read_csv("Dados/CVLI_PROCESSADO.csv", index_col=0, parse_dates=True)
    #previsao_sarima = executar_sarima(df)
    
    #print(previsao_sarima)
    
    previsao_exponential_Smoothing = executar_exponential_Smoothing(df)

    print(previsao_exponential_Smoothing)

if __name__ == "__main__":
    executar()