
class Nodo():
    def __init__(self, valor):
        self.izquierda=None
        self.derecha=None
        self.valor=valor
        self.altura=1

class Arbol_AVL():
    def __init__(self,Nodo):
        self.raiz=Nodo

    def balancear(Nodo):

        actualizar_altura(Nodo)
        dif = H(Nodo.izquierda())-H(Nodo.derecha())

        if(dif > 1):

            if (H(Nodo.izquierda().izquierda()) > H(Nodo.izquierda().derecha())):
                Nodo=rotar_derecha(Nodo)
            else:
                Nodo.izquierda=rotar_izquierda(Nodo.izquierda())
                Nodo=rotar_derecha(Nodo)
        
        elif(dif < 1):
            
            if( H (Nodo.derecha().derecha()) > H(Nodo.derecha().izquierda()) ):
                Nodo.rotar_izquierda(Nodo)
            else:
                Nodo.derecha= rotar_derecha(Nodo.derecha())
                Nodo=rotar_izquierda(Nodo)

        return Nodo;  

    def insertar(self,Nodo,valor):
        if(Nodo == None):
            return  Nodo(valor)
        
        elif(valor < Nodo.valor()):
            Nodo.izquierda=insertar(Nodo.izquierda(),valor)

        elif(valor > Nodo.valor()):
            Nodo.derecha=insertar(Nodo.derecha().valor)
        else:
            print("valor duplica3")
        
        return balancear(Nodo)

    def buscar(self,Nodo,valor):
        if Nodo is None:
            return False
        if Nodo.valor > valor:
            return self.buscar( Nodo.izquierda,valor)
        elif Nodo.valor < valor:
            return self.buscar( Nodo.derecha,valor)
        return Nodo

    def borrar(Nodo,valor):
        if(Nodo==None):
            return Nodo

        elif(valor < Nodo.valor()):
            Nodo.izquierda=borrar(Nodo.izquierda(),valor)

        elif(valor > Nodo.valor()):
            Nodo.derecha=borrar(Nodo.derecha(),valor)
        else:
            if(Nodo.izquierda==None):
                Nodo =  Nodo.derecha

            elif(Nodo.derecha==None):
                Nodo = Nodo.izquierda
            
            else:
                decendiente_masizq=decendiente_masizq(Nodo.derecha())
                Nodo.valor=decendiente_masizq.valor
                Nodo.derecha=borrar(Nodo.derecha(),N.valor())

        if(Nodo!= None):
            Nodo =balancear(Nodo)
        return Nodo

    def H(Nodo):
        return Nodo.altura
    
    def actualizar_altura(Nodo):
        if (Nodo==None):
            return 0
        else:
            Nodo.altura=Nodo.altura + max(H(Nodo.derecha()),H(Nodo.ezquierda()))
            return Nodo.altura

    def decendiente_masizq(Nodo):
        if(Nodo==None):
            return None
        else:
            if (Nodo.ezquierda()!=None):
                decendiente_masizq(Nodo.izquierda)
            else:
                return Nodo






