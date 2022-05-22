import PySimpleGUI as sg

if __name__ == '__main__':
    layout = [[]]

    window = sg.Window('Company Analysis', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

    window.close()
