
class Nodo():
    def __init__(self, valor):
        self.izquierda=None
        self.derecha=None
        self.valor=valor
        self.altura=1

class Arbol_AVL():
    def __init__(self):
        self.raiz=None

    def balancear(T):

        actualizar_altura(T)
        dif = H(T.izquierda())-H(T.derecha())

        if(dif > 1):

            if (H(T.izquierda().izquierda()) > H(T.izquierda().derecha())):
                T=rotar_derecha(T)
            else:
                T.izquierda=rotar_izquierda(T.izquierda())
                T=rotar_derecha(T)
        
        elif(dif < 1):
            
            if( H (T.derecha().derecha()) > H(T.derecha().izquierda()) ):
                T.rotar_izquierda(T)
            else:
                T.derecha= rotar_derecha(T.derecha())
                T=rotar_izquierda(T)

        return T;  

    def insertar(self,T,valor):
        if(T == None):
            self.raiz=Nodo(valor)
            return  Nodo(valor)
        
        elif(valor < T.valor()):
            T.izquierda=insertar(T.izquierda(),valor)

        elif(valor > T.valor()):
            T.derecha=insertar(T.derecha().valor)
        else:
            print("valor duplica3")
        
        return balancear(T)

    def buscar(valor):
        actual=self.raiz
        
        while(actual!=N)

    def borrar(T,valor):
        return T

    def actualizar_altura(T):
        return T
    
    def H(T):
        if (T==None):
            return 0
        else:
           
            return T.altura + max(H(T.derecha()),H(T.ezquierda()))
        




