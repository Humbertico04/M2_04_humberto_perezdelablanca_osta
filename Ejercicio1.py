#Creo una lista y una tupla que incluyen colores y las muestro por pantalla
lista = ["Blanco", "Azul", "Rojo", "Amarillo"]
tupla = ("Negro", "Morado", "Verde", "Naranja")
print(lista)
print(tupla)

print("\n")

#Muestro por pantalla el segundo elemento de la lista y el penúltimo de la tupla
print(lista[1])
print(tupla[-2])

print("\n")

#Modifico un elemento de la lista, en las tuplas esto no es posible
lista[0]="Marrón"
print(lista)
print(tupla)

print("\n")

#Muestro por pantalla el número de elementos de la lista y la tupla
print(len(lista))
print(len(tupla))

print("\n")

#Compruebo si "Azul" está incluido en la lista y/o en la tupla
print("Azul" in lista)
print("Azul" in tupla)

print("\n")

#Le añado un elemento a lista. Una vez más no es posible hacer esto con la tupla pues es inmutable.
lista.append("Blanco")
print(lista)
print(tupla)

print("\n")

#Elimino todo el contenido de la lista y lo muestro, la tupla es intocable
del lista[:]
print(lista)
print(tupla)