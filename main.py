import PySimpleGUI as sg
from plots import plot_media_anos, plot_mes_especifico, plot_ano_especifico
from gerador import GenDataFrame


def abrir_consulta():
    pass


def abrir_visualizacao_plotagem():
    frame_layout_plot = [
        [sg.Button('Despache por ano específico (todos os meses)',
                   font='Any 12', size=(50, 3), key='plot_ano')],
        [sg.Button('Despache por mês específico (todos os anos)',
                   font='Any 12', size=(50, 3), key='plot_mes')],
        [sg.Button('Despache por todos os anos', font='Any 12', size=(50, 3), key='plot_todos_anos')],
    ]
    layout_plot = [
        [sg.Frame('PLOTAGENS', frame_layout_plot, font='Any 20', title_color='black', border_width=5)],
        [sg.Button('Voltar', font='Any 12', size=(24, 2), key='voltar'),
         sg.Button('Sair', font='Any 12', size=(24, 2), key='sair')],
    ]
    window_plot = sg.Window('Plotagens', layout_plot)
    while True:
        event, values = window_plot.Read()
        if event in (sg.WIN_CLOSED, 'sair'):
            break
        if event == 'voltar':
            window_plot.close()
            main()

    window_plot.close()


def abrir_dataframes_rna():
    pass


def main():
    frame_layout = [
        [sg.Button('Consultar fontes energéticas disponívels', font='Any 12', size=(50, 3), key='consulta')],
        [sg.Button('Visualização e Plotagem', font='Any 12', size=(50, 3), key='plotagem')],
        [sg.Button('Dataframes e RNA', font='Any 12', size=(50, 3), key='dataframes_rna')],
    ]
    layout = [
        [sg.Frame('MENU', frame_layout, font='Any 20', title_color='black', border_width=5)],
        [sg.Button('Alguma coisa', font='Any 12', size=(24, 2)),
         sg.Button('Sair', font='Any 12', size=(24, 2), key='sair')],
    ]
    window_menu = sg.Window('Menu', layout)
    while True:
        event, values = window_menu.Read()
        if event in (sg.WIN_CLOSED, 'sair'):
            break
        if event == 'consulta':
            abrir_consulta()
        if event == 'plotagem':
            window_menu.close()
            abrir_visualizacao_plotagem()
        if event == 'dataframes_rna':
            abrir_dataframes_rna()

    window_menu.Close()


if __name__ == '__main__':
    main()
