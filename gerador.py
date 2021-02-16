import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

# --------------------------------------------- TRATAMENTO DE DADOS ----------------------------------------------------

db_padrao = pd.read_csv('GeracaoFonte.csv')
del db_padrao['dthProcessamento']
del db_padrao['ideGeracaoFonte']
imputer = SimpleImputer(missing_values=np.NaN, strategy='constant', fill_value=0)
imputer = imputer.fit(db_padrao[::])
db_padrao = imputer.transform(db_padrao[::])


# ------------------------------------------- CLASSE GERADORA DE DF ----------------------------------------------------
class GenDataFrame:

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

