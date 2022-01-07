import threading 
import time
import sys
import os
import random

# implementacion de una cola de series []
class Queue_de_series:
    def __init__(self):
        self.series = []

    def isEmpty(self):
        return self.series == []

    def enqueue(self, serie):
        self.series.insert(0,serie)

    def dequeue(self):
        if self.size()==0:
            print("lista vacia")
            return ("lista vacia")
        return self.series.pop()

    def size(self):
        return len(self.series)

#definir la main queue para las series      
queue = Queue_de_series()
global mutex_piscina1
global mutex_piscina2
mutex_piscina1 = threading.Lock()
mutex_piscina2 = threading.Lock()
class rellenador_series(threading.Thread):
    def run(self):
        
        while (True):
            # tiempo para encolar la serie
            print("encolando")
            time.sleep(random.randint(1, 5))
            time.sleep(10)
            # encolar la serie
            queue.enqueue([1,2,3,4,5,6,7,8])
            print("ingresado: ", [1,2,3,4,5,6,7,8] )
            time.sleep(1)




#Para desencolar hay 2 threds 1 para cada 
class desencolador(threading.Thread):
    def run(self):
        while (True):
            mutex_piscina1.acquire()
            print("desencolando")
            # tiempo para desencolar la serie
            time.sleep(random.randint(1, 7))
            #time.sleep(3)
            # encolar la serie
            queue.dequeue()
            print("sacada una serie a piscina 1")
            mutex_piscina1.release()
            mutex_piscina2.acquire()
            print("desencolando")
            # tiempo para desencolar la serie a la piscina 1
            time.sleep(random.randint(1, 7))
            #time.sleep(3)
            # encolar la serie
            queue.dequeue()
            print("sacada una serie a piscina 2")
            mutex_piscina2.release()


rellenador = rellenador_series()
rellenador.start()
desencolador=desencolador()
desencolador.start()

rellenador.join()
desencolador.join()


