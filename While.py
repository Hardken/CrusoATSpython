#Bucle While
import math
numero =int(input("Digite un numero: "))

while numero<0:
    print("Error-> Numero debe ser un numero positivo")
    numero =int(input("Digite un numero: "))

print(f"\nSu raiz cuadrada es: {(math.sqrt(numero)):.2f}")

i = 0
while i<10:
    print(i)
    i += 1