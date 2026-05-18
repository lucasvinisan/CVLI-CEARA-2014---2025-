from src.sarima.sarima import executar_sarima
from src.exponential_smoothing.exponential_smoothing import executar_exponential_smoothing
from src.prophet.prophet_cvli import executar_prophet
import pandas as pd 
import joblib 
import webbrowser
import os

def executar():

    
    #Caregando Dados
    df = pd.read_csv("dados/cvli_processados.csv", index_col=0, parse_dates=True)

    
    # |----- Aplicando modelos estatísticos -------|

    # Modelo exponential smoothing     
    previsao_exponential_smoothing = executar_exponential_smoothing(df)

    #Modelo Sarima
    previsao_sarima = executar_sarima(df)

    #Modelo prophet
    previsao_prophet = executar_prophet(df)
    
    
    # |-------- Salvando modelo geradas em arquivo do tipo .joblib -----------|
    
    # Modelo sarima
    joblib.dump(previsao_sarima, 'models/modelo_sarima.joblib')
    
    # Modelo Exponential Smoothing
    joblib.dump(previsao_exponential_smoothing, 'models/modelo_exponential_smoothing.joblib')
   
    # Modelo prophet 
    joblib.dump(previsao_prophet, 'models/modelo_previsao_prophet.joblib')
   
    
    # |-------- Salvando previsões geradas em arquivo do tipo .csv-----------|
    
    # Modelo Exponential Smoothing 
    previsao_exponential_smoothing.to_csv('outputs/previsao_exponential_smoothing', index=False)
    
    # Modelo prophet 
    previsao_prophet.to_csv('outputs/previsao_prophet', index=False)
    
    # Modelo SARIMA
    previsao_sarima.to_csv('outputs/previsao_sarima', index=False)


def abrir_dashboard():
    caminho_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_html = os.path.join(caminho_atual, 'index.html')
    
    if os.path.exists(caminho_html):
        url = 'file://' + os.path.realpath(caminho_html)
        webbrowser.open(url)
    else:
        print(f"Erro: O arquivo {caminho_html} não foi encontrado.")
    
if __name__ == "__main__":
    #executar()
    abrir_dashboard()