
class Hash:
    def __init__( self ):
        self.data = []
        for i in range( 0, 51 ):
            self.data.append( None )
    
    def agrega( self, num ):
        indice = int(int((num * 13 + 7) / 3) * 11 / 5 ) % 50
        if self.data[indice] == None:
            self.data[indice] = num
            print( "El número", num, "será agregado en el índice", indice )
        else:
            print( "Hay una colisión, tendremos que hacer un ajuste con una lista" )
    
    def buscaElemento( self, num ):
        indice = int(int((num * 13 + 7) / 3) * 11 / 5 ) % 50
        if self.data[indice] == None:
            print( "Ese número aún no se encuentra en nuestra tabla de hash" )
        else:
            print( "El número se encuentra en el índice", indice, "de nuestra tabla de hash." )
            return indice