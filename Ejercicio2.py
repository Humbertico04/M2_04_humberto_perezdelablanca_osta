#Creo un set y un diccionario que incluyen colores y las muestro por pantalla
set=set(["Azul", "Rojo", "Amarillo", "Azul"])
print(set)
print("\n")
diccionario = {"Morado":"Poder", "Verde":"Tiempo","Naranja":"Alma"}
print(diccionario,"\n")

#No es posible mostrar un elemento ordenado de un set, pues estos no tienen orden. Del diccionario tampoco es posible obtener una clave:valor porque tampoco tiene orden, sin embargo a través de claves podemos obtener valores.
print(diccionario['Morado'],"\n")

#Los elementos de un set no se pueden modificar, sin embargo, los del diccionario si.
diccionario["Verde"] = "Extraño"
print(diccionario, "\n")

#Usamos la función len para ver el tamaño
print("Tamaño del set:", len(set))
print("Tamaño del set:", len(diccionario), "\n")

#Usamos in para comprobar si los elementos están incluidos o no
print("Rojo" in set)
print("Negro" in diccionario, "\n")

#Añadimos elementos al set con .add() y al diccionario
set.add("Blanco")
print(set)
diccionario["Celeste"] = "Ego"
print(diccionario, "\n")

#Probamos que se pueden eliminar elementos individualmente y después eliminamos todo el contenido con .clear()
set.remove("Azul")
del diccionario["Verde"]
print(set)
print(diccionario, "\n")
set.clear()
print(set)
diccionario.clear()
print(diccionario)