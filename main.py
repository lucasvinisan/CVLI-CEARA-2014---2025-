from src.sarima import executar_sarima

import pandas as pd 

def executar():

    df = pd.read_csv("Dados/CVLI_PROCESSADO.csv", index_col=0, parse_dates=True)
    executar_sarima(df)

    #Posso colocar no final para executar_sarima retorna os dados previstos.
     
     

    
if __name__ == "__main__":
    executar()