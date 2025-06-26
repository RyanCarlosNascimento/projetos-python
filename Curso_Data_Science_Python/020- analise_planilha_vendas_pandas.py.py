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

# Importação das bibliotecas
import pandas as pd
from tabulate import tabulate

# Importação do arquivo Excel
data_frame = pd.read_excel('Base Aula 002 - Exemplo .xlsx')

print(data_frame) # -> Mostra Head e Tail.
print(data_frame.info()) # Visão geral/resumo da tabela
print(data_frame.describe()) # Estatísticas descritivas das colunas

#2.1
print('-------------------------------------------------------')
print('Países com mais vendas: ')
print(tabulate(data_frame[['País', 'Total']].groupby('País').sum().sort_values('Total', ascending=False),headers='keys',tablefmt='fancy_grid'))
#print(data_frame[['País', 'Total']].groupby('País').sum().sort_values('Total', ascending = False)) #Usa país como categórica, soma e calcula o total para cada país
# E somente assim eu posso usar sort_values.


#2.2 O melhor vendedor -> Discutir com o cliente o que ele quer/o que considera importante.
print('-------------------------------------------------------')
print('Dados para melhor Vendedor: ')
data_frame['Lucro'] = data_frame['Total'] - data_frame['Preço de Compra']
print(tabulate(data_frame[['Lucro', 'Quantidade', 'Desconto', 'Vendedor', 'Produto']].groupby(['Produto', 'Vendedor']).sum().sort_values('Lucro', ascending = False),headers='keys',tablefmt='fancy_grid'))
print('-------------------------------------------------------')
print(tabulate(data_frame[['Vendedor', 'Total', 'Quantidade']].groupby('Vendedor').agg(['mean','sum']),headers='keys',tablefmt='fancy_grid'))


#2.3 O melhor tipo de loja
print('-------------------------------------------------------')
print('Dados para melhor Loja: ')

# Mostrar todas as colunas
pd.set_option('display.max_columns', None)

# Mostrar todas as linhas (se necessário)
pd.set_option('display.max_rows', None)

# Impedir truncamento de largura
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

data_frame['Data Envio'] = pd.to_datetime(data_frame['Data Envio']) #Converte para o tipo DATA
data_frame['Data Entrega'] = pd.to_datetime(data_frame['Data Entrega']) #Converte para o tipo DATA
data_frame['Tempo de Entrega'] = data_frame['Data Entrega'] - data_frame['Data Envio']
data_frame_consolidado = data_frame[['Lucro', 'Quantidade', 'Desconto', 'Loja', 'Devolucao','Tempo de Entrega']].groupby(['Devolucao', 'Loja']).sum()
print(tabulate(data_frame_consolidado.sort_values(('Lucro', ascending=False),headers='keys',tablefmt='fancy_grid'))) @@

print()
print('-------------------------------------------------------')
print('Quantidade de devoluções por loja: ')
print(tabulate([['Loja','Devolucao']].groupby(['Loja']).count(),headers='keys',tablefmt='fancy_grid'))

print()
print('-------------------------------------------------------')
data_frame_consolidado = data_frame[['Loja', 'Total', 'Quantidade', 'Produto']].groupby(['Loja','Produto']).agg(['max','sum'])
print(tabulate(data_frame_consolidado.sort_values(('Quantidade', 'sum'),headers='keys',tablefmt='fancy_grid')))

# 2.4 - Qual é o tipo de envio mais usado
print('-----------------------------------------')
print('Tipo de envio mais utilizado: ')
data_frame_consolidado = data_frame[['Tipo de Envio', 'Quantidade', 'Peso']].groupby('Tipo de Envio').agg(['mean','sum'])
print(tabulate(data_frame_consolidado.sort_values(('Quantidade', 'sum'),headers='keys',tablefmt='fancy_grid')))
#Aqui preciso considerar a quantidade vendida e o peso, não só a quantidade de vezes que aparece, pq uma venda

# 2.5 - Qual o público que mais atendemos (Gênero)
print('-----------------------------------------')
print('Gênero mais atendido: ')
data_frame_consolidado1 = data_frame[['Gênero','Total','Quantidade']].groupby('Gênero').agg(['mean','sum'])
print(tabulate(data_frame_consolidado1.sort_values(('Quantidade','sum'),headers='keys',tablefmt='fancy_grid')))
#Não é só quantas vezes atendemos, mas como atendemos, como foi essa venda.

# 2.6 - Quem fez as 3 maiores vendas
print('----(-------------------------------------')
print('Top 3 maiores vendas (R$): ')
print(tabulate(data_frame[['Vededor', 'Total']].sort_values('Total', ascending=False).head(3),headers='keys',tablefmt='fancy_grid'))
print(tabulate(data_frame[['Vededor', 'Quantidade']].sort_values('Quantidade', ascending=False).head(3),headers='keys',tablefmt='fancy_grid'))


# 2.7 - Adicione uma nova coluna comissão (Total * 5%)
print('-----------------------------------------')
print('Comissão (5%): ')
comissao = data_frame['Comissão'] = data_frame['Total'] * 1.05
print(tabulate(round(data_frame[['Vendedor','Comissão']].groupby(['Vendedor']).sum().sort_values('Comissão', ascending=False),2),headers='keys',tablefmt='fancy_grid'))