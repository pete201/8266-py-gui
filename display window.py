from tkinter.constants import RIGHT
import PySimpleGUI as sg

layout = [
    [sg.Text('Yaw:', size=8), sg.Text('value', key='yawOut')],
    [sg.Text('Pitch:', size=8), sg.Text('value', key='pitchOut', justification=RIGHT)],
    [sg.Text('Roll:', size=8), sg.Text('value', key='rollOut')],
    [sg.Text('')],
    [sg.Text('Yaw:'), sg.Input('', key='yawIn', size=6), sg.Text('Pitch:'), sg.Input('', key='pitchIn', size=6), sg.Text('Roll:'), sg.Input('', key='rollIn', size=6)],
    [sg.Button('Update'), sg.Button('Exit')]
]

window = sg.Window('8266 readout', layout)



while True:
    event, values = window.read()

    if event in ('Exit', None): break

    #print(values['yawIn'])

    window['yawOut'].update(values['yawIn'])
    window['pitchOut'].update(values['pitchIn'])
    window['rollOut'].update(values['rollIn'])
    

window.close()
