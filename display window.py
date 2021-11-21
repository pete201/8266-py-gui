from tkinter.constants import RIGHT
import PySimpleGUI as sg
from decimal import Decimal
from readSerialThread import restartArduino, readArduino
from threading import Thread
from queue import Queue


# firstly restart the 8266...
restartArduino()

# set up a queue to handle the incoming serial input from 8266
# format is Yaw, Pitch, Roll, Button
q = Queue()

# define the layout of the GUI window
layout = [
    [sg.Text('Yaw:', size=8), sg.Text('value', key='yawOut', size=7, justification=RIGHT)],
    [sg.Text('Pitch:', size=8), sg.Text('value', key='pitchOut', size=7, justification=RIGHT)],
    [sg.Text('Roll:', size=8), sg.Text('value', key='rollOut', size=7, justification=RIGHT)],
    [sg.Text('')],
    #[sg.Text('Yaw:'), sg.Input('', key='yawIn', size=6), sg.Text('Pitch:'), sg.Input('', key='pitchIn', size=6), sg.Text('Roll:'), sg.Input('', key='rollIn', size=6)],
    #[sg.Button('Update'), sg.Button('Exit')]
    [sg.Button('Exit')]
]

# start the GUI window using the specified layout
window = sg.Window('8266 readout', layout)

def main():
    # https://realpython.com/intro-to-python-threading/
    # a deamon thread will end when __main__ends (otherwise it will keep running!)
    # set up a thread to read the serial input from 8266 and store in q
    worker = Thread(target=readArduino, args=(q,))
    worker.setDaemon(True)
    worker.start()


    # variables to hold the values read from 8266 input q
    ypr = 0
    button = 1

    while True:
        # look to see if there is data from the 8266
        while q.qsize() > 0:        # while loop reads all available data since last read
            ypr = q.get()
            #print(ypr, "\t", q.qsize())

        # if we have data from 8266 then update the ypr anc button values
        if ypr != 0:
            try:
                yaw = float(ypr[0])
                pitch = float(ypr[1])
                roll = float(ypr[2]) #TODO THIS SHOULD BE ypr[2] for roll
                button = int(ypr[3])
            except:
                #print("serial read exception!")
                pass
        

        # listen for events from the GUI. NOTE there is a timeout so the GUI will update periodically without user input
        event, values = window.read(timeout=500)

        if event in ('Exit', None): break                                   # event 'None' is passed when closing the window by clicking x

        try:                                                                # try necessary to handle non-decimal values (e.g. blank value)
            window['yawOut'].update(round   (yaw, 2))                 # round to 2 decimal places
            window['pitchOut'].update(round (pitch,2))
            window['rollOut'].update(round  (roll,2))
        except: pass


    window.close()


if __name__ == '__main__':
    main()


exit()
