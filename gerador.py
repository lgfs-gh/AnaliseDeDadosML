import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

# --------------------------------------------- TRATAMENTO DE DADOS ----------------------------------------------------

db_padrao = pd.read_csv('GeracaoFonte.csv')  # Faz a leitura do banco de dados
del db_padrao['dthProcessamento']  # Deleta a coluna dthProcessamento (é uma coluna vazia)
del db_padrao['ideGeracaoFonte']  # Deleta a colune de identificadores
"""
Aqui é utilizado um SimpleImputer para remover os valores não númericos (NaN)
"""
imputer = SimpleImputer(missing_values=np.NaN, strategy='constant', fill_value=0)  # Cria o imputer
imputer = imputer.fit(db_padrao[::])
db_padrao = imputer.transform(db_padrao[::])  # Retorna a tabela sem valores NaN


# ------------------------------------------- CLASSE GERADORA DE DF ----------------------------------------------------
class GenDataFrame:
    """
    # Gerador de dataframe #

    Esta classe permite a criação de dataframes personalizados
    Os parametros de criação que podem ou não ser passados são:
    fonte -> o usuário define pelo nome (string) uma fonte energética.
    mes -> o usuário define com um número (int) o mês desejado.
    ano -> o usuário define com um número (int) o ano desejado.

    Por padrão os valores dos atributos são iniciados com a string 'todos'
    assim retornado todos os valores do dataframe base.
    Alterando os parâmetros de criação, é possível obter por exemplo:

    **Para gerar o dataframe, é usado o método 'gerar()'

    1) Um dataframe contendo informações sobre a fonte eolica:
    variavel = GenDataFrame(fonte='Eolicas').gerar()

    1) Um dataframe contendo informações sobre a fonte carvão no mês de janeiro, em todos os anos:
    variavel = GenDataFrame(fonte='Carvao', mes=1).gerar()

    3) Um dataframe contendo informações sobre a fonte eolica em 2012:
    variavel = GenDataFrame(fonte='Eolicas', ano=2012).gerar()

    4) Um dataframe contendo informações sobre todas as fontes em novembro de 2015:
    variavel = GenDataFrame(mes=11, ano=2015).gerar()
    """

    def __init__(self, fonte='todos', mes: int = 'todos', ano: int = 'todos'):
        self.__fonte = fonte
        self.__mes = mes
        self.__ano = ano
        self.__db = db_padrao

    def gerar(self):
        parametros = {'fonte': [], 'despache': [], 'mes': [], 'ano': []}

        def preencher(dados, i):
            dados['fonte'].append(i[0])
            dados['despache'].append(i[1])
            dados['mes'].append(i[2])
            dados['ano'].append(i[3])

        if self.__fonte == 'todos' and self.__mes == 'todos' and self.__ano == 'todos':
            for i in self.__db:
                preencher(parametros, i)
            df = pd.DataFrame(parametros)
            return df
        elif self.__fonte != 'todos' and self.__mes != 'todos' and self.__ano != 'todos':
            for i in self.__db:
                if i[0] == self.__fonte and i[2] == self.__mes and i[3] == self.__ano:
                    preencher(parametros, i)
            df = pd.DataFrame(parametros)
            return df
        elif self.__fonte != 'todos':
            if self.__mes == 'todos' and self.__ano == 'todos':
                for i in self.__db:
                    if i[0] == self.__fonte:
                        preencher(parametros, i)
                df = pd.DataFrame(parametros)
                return df
            elif self.__mes != 'todos' and self.__ano == 'todos':
                for i in self.__db:
                    if i[0] == self.__fonte and i[2] == self.__mes:
                        preencher(parametros, i)
                df = pd.DataFrame(parametros)
                return df
            else:
                for i in self.__db:
                    if i[0] == self.__fonte and i[3] == self.__ano:
                        preencher(parametros, i)
                df = pd.DataFrame(parametros)
                return df
        elif self.__mes != 'todos':
            if self.__fonte == 'todos' and self.__ano == 'todos':
                for i in self.__db:
                    if i[2] == self.__mes:
                        preencher(parametros, i)
                df = pd.DataFrame(parametros)
                return df
            elif self.__fonte != 'todos' and self.__ano == 'todos':
                for i in self.__db:
                    if i[0] == self.__fonte and i[2] == self.__mes:
                        preencher(parametros, i)
                df = pd.DataFrame(parametros)
                return df
            else:
                for i in self.__db:
                    if i[2] == self.__mes and i[3] == self.__ano:
                        preencher(parametros, i)
                df = pd.DataFrame(parametros)
                return df
        elif self.__ano != 'todos':
            if self.__fonte == 'todos' and self.__mes == 'todos':
                for i in self.__db:
                    if i[3] == self.__ano:
                        preencher(parametros, i)
                df = pd.DataFrame(parametros)
                return df
            elif self.__fonte != 'todos' and self.__mes == 'todos':
                for i in self.__db:
                    if i[0] == self.__fonte and i[3] == self.__ano:
                        preencher(parametros, i)
                df = pd.DataFrame(parametros)
                return df
            else:
                for i in self.__db:
                    if i[2] == self.__mes and i[3] == self.__ano:
                        preencher(parametros, i)
                df = pd.DataFrame(parametros)
                return df
        else:
            print('Algo deu errado')

