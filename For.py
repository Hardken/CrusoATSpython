# Bucle for

for i in [1,2,3,4,5]:
    print("Hola mundo")

coleccion= (1,2,3,4,5, "Andres")

for i in coleccion:
    print(f"Elemento: {i}")

coleccion2 = {"Andres":19,"Naria":23,"jose":45,"luis":12}
for i in coleccion2:
    print(f"{coleccion2[i]}")
    print(f"{i} -> {coleccion2[i]}")

for clave,valor in coleccion2.items():
    print(f"{clave} -> {valor}")

coleccion3 = "Andres"
for i in coleccion3:
    print(f"Hola")
    print(f"{i}")
    print(f"{i}", end=".")

for