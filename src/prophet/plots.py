
import matplotlib.pyplot as plt
import pandas as pd

#Definindo globalmente o style dos plots 
plt.style.use('grayscale') 

def plotar_previsao_2026(previsao_2026):
    fig, ax = plt.subplots(figsize=(12, 5))

    datas = pd.to_datetime(previsao_2026['ds'])

    ax.plot(datas, previsao_2026['yhat'], color='blue', marker='o', linewidth=1.5, label='Previsão')

    ax.fill_between(
        datas,
        previsao_2026['yhat_lower'],
        previsao_2026['yhat_upper'],
        alpha=0.2,
        color='blue',
        label='IC 95%'
    )

    for idx, row in previsao_2026.iterrows():  # ← dentro da função
        ax.annotate(
            f"{row['yhat']}\n[{row['yhat_lower']}–{row['yhat_upper']}]",
            xy=(pd.to_datetime(row['ds']), row['yhat']),
            xytext=(0, 14),
            textcoords='offset points',
            ha='center',
            fontsize=8,
            color='black'
        )

    ax.set_title('Previsão CVLI — Abril a Dezembro 2026', fontsize=14, fontweight='bold')
    ax.set_xlabel('Mês')
    ax.set_ylabel('CVLI')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
