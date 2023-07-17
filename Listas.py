#Listas = arreglos o vectores

lista = ["Lunes","Martes","Miercoles","Jueves","Viernes",40,5.67,[1,2,3],True]

print(lista)#imprime toda la lista
print(lista[0])#imprime el lunes 
print(lista[-1])#imprime el viernes, comiensa desde el ultimo elemento de la lista
print(lista[0:3])#imprime desde el lunes hasta el miercoles pues va una hasta una posicion anterior del ultimo numero
print(lista[2:])#imprime desde el martes
print(len(lista))#cuenta cuantos elementos hay en la lista


Lista = [1,2,4,5]
Lista.append(6)#agrega elementos al final de la lista
Lista.insert(2,3)#agg en la posicion 2 el numero 3
Lista.extend([7,8,9])#cancatena listas o las junta dejando los añadidos al final de la lista
Lista2 = [10,11,12]
Lista3 = [Lista+Lista2]#sima las listas
print(3 in Lista)#Busca si el elemento esta en la lista
print(Lista.index(5))#da la posicion en la que este ubicado el elemento deseado 
LiTa = [1,2,3,4,5,"Andres",1,2,3,1,"Andres",1]#pueden haber valores repetidos
print(LiTa.count(1))#dice cuantos elemtentos hay en una lista, en este caso cuantas veces el 1 aparece en la lista
Lista.pop()#Elimina el ultimo valor en la lista
Lista.pop(2)#Elimina el valor en la posicion indicada de la lista
Lista.remove(5)#Elimina el valor indicado de la lista en este caso el 5
Lista.clear()#Elimina todos los elementos de la lista dejandola vacia
Lista.reverse()#invierte la lista
LisTaa = [5,4,-7,9,0,2,11,3]
LisTaa.sort()#ordena la lista ascendentemente
LisTaa.sort(reverse=True)#ordena la lista descendentemente