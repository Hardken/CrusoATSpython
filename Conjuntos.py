#conjuntos

conjunto = set()#creacion de un conjunto vacio
conjunto = {1,2,3,"hola",4.56}#cualquier tipo de dato menos otra coleccion, lista/tupla, etc y valores duplicados#se puede def asi tambien solo que para python esto seria un diccionario si no tubiera datos
conjunto.add(5)#añade el dato en cualquier posicion
conjunto.discard(3)#elimina un dato del conjunto
conjunto.clear()#deja el conjunto vacio elimando todos los datos que contiene
print(3 in conjunto)#buscar dato o elemento en el conjunto
print(conjunto)

a = {1,2,3}
b = {3,5,6}

c = a | b #union de dos conjuntos
c = a - b #diferencia del conjunto elementos que no estan eb b pero si en a

print()