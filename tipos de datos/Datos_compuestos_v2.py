# =========================
# DATOS COMPUESTOS
# =========================


# -------------------------
# LISTA (list)
# -------------------------

# Una lista es un conjunto de datos que puede contener
# diferentes tipos de datos, como cadenas de texto,
# números y valores booleanos.

lista = ["manzana", "banana", True, 1, 2, 3.5]

# Podemos crear diferentes listas.

lista2 = ["pera", "sandía", False, 4, 5, 6.5]

# Para seleccionar un elemento de la lista,
# utilizamos su índice entre corchetes [].
#
# IMPORTANTE: los índices empiezan en 0.

print(lista[0])  # manzana
print(lista[1])  # banana


# -------------------------
# TUPLA (tuple)
# -------------------------

# Una tupla es parecida a una lista,
# pero no se puede modificar después de crearla.
#
# No podemos agregar, eliminar o cambiar
# elementos de una tupla.

tupla = ("manzana", "banana", True, 1, 2, 3.5)

print(tupla)
# ('manzana', 'banana', True, 1, 2, 3.5)

print(tupla[0])  # manzana


# -------------------------
# SET (set)
# -------------------------

# Un set es un conjunto de datos que no permite
# elementos duplicados.
#
# No podemos acceder a sus elementos mediante
# un índice como hacemos en las listas.

mi_set = {"manzana", "banana", True, 1, 2, 3.5}

# Esto daría error:
# print(mi_set[1])


# -------------------------
# DICCIONARIO (dict)
# -------------------------

# Un diccionario almacena datos mediante pares:
#
# clave (key) : valor (value)
#
# Cada elemento se separa mediante una coma.

mi_diccionario = {

    # key : value

    "nombre": "Pablo",

    "edad": 18,

    "esta_emocionado": True,

    "altura": 1.68
}

# Para acceder a un valor utilizamos su clave.

print(mi_diccionario["nombre"])  # Pablo
print(mi_diccionario["edad"])    # 18
