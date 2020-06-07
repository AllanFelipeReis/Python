import PySimpleGUI as sg
from funcao import valor_dado


sg.theme('Dark')


tx_titulo = sg.Text('Simulador de Dado', size=(500, None),
                    justification='center')
bt_girar_dado = sg.Button('Girar o Dado', key='Girar', pad=((30, 0), 20))
bt_sair = sg.Button('Sair', button_color=('white', 'red'), pad=((30, 0), 20))
tx_resp = sg.Text(size=(500, None), justification='center', key='Resp')


desenho = [
            [tx_titulo],
            [bt_girar_dado, bt_sair],
            [tx_resp]
        ]


janela = sg.Window('Simulador de Dado', desenho, size=(300, 200))


while True:

    event, values = janela.read()

    if event in (None, 'Sair'):
        break

    if event == 'Girar':
        janela['Resp'].update(valor_dado())

janela.close()
