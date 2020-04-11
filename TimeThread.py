
import threading
import time
import os

class TimeThread (threading.Thread):
  
    def __init__(self):
        threading.Thread.__init__(self)
        self.stopit = threading.Event()
  
    def stop(self):
        self.stopit.set()

    def isStopped(self):
        return self.stopit.isSet()

    def run(self):
        cont = 10
        #function to measure the time in a different thread
        while True:
            
            if self.isStopped():
                return
            elif (cont) ==0:
                print("Se acabo tu tiempo, presiona enter para continuar")
                return
            print("{}.".format(cont),end=' ' )
            cont-=1
            time.sleep(1)