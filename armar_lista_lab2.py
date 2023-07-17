# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 21:48:11 2020

@author: Admin_invitado
"""
import csv

# Creamos la clase node para los clientes
class node:
    def __init__(self, Id = None, Tipo=None, Operacion=None, Tiempo=0, next = None):
        self.Id = Id
        self.Tipo=Tipo
        self.Operacion=Operacion
        self.Tiempo=0
        self.next = next
    
    def __repr__(self):
        return str(self.__dict__)

# Creamos la clase linked_list
class linked_list: 
    def __init__(self):
        self.head = None
    
    # Método para agregar elementos al final de la cola de la linked list
    def add_at_cola(self, nodo):
        nodo.next=self.head
        self.head = nodo

    # Método para verificar si la estructura de datos esta vacia
    def is_empty(self):
        return self.head == None

    # Método para agregar elementos al inicio de la cola en la linked list
    def add_at_primero(self, nodo):
        if not self.head:
            self.head = nodo
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = nodo
    
    # Método para eleminar nodos según el valor del ID
    def delete_node(self, key):
        curr = self.head
        prev = None
        while curr and curr.Id != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    # Método para obtener el ultimo nodo
    def get_last_node(self):
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        return temp

    # Método para imprimir la lista de nodos
    def print_list( self ):
        node = self.head
        while node != None:
            print ("Cliente ID {0} del Tipo {1} y Tiempo de atención {2}".format(node.Id, node.Tipo, node.Tiempo))
            node = node.next

# Esta función permite leer un archivo .csv  datos separados por coma
def leer_archivo_csv(vector, archivo):
    '''
    El archivo en cada línea trae el IdCliente, Tipo de Cliente, Operación
    El Tipo de Cliente será P (preferencial), T (Tercera Edad) y N (Normal)
    La operación a realizar será C (Consignar), R (Retirar) y T (Transferencia)
    '''
    with open(archivo, newline='') as File:  
        reader = csv.reader(File)
        for row in reader:
            '''
              Cada fila (row) trae los 3 campos Id, Tipo y operación
              row es una lista con los tres elementos que son los campos del nodo
              y entonces se mueven al nodo para la lista que queramos utilizar
            '''
            v=node(Id = row[0], Tipo=row[1], Operacion=row[2], Tiempo=0)  
            #v=node(row[0], row[1], row[2], Tiempo=0)
            vector.append(v)



# Código del programa
print("** BIENVENIDO **")
'''
Aquí debe colocar el código para las opciones de menú
'''

'''
A continuación se leeran los datos del archivo
y se almacenan en una lista (vector)
sin tener en cuenta el tipo de cliente
'''
v=[]  #declaro una lista vacia
leer_archivo_csv(v, 'clientes.csv')

'''
Se propone ahora recorrer la lista y aplicar los criterios
del problema, para este ejemplo solo se armara la lista
enlazada pero sin los criterios del problema
'''

cola = linked_list() # Instancia de la clase lista
for elemento in v:
    if elemento.Tipo =="T":
        print("Cliente Tercera Edad")
        # Aquí se agrega de primero hay que ajustar según el problema
        cola.add_at_primero(elemento)
    elif elemento.Tipo=="P":
        print("Cliente Preferencial")
        # Aquí se agrega de último hay que ajustar según el problema
        cola.add_at_cola(elemento)
    else:
        print("Cliente Normal")
        # Aquí se agrega de último sería el caso de cliente normal
        cola.add_at_cola(elemento)

'''
s.add_at_front(5) # Agregamos un elemento al frente del nodo
s.add_at_end(8) # Agregamos un elemento al final del nodo
s.add_at_front(9) # Agregamos otro elemento al frente del nodo
'''
cola.print_list() # Imprimimos la lista de nodos

#Ejemplo de como eliminar un nodo por el ID
cola.delete_node("1015")
print("** prueba **")
cola.print_list() # Imprimimos la lista de nodos