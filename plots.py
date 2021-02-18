import matplotlib.pyplot as plt
from gerador import GenDataFrame

# ----------------------------------- Gerando dataframes de teste ------------------------------------------------------
data_base = GenDataFrame().gerar()
data = GenDataFrame(fonte=['Eolicas', 'Carvao'], mes=[1, 2, 3, 10, 11, 12]).gerar()
data2 = GenDataFrame(fonte=['Hidreletricas exclusive Itaipu', 'Itaipu', 'Gas Natural', 'Biomassas'],
                     mes=[1, 2, 3, 10, 11, 12]).gerar()


# --------------------------------------------- PLOTAGEM ---------------------------------------------------------------
def line_plot(dataframe, nome_do_arquivo: str = 'plot') -> None:
    """
    # Método de plotagem # FUNCIONAL / INCOMPLETO
    Plota gráficos para ánalise do despache por ano.

    EXs:
    line_plot(data2, 'plotagem')
    line_plot(data)

    :param dataframe: Neste parâmetro é passado dataframe que irá ser plotado
    :param nome_do_arquivo: Neste parâmetro é passado o nome do arquivo que será salvo, por padrão o nome é 'plot'.
    :return: None
    """
    hidreletricas: dict = {'fonte': 'Hidreletricas exclusive Itaipu', 'despache': [], 'mes': [], 'ano': []}
    itaipu: dict = {'fonte': 'Itaipu', 'despache': [], 'mes': [], 'ano': []}
    oleo_diesel_combustivel: dict = {'fonte': 'Oleo Diesel/Combustivel', 'despache': [], 'mes': [], 'ano': []}
    gas_natural: dict = {'fonte': 'Gas Natural', 'despache': [], 'mes': [], 'ano': []}
    carvao: dict = {'fonte': 'Carvao', 'despache': [], 'mes': [], 'ano': []}
    eolica: dict = {'fonte': 'Eolicas', 'despache': [], 'mes': [], 'ano': []}
    biomassa: dict = {'fonte': 'Biomassas', 'despache': [], 'mes': [], 'ano': []}
    nuclear: dict = {'fonte': 'Nuclear', 'despache': [], 'mes': [], 'ano': []}
    residuos: dict = {'fonte': 'Residuos Processos Industriais', 'despache': [], 'mes': [], 'ano': []}
    energia_fora_sin: dict = {'fonte': 'Energia produzida fora do SIN', 'despache': [], 'mes': [], 'ano': []}

    legendas = []

    for row in dataframe.iterrows():
        for i in row[1]:
            if i == 'Hidreletricas exclusive Itaipu':
                hidreletricas['despache'].append(row[1][1])
                hidreletricas['mes'].append(row[1][2])
                hidreletricas['ano'].append(row[1][3])
                plt.plot(hidreletricas['ano'], hidreletricas['despache'], c='darkcyan')
                if 'Hidreletricas exclusive Itaipu' in legendas:
                    pass
                else:
                    legendas.append(row[1][0])
            elif i == 'Itaipu':
                itaipu['despache'].append(row[1][1])
                itaipu['mes'].append(row[1][2])
                itaipu['ano'].append(row[1][3])
                plt.plot(itaipu['ano'], itaipu['despache'], c='darkturquoise')
                if 'Itaipu' in legendas:
                    pass
                else:
                    legendas.append(row[1][0])
            elif i == 'Oleo Diesel/Combustivel':
                oleo_diesel_combustivel['despache'].append(row[1][1])
                oleo_diesel_combustivel['mes'].append(row[1][2])
                oleo_diesel_combustivel['ano'].append(row[1][3])
                plt.plot(oleo_diesel_combustivel['ano'], oleo_diesel_combustivel['despache'], c='darkgoldenrod')
                plt.plot(itaipu['ano'], itaipu['despache'], c='blue')
                if 'Oleo Diesel/Combustivel' in legendas:
                    pass
                else:
                    legendas.append(row[1][0])
            elif i == 'Gas Natural':
                gas_natural['despache'].append(row[1][1])
                gas_natural['mes'].append(row[1][2])
                gas_natural['ano'].append(row[1][3])
                plt.plot(gas_natural['ano'], gas_natural['despache'], c='lightgrey')
                if 'Gas Natural' in legendas:
                    pass
                else:
                    legendas.append(row[1][0])
            elif i == 'Carvao':
                carvao['despache'].append(row[1][1])
                carvao['mes'].append(row[1][2])
                carvao['ano'].append(row[1][3])
                plt.plot(carvao['ano'], carvao['despache'], c='black')
                if 'Carvao' in legendas:
                    pass
                else:
                    legendas.append(row[1][0])
            elif i == 'Eolicas':
                eolica['despache'].append(row[1][1])
                eolica['mes'].append(row[1][2])
                eolica['ano'].append(row[1][3])
                plt.plot(eolica['ano'], eolica['despache'], c='powderblue')
                if 'Eolicas' in legendas:
                    pass
                else:
                    legendas.append(row[1][0])
            elif i == 'Biomassas':
                biomassa['despache'].append(row[1][1])
                biomassa['mes'].append(row[1][2])
                biomassa['ano'].append(row[1][3])
                plt.plot(biomassa['ano'], biomassa['despache'], c='red')
                if 'Biomassas' in legendas:
                    pass
                else:
                    legendas.append(row[1][0])
            elif i == 'Nuclear':
                nuclear['despache'].append(row[1][1])
                nuclear['mes'].append(row[1][2])
                nuclear['ano'].append(row[1][3])
                plt.plot(nuclear['ano'], nuclear['despache'], c='gold')
                if 'Nuclear' in legendas:
                    pass
                else:
                    legendas.append(row[1][0])
            elif i == 'Residuos Processos Industriais':
                nuclear['despache'].append(row[1][1])
                nuclear['mes'].append(row[1][2])
                nuclear['ano'].append(row[1][3])
                plt.plot(residuos['ano'], residuos['despache'], c='lime')
                if 'Residuos Processos Industriais' in legendas:
                    pass
                else:
                    legendas.append(row[1][0])
            elif i == 'Energia produzida fora do SIN':
                energia_fora_sin['despache'].append(row[1][1])
                energia_fora_sin['mes'].append(row[1][2])
                energia_fora_sin['ano'].append(row[1][3])
                plt.plot(energia_fora_sin['ano'], energia_fora_sin['despache'], c='dimgrey')
                if 'Energia produzida fora do SIN' in legendas:
                    pass
                else:
                    legendas.append(row[1][0])

    plt.xlabel('Anos')
    plt.ylabel('Despache GWh')
    plt.legend(legendas)
    plt.savefig(nome_do_arquivo)
