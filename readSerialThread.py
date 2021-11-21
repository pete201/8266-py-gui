import serial
import json
from queue import Queue
from threading import Thread


MyFile = open('.vscode/arduino.json')
MyData = json.load(MyFile)
MyPort = MyData['port']
MyFile.close()

arduino = serial.Serial(port=MyPort, baudrate=115200, timeout=.1)
arduino.reset_input_buffer


def restartArduino():
  arduino.close
  arduino.reset_input_buffer
  arduino.open


def readArduino(commQ):
  while True:
    while arduino.in_waiting > 1:
      data = str(arduino.readline())    # data format is Yaw[0], Pitch[1], Roll[2], Button[3]

      try:
        if 'ypr' and '\\n' in data:
          yaw = data.split('\\t')[1]
          pitch = data.split('\\t')[2]
          roll = data.split('\\t')[3]
          button = data.split('\\t')[4].replace('\\r\\n\'','')

          commQ.put([yaw,pitch,roll,button])
          commQ.task_done()
      except:
        pass


q = Queue()

def main():
  
  worker = Thread(target=readArduino, args=(q,))
  worker.setDaemon(True)
  worker.start()

  for x in range(20):
    print(q.get())

  #q.join()   # do NOT do this as main will not exit since threads are still running

  exit()

    

if __name__ == '__main__':
    main()