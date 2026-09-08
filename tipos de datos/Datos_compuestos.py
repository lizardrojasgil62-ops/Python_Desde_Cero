#Lista: es un conjunto de datos que puede contener diferentes tipos de datos, como cadenas de texto, números y valores booleanos.
lista=["manzana", "banana", True, 1, 2, 3.5 ]

#Las listas se pueden enumerar, creando diferentes listas.
lista2=["pera", "sandía", False, 4, 5, 6.5 ]

#Para seleccionar un elemento de la lista, entre corchetes se indica el orden del elemento del 0 al 9.
print( lista[0] ) # manzana

#Tupla: es lo mismo que una lista, pero no se puede modificar, es decir, no se pueden agregar, eliminar o cambiar elementos de la tupla.
tupla=("manzana", "banana", True, 1, 2, 3.5)
print( tupla ) # ('manzana', 'banana', True, 1, 2, 3.5)
print( tupla[0] ) # manzana

#SET: es un conjunto de datos que no permite elementos duplicados y no se puede acceder a los elementos mediante un índice.
set={"manzana", "banana", True, 1, 2, 3.5}
#print( set[1]) Error

#Diccionario (DICT): es como una lista pero en vez de usar el indice, se usan keys. Se ponen comas entre (keys:value) menos el ultimo.
dict={
    #key: value
    'nombre': "Pablo",
    'edad': 18,
    'esta_emocionado': True,
    'altura': 1.68
}
#print(dict[1]) Error
print(dict["nombre"]) #Pablo
