from Hash import Hash
from Node import Node

tablaNumeros = Hash()

persona1 = Node( "Alex", "Martinez", 123 )
tablaNumeros.agrega( persona1 )
persona2 = Node( "Martha", "Sanchez", 456 )
tablaNumeros.agrega( persona2 )
persona3 = Node( "Antonio", "Morales", 789 )
tablaNumeros.agrega( persona3 )

tablaNumeros.actualizaElemento( 123, "Alexander", "Gomez" )
tablaNumeros.actualizaElemento( 789, "Julieta", "Martinez" )

tablaNumeros.actualizaElemento( 562, "Ruebn", "Dainitin" )

# Crear el método borra elemento. Este método recibe un identificador para eliminar de
# la tabla de Hash. 
# En caso de que no se encuentre el nodo mostrar el mensaje "Identificador no encontrado"

# Crea un método que aumente la capacidad de la tabla de hash.
# Actualizar la capacidad nueva.
# Reacomodar los nodos/elementos que ya existían dentro de la tabla de hash.
