import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
import numpy as np
from sklearn.impute import SimpleImputer


# ----------------- Tratamento de dados
db = pd.read_csv('GeracaoFonte.csv')
del db['dthProcessamento']
del db['ideGeracaoFonte']
imputer = SimpleImputer(missing_values=np.NaN, strategy='constant', fill_value=0)
imputer = imputer.fit(db[::])
db = imputer.transform(db[::])

# db[:, 0] = LabelEncoder().fit_transform(db[:, 0])
mes_input = 1
ano_input = 2010
fonte_input = 'Carvao'

# For só para o mês
print('------- INPUT DO MÊS ----------')
parametros = {'fonte': [], 'despache': [], 'mes': [], 'ano': []}
for i in db:
    if i[2] == mes_input:
        parametros['fonte'].append(i[0])
        parametros['despache'].append(i[1])
        parametros['mes'].append(i[2])
        parametros['ano'].append(i[3])
df = pd.DataFrame(parametros)
print(df)

print('------------------------------------------')

# For para ano e mês
print('------- INPUT DO ANO E MÊS ----------')
parametros = {'fonte': [], 'despache': [], 'mes': [], 'ano': []}
for i in db:
    if i[2] == mes_input and i[3] == ano_input:
        parametros['fonte'].append(i[0])
        parametros['despache'].append(i[1])
        parametros['mes'].append(i[2])
        parametros['ano'].append(i[3])
df = pd.DataFrame(parametros)
print(df)

print('------------------------------------------')

# For para o ano
print('------- INPUT DO ANO ----------')
parametros = {'fonte': [], 'despache': [], 'mes': [], 'ano': []}
for i in db:
    if i[3] == ano_input:
        parametros['fonte'].append(i[0])
        parametros['despache'].append(i[1])
        parametros['mes'].append(i[2])
        parametros['ano'].append(i[3])
df = pd.DataFrame(parametros)
print(df)

print('------------------------------------------')
# For para ano, mês e fonte de energia
print('------- INPUT DO ANO, MÊS E FONTE DE ENERGIA ----------')
parametros = {'fonte': [], 'despache': [], 'mes': [], 'ano': []}
for i in db:
    if i[0] == fonte_input and i[2] == mes_input and i[3] == ano_input:
        parametros['fonte'].append(i[0])
        parametros['despache'].append(i[1])
        parametros['mes'].append(i[2])
        parametros['ano'].append(i[3])
df = pd.DataFrame(parametros)
print(df)

print('------------------------------------------')
# For para ano e fonte de energia
print('------- INPUT DO ANO E FONTE DE ENERGIA ----------')
parametros = {'fonte': [], 'despache': [], 'mes': [], 'ano': []}
for i in db:
    if i[0] == fonte_input and i[3] == ano_input:
        parametros['fonte'].append(i[0])
        parametros['despache'].append(i[1])
        parametros['mes'].append(i[2])
        parametros['ano'].append(i[3])
df = pd.DataFrame(parametros)
print(df)

print('------------------------------------------')
# For para mês e fonte de energia
print('------- INPUT DO MÊS E FONTE DE ENERGIA ----------')
parametros = {'fonte': [], 'despache': [], 'mes': [], 'ano': []}
for i in db:
    if i[0] == fonte_input and i[2] == mes_input:
        parametros['fonte'].append(i[0])
        parametros['despache'].append(i[1])
        parametros['mes'].append(i[2])
        parametros['ano'].append(i[3])
df = pd.DataFrame(parametros)
print(df)

# For para mês e fonte de energia
print('------- INPUT DO MÊS E FONTE DE ENERGIA ----------')
parametros = {'fonte': [], 'despache': [], 'mes': [], 'ano': []}
for i in db:
    if i[0] == fonte_input and i[2] == mes_input:
        parametros['fonte'].append(i[0])
        parametros['despache'].append(i[1])
        parametros['mes'].append(i[2])
        parametros['ano'].append(i[3])
df = pd.DataFrame(parametros)
print(df)
print(f"Fonte: {fonte_input}\n"
      f"Média do mês {mes_input} (todos os anos): {np.mean(parametros['despache'])}")

# For para ano e fonte de energia
print('------- INPUT DO ANO E FONTE DE ENERGIA ----------')
parametros = {'fonte': [], 'despache': [], 'mes': [], 'ano': []}
for i in db:
    if i[0] == fonte_input and i[3] == ano_input:
        parametros['fonte'].append(i[0])
        parametros['despache'].append(i[1])
        parametros['mes'].append(i[2])
        parametros['ano'].append(i[3])
df = pd.DataFrame(parametros)
print(df)
print(f"Fonte: {fonte_input}\n"
      f"Média do ano {ano_input} (todos os meses): {np.mean(parametros['despache'])}")

# For para fonte de energia
print('------- INPUT FONTE DE ENERGIA ----------')
parametros = {'fonte': [], 'despache': [], 'mes': [], 'ano': []}
for i in db:
    if i[0] == fonte_input:
        parametros['fonte'].append(i[0])
        parametros['despache'].append(i[1])
        parametros['mes'].append(i[2])
        parametros['ano'].append(i[3])
df = pd.DataFrame(parametros)
print(df)
print(f"Fonte: {fonte_input}\n"
      f"Média de todos os anos e meses: {np.mean(parametros['despache'])}")



if __name__ == '__main__':
    print('end')
