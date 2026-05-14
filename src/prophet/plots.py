
import matplotlib.pyplot as plt

#Definindo globalmente o style dos plots 
plt.style.use('grayscale') 

def ploat_previsao_2026(previsao_2026):
    

    fig, ax = plt.subplots(figsize=(10, 5))
    
    ax.plot(previsao_2026['ds'], previsao_2026['yhat'], 
            color='blue', marker='o', label='Previsão')
    
    ax.fill_between(previsao_2026['ds'], 
                    previsao_2026['yhat_lower'], 
                    previsao_2026['yhat_upper'], 
                    alpha=0.3, color='blue', label='Intervalo de confiança')

    ax.set_title('Previsão CVLI — Abril a Dezembro 2026')
    ax.set_xlabel('MES')
    ax.set_ylabel('CVLI')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    return previsao_2026
