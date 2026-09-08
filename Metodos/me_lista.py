#creando una lista con list()
lista = list(["corsair","razer","logitech"])

#devulve la cantidad de elementos
cantidad_elementos = len(lista)

#Agregando un elemento a la lista
lista.append("msi")

#agregando un elemento a la lista en un indice exacto
lista.insert(2,"lenovo")

#agregando varios elementos a la lista
lista.extend(["lg","samsung"])

#eliminando un elemento de la lista por el indice
lista.pop(0)
lista.pop(-1) #elimina del ultimo hacia atras (-1, -2...)

#removiendo un elemento de la lista por su valor
lista.remove("msi")

#eliminando todos los elementos de la lista
#lista.clear()

#ordenando la lista ascendente,  si usamos el parametro reverse= true lo ordena en reverssa
lista2 = list([False, True, True, 12, 12321, 9090])
#lista2.sort()

#invirtiendo los elementos de una lista
lista2.reverse()

print(lista2)
