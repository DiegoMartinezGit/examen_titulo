
import threading 
import time
import sys
import os
import random
class Queue_despacho:
    def __init__(self):
        self.pedidos = []

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
        return len(self.pedidos)

class Preparador_pedido(threading.Thread):
    def run(self):
        
        while (True):
            # tiempo para preparar pedido
            print("llega pedido")
            #time.sleep(random.randint(1, 5))
            time.sleep(5)
            # encolar a cola de despacho
            queue.enqueue([1,2,3,4,5,6,7,8])
            print("ingresado: ", [1,2,3,4,5,6,7,8] )
            time.sleep(1)

class Despachador(threading.Thread):
    def run(self):
        while (True):
            # tiempo para encolar la serie
            print("llega pedido")
            time.sleep(random.randint(1, 5))
            time.sleep(10)
            # encolar pedido
            queue.enqueue([1,2,3,4,5,6,7,8])
            print("ingresado: ", [1,2,3,4,5,6,7,8] )
            time.sleep(1)