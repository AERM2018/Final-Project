
import threading
import time

class TimeThread (threading.Thread):
    #constructor method
    def __init__(self)
        threading.Thread.__init__(self)
        #create a internal variable that allow me to stop the thread, at the begginig is False
        self.stopit = threading.Event()
        
    # this method change the value of the variable and set it on True
    def stop(self):
        self.stopit.set()
    # it method returns me the variable's value
    def isStopped(self):
        return self.stopit.isSet()
    
    # this is what the thread is going to do when I invoke the function start in the main thread
    def run(self):
        cont = 12
        #function to measure the time in a different thread
        while True:
            
            if self.isStopped():
                return
            elif (cont) ==0:
                print("Se acabo tu tiempo, presiona enter para continuar")
                return
            print("{} ->".format(cont),end=' ' )
            cont-=1
            time.sleep(1)
