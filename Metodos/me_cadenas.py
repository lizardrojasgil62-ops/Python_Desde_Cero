cadena1 = "holamundo"
cadena2 = "Logitech es mejor que razer"

#.dir() devuelve los atributos validos al objeto.(FUNCIÓN)
#print(dir())

# METODOS -> DATO . METODO + ()




#.upper() convierte en mayusculas.
mayusc = cadena1.upper()

#.lower() convierte en minusculas.
minusc = cadena1.lower()

#.capitalize() primera letra en mayuscula. (primero funciona como un lower y luego solo la primera en mayuscula.)
primera_letra_mayusc = cadena1.capitalize()





#.find() Buscamos una cadena en otra cadena , si no hay coincidencias, devuelve -1
cadena1 = "hola mundo"
#          0123456789

busqueda_find = cadena1.find("x")

#.index() Buscamos una cadena en otra cadena, si no hay coincidencias , lanza una expceción.
busqueda_index = cadena1.index("h")





#.insnumeric() si es numerico devuelve true, sino false.
es_numerico = cadena1.isnumeric()

#.isalpha() si es alfanumerico duvuelve true sino false. (los espaciones no son caracteres alfanumericos)
es_alfanumerico = cadena1.isalpha()




#contamos las coincidencias de una cadena dentro de otra cadnena , devuelve la cantidad de coincidencias.
contar_coincidencias = cadena1.count("o")

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)




#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza_con = cadena1.startswith("h")


#verificamos si una cadena termina con otra cadena dada, si es asi devuelve true
termina_con = cadena1.endswith("mundo")





#Remplaza un pedazo de la cadena dada por otra dada
cadena_nueva = cadena1.replace(" ", ",")

#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(" ")

print(cadena_separada[0])

print(type(cadena_separada))
#.upper() sirva para convertir todo en mayusculas
#.lowe
