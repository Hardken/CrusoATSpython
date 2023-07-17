#condicionales en python

numero = int(input("Digite un numero: "))

if numero>0:
    print("El numero es positivo")#con la sangria se sabe si pertenece al if
elif numero==0:#else if
    print("El numero es cero 0")
else:
    print("El numero es negativo")#con la sangria se sabe si pertenece al else

print("fin del programa")# ya no pertenese al if

#condicionales combinados
edad= int(input("Digite su edad: "))

if edad>0 and edad<100: #condicionales combinados, #0<edad<100 es lo mismo que edad>0 and edad<100: #no existen los swicht
    print("Edad correcta")
    if edad>=18:
        print("es mayor de edad")
else:
    print("Edad incorrecta")
