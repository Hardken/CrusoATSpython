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

#Codigo Programa
opc= 'False'
while opc == 'False':
    print("Bievenido")
    print("1.Ingresar clientes al Banco")
    print("2.Presentar cola de atencion")
    print("3.Atender a los clientes y generar Promedios de tiempo de atencion")
    print("4.salir")
    n=int(input("Digite la opcion que desea realizar: "))
    Tiempo3raedad = 0
    teraedad = 0
    Tiempopreferencial = 0
    prefe = 0
    TiempoaNormal = 0
    norm = 0
    if n==1:
        v=[]  #declaro una lista vacia
        print("Se estan ingresando los clientes")
        leer_archivo_csv(v, 'clientes.csv')
        cola = linked_list() # Instancia de la clase lista
        print("Se han ingresa los clientes")
    opc=str(input("Desea salir otra vez al menu? true=si/false=no: "))
    print("Bievenido")
    print("1.Ingresar clientes al Banco")
    print("2.Presentar cola de atencion")
    print("3.Atender a los clientes y generar Promedios de tiempo de atencion")
    print("4.salir")
    n=int(input("Digite la opcion que desea realizar: "))
    if n==2:
        for elemento in v:            
            if elemento.Tipo== "N":         
                if elemento.Tipo=="N" and elemento.Operacion == "C":
                    print("Cliente Normal")
                    # Aquí se agrega de último hay que ajustar según el problema
                    elemento.Tiempo = 6
                    TiempoaNormal = TiempoaNormal + elemento.Tiempo
                    cola.add_at_cola(elemento)    
                    norm = norm + 1
                elif elemento.Tipo=="N" and elemento.Operacion == "T":
                    print("Cliente Normal")
                    # Aquí se agrega de último hay que ajustar según el problema
                    elemento.Tiempo = 6
                    TiempoaNormal = TiempoaNormal + elemento.Tiempo
                    cola.add_at_cola(elemento)    
                    norm = norm + 1                             
                elif elemento.Tipo=="N" and elemento.Operacion == "R":
                    print("Cliente Normal") 
                    # Aquí se agrega de último sería el caso de cliente normal
                    elemento.Tiempo = 6
                    TiempoaNormal = TiempoaNormal + elemento.Tiempo
                    cola.add_at_cola(elemento)
                    norm = norm + 1        
        for elemento in v:              
            if elemento.Tipo== "P":               
                if elemento.Tipo=="P" and elemento.Operacion == "C":
                    print("Cliente Preferencial")
                    # Aquí se agrega de último hay que ajustar según el problema
                    elemento.Tiempo = 8
                    Tiempopreferencial = Tiempopreferencial + elemento.Tiempo
                    cola.add_at_primero(elemento)
                    prefe = prefe + 1
                elif elemento.Tipo=="P" and elemento.Operacion == "T":
                    print("Cliente Preferencial")
                    # Aquí se agrega de último hay que ajustar según el problema
                    elemento.Tiempo = 6
                    Tiempopreferencial = Tiempopreferencial + elemento.Tiempo
                    cola.add_at_primero(elemento)
                    prefe = prefe + 1
                elif elemento.Tipo=="P" and elemento.Operacion == "R":
                    print("Cliente Preferencial")
                    # Aquí se agrega de último hay que ajustar según el problema
                    elemento.Tiempo = 6
                    Tiempopreferencial = Tiempopreferencial + elemento.Tiempo
                    cola.add_at_primero(elemento)  
                    prefe = prefe + 1
        for elemento in v:
            if elemento.Tipo== "T": 
                if elemento.Tipo =="T" and elemento.Operacion == "C":
                    print("Cliente Tercera Edad")
                    # Aquí se agrega de primero hay que ajustar según el problema
                    elemento.Tiempo = 12
                    Tiempo3raedad = Tiempo3raedad + elemento.Tiempo
                    cola.add_at_primero(elemento)
                    teraedad = teraedad + 1
                elif elemento.Tipo =="T" and elemento.Operacion == "T":
                    print("Cliente Tercera Edad")
                    # Aquí se agrega de primero hay que ajustar según el problema
                    elemento.Tiempo = 10
                    Tiempo3raedad = Tiempo3raedad  + elemento.Tiempo
                    cola.add_at_primero(elemento)    
                    teraedad = teraedad + 1
                elif elemento.Tipo =="T" and elemento.Operacion == "R":
                    print("Cliente Tercera Edad")
                    # Aquí se agrega de primero hay que ajustar según el problema
                    elemento.Tiempo = 9
                    Tiempo3raedad =Tiempo3raedad + elemento.Tiempo
                    cola.add_at_primero(elemento)
                    teraedad = teraedad + 1                    
    cola.print_list()
    opc=str(input("Desea salir otra vez al menu? true=si/false=no: "))
    print("Bievenido")
    print("1.Ingresar clientes al Banco")
    print("2.Presentar cola de atencion")
    print("3.Atender a los clientes y generar Promedios de tiempo de atencion")
    print("4.salir")
    n=int(input("Digite la opcion que desea realizar: "))
    if n==3:
        Tiempo3raedad = (Tiempo3raedad/teraedad)
        Tiempopreferencial = (Tiempopreferencial/prefe)
        TiempoaNormal = (TiempoaNormal/norm)
        print(f"El promedio de atencion a un cliente de 3ra edad es: {Tiempo3raedad}")
        print(f"El promedio de atencion a un cliente preferencial es: {Tiempopreferencial}")
        print(f"El promedio de atencion a un cliente normal es: {TiempoaNormal}")
    opc=str(input("Desea salir otra vez al menu? true=si/false=no: "))
    print("Bievenido")
    print("1.Ingresar clientes al Banco")
    print("2.Presentar cola de atencion")
    print("3.Atender a los clientes y generar Promedios de tiempo de atencion")
    print("4.salir")
    n=int(input("Digite la opcion que desea realizar: "))
    if n==4:
        opc = 'True'
        print("Fin del programa")
        exit()