from Node import Node

class Hash:
    def __init__( self ):
        self.data = []
        self.capacidad = 5
        for i in range( 0, self.capacidad + 1 ):
            self.data.append( None )
    
    def agrega( self, nuevoNodo ):
        indice = int(int((nuevoNodo.identificador * 13 + 7) / 3) * 11 / 5 ) % self.capacidad
        if self.data[indice] == None:
            self.data[indice] = nuevoNodo
            print( "El nodo será agregado en el índice", indice )
        else:
            aux = self.data[indice]
            while aux.next != None:
                aux = aux.next
            aux.next = nuevoNodo
            print( "El nodo será agregado en el índice", indice, "Ya existía un nodo en este índice." )
    
    def buscaElemento( self, num ):
        indice = int(int((num * 13 + 7) / 3) * 11 / 5 ) % self.capacidad
        if self.data[indice] == None:
            print( "Ese número aún no se encuentra en nuestra tabla de hash" )
        else:
            print( "El número se encuentra en el índice", indice, "de nuestra tabla de hash." )
            return indice

    def actualizaElemento( self, identificador, nombre, apellido ):
        indice = int(int((identificador * 13 + 7) / 3) * 11 / 5 ) % self.capacidad
        if self.data[indice] == None:
            print( "No tenemos nada que actualizar, el identificador no existe en nuestra tabla de Hash." )
        else:
            if self.data[indice].next == None:
                if self.data[indice].identificador == identificador:
                    self.data[indice].nombre = nombre
                    self.data[indice].apellido = apellido
                else:
                    print( "No tenemos nada que actualizar, el identificador no existe en nuestra tabla de Hash." )
            else:
                aux = self.data[indice]
                while aux != None:
                    if aux.identificador == identificador:
                        aux.nombre = nombre
                        aux.apellido = apellido
                        return "Nodo actualizado"
                    else:
                        aux = aux.next
                print( "No tenemos nada que actualizar, el identificador no existe en nuestra tabla de Hash." )

