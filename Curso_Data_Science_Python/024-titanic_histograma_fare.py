import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data_frame = pd.read_csv('Titanic-Dataset.csv')

#25 - Histograma Métrico - Não comparo com uma variavel categórica, apenas com métricas
sns.histplot(x = 'Fare', data = data_frame, bins=30, color='red')
plt.title("📈 Distribuição do Total da Conta")
plt.show()

#Eixo X -> Valor/Intervalo de gastos das pessoas.
#Eixo Y -> Frêquencia, quantas vezes o gasto do eixo X aconteceu
#No gráfico percebe-se que MTS pessoas (1°classe) gastaram pouco para estar lá, já que quase 800 pessoas ficaram no intervalo de 15-25
#Enquanto a 2° e 3° classe que gastou um valor maior com passagens, foi em uma quantidade mt menor

