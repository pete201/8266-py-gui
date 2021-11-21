from readSerialThread import restartArduino, readArduino
from threading import Thread
from queue import Queue


def constrain(val, valMin, valMax):
    if val < valMin:
        val = valMin
    if val > valMax:
        val = valMax
    return val


restartArduino()


q = Queue()

def main():
  # https://realpython.com/intro-to-python-threading/
  # a deamon thread will end when __main__ends (otherwise it will keep running!)
  worker = Thread(target=readArduino, args=(q,))
  worker.setDaemon(True)
  worker.start()

  ypr = 0
  button = 1

  while True:
    while q.qsize() > 0:        # while loop reads all available data since last read
        ypr = q.get()
        #print(ypr, "\t", q.qsize())


    if ypr != 0:
        try:
            yaw = float(ypr[0])
            pitch = float(ypr[1])
            roll = float(ypr[2]) #TODO THIS SHOULD BE ypr[2] for roll
            button = int(ypr[3])


        except:
            #print("exception!")
            pass

    if keyboard.is_pressed('esc'):
        break


  #q.join()   # do NOT do this as main will not exit since threads are still running
  exit()


if __name__ == '__main__':
    main()


exit()





    

