from Hash import Hash
from Node import Node

tablaNumeros = Hash()

persona1 = Node( "Alex", "Martinez", 123 )
tablaNumeros.agrega( persona1 )
persona2 = Node( "Martha", "Sanchez", 456 )
tablaNumeros.agrega( persona2 )
persona3 = Node( "Antonio", "Morales", 789 )
tablaNumeros.agrega( persona3 )

print(tablaNumeros.data[1].identificador )
print(tablaNumeros.data[1].next.identificador )






# Almacenar Nodos que contengan campos para nombre, apellido, identificador, next.
# Agregar nodos a la tabla de Hash en lugar de números enteros.
# Modificar el método para que reciba un Nodo. 
# En el agrega contemplar la lógica para colisiones. 

# Crear el método actualiza elemento. Este método recibe un identificador y los campos 
# a actualizar.
# En caso de que no se encuentre el nodo mostrar el mensaje "Identificador no encontrado"

# Crear el método borra elemento. Este método recibe un identificador para eliminar de
# la tabla de Hash. 
# En caso de que no se encuentre el nodo mostrar el mensaje "Identificador no encontrado"