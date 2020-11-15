from random import randrange
import PySimpleGUI as sg

layout = [[sg.Image('sheldon.png', key='-shuffle-', enable_events=True)],
          [sg.Button('Exit')]]
window = sg.Window('BBT Picker', layout)

while True:
    event, value = window.Read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == '-shuffle-':
        season = randrange(1,12,1)
        if season == 1:
            episode = randrange(1,17,1)
        elif season == 2 or season == 3:
            episode = randrange(1,23,1)
        else:
            episode = randrange(1,14,1)
        sg.popup(f'S{season}E{episode}')

window.Close()