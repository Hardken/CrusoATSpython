#Tuplas
tupla=(4,"Hola",1.78,[1,2,3],4)
lista = list(tupla) #combertir tupla a lista
lista1= [4,"Hola",1.78,[1,2,3],4]
tupla1 = tupla(lista1) #combierte una lista en una tupla
print(tupla)
print(tupla[1,-3,1:])
print(tupla.index())
print(tupla.count())
print(len(tupla))