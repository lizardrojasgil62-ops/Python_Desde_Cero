#las variables son espacios de memoria que se usa para almacenar datos que pueden variar.
#las variables se declaran y luego se definen con un valor que puede cambiar.

#Definiendo una variable con camelCase:
nombreCompleto = "Pablo Rojas"

#Definiendo una variable con snake_case:
nombre_completo = "Pablo Rojas"

#print( nombreCompleto ) # Pablo Rojas 
#print es lo que se una función para imprimir en pantalla una variable o cualquier tipo de dato

a = 2
b = 3
c = a + b

print( c ) # 5

nombre = "Pablo "

print( nombre ) # Pablo Rojas

fruta = "manzana"
print( fruta ) # manzana

#las variables ya declaradas pueden redefinirse con un nuevo valor.

fruta = "pera"
fruta = "sandía"
fruta = "naranja"
print( fruta ) # naranja

#es lo mismo sumar un numero a la variable que redefinirla con un nuevo valor, pero es mas eficiente sumar a la variable.
#Example reedefiniendo la variable con un nuevo valor:
numero = 10
numero = 10 + 1
print ( numero ) # 11

#Example sumando a la variable con el operador += al valor de la variable:
numero = 10
numero += 1 
print( numero ) # 11

#se puede sumar a la varibale varias veces, y el valor final ser la suma de toodas las sumas.
numero = 10
numero += 5
numero += 5 
print( numero ) # 20

#los espacios también se consideran caracteres, por lo que si no se colocan espacios entre las palabras, estas se verán pegadas.
#Example sin espacios:
nombre = "Pablo"
bienvenida = "Hola" + nombre + ",bienvenido a Python"
print( bienvenida ) # HolaPablo,bienvenido a Python

#Example con espacios:
nombre = "Pablo"
bienvenida = "Hola " + nombre + ", bienvenido a Python"
print( bienvenida ) # Hola Pablo, bienvenido a Python

#si se intenta concatenar un string con un número, se producirá un error de tipo, ya que no se pueden concatenar diferentes tipos de datos.
#Para ello, se puede convertir cualquier dato usando f-strings a string.
#Example:
nombre = 5
bienvenida = "Hola " + nombre + ", bienvenido a Python"
print( bienvenida ) # TypeError: can only concatenate str (not "int") to str

#Exapmle sin f-strings:
bienvenida = "Hola {nombre}, bienvenido a Python"
print( bienvenida ) # Hola {nombre}, bienvenido a Python

#Example con f-strings:
bienvenida = f"Hola {nombre}, bienvenido a Python"
print( bienvenida ) # Hola 5, bienvenido a Python

#para dejar de definir una variable, se puede usar la palabra reservada del, que elimina la variable de la memoria.
color = "rojo"
print( color ) # rojo
del color
# print( color ) # NameError: name 'color' is not defined

#Cuando la variable ya esta creada y se aplica a otras por más que la eliminemos despues sigue existiendo en la variable ya aplicada:
colores = 10
paletadecolores = f"la paleta de colores tiene {colores} colores diferentes"
print( paletadecolores ) # la paleta de colores tiene 10 colores
del colores
print( paletadecolores ) # la paleta de colores tiene 10 colores

colores = 10
del colores
paletadecolores = f"la paleta de colores tiene {colores} colores diferentes"
print( paletadecolores ) # NameError: name 'colores' is not defined

#Operadores de pertenencia: in, not in
numero = 10
calculadora = f"la calculadora tiene {numero} botones"

print( "10" in calculadora ) # True
print( "20" in calculadora ) # False

print( "10" not in calculadora ) # False
print( "20" not in calculadora ) # True
