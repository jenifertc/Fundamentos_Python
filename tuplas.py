#TUPLAS
#Estructura
tupla = ("elemento_1","elemento_2","elemento_3")
print(type(tupla))

tupla_2 = "a","b","c"
print(type(tupla_2))

tupla_3 = ("hola") #tipo string, pero si le agrego una coma despues del "hola", lo convierte en tuple
print(type(tupla_3))

tupla_4 = tuple("hola") #castear
print(tupla_4)
print(type(tupla_4))

tupla_mixta = ("hola", 123, 3, 34, True,[1,2,3])
print(tupla_mixta)

aprendices = ("Dayana", "Jhon", "Miguel","Oscar", "Pepito","Jhon")
print(aprendices)

#Acceder a un elemento de la Tupla
print(aprendices[2])

#Modificar un elemento de la tupla
"""aprendices[0] = "Diana"
print(aprendices)""" #en las tuplas no se puede eliminar ni modificar elementos

#Consultar rangos de elementos de las tuplas
print(aprendices[0:2])
print(aprendices[0::]) #con los dos puntos me muestra toda la tupla

#Concatenar tuplas +
tupla_uno = (1,2,3)
tupla_dos = (4,5,6)
tupla_suma = tupla_uno + tupla_dos
print(tupla_suma)

#Multiplicarf Tupla
tupla_multiplicacion = tupla_uno * 3
print(tupla_multiplicacion)

#Metodos de las tuplas

#Medir la longitud de la tupla .len()
print(len(aprendices))

#Contar elementos repetidos en una tupla .count()
print(aprendices.count("Jhon")) 

#Obtener el indice de un elemento .index()
print(aprendices.index("Dayana"))

#MODIFICAR UNA TUPLA CONVIRTIENDOLA EN LISTA
lenguajes = ("HTML","CSS","JavaScript")
print(lenguajes)
print(type(lenguajes))

lista_lenguajes = list(lenguajes) #Convierte la tupla en lista
print(lista_lenguajes)
print(type(lista_lenguajes))

lista_lenguajes.append("Python")#Agregar un elemento
print(lista_lenguajes)

lenguajes = tuple(lista_lenguajes) #convierte la lista de nuevo a tupla
print(lenguajes)
print(type(lenguajes))

#Comprobacion de pertenencia con IN busqueda
print("Python" in lenguajes)
print("C++" in lenguajes)

if "HTML" in lenguajes:
    print("HTML, fue encontrado en la tupla")
else:
    print("HTML, no fue encontrado en la tupla")

#Empaquetar Tuplas
programa_1 = "ADSO"
programa_2 = "SST"
programa_3 = "Topografia"
tuplas_programas = (programa_1,programa_2,programa_3)
print(tuplas_programas)
print(type(tuplas_programas))

#Desempaquetar
tupla_ciudades = ("Duitama", "Sogamoso", "Tunja")
ciudad_1,ciudad_2,ciudad_3 = tupla_ciudades
print(ciudad_1)
print(ciudad_2)
print(ciudad_3)

#Iterar o recorrer una tupla con FOR
for ciudad in tupla_ciudades:
    print(ciudad)
