class Nodo:
    def __init__(self,dato=None):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaCircularDoble:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        if self.primero == None:
            return True
        else:
            return False
    
    def agregar_inicio(self,dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
        self.unir_nodos()
    
    def agregar_final(self,dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
        self.unir_nodos()

    def EliminarPrimero(self):
        if self.vacia():
            print("Tu estructura esta vacia")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.siguiente
        self.unir_nodos()

    def EliminarUltimo(self):
        if self.vacia():
            print("Tu estructura esta vacia")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.ultimo = self.ultimo.anterior
        self.unir_nodos()
    
    def unir_nodos(self):
        self.primero.anterior = self.ultimo
        self.ultimo.siguiente = self.primero

    def RecorrerInicioFin(self):
        aux = self.primero
        while aux:
            print(aux.dato)
            aux = aux.siguiente
            if aux == self.primero:
                break
    
    def RecorrerFinInicio(self):
        aux = self.ultimo
        while aux:
            print(aux.dato)
            aux = aux.anterior
            if aux == self.ultimo:
                break

    def longitud(self):
        nodo = self.primero
        numero = 1
        while nodo != self.ultimo:
            nodo=nodo.siguiente
            numero+=1
        return numero

    def getPrimero(self):
        return self.primero

    def getUltimo(self):
        return self.ultimo
