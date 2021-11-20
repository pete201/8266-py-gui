from tkinter.constants import RIGHT
import PySimpleGUI as sg
from decimal import Decimal

layout = [
    [sg.Text('Yaw:', size=8), sg.Text('value', key='yawOut', size=7, justification=RIGHT)],
    [sg.Text('Pitch:', size=8), sg.Text('value', key='pitchOut', size=7, justification=RIGHT)],
    [sg.Text('Roll:', size=8), sg.Text('value', key='rollOut', size=7, justification=RIGHT)],
    [sg.Text('')],
    [sg.Text('Yaw:'), sg.Input('', key='yawIn', size=6), sg.Text('Pitch:'), sg.Input('', key='pitchIn', size=6), sg.Text('Roll:'), sg.Input('', key='rollIn', size=6)],
    [sg.Button('Update'), sg.Button('Exit')]
]

window = sg.Window('8266 readout', layout)


while True:
    event, values = window.read()

    if event in ('Exit', None): break                                   # event 'None' is passed when closing the window by clicking x

    try:                                                                # try necessary to handle non-decimal values (e.g. blank value)
        window['yawOut'].update(round(Decimal(values['yawIn']), 2))     # 'values' are strings - convert to Decimal and round to 2 decimal places
        window['pitchOut'].update(round(Decimal(values['pitchIn']),2))
        window['rollOut'].update(round(Decimal(values['rollIn']),2))
    except: pass

window.close()
