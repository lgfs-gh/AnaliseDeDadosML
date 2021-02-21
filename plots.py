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

    # Lista de Legendas
    legendas: list = []

    # Despache em um ano específico
    # ------------------------ Hidreletricas exclusive Itaipu ------------------------ #
    # Itera nas linhas da database
    for row in data.iterrows():
        # Checa (em row[1][0])o nome da fonte e checa se essa fonte foi passada como parâmetro
        if row[1][0] == 'Hidreletricas exclusive Itaipu' \
                and 'Hidreletricas exclusive Itaipu' in fonte:
            # Se sim, checa (em row[1][3]) se o valor é correspondente ao passado como parâmetro
            if row[1][3] == ano:
                # Adiciona ao respectivo dicionário os valores de despache e meses
                hidreletricas['despache'].append(row[1][1])
                hidreletricas['mes'].append(row[1][2])
                # Adiciona ao plot despache/mes
                plt.plot(hidreletricas['mes'], hidreletricas['despache'], c='darkcyan')
            # Checa se a fonte está nas legendas
            if 'Hidreletricas exclusive Itaipu' in legendas:
                pass
            else:
                legendas.append(row[1][0])

        # ------------------------ Itaipu ------------------------ #
        # Checa (em row[1][0])o nome da fonte e checa se essa fonte foi passada como parâmetro
        elif row[1][0] == 'Itaipu' and 'Itaipu' in fonte:
            # Se sim, checa (em row[1][3]) se o valor é correspondente ao passado como parâmetro
            if row[1][3] == ano:
                # Adiciona ao respectivo dicionário os valores de despache e meses
                itaipu['despache'].append(row[1][1])
                itaipu['mes'].append(row[1][2])
                # Adiciona ao plot despache/mes
                plt.plot(itaipu['mes'], itaipu['despache'], c='darkturquoise')
            # Checa se a fonte está nas legendas
            if 'Itaipu' in legendas:
                pass
            else:
                legendas.append(row[1][0])

        # ------------------------ Oleo Disel / Combustivel ------------------------ #
        # Checa (em row[1][0])o nome da fonte e checa se essa fonte foi passada como parâmetro
        elif row[1][0] == 'Oleo Diesel / Combustivel' and 'Oleo Diesel / Combustivel' in fonte:
            # Se sim, checa (em row[1][3]) se o valor é correspondente ao passado como parâmetro
            if row[1][3] == ano:
                # Adiciona ao respectivo dicionário os valores de despache e meses
                oleo_diesel_combustivel['despache'].append(row[1][1])
                oleo_diesel_combustivel['mes'].append(row[1][2])
                # Adiciona ao plot despache/mes
                plt.plot(oleo_diesel_combustivel['mes'], oleo_diesel_combustivel['despache'], c='darkgoldenrod')
            # Checa se a fonte está nas legendas
            if 'Oleo Diesel / Combustivel' in legendas:
                pass
            else:
                legendas.append(row[1][0])

        # ------------------------ Gas Natural ------------------------ #
        # Checa (em row[1][0])o nome da fonte e checa se essa fonte foi passada como parâmetro
        elif row[1][0] == 'Gas Natural' and 'Gas Natural' in fonte:
            # Se sim, checa (em row[1][3]) se o valor é correspondente ao passado como parâmetro
            if row[1][3] == ano:
                # Adiciona ao respectivo dicionário os valores de despache e meses
                gas_natural['despache'].append(row[1][1])
                gas_natural['mes'].append(row[1][2])
                # Adiciona ao plot despache/mes
                plt.plot(gas_natural['mes'], gas_natural['despache'], c='lightgrey')
            # Checa se a fonte está nas legendas
            if 'Gas Natural' in legendas:
                pass
            else:
                legendas.append(row[1][0])

        # ------------------------ Carvao ------------------------ #
        # Checa (em row[1][0])o nome da fonte e checa se essa fonte foi passada como parâmetro
        elif row[1][0] == 'Carvao' and 'Carvao' in fonte:
            # Se sim, checa (em row[1][3]) se o valor é correspondente ao passado como parâmetro
            if row[1][3] == ano:
                # Adiciona ao respectivo dicionário os valores de despache e meses
                carvao['despache'].append(row[1][1])
                carvao['mes'].append(row[1][2])
                # Adiciona ao plot despache/mes
                plt.plot(carvao['mes'], carvao['despache'], c='black')
            # Checa se a fonte está nas legendas
            if 'Carvao' in legendas:
                pass
            else:
                legendas.append(row[1][0])

        # ------------------------ Eolicas ------------------------ #
        # Checa (em row[1][0])o nome da fonte e checa se essa fonte foi passada como parâmetro
        elif row[1][0] == 'Eolicas' and 'Eolicas' in fonte:
            # Se sim, checa (em row[1][3]) se o valor é correspondente ao passado como parâmetro
            if row[1][3] == ano:
                # Adiciona ao respectivo dicionário os valores de despache e meses
                eolica['despache'].append(row[1][1])
                eolica['mes'].append(row[1][2])
                # Adiciona ao plot despache/mes
                plt.plot(eolica['mes'], eolica['despache'], c='powderblue')
            # Checa se a fonte está nas legendas
            if 'Eolicas' in legendas:
                pass
            else:
                legendas.append(row[1][0])

        # ------------------------ Biomassas ------------------------ #
        # Checa (em row[1][0])o nome da fonte e checa se essa fonte foi passada como parâmetro
        elif row[1][0] == 'Biomassas' and 'Biomassas' in fonte:
            if row[1][3] == ano:
                # Adiciona ao respectivo dicionário os valores de despache e meses
                biomassa['despache'].append(row[1][1])
                biomassa['mes'].append(row[1][2])
                # Adiciona ao plot despache/mes
                plt.plot(biomassa['mes'], biomassa['despache'], c='red')
            # Checa se a fonte está nas legendas
            if 'Biomassas' in legendas:
                pass
            else:
                legendas.append(row[1][0])

        # ------------------------ Nuclear ------------------------ #
        # Checa (em row[1][0])o nome da fonte e checa se essa fonte foi passada como parâmetro
        elif row[1][0] == 'Nuclear' and 'Nuclear' in fonte:
            # Se sim, checa (em row[1][3]) se o valor é correspondente ao passado como parâmetro
            if row[1][3] == ano:
                # Adiciona ao respectivo dicionário os valores de despache e meses
                nuclear['despache'].append(row[1][1])
                nuclear['mes'].append(row[1][2])
                # Adiciona ao plot despache/mes
                plt.plot(nuclear['mes'], nuclear['despache'], c='gold')
            # Checa se a fonte está nas legendas
            if 'Nuclear' in legendas:
                pass
            else:
                legendas.append(row[1][0])

        # ------------------------ Residuos Processos Industriais ------------------------ #
        # Checa (em row[1][0])o nome da fonte e checa se essa fonte foi passada como parâmetro
        elif row[1][0] == 'Residuos Processos Industriais' \
                and 'Residuos Processos Industriais' in fonte:
            # Se sim, checa (em row[1][3]) se o valor é correspondente ao passado como parâmetro
            if row[1][3] == ano:
                # Adiciona ao respectivo dicionário os valores de despache e meses
                residuos['despache'].append(row[1][1])
                residuos['mes'].append(row[1][2])
                # Adiciona ao plot despache/mes
                plt.plot(residuos['mes'], residuos['despache'], c='lime')
            # Checa se a fonte está nas legendas
            if 'Residuos Processos Industriais' in legendas:
                pass
            else:
                legendas.append(row[1][0])

        # ------------------------ Energia produzida fora do SIN ------------------------ #
        # Checa (em row[1][0])o nome da fonte e checa se essa fonte foi passada como parâmetro
        elif row[1][0] == 'Energia produzida fora do SIN' \
                and 'Energia produzida fora do SIN' in fonte:
            # Se sim, checa (em row[1][3]) se o valor é correspondente ao passado como parâmetro
            if row[1][3] == ano:
                # Adiciona ao respectivo dicionário os valores de despache e meses
                energia_fora_sin['despache'].append(row[1][1])
                energia_fora_sin['mes'].append(row[1][2])
                # Adiciona ao plot despache/mes
                plt.plot(energia_fora_sin['mes'], energia_fora_sin['despache'], c='dimgrey')
            # Checa se a fonte está nas legendas
            if 'Energia produzida fora do SIN' in legendas:
                pass
            else:
                legendas.append(row[1][0])

    # -------- PLOT -------- #
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

    # Lista de Legendas
    legendas: list = []

    # Itera nas linhas do dataframe
    for row in data.iterrows():
        # Itera em cada item de row[1] (row[0] é id, row[1] contém os dados)
        for i in row[1]:
            # ------------------------ Hidreletricas exclusive Itaipu ------------------------ #
            # Verifica se o item é igual a fonte (string) e foi passado como parâmetro
            if i == 'Hidreletricas exclusive Itaipu' \
                    and 'Hidreletricas exclusive Itaipu' in fonte:
                # Se sim, verifica se o mês (row[1][2]) tem valor igual ao mes (parâmetro)
                if row[1][2] == mes:
                    # Adiciona ao respectivo dicionário os valores de despache e anos
                    hidreletricas['despache'].append(row[1][1])
                    hidreletricas['ano'].append(row[1][3])
                    # Adiciona ao plot despache/ano
                    plt.plot(hidreletricas['ano'], hidreletricas['despache'], c='darkcyan')
                    # Checa se a fonte está nas legendas
                    if 'Hidreletricas exclusive Itaipu' in legendas:
                        pass
                    else:
                        legendas.append(row[1][0])

            # ------------------------ Itaipu ------------------------ #
            # Verifica se o item é igual a fonte (string) e foi passado como parâmetro
            elif i == 'Itaipu' and 'Itaipu' in fonte:
                # Se sim, verifica se o mês (row[1][2]) tem valor igual ao mes (parâmetro)
                if row[1][2] == mes:
                    # Adiciona ao respectivo dicionário os valores de despache e anos
                    itaipu['despache'].append(row[1][1])
                    itaipu['ano'].append(row[1][3])
                    # Adiciona ao plot despache/ano
                    plt.plot(itaipu['ano'], itaipu['despache'], c='darkturquoise')
                    # Checa se a fonte está nas legendas
                    if 'Itaipu' in legendas:
                        pass
                    else:
                        legendas.append(row[1][0])

            # ------------------------ Oleo Diesel / Combustivel ------------------------ #
            # Verifica se o item é igual a fonte (string) e foi passado como parâmetro
            elif i == 'Oleo Diesel / Combustivel' and 'Oleo Diesel / Combustivel' in fonte:
                # Se sim, verifica se o mês (row[1][2]) tem valor igual ao mes (parâmetro)
                if row[1][2] == mes:
                    # Adiciona ao respectivo dicionário os valores de despache e anos
                    oleo_diesel_combustivel['despache'].append(row[1][1])
                    oleo_diesel_combustivel['ano'].append(row[1][3])
                    # Adiciona ao plot despache/ano
                    plt.plot(oleo_diesel_combustivel['ano'],
                             oleo_diesel_combustivel['despache'],
                             c='darkgoldenrod')
                    plt.plot(itaipu['ano'], itaipu['despache'], c='blue')
                    # Checa se a fonte está nas legendas
                    if 'Oleo Diesel / Combustivel' in legendas:
                        pass
                    else:
                        legendas.append(row[1][0])

            # ------------------------ Gas Natural ------------------------ #
            # Verifica se o item é igual a fonte (string) e foi passado como parâmetro
            elif i == 'Gas Natural' and 'Gas Natural' in fonte:
                # Se sim, verifica se o mês (row[1][2]) tem valor igual ao mes (parâmetro)
                if row[1][2] == mes:
                    # Adiciona ao respectivo dicionário os valores de despache e anos
                    gas_natural['despache'].append(row[1][1])
                    gas_natural['ano'].append(row[1][3])
                    # Adiciona ao plot despache/ano
                    plt.plot(gas_natural['ano'], gas_natural['despache'], c='lightgrey')
                    # Checa se a fonte está nas legendas
                    if 'Gas Natural' in legendas:
                        pass
                    else:
                        legendas.append(row[1][0])

            # ------------------------ Carvao ------------------------ #
            # Verifica se o item é igual a fonte (string) e foi passado como parâmetro
            elif i == 'Carvao' and 'Carvao' in fonte:
                # Se sim, verifica se o mês (row[1][2]) tem valor igual ao mes (parâmetro)
                if row[1][2] == mes:
                    # Adiciona ao respectivo dicionário os valores de despache e anos
                    carvao['despache'].append(row[1][1])
                    carvao['ano'].append(row[1][3])
                    # Adiciona ao plot despache/ano
                    plt.plot(carvao['ano'], carvao['despache'], c='black')
                    # Checa se a fonte está nas legendas
                    if 'Carvao' in legendas:
                        pass
                    else:
                        legendas.append(row[1][0])

            # ------------------------ Eolicas ------------------------ #
            # Verifica se o item é igual a fonte (string) e foi passado como parâmetro
            elif i == 'Eolicas' and 'Eolicas' in fonte:
                # Se sim, verifica se o mês (row[1][2]) tem valor igual ao mes (parâmetro)
                if row[1][2] == mes:
                    # Adiciona ao respectivo dicionário os valores de despache e anos
                    eolica['despache'].append(row[1][1])
                    eolica['ano'].append(row[1][3])
                    # Adiciona ao plot despache/ano
                    plt.plot(eolica['ano'], eolica['despache'], c='powderblue')
                    # Checa se a fonte está nas legendas
                    if 'Eolicas' in legendas:
                        pass
                    else:
                        legendas.append(row[1][0])

            # ------------------------ Biomassas ------------------------ #
            # Verifica se o item é igual a fonte (string) e foi passado como parâmetro
            elif i == 'Biomassas' and 'Biomassas' in fonte:
                # Se sim, verifica se o mês (row[1][2]) tem valor igual ao mes (parâmetro)
                if row[1][2] == mes:
                    # Adiciona ao respectivo dicionário os valores de despache e anos
                    biomassa['despache'].append(row[1][1])
                    biomassa['ano'].append(row[1][3])
                    # Adiciona ao plot despache/ano
                    plt.plot(biomassa['ano'], biomassa['despache'], c='red')
                    # Checa se a fonte está nas legendas
                    if 'Biomassas' in legendas:
                        pass
                    else:
                        legendas.append(row[1][0])

            # ------------------------ Nuclear ------------------------ #
            # Verifica se o item é igual a fonte (string) e foi passado como parâmetro
            elif i == 'Nuclear' and 'Nuclear' in fonte:
                # Se sim, verifica se o mês (row[1][2]) tem valor igual ao mes (parâmetro)
                if row[1][2] == mes:
                    # Adiciona ao respectivo dicionário os valores de despache e anos
                    nuclear['despache'].append(row[1][1])
                    nuclear['ano'].append(row[1][3])
                    # Adiciona ao plot despache/ano
                    plt.plot(nuclear['ano'], nuclear['despache'], c='gold')
                    # Checa se a fonte está nas legendas
                    if 'Nuclear' in legendas:
                        pass
                    else:
                        legendas.append(row[1][0])

            # ------------------------ Residuos Processos Industriais ------------------------ #
            # Verifica se o item é igual a fonte (string) e foi passado como parâmetro
            elif i == 'Residuos Processos Industriais' \
                    and 'Residuos Processos Industriais' in fonte:
                # Se sim, verifica se o mês (row[1][2]) tem valor igual ao mes (parâmetro)
                if row[1][2] == mes:
                    # Adiciona ao respectivo dicionário os valores de despache e anos
                    residuos['despache'].append(row[1][1])
                    residuos['ano'].append(row[1][3])
                    # Adiciona ao plot despache/ano
                    plt.plot(residuos['ano'], residuos['despache'], c='lime')
                    # Checa se a fonte está nas legendas
                    if 'Residuos Processos Industriais' in legendas:
                        pass
                    else:
                        legendas.append(row[1][0])

            # ------------------------ Energia produzida fora do SIN ------------------------ #
            # Verifica se o item é igual a fonte (string) e foi passado como parâmetro
            elif i == 'Energia produzida fora do SIN' \
                    and 'Energia produzida fora do SIN' in fonte:
                # Se sim, verifica se o mês (row[1][2]) tem valor igual ao mes (parâmetro)
                if row[1][2] == mes:
                    # Adiciona ao respectivo dicionário os valores de despache e anos
                    energia_fora_sin['despache'].append(row[1][1])
                    energia_fora_sin['ano'].append(row[1][3])
                    # Adiciona ao plot despache/ano
                    plt.plot(energia_fora_sin['ano'], energia_fora_sin['despache'], c='dimgrey')
                    # Checa se a fonte está nas legendas
                    if 'Energia produzida fora do SIN' in legendas:
                        pass
                    else:
                        legendas.append(row[1][0])

    # ------ PLOT ------ #
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

    # Lista de Legendas
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
    # ------------------------ Hidreletricas exclusive Itaipu ------------------------ #
    # Verifica se a fonte (string) e foi passada como parâmetro
    if 'Hidreletricas exclusive Itaipu' in fonte:
        # Itera as linha do dataframe
        for row in data.iterrows():
            # Verifica se a fonte (row[1][0]) tiver o valor igual a string
            if row[1][0] == 'Hidreletricas exclusive Itaipu':
                # Verifica se a fonte está nas legendas
                if 'Hidreletricas exclusive Itaipu' in legendas:
                    pass
                else:
                    legendas.append(row[1][0])
                # Preenche os meses
                preencher_meses()
        # Adiciona as médias no respectivo dicionário
        for i in range(1, 13):
            hidreletricas['media'].append(mean(meses[i]))
            meses[i].clear()
        # Adiciona ao plot (media/mes)
        plt.plot(qnt_meses, hidreletricas['media'], c='darkcyan')

    # ------------------------ Itaipu ------------------------ #
    # Verifica se a fonte (string) e foi passada como parâmetro
    if 'Itaipu' in fonte:
        # Itera as linha do dataframe
        for row in data.iterrows():
            # Verifica se a fonte (row[1][0]) tiver o valor igual a string
            if row[1][0] == 'Itaipu':
                # Verifica se a fonte está nas legendas
                if 'Itaipu' in legendas:
                    pass
                else:
                    legendas.append(row[1][0])
                # Preenche os meses
                preencher_meses()
        # Adiciona as médias no respectivo dicionário
        for i in range(1, 13):
            itaipu['media'].append(mean(meses[i]))
            meses[i].clear()
        # Adiciona ao plot (media/mes)
        plt.plot(qnt_meses, itaipu['media'], c='darkturquoise')

    # ------------------------ Oleo Diesel / Combustivel ------------------------ #
    # Verifica se a fonte (string) e foi passada como parâmetro
    if 'Oleo Diesel / Combustivel' in fonte:
        # Itera as linha do dataframe
        for row in data.iterrows():
            # Verifica se a fonte (row[1][0]) tiver o valor igual a string
            if row[1][0] == 'Oleo Diesel / Combustivel':
                # Verifica se a fonte está nas legendas
                if 'Oleo Diesel / Combustivel' in legendas:
                    pass
                else:
                    legendas.append(row[1][0])
                # Preenche os meses
                preencher_meses()
        # Adiciona as médias no respectivo dicionário
        for i in range(1, 13):
            oleo_diesel_combustivel['media'].append(mean(meses[i]))
            meses[i].clear()
        # Adiciona ao plot (media/mes)
        plt.plot(qnt_meses, oleo_diesel_combustivel['media'], c='darkgoldenrod')

    # ------------------------ Gas Natural ------------------------ #
    # Verifica se a fonte (string) e foi passada como parâmetro
    if 'Gas Natural' in fonte:
        # Itera as linha do dataframe
        for row in data.iterrows():
            # Verifica se a fonte (row[1][0]) tiver o valor igual a string
            if row[1][0] == 'Gas Natural':
                # Verifica se a fonte está nas legendas
                if 'Gas Natural' in legendas:
                    pass
                else:
                    legendas.append(row[1][0])
                # Preenche os meses
                preencher_meses()
        # Adiciona as médias no respectivo dicionário
        for i in range(1, 13):
            gas_natural['media'].append(mean(meses[i]))
            meses[i].clear()
        # Adiciona ao plot (media/mes)
        plt.plot(qnt_meses, gas_natural['media'], c='lightgrey')

    # ------------------------ Carvao ------------------------ #
    # Verifica se a fonte (string) e foi passada como parâmetro
    if 'Carvao' in fonte:
        # Itera as linha do dataframe
        for row in data.iterrows():
            # Verifica se a fonte (row[1][0]) tiver o valor igual a string
            if row[1][0] == 'Carvao':
                # Verifica se a fonte está nas legendas
                if 'Carvao' in legendas:
                    pass
                else:
                    legendas.append(row[1][0])
                # Preenche os meses
                preencher_meses()
        # Adiciona as médias no respectivo dicionário
        for i in range(1, 13):
            carvao['media'].append(mean(meses[i]))
            meses[i].clear()
        # Adiciona ao plot (media/mes)
        plt.plot(qnt_meses, carvao['media'], c='black')

    # ------------------------ Eolicas ------------------------ #
    # Verifica se a fonte (string) e foi passada como parâmetro
    if 'Eolicas' in fonte:
        # Itera as linha do dataframe
        for row in data.iterrows():
            # Verifica se a fonte (row[1][0]) tiver o valor igual a string
            if row[1][0] == 'Eolicas' and 'Eolicas':
                # Verifica se a fonte está nas legendas
                if 'Eolicas' in legendas:
                    pass
                else:
                    legendas.append(row[1][0])
                # Preenche os meses
                preencher_meses()
        # Adiciona as médias no respectivo dicionário
        for i in range(1, 13):
            eolica['media'].append(mean(meses[i]))
            meses[i].clear()
        # Adiciona ao plot (media/mes)
        plt.plot(qnt_meses, eolica['media'], c='powderblue')

    # ------------------------ Biomassas ------------------------ #
    # Verifica se a fonte (string) e foi passada como parâmetro
    if 'Biomassas' in fonte:
        # Itera as linha do dataframe
        for row in data.iterrows():
            # Verifica se a fonte (row[1][0]) tiver o valor igual a string
            if row[1][0] == 'Biomassas':
                # Verifica se a fonte está nas legendas
                if 'Biomassas' in legendas:
                    pass
                else:
                    legendas.append(row[1][0])
                # Preenche os meses
                preencher_meses()
        # Adiciona as médias no respectivo dicionário
        for i in range(1, 13):
            biomassa['media'].append(mean(meses[i]))
            meses[i].clear()
        # Adiciona ao plot (media/mes)
        plt.plot(qnt_meses, biomassa['media'], c='red')

    # ------------------------ Nuclear ------------------------ #
    # Verifica se a fonte (string) e foi passada como parâmetro
    if 'Nuclear' in fonte:
        # Itera as linha do dataframe
        for row in data.iterrows():
            # Verifica se a fonte (row[1][0]) tiver o valor igual a string
            if row[1][0] == 'Nuclear':
                # Verifica se a fonte está nas legendas
                if 'Nuclear' in legendas:
                    pass
                else:
                    legendas.append(row[1][0])
                # Preenche os meses
                preencher_meses()
        # Adiciona as médias no respectivo dicionário
        for i in range(1, 13):
            nuclear['media'].append(mean(meses[i]))
            meses[i].clear()
        # Adiciona ao plot (media/mes)
        plt.plot(qnt_meses, nuclear['media'], c='gold')

    # ------------------------ Residuos Processos Industriais ------------------------ #
    # Verifica se a fonte (string) e foi passada como parâmetro
    if 'Residuos Processos Industriais' in fonte:
        # Itera as linha do dataframe
        for row in data.iterrows():
            # Verifica se a fonte (row[1][0]) tiver o valor igual a string
            if row[1][0] == 'Residuos Processos Industriais':
                # Verifica se a fonte está nas legendas
                if 'Residuos Processos Industriais' in legendas:
                    pass
                else:
                    legendas.append(row[1][0])
                # Preenche os meses
                preencher_meses()
        # Adiciona as médias no respectivo dicionário
        for i in range(1, 13):
            residuos['media'].append(mean(meses[i]))
            meses[i].clear()
        # Adiciona ao plot (media/mes)
        plt.plot(qnt_meses, residuos['media'], c='lime')

    # ------------------------ Energia produzida fora do SIN ------------------------ #
    # Verifica se a fonte (string) e foi passada como parâmetro
    if 'Energia produzida fora do SIN' in fonte:
        # Itera as linha do dataframe
        for row in data.iterrows():
            # Verifica se a fonte (row[1][0]) tiver o valor igual a string
            if row[1][0] == 'Energia produzida fora do SIN':
                # Verifica se a fonte está nas legendas
                if 'Energia produzida fora do SIN' in legendas:
                    pass
                else:
                    legendas.append(row[1][0])
                # Preenche os meses
                preencher_meses()
        # Adiciona as médias no respectivo dicionário
        for i in range(1, 13):
            energia_fora_sin['media'].append(mean(meses[i]))
            meses[i].clear()
        # Adiciona ao plot (media/mes)
        plt.plot(qnt_meses, energia_fora_sin['media'], c='grey')

    # ------ PLOT ------ #
    plt.title(f'{fonte} | Média por mês de todos os anos')
    plt.xlabel('Meses')
    plt.ylabel('Despache GWh')
    plt.legend(legendas)
    plt.tight_layout()
    plt.show()
