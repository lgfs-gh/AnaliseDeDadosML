from time import sleep
import PySimpleGUI as sg
from plots import plot_media_anos, plot_mes_especifico, plot_ano_especifico
from gerador import GenDataFrame


def main():
    # ------ Variaveis ------ #
    opcao_visivel = False
    plot_ano = False
    plot_mes = False
    plot_media = False
    dados = {'fontes': [], 'meses': [], 'anos': []}

    def preencher_fontes():
        if i == 1:
            dados['fontes'].append('Hidreletricas exclusive Itaipu')
        elif i == 2:
            dados['fontes'].append('Itaipu')
        elif i == 3:
            dados['fontes'].append('Oleo Diesel / Combustivel')
        elif i == 4:
            dados['fontes'].append('Gas Natural')
        elif i == 5:
            dados['fontes'].append('Carvao')
        elif i == 6:
            dados['fontes'].append('Eolicas')
        elif i == 7:
            dados['fontes'].append('Biomassas')
        elif i == 8:
            dados['fontes'].append('Nuclear')
        elif i == 9:
            dados['fontes'].append('Residuos Processos Industriais')
        elif i == 10:
            dados['fontes'].append('Energia produzida fora do SIN')

    def preencher_meses():
        if i == 1:
            dados['meses'].append(1)
        elif i == 2:
            dados['meses'].append(2)
        elif i == 3:
            dados['meses'].append(3)
        elif i == 4:
            dados['meses'].append(4)
        elif i == 5:
            dados['meses'].append(5)
        elif i == 6:
            dados['meses'].append(6)
        elif i == 7:
            dados['meses'].append(7)
        elif i == 8:
            dados['meses'].append(8)
        elif i == 9:
            dados['meses'].append(9)
        elif i == 10:
            dados['meses'].append(10)
        elif i == 11:
            dados['meses'].append(11)
        elif i == 12:
            dados['meses'].append(12)

    def preencher_anos():
        if i == 1:
            dados['anos'].append(2000)
        elif i == 2:
            dados['anos'].append(2001)
        elif i == 3:
            dados['anos'].append(2002)
        elif i == 4:
            dados['anos'].append(2003)
        elif i == 5:
            dados['anos'].append(2004)
        elif i == 6:
            dados['anos'].append(2005)
        elif i == 7:
            dados['anos'].append(2006)
        elif i == 8:
            dados['anos'].append(2007)
        elif i == 9:
            dados['anos'].append(2008)
        elif i == 10:
            dados['anos'].append(2009)
        elif i == 11:
            dados['anos'].append(2010)
        elif i == 12:
            dados['anos'].append(2011)
        elif i == 13:
            dados['anos'].append(2012)
        elif i == 14:
            dados['anos'].append(2013)
        elif i == 15:
            dados['anos'].append(2014)
        elif i == 16:
            dados['anos'].append(2015)
        elif i == 17:
            dados['anos'].append(2016)
        elif i == 18:
            dados['anos'].append(2017)
        elif i == 19:
            dados['anos'].append(2018)
        elif i == 20:
            dados['anos'].append(2019)
        elif i == 21:
            dados['anos'].append(2020)

    # ------ Definindo o Menu  ------ #
    menu_def = [['&Arquivo', ['&Abrir', '&Salvar', '&Propriedades', 'S&air']],
                ['&Editar', ['&Colar', ['Especial', 'Normal', ], 'Desfazer'], ],
                ['&BarraExemplo', ['---', 'Command &1', 'Command &2', '---', 'Command &3', 'Command &4']],
                ['&Ajuda', '&Sobre...'], ]

    right_click_menu = ['Unused', ['Right', '!&Click', '&Menu', 'E&xit', 'Properties']]

    # ------ Modos de plotagem  ------ #
    frame_plot = [
        [sg.Button('Despache por ano específico', font='Any 12', size=(35, 3),
                   key='plot_ano')],
        [sg.Button('Despache por mês específico', font='Any 12', size=(35, 3),
                   key='plot_mes')],
        [sg.Button('Média de despache para todos os anos', font='Any 12', size=(35, 3),
                   key='plot_media')]
    ]

    # ------ Configurações Dataframe  ------ #
    frame_rna = [
        [sg.Button('Configurar um dataframe', font='Any 12', size=(35, 3),
                   key='_df_config_')],
        [sg.Button('Configurar RNA', font='Any 12', size=(35, 3),
                   key='_rna_config_')],
        [sg.Button('Gerar previsão', font='Any 12', size=(35, 3),
                   key='_gerar_prev_')]
    ]

    # ------ Layout Colunas ------ #
    layout_coluna_fontes = [
        [sg.Checkbox(' Hidreletricas Exclusive Itaipu', key='_frame_fontes_1')],
        [sg.Checkbox(' Itaipu', key='_frame_fontes_2')],
        [sg.Checkbox(' Oleo Diesel / Combustivel', key='_frame_fontes_3')],
        [sg.Checkbox(' Gas Natural', key='_frame_fontes_4')],
        [sg.Checkbox(' Carvao', key='_frame_fontes_5')],
        [sg.Checkbox(' Eolicas', key='_frame_fontes_6')],
        [sg.Checkbox(' Biomassas', key='_frame_fontes_7')],
        [sg.Checkbox(' Nuclear', key='_frame_fontes_8')],
        [sg.Checkbox(' Residuos Processos Industriais', key='_frame_fontes_9')],
        [sg.Checkbox(' Energia produzida fora do SIN', key='_frame_fontes_10')]
    ]

    layout_coluna_meses = [
        [sg.Checkbox(' 1 - Janeiro  ', disabled=True, key='_frame_meses_1'),
         sg.Checkbox(' 11 - Novembro', disabled=True, key='_frame_meses_11')],
        [sg.Checkbox(' 2 - Fevereiro', disabled=True, key='_frame_meses_2'),
         sg.Checkbox(' 12 - Dezembro', disabled=True, key='_frame_meses_12')],
        [sg.Checkbox(' 3 - Março', disabled=True, key='_frame_meses_3')],
        [sg.Checkbox(' 4 - Abril', disabled=True, key='_frame_meses_4')],
        [sg.Checkbox(' 5 - Maio', disabled=True, key='_frame_meses_5')],
        [sg.Checkbox(' 6 - Junho', disabled=True, key='_frame_meses_6')],
        [sg.Checkbox(' 7 - Julho', disabled=True, key='_frame_meses_7')],
        [sg.Checkbox(' 8 - Agosto', disabled=True, key='_frame_meses_8')],
        [sg.Checkbox(' 9 - Setembro', disabled=True, key='_frame_meses_9')],
        [sg.Checkbox(' 10 - Outubro', disabled=True, key='_frame_meses_10')]
    ]

    layout_coluna_anos = [
        [sg.Checkbox(' 2000', disabled=True, key='_frame_anos_1'),
         sg.Checkbox(' 2010', disabled=True, key='_frame_anos_11'),
         sg.Checkbox(' 2020', disabled=True, key='_frame_anos_21')],
        [sg.Checkbox(' 2001', disabled=True, key='_frame_anos_2'),
         sg.Checkbox(' 2011', disabled=True, key='_frame_anos_12')],
        [sg.Checkbox(' 2002', disabled=True, key='_frame_anos_3'),
         sg.Checkbox(' 2012', disabled=True, key='_frame_anos_13')],
        [sg.Checkbox(' 2003', disabled=True, key='_frame_anos_4'),
         sg.Checkbox(' 2013', disabled=True, key='_frame_anos_14')],
        [sg.Checkbox(' 2004', disabled=True, key='_frame_anos_5'),
         sg.Checkbox(' 2014', disabled=True, key='_frame_anos_15')],
        [sg.Checkbox(' 2005', disabled=True, key='_frame_anos_6'),
         sg.Checkbox(' 2015', disabled=True, key='_frame_anos_16')],
        [sg.Checkbox(' 2006', disabled=True, key='_frame_anos_7'),
         sg.Checkbox(' 2016', disabled=True, key='_frame_anos_17')],
        [sg.Checkbox(' 2007', disabled=True, key='_frame_anos_8'),
         sg.Checkbox(' 2017', disabled=True, key='_frame_anos_18')],
        [sg.Checkbox(' 2008', disabled=True, key='_frame_anos_9'),
         sg.Checkbox(' 2018', disabled=True, key='_frame_anos_19')],
        [sg.Checkbox(' 2009', disabled=True, key='_frame_anos_10'),
         sg.Checkbox(' 2019', disabled=True, key='_frame_anos_20')],
    ]
    # ------ Configurando a plotagem  ------ #
    frame_opcoes = [
        [sg.Frame('Fontes', layout_coluna_fontes),
         sg.Frame('Meses', layout_coluna_meses),
         sg.Frame('Anos', layout_coluna_anos)]
    ]

    # ------ PLOT CANVAS  ------ #
    frame_grafico = [
        []
    ]

    # ---------- LAYOUT ------------ #
    layout = [
        [sg.Menu(menu_def)],
        [sg.Frame('RNA', frame_rna, font='Any 20', title_color='black',
                  border_width=5, visible=True, key='_rna_'),
         sg.Frame('PLOT', frame_plot, font='Any 20', title_color='black',
                  border_width=5, visible=True, key='_plot_'),
         sg.Frame('OPCOES', frame_opcoes, font='Any 20', title_color='black',
                  border_width=5, visible=False, key='_opcoes_'),
         sg.Frame('GRAFICO', frame_grafico, font='Any 20', title_color='black',
                  border_width=5, visible=False, key='_grafico_')],
        [sg.Button('Gerar', font='Any 12', size=(30, 1), visible=False, key='_gerar_'),
         sg.Button('Plotar', font='Any 12', size=(30, 1), visible=False, key='_plotar_'),
         sg.Button('Sair', font='Any 12', size=(30, 1), key='sair')],
    ]
    # ---------- JANELA ------------ #
    window = sg.Window('Menu',
                       layout,
                       element_justification='c',
                       default_element_size=(12, 1),
                       right_click_menu=right_click_menu,
                       default_button_element_size=(12, 1))
    while True:
        # ------ Condições de saída ------ #
        event, values = window.Read()
        if event in (sg.WIN_CLOSED, 'sair'):
            break

        # ------ Escolhas do menu ------ #
        if event == 'About...':
            window.disappear()
            sg.popup('About this program', 'Version 1.0', 'PySimpleGUI rocks...')
            window.reappear()
        elif event == 'Open':
            filename = sg.popup_get_file('file to open', no_window=True)
            print(filename)
        elif event == 'Properties':
            pass
        elif event == '-BMENU-':
            print('You selected from the button menu:', values['-BMENU-'])

        # ================ Menus de plotagem ================ #

        # 1 - PLOT POR ANO
        if event == 'plot_ano' and opcao_visivel is False:
            window.FindElement('_plot_').Update(visible=False)
            window.FindElement('_rna_').Update(visible=False)
            for i in range(1, 22):
                window.FindElement(f'_frame_anos_{str(i)}').Update(disabled=False)
            window.FindElement('_opcoes_').Update(visible=True)
            window.FindElement('_plotar_').Update(visible=True)
            plot_ano = True
            opcao_visivel = True

        # 2 - PLOT POR MES
        if event == 'plot_mes' and opcao_visivel is False:
            window.FindElement('_plot_').Update(visible=False)
            window.FindElement('_rna_').Update(visible=False)
            for i in range(1, 13):
                window.FindElement(f'_frame_meses_{str(i)}').Update(disabled=False)
            window.FindElement('_opcoes_').Update(visible=True)
            window.FindElement('_plotar_').Update(visible=True)
            plot_mes = True
            opcao_visivel = True

        # 3 - PLOT MEDIA
        if event == 'plot_media' and opcao_visivel is False:
            window.FindElement('_plot_').Update(visible=False)
            window.FindElement('_rna_').Update(visible=False)
            window.FindElement('_opcoes_').Update(visible=True)
            window.FindElement('_plotar_').Update(visible=True)
            plot_media = True
            opcao_visivel = True

        # ================ Menus RNA ================ #

        # 1 - Configurar dataframe
        if event == '_df_config_' and opcao_visivel is False:
            window.FindElement('_plot_').Update(visible=False)
            window.FindElement('_rna_').Update(visible=False)
            for i in range(1, 22):
                window.FindElement(f'_frame_anos_{str(i)}').Update(disabled=False)
            for i in range(1, 13):
                window.FindElement(f'_frame_meses_{str(i)}').Update(disabled=False)
            window.FindElement('_opcoes_').Update(visible=True)
            window.FindElement('_gerar_').Update(visible=True)
            opcao_visivel = True

        # ------ Menu de opções ------ #
        if event == '_gerar_':
            for i in range(1, 11):
                if values[f'_frame_fontes_{str(i)}']:
                    preencher_fontes()
            for i in range(1, 13):
                if values[f'_frame_meses_{str(i)}']:
                    preencher_meses()
            for i in range(1, 22):
                if values[f'_frame_anos_{str(i)}']:
                    preencher_anos()
            df = GenDataFrame(dados['fontes'], dados['meses'], dados['anos']).gerar()
            print(df)
            dados['fontes'].clear()
            dados['meses'].clear()
            dados['anos'].clear()
            window.close()
            sg.popup('Dataframe gerado com sucesso!', title='DATAFRAME', custom_text='     VOLTAR AO MENU     ')
            main()

        if event == '_plotar_':
            for i in range(1, 11):
                if values[f'_frame_fontes_{str(i)}']:
                    preencher_fontes()
            for i in range(1, 13):
                if values[f'_frame_meses_{str(i)}']:
                    preencher_meses()
            for i in range(1, 22):
                if values[f'_frame_anos_{str(i)}']:
                    preencher_anos()
            if plot_ano:
                for ano in dados['anos']:
                    plot_ano_especifico(dados['fontes'], ano)
                    dados['fontes'].clear()
                    dados['anos'].clear()
            if plot_mes:
                for mes in dados['meses']:
                    plot_mes_especifico(dados['fontes'], mes)
                    dados['fontes'].clear()
                    dados['meses'].clear()
            if plot_media:
                plot_media_anos(dados['fontes'])
                dados['fontes'].clear()
    window.Close()


if __name__ == '__main__':
    main()
