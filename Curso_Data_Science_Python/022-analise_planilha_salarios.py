# Crie um programa que:
    # 1. Importe a biblioteca pandas como pd
    # 2. Leia um DataFrame “Salarios.csv” e nomei-o de data_frame
    # 3. Retorne o head do DataFrame
    # 4. Use o método .info(), para descobrir quantas entradas ele tem
    # 5. Qual é a média de Pagamento Base?
    # 6. Qual é o maior montante pago em OvertimePay?
    # 7. Qual é a profissão do ‘JOSEPH DRISCOLL’
    # 8. Qual o nome da pessoa mais bem paga
    # 9. Qual é a media de pagamento base por ano? #Caso não esteja disponivel, crie a coluna
    # 10. Quantas profissoes únicas existem?
    # 10.1 Exporte o arquivo

# 1. Importação da biblioteca pandas
import pandas as pd

# 2. Leitura e nomeação de um DataFrame “Salarios.csv”
data_frame = pd.read_csv('Salarios.csv')

# 3. Head do DataFrame
print('Head do DataFrame: ')
print(data_frame.head())

# 4. Info no DataFrame
print('-' * 50)
print()
print('Info no DataFrame: ')
print(data_frame.info())

# 5. A média de Pagamento Base
print('-' * 50)
print()
print('Média de Pagamento Base: ')
print(f'R$ {round(data_frame['BasePay'].mean(),2)}')

# 6. Maior montante pago em OvertimePay (Horas Extras):
print('-' * 50)
print()
print('Maior valor de OvertimePay/Horas Extras:')
print(f'R$ {(data_frame['OvertimePay'].max())}')

# 7. Qual é a profissão do ‘JOSEPH DRISCOLL’ -> Filtrando uma coluna pela outra.
print('-' * 50)
print()
print('Profissão do JOSEPH DRISCOL:')
print(data_frame[data_frame['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'].values[0])

#data_frame['EmployeeName'] == 'JOSEPH DRISCOLL'
#Passo 1: Acha as linhas onde EmployeeName é “JOSEPH DRISCOLL”, faz um verdadeiro/falso, onde só JOSEPH é true.

#data_frame[data_frame['EmployeeName'] == 'JOSEPH DRISCOLL']
#Passo 2: Isso mostra só as linhas onde a condição era True, no caso só a linha do JOSEPH.

# data_frame[data_frame['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']
#Passo 3: Pegue só a coluna “JobTitle” dessa linha

# data_frame[data_frame['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'].values[0]
#Passo 4: Pegue só o texto “CAPTAIN, FIRE” e não o 'dtype: object'

# 8. Nome da pessoa mais bem paga
print('-' * 50)
print()
print('Pessoa com maior contigente salarial: ')
print(data_frame[data_frame['TotalPayBenefits'] == data_frame['TotalPayBenefits'].max()][['EmployeeName','TotalPayBenefits']].values[0])
print(data_frame['EmployeeName'][data_frame['TotalPay'] == data_frame['TotalPay'].max()])

# data_frame['TotalPayBenefits'].max() -> Me diz qual o maior valor
# data_frame[data_frame['TotalPayBenefits'] == data_frame['TotalPayBenefits'].max()] -> Faz um filtro para pegar a única
#linha em que o max() calculado é TRUE. Que é a linha do Nathaniel

# 9. Média de pagamento base por ano -> 'Por' sinal de GroupBy
print('-' * 50)
print()
print('Média de pagamento base por ano: ')
data_frame_consolidado = data_frame[['TotalPayBenefits', 'Year']].groupby(['Year']).mean().sort_values('Year', ascending=True)
print(f'R${round(data_frame_consolidado, 2)}')

# 10. Quantas profissoes únicas existem?
print('-' * 50)
print()
print('Quantidade de profissões únicas: ')
print(data_frame['JobTitle'].nunique())
print(data_frame['JobTitle'].unique())

data_frame.to_csv('Salarios_revisada.csv')
