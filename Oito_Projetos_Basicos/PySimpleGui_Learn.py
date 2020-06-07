import PySimpleGUI as sg

sg.theme('Dark')   # Add a touch of color
# All the stuff inside your window.
layout = [
            [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')]
         ]
# sg.set_options(size=(5000, 4000))
# Create the Window
window = sg.Window('Window Title', layout, size=(500, 500))
# Size window
# w, h = sg.Window.get_screen_size()
# print(w, h)
# window.Size((5000, 5000))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
