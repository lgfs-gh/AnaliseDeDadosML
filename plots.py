import matplotlib.pyplot as plt
from gerador import GenDataFrame

data_base = GenDataFrame().gerar()
data = GenDataFrame(fonte='Eolicas', mes=10).gerar()
data2 = GenDataFrame(fonte='Carvao', ano=2015).gerar()


def plotar_fonte_mes_especifico(database):
    nome = []
    despache = []
    mes = []
    ano = []

    for row in database.iterrows():
        nome.append(row[1][0])
        despache.append(row[1][1])
        mes.append(row[1][2])
        ano.append(row[1][3])

    plt.plot(ano, despache)
    plt.title(f'{nome[0]} | Despache do mês {mes[0]} (por ano)')
    plt.xlabel('Anos')
    plt.ylabel('Despache GWh')
    plt.savefig('plot_mes_especifico_todos_anos')


def plotar_fonte_ano_especifico(database):
    nome = []
    despache = []
    mes = []
    ano = []

    for row in database.iterrows():
        nome.append(row[1][0])
        despache.append(row[1][1])
        mes.append(row[1][2])
        ano.append(row[1][3])

    plt.plot(mes, despache)
    plt.title(f'{nome[0]} | Despache do ano {ano[0]}')
    plt.xlabel('Meses')
    plt.ylabel('Despache GWh')
    plt.savefig('plot_ano_especifico_todos_meses')


def plotar_mes_especifico(database):
    nome = []
    despache = []
    mes = []
    ano = []

    for row in database.iterrows():
        nome.append(row[1][0])
        despache.append(row[1][1])
        mes.append(row[1][2])
        ano.append(row[1][3])

    plt.plot(ano, despache)
    plt.title(f'{nome[0]} | Despache do mês {mes[0]} (por ano)')
    plt.xlabel('Anos')
    plt.ylabel('Despache GWh')
    plt.savefig('plot_mes_especifico_todos_anos')
