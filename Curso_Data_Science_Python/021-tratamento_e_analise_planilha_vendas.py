# 1. Importe a Vendas_Incorreto
 # 2. Trate todos os dados incorretos
  # 3. Analise estatisticamente o arquivo
   # Exporte o arquivo

import pandas as pd
from tabulate import tabulate

# 1. Importação da planilha 'Vendas_Incorreto'
data_frame = pd.read_excel("Vendas_Incorreto.xlsx")

# 2. Tramento de dados - Exclui linhas e colunas vazias
data_frame.dropna(thresh=1, inplace=True) # Remove todas as linhas que só têm valores nulos.
data_frame.dropna(axis=1, inplace=True) # Remove todas as colunas que só têm valores nulos.
#'inplace=True' -> Altera na base de dados original.

# 3. Analise do arquivo
print(data_frame.head()) # Mostra as 5 primeiras linhas
print(data_frame.tail()) # Mostra as ultimas 5 linhas
print('-' * 50)
print(data_frame.info()) # Visão geral/resumo da tabela
print('-' * 50)
print(data_frame.describe()) # Pega cada uma das colunas e mostra dados/analises estátisticas


# 1. Vendas totais por vendedor: identificar quem vende mais.
data_frame_consolidado = data_frame[['Total', 'Vendedor']].groupby(['Vendedor']).sum()
print(tabulate(data_frame_consolidado.sort_values('Total', ascending=False),headers='keys', tablefmt='fancy_grid'))

# 2. Lucro bruto por produto: Analisando preços e quantidades.
print('-'*50)
print()
print('Lucro por produto: ')
data_frame['Lucro'] = data_frame['Total'] - data_frame['Preço de Compra']
data_frame_consolidado = data_frame[['Lucro', 'Produto']].groupby(['Produto']).sum()
print(tabulate(data_frame_consolidado.sort_values('Lucro', ascending=False),headers='keys', tablefmt='fancy_grid'))

# 3. Tempo médio entre pedido e entrega: eficiência logística.
print('-'*50)
print()
print('Tempo médio entre pedido e entrega -> Eficiência logística: ')
data_frame['Data Envio'] = pd.to_datetime(data_frame['Data Envio']) # Converte a coluna 'Data Envio' de texto (string)
# ou outro formato para o tipo datetime.
data_frame['Data Entrega'] = pd.to_datetime(data_frame['Data Entrega']) # Converte a coluna 'Data Entrega' de texto (string)
# ou outro formato para o tipo datetime.
data_frame['Tempo de Entrega'] = (data_frame['Data Entrega'] - data_frame['Data Envio']).dt.days
#.dt.days pega só o número de dias inteiros dessa diferença.

# Cálculo da média de tempo de entrega
tempo_medio = round(data_frame[['Tempo de Entrega', 'Loja']].groupby('Loja').mean(),2)

# Apresentação formatada
print(tabulate(tempo_medio.sort_values('Tempo de Entrega', ascending=False),
               headers='keys', tablefmt='fancy_grid'))

# 4. Análise de devoluções: qual produto ou loja tem mais problemas.
print('-'*50)
print()
print('Devoluções por produto: ')
print(data_frame[['Quantidade', 'Produto', 'Devolucao']].groupby(['Produto', 'Devolucao']).sum())

# 5. Distribuição de vendas por país.
print('-'*50)
print()
print('Distribuição de vendas por país: ')
data_frame_consolidado = data_frame[['Total', 'País']].groupby('País').sum()
print(tabulate(data_frame_consolidado.sort_values('Total', ascending=False),headers='keys', tablefmt='fancy_grid'))



