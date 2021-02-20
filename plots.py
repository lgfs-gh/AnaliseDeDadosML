import matplotlib.pyplot as plt
from numpy import mean

from gerador import GenDataFrame

# ----------------------------------- Gerando dataframes de teste ------------------------------------------------------
data = GenDataFrame().gerar()


# ----------------------------------- PLOTAGEM  ANO ESPECÍFICO ---------------------------------------------------------
def plot_ano_especifico(fonte: list, ano: int) -> None:
    """
    Plota o despache das fontes passadas como parâmetro por ano específico.

    ex: plot_ano_especifico(['Hidreletricas exclusive Itaipu', 'Itaipu'], 2019)

    ## Reduzir as repetições de código
    ## Reduzir a quantidade de variáveis
    ## Aumentar o escopo do método

    :param fonte: fontes passadas dentro de uma lista
    :param ano: ano presentado por um inteiro
    :return: None
    """

    # Fontes representadas por dicionário
    hidreletricas: dict = {'despache': [], 'mes': []}
    itaipu: dict = {'despache': [], 'mes': [], 'ano': []}
    oleo_diesel_combustivel: dict = {'despache': [], 'mes': []}
    gas_natural: dict = {'despache': [], 'mes': []}
    carvao: dict = {'despache': [], 'mes': []}
    eolica: dict = {'despache': [], 'mes': []}
    biomassa: dict = {'despache': [], 'mes': []}
    nuclear: dict = {'despache': [], 'mes': []}
    residuos: dict = {'despache': [], 'mes': []}
    energia_fora_sin: dict = {'despache': [], 'mes': []}

    legendas: list = []

    # Despache em um ano específico
    for row in data.iterrows():
        if row[1][0] == 'Hidreletricas exclusive Itaipu' and 'Hidreletricas exclusive Itaipu' in fonte:
            if row[1][3] == ano:
                hidreletricas['despache'].append(row[1][1])
                hidreletricas['mes'].append(row[1][2])
                plt.plot(hidreletricas['mes'], hidreletricas['despache'], c='darkcyan')
                if 'Hidreletricas exclusive Itaipu' in legendas:
                    pass
                else:
                    legendas.append(row[1][0])
        elif row[1][0] == 'Itaipu' and 'Itaipu' in fonte:
            if row[1][3] == ano:
                itaipu['despache'].append(row[1][1])
                itaipu['mes'].append(row[1][2])
                plt.plot(itaipu['mes'], itaipu['despache'], c='darkturquoise')
            if 'Itaipu' in legendas:
                pass
            else:
                legendas.append(row[1][0])
        elif row[1][0] == 'Oleo Diesel/Combustivel' and 'Oleo Diesel/Combustivel' in fonte:
            if row[1][3] == ano:
                oleo_diesel_combustivel['despache'].append(row[1][1])
                oleo_diesel_combustivel['mes'].append(row[1][2])
                plt.plot(oleo_diesel_combustivel['mes'], oleo_diesel_combustivel['despache'], c='darkgoldenrod')
            if 'Oleo Diesel/Combustivel' in legendas:
                pass
            else:
                legendas.append(row[1][0])
        elif row[1][0] == 'Gas Natural' and 'Gas Natural' in fonte:
            if row[1][3] == ano:
                gas_natural['despache'].append(row[1][1])
                gas_natural['mes'].append(row[1][2])
                plt.plot(gas_natural['mes'], gas_natural['despache'], c='lightgrey')
            if 'Gas Natural' in legendas:
                pass
            else:
                legendas.append(row[1][0])
        elif row[1][0] == 'Carvao' and 'Carvao' in fonte:
            if row[1][3] == ano:
                carvao['despache'].append(row[1][1])
                carvao['mes'].append(row[1][2])
                plt.plot(carvao['mes'], carvao['despache'], c='black')
            if 'Carvao' in legendas:
                pass
            else:
                legendas.append(row[1][0])
        elif row[1][0] == 'Eolicas' and 'Eolicas' in fonte:
            if row[1][3] == ano:
                eolica['despache'].append(row[1][1])
                eolica['mes'].append(row[1][2])
                plt.plot(eolica['mes'], eolica['despache'], c='powderblue')
            if 'Eolicas' in legendas:
                pass
            else:
                legendas.append(row[1][0])
        elif row[1][0] == 'Biomassas' and 'Biomassas' in fonte:
            if row[1][3] == ano:
                biomassa['despache'].append(row[1][1])
                biomassa['mes'].append(row[1][2])
                plt.plot(biomassa['mes'], biomassa['despache'], c='red')
            if 'Biomassas' in legendas:
                pass
            else:
                legendas.append(row[1][0])
        elif row[1][0] == 'Nuclear' and 'Nuclear' in fonte:
            if row[1][3] == ano:
                nuclear['despache'].append(row[1][1])
                nuclear['mes'].append(row[1][2])
                plt.plot(nuclear['mes'], nuclear['despache'], c='gold')
            if 'Nuclear' in legendas:
                pass
            else:
                legendas.append(row[1][0])
        elif row[1][0] == 'Residuos Processos Industriais' and 'Residuos Processos Industriais' in fonte:
            if row[1][3] == ano:
                nuclear['despache'].append(row[1][1])
                nuclear['mes'].append(row[1][2])
                plt.plot(residuos['mes'], residuos['despache'], c='lime')
            if 'Residuos Processos Industriais' in legendas:
                pass
            else:
                legendas.append(row[1][0])
        elif row[1][0] == 'Energia produzida fora do SIN' and 'Energia produzida fora do SIN' in fonte:
            if row[1][3] == ano:
                energia_fora_sin['despache'].append(row[1][1])
                energia_fora_sin['mes'].append(row[1][2])
                plt.plot(energia_fora_sin['mes'], energia_fora_sin['despache'], c='dimgrey')
            if 'Energia produzida fora do SIN' in legendas:
                pass
            else:
                legendas.append(row[1][0])

    plt.title(f'{fonte} | {ano}')
    plt.xlabel('Meses')
    plt.ylabel('Despache GWh')
    plt.legend(legendas)
    plt.show()


# --------------------------------- PLOTAGEM MÊS ESPECIFICO TODOS OS ANOS -----------------------------------------
def plot_mes_especifico(fonte: list, mes: int) -> None:
    """
    Plota o gráfico de despache do mês escolhido para as fontes passadas como parâmetro.

    ex: plot_mes_especifico(['Hidreletricas exclusive Itaipu', 'Itaipu'], 1)

    ## Reduzir as repetições de código
    ## Reduzir a quantidade de variáveis
    ## Aumentar o escopo do método

    :param fonte: lista de fontes
    :param mes: mês representado por um número inteiro
    :return: None
    """

    # Fontes representadas por dicionário
    hidreletricas: dict = {'despache': [], 'ano': []}
    itaipu: dict = {'despache': [], 'ano': []}
    oleo_diesel_combustivel: dict = {'despache': [], 'ano': []}
    gas_natural: dict = {'despache': [], 'ano': []}
    carvao: dict = {'despache': [], 'ano': []}
    eolica: dict = {'despache': [], 'ano': []}
    biomassa: dict = {'despache': [], 'ano': []}
    nuclear: dict = {'despache': [], 'ano': []}
    residuos: dict = {'despache': [], 'ano': []}
    energia_fora_sin: dict = {'despache': [], 'ano': []}

    legendas: list = []

    for row in data.iterrows():
        for i in row[1]:
            if i == 'Hidreletricas exclusive Itaipu' and 'Hidreletricas exclusive Itaipu' in fonte:
                if row[1][2] == mes:
                    hidreletricas['despache'].append(row[1][1])
                    hidreletricas['ano'].append(row[1][3])
                    plt.plot(hidreletricas['ano'], hidreletricas['despache'], c='darkcyan')
                    if 'Hidreletricas exclusive Itaipu' in legendas:
                        pass
                    else:
                        legendas.append(row[1][0])
            elif i == 'Itaipu' and 'Itaipu' in fonte:
                if row[1][2] == mes:
                    itaipu['despache'].append(row[1][1])
                    itaipu['ano'].append(row[1][3])
                    plt.plot(itaipu['ano'], itaipu['despache'], c='darkturquoise')
                    if 'Itaipu' in legendas:
                        pass
                    else:
                        legendas.append(row[1][0])
            elif i == 'Oleo Diesel/Combustivel' and 'Oleo Diesel/Combustivel' in fonte:
                if row[1][2] == mes:
                    oleo_diesel_combustivel['despache'].append(row[1][1])
                    oleo_diesel_combustivel['ano'].append(row[1][3])
                    plt.plot(oleo_diesel_combustivel['ano'], oleo_diesel_combustivel['despache'], c='darkgoldenrod')
                    plt.plot(itaipu['ano'], itaipu['despache'], c='blue')
                    if 'Oleo Diesel/Combustivel' in legendas:
                        pass
                    else:
                        legendas.append(row[1][0])
            elif i == 'Gas Natural' and 'Gas Natural' in fonte:
                if row[1][2] == mes:
                    gas_natural['despache'].append(row[1][1])
                    gas_natural['ano'].append(row[1][3])
                    plt.plot(gas_natural['ano'], gas_natural['despache'], c='lightgrey')
                    if 'Gas Natural' in legendas:
                        pass
                    else:
                        legendas.append(row[1][0])
            elif i == 'Carvao' and 'Carvao' in fonte:
                if row[1][2] == mes:
                    carvao['despache'].append(row[1][1])
                    carvao['ano'].append(row[1][3])
                    plt.plot(carvao['ano'], carvao['despache'], c='black')
                    if 'Carvao' in legendas:
                        pass
                    else:
                        legendas.append(row[1][0])
            elif i == 'Eolicas' and 'Eolicas' in fonte:
                if row[1][2] == mes:
                    eolica['despache'].append(row[1][1])
                    eolica['ano'].append(row[1][3])
                    plt.plot(eolica['ano'], eolica['despache'], c='powderblue')
                    if 'Eolicas' in legendas:
                        pass
                    else:
                        legendas.append(row[1][0])
            elif i == 'Biomassas' and 'Biomassas' in fonte:
                if row[1][2] == mes:
                    biomassa['despache'].append(row[1][1])
                    biomassa['ano'].append(row[1][3])
                    plt.plot(biomassa['ano'], biomassa['despache'], c='red')
                    if 'Biomassas' in legendas:
                        pass
                    else:
                        legendas.append(row[1][0])
            elif i == 'Nuclear' and 'Nuclear' in fonte:
                if row[1][2] == mes:
                    nuclear['despache'].append(row[1][1])
                    nuclear['ano'].append(row[1][3])
                    plt.plot(nuclear['ano'], nuclear['despache'], c='gold')
                    if 'Nuclear' in legendas:
                        pass
                    else:
                        legendas.append(row[1][0])
            elif i == 'Residuos Processos Industriais' and 'Residuos Processos Industriais' in fonte:
                if row[1][2] == mes:
                    nuclear['despache'].append(row[1][1])
                    nuclear['ano'].append(row[1][3])
                    plt.plot(residuos['ano'], residuos['despache'], c='lime')
                    if 'Residuos Processos Industriais' in legendas:
                        pass
                    else:
                        legendas.append(row[1][0])
            elif i == 'Energia produzida fora do SIN' and 'Energia produzida fora do SIN' in fonte:
                if row[1][2] == mes:
                    energia_fora_sin['despache'].append(row[1][1])
                    energia_fora_sin['ano'].append(row[1][3])
                    plt.plot(energia_fora_sin['ano'], energia_fora_sin['despache'], c='dimgrey')
                    if 'Energia produzida fora do SIN' in legendas:
                        pass
                    else:
                        legendas.append(row[1][0])

    plt.title(f'{fonte} | mês {mes} (todos os anos)')
    plt.xlabel('Anos')
    plt.ylabel('Despache GWh')
    plt.legend(legendas)
    plt.tight_layout()
    plt.show()


# ------------------------------------ PLOTAGEM TODOS OS ANOS MÉDIA  ----------------------------------------------
def plot_media_anos(fonte: list) -> None:
    """
    Plota um gráfico para visualização da média de despache de todos os anos para as fontes passadas
    como parâmetro.

    ex: plot_media_anos(['Hidreletricas exclusive Itaipu', 'Itaipu'])

    ## Reduzir as repetições de código
    ## Reduzir a quantidade de variáveis
    ## Aumentar o escopo do método

    :param fonte: lista contendo as fontes que o usuário deseja consultar
    :return: None
    """

    # Fontes representadas por dicionário
    hidreletricas: dict = {'media': []}
    itaipu: dict = {'media': []}
    oleo_diesel_combustivel: dict = {'media': []}
    gas_natural: dict = {'media': []}
    carvao: dict = {'media': []}
    eolica: dict = {'media': []}
    biomassa: dict = {'media': []}
    nuclear: dict = {'media': []}
    residuos: dict = {'media': []}
    energia_fora_sin: dict = {'media': []}

    legendas: list = []

    # Dicionário de armazenamento do valor da média por mês
    meses = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [],
             7: [], 8: [], 9: [], 10: [], 11: [], 12: []}

    # Quantidade de meses
    qnt_meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    def preencher_meses():  # ADICIONA OS DESPACHES POR MÊS
        if row[1][2] == 1:
            meses[1].append(row[1][1])
        if row[1][2] == 2:
            meses[2].append(row[1][1])
        if row[1][2] == 3:
            meses[3].append(row[1][1])
        if row[1][2] == 4:
            meses[4].append(row[1][1])
        if row[1][2] == 5:
            meses[5].append(row[1][1])
        if row[1][2] == 6:
            meses[6].append(row[1][1])
        if row[1][2] == 7:
            meses[7].append(row[1][1])
        if row[1][2] == 8:
            meses[8].append(row[1][1])
        if row[1][2] == 9:
            meses[9].append(row[1][1])
        if row[1][2] == 10:
            meses[10].append(row[1][1])
        if row[1][2] == 11:
            meses[11].append(row[1][1])
        if row[1][2] == 12:
            meses[12].append(row[1][1])

    # REDUZIR REPETIÇÃO DE CÓDIGO!
    if 'Hidreletricas exclusive Itaipu' in fonte:
        for row in data.iterrows():
            if row[1][0] == 'Hidreletricas exclusive Itaipu':
                if 'Hidreletricas exclusive Itaipu' in legendas:
                    pass
                else:
                    legendas.append(row[1][0])
                preencher_meses()
        for i in range(1, 13):
            hidreletricas['media'].append(mean(meses[i]))
            meses[i].clear()
        plt.plot(qnt_meses, hidreletricas['media'], c='darkcyan')

    if 'Itaipu' in fonte:
        for row in data.iterrows():
            if row[1][0] == 'Itaipu':
                if 'Itaipu' in legendas:
                    pass
                else:
                    legendas.append(row[1][0])
                preencher_meses()
        for i in range(1, 13):
            itaipu['media'].append(mean(meses[i]))
            meses[i].clear()
        plt.plot(qnt_meses, itaipu['media'], c='darkturquoise')

    if 'Oleo Diesel/Combustivel' in fonte:
        for row in data.iterrows():
            if row[1][0] == 'Oleo Diesel/Combustivel':
                if 'Oleo Diesel/Combustivel' in legendas:
                    pass
                else:
                    legendas.append(row[1][0])
                preencher_meses()
        for i in range(1, 13):
            oleo_diesel_combustivel['media'].append(mean(meses[i]))
            meses[i].clear()
        plt.plot(qnt_meses, oleo_diesel_combustivel['media'], c='darkgoldenrod')

    if 'Gas Natural' in fonte:
        for row in data.iterrows():
            if row[1][0] == 'Gas Natural':
                if 'Gas Natural' in legendas:
                    pass
                else:
                    legendas.append(row[1][0])
                preencher_meses()
        for i in range(1, 13):
            gas_natural['media'].append(mean(meses[i]))
            meses[i].clear()
        plt.plot(qnt_meses, gas_natural['media'], c='lightgrey')

    if 'Carvao' in fonte:
        for row in data.iterrows():
            if row[1][0] == 'Carvao':
                if 'Carvao' in legendas:
                    pass
                else:
                    legendas.append(row[1][0])
                preencher_meses()
        for i in range(1, 13):
            carvao['media'].append(mean(meses[i]))
            meses[i].clear()
        plt.plot(qnt_meses, carvao['media'], c='black')

    if 'Eolicas' in fonte:
        for row in data.iterrows():
            if row[1][0] == 'Eolicas' and 'Eolicas':
                if 'Eolicas' in legendas:
                    pass
                else:
                    legendas.append(row[1][0])
                preencher_meses()
        for i in range(1, 13):
            eolica['media'].append(mean(meses[i]))
            meses[i].clear()
        plt.plot(qnt_meses, eolica['media'], c='powderblue')

    if 'Biomassas' in fonte:
        for row in data.iterrows():
            if row[1][0] == 'Biomassas':
                if 'Biomassas' in legendas:
                    pass
                else:
                    legendas.append(row[1][0])
                preencher_meses()
        for i in range(1, 13):
            biomassa['media'].append(mean(meses[i]))
            meses[i].clear()
        plt.plot(qnt_meses, biomassa['media'], c='red')

    if 'Nuclear' in fonte:
        for row in data.iterrows():
            if row[1][0] == 'Nuclear':
                if 'Nuclear' in legendas:
                    pass
                else:
                    legendas.append(row[1][0])
                preencher_meses()
        for i in range(1, 13):
            nuclear['media'].append(mean(meses[i]))
            meses[i].clear()
        plt.plot(qnt_meses, nuclear['media'], c='gold')

    if 'Residuos Processos Industriais' in fonte:
        for row in data.iterrows():
            if row[1][0] == 'Residuos Processos Industriais':
                if 'Residuos Processos Industriais' in legendas:
                    pass
                else:
                    legendas.append(row[1][0])
                preencher_meses()
        for i in range(1, 13):
            residuos['media'].append(mean(meses[i]))
            meses[i].clear()
        plt.plot(qnt_meses, residuos['media'], c='lime')

    if 'Energia produzida fora do SIN' in fonte:
        for row in data.iterrows():
            if row[1][0] == 'Energia produzida fora do SIN':
                if 'Energia produzida fora do SIN' in legendas:
                    pass
                else:
                    legendas.append(row[1][0])
                preencher_meses()
        for i in range(1, 13):
            energia_fora_sin['media'].append(mean(meses[i]))
            meses[i].clear()
        plt.plot(qnt_meses, energia_fora_sin['media'], c='grey')

    plt.title(f'{fonte} | Média por mês de todos os anos')
    plt.xlabel('Meses')
    plt.ylabel('Despache GWh')
    plt.legend(legendas)
    plt.tight_layout()
    plt.show()
