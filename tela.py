import PySimpleGUI as sg
# teste


class Interface:

    def __init__(self):

        # LAYOUT
        layout = [
            [sg.Text('Fonte(s)'), sg.InputText()],
            [sg.Text('Mes(es)'), sg.InputText()],
            [sg.Text('Ano(s)'), sg.Input()],
            [sg.Button('Gerar')]
        ]

        # JANELA
        janela = sg.Window('Dados do Dataframe').layout(layout)

        # Extrair dados da tela
        self.button, self.values = janela.Read()

    def Iniciar(self):
        for chave, valor in self.values.items():
            print(valor)


tela = Interface()
tela.Iniciar()
