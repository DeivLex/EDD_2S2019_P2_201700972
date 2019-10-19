# Creamos la clase nodo
class Nodo(object):
    def __init__(self,INDEX=None, TIMESTAMP = None , CLASS=None, DATA=None, PREVIOUSHASH = None , HASH=None):
        self.INDEX=INDEX
        self.TIMESTAMP=TIMESTAMP
        self.CLASS=CLASS
        self.DATA=DATA
        self.PREVIOUSHASH=PREVIOUSHASH
        self.HASH=HASH
        self.pSig = None
        self.pAnt = None
    
# Creamos la clase linked_list
class ListaDoble(object): 
    def __init__(self):
        self.__primero = None
        self.__ultimo = None
    
    # Método para verificar si la estructura de datos esta vacia
    def EstaVacia(self):
        if self.__primero == None:
            return True

        # Método para agregar elementos en el frente de la linked list
    def AddInicio(self, INDEX, TIMESTAMP, CLASS, DATA, PREVIOUSHASH , HASH):
        nuevo = Nodo(INDEX,TIMESTAMP,CLASS,DATA,PREVIOUSHASH,HASH)
        if self.EstaVacia()==True:
            self.__primero = self.__ultimo = nuevo
        else:
            nuevo.pSig = self.__primero
            self.__primero.pAnt = nuevo
            self.__primero = nuevo

    # Método para agregar elementos al final de la linked list
    def AddFinal(self, INDEX, TIMESTAMP, CLASS, DATA, PREVIOUSHASH , HASH):
        nuevo = Nodo(INDEX,TIMESTAMP,CLASS,DATA,PREVIOUSHASH,HASH)
        if self.EstaVacia()==True:
            self.__primero = self.__ultimo = nuevo
        else:
            self.__ultimo.pSig = nuevo
            nuevo.pAnt = self.__ultimo
            self.__ultimo = nuevo
    
    # Método para eleminar (Por posicion) nodos
    def Eliminar(self, key):
        anterior = self.__primero
        actual = self.__primero
        k=0
        if key>0:
            while k!=key and actual.pSig !=None:
                anterior = actual
                actual = actual.pSig
                k+=1
            if k==key:
                temporal = actual.pSig
                anterior.pSig = actual.pSig
                temporal.pAnt = anterior
    
    def EliminarPrimero(self):
        if self.EstaVacia()==True:
            print("Lista vacia")
        elif self.__primero == self.__ultimo:
            self.__primero = None
            self.__ultimo = None
        else:
            temp = self.__primero
            self.__primero = self.__primero.pSig
            self.__primero.pAnt = None
            temp = None
    
    def EliminarUltimo(self):
        if self.__ultimo.pAnt==None:
            self.__primero = None
            self.__ultimo = None
        else:
            self.__ultimo = self.__ultimo.pAnt
            self.__ultimo.pSig = None

    # Método para imprimir la lista de nodos
    def Imprimir(self):
        if self.EstaVacia()==True:
            print("Lista vacia")
        else:    
            Validar = True
            node = self.__primero
            while (Validar):
                print(node.HASH,node.PREVIOUSHASH,end =" => ")
                if node == self.__ultimo:
                    Validar = False
                else:
                    node = node.pSig
    def ImprimirAlReves(self):
        if self.EstaVacia()==True:
            print("Lista vacia")
        else:    
            Validar = True
            node = self.__ultimo
            while (Validar):
                print(node.HASH,node.PREVIOUSHASH,end =" => ")
                if node == self.__primero:
                    Validar = False
                else:
                    node = node.pAnt
    
    def head(self):
        return self.__primero 

    def final(self):
        return self.__ultimo

    def vaciar(self):
        self.__primero=None
        self.__ultimo=None

