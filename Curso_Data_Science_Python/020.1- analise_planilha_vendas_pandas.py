# 1.Importe a Base Aula 002 - Exemplo.xlsx
# 2. Encontre a Informação
    # 2.1 - Qual país vendeu mais(Total)?
    # 2.2 - Qual o melhor vendedor? -> O que é MELHOR? O cliente define (MELHOR COMO?)
    # 2.3 - Qual o melhor tipo de loja? # Posso usar X² e Pearson.
    # 2.4 - Qual é o tipo de envio mais usado?
    # 2.5 - Qual o público que mais atendemos (Gênero)?
    # 2.6 - Quem fez as 3 maiores vendas?
    # 2.7 - Adicione uma nova coluna comissão (Total * 5%)
# Exporte o arquivo

import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import seaborn as sns

data_frame = pd.read_excel('Base Aula 002 - Exemplo .xlsx')

print(data_frame) # -> Mostra Head e Tail.
print(data_frame.info()) # Visão geral/resumo da tabela (POSIÇÃO, COLUNA, SE TEM VAZIOS OU NÃO E TIPO)
print(data_frame.describe()) # Pega cada uma das colunas e mostra A CONTAGEM DE VALORES, MÉDIA, MODA, MEDIANA, 1°,2°,3° e 4° Quartil

#2.1
print('-------------------------------------------------------')
print('Países com mais vendas: ')
print(data_frame[['País', 'Total']].groupby('País').sum().sort_values('Total')) #Uso país como categórica, somo e calculo o total para cada país
# E somente assim eu posso usar sort_values.


#2.2 O melhor vendedor
print('-------------------------------------------------------')
data_frame['Lucro'] = data_frame['Total'] - data_frame['Preço de Compra']
print(data_frame[['Lucro', 'Quantidade', 'Desconto', 'Vendedor', 'Produto']].groupby(['Produto', 'Vendedor']).sum().sort_values('Lucro', ascending = False))


#2.3 O melhor tipo de loja
print('-------------------------------------------------------')

# Mostrar todas as colunas
pd.set_option('display.max_columns', None)

# Mostrar todas as linhas (se necessário)
pd.set_option('display.max_rows', None)

# Impedir truncamento de largura
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

'''
data_frame['Data Envio'] = pd.to_datetime(data_frame['Data Envio']) #Converte para o tipo DATA
data_frame['Data Entrega'] = pd.to_datetime(data_frame['Data Entrega']) #Converte para o tipo DATA
data_frame['Tempo de Entrega'] = data_frame['Data Entrega'] - data_frame['Data Envio']
print(data_frame[['Lucro', 'Quantidade', 'Desconto', 'Produto', 'Loja', 'Devolucao','Tempo de Entrega' ]].groupby(['Loja', 'Produto', 'Devolucao']).sum().sort_values('Lucro', ascending = False))
'''
data_frame['Data Envio'] = pd.to_datetime(data_frame['Data Envio']) #Converte para o tipo DATA
data_frame['Data Entrega'] = pd.to_datetime(data_frame['Data Entrega']) #Converte para o tipo DATA
data_frame['Tempo de Entrega'] = data_frame['Data Entrega'] - data_frame['Data Envio']
#print(data_frame[['Lucro', 'Quantidade', 'Desconto', 'Loja', 'Sem_Devolucoes','Tempo de Entrega' ]].groupby(['Loja']).sum().sort_values('Lucro', ascending = False))

print(data_frame[['Lucro', 'Quantidade', 'Desconto', 'Loja', 'Devolucao','Tempo de Entrega' ]].groupby(['Devolucao', 'Loja']).sum().sort_values('Lucro', ascending = False))

print(data_frame[['Loja', 'Devolucao' ]].groupby(['Loja']).count())

'''
df_limpo = data_frame[['Loja', 'Devolucao' ]].groupby(['Loja']).count()
sns.barplot(df_limpo, df_limpo['Loja'],  df_limpo.values)
plt.show()
'''

# 2.4 - Qual é o tipo de envio mais usado
print('-----------------------------------------')
print('Tipo de envio mais utilizado: ')
print(data_frame['Tipo de Envio'].value_counts())

# 2.5 - Qual o público que mais atendemos (Gênero)
print('-----------------------------------------')
print('Público que mais atendemos: ')
print(data_frame['Gênero'].value_counts())

# 2.6 - Quem fez as 3 maiores vendas

# 2.7 - Adicione uma nova coluna comissão (Total * 5%)