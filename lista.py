#LISTAS

#Estructura de una lista
lista = ["dato_1","dato_2","dato_3"]
print(type(lista))

#Lista Mixta
lista_mixta = [1,"Hola", 3.14, True, ["Adso",17]]
print(type(lista_mixta))

#LISTA DE APRENDICES SENA ADSO 3233140
aprendices = ["Jenifer","Luis","Liz","Aleja","Miguel"]
print(aprendices[3])

#MODIFICAR UN ELEMENTO DE LA LISTA
aprendices[2] = "Fernando"
print(aprendices)

#CONSULTAR RANGOS DE ELEMENTOS DE UNA LISTA
print(aprendices[0:3])
print(aprendices[2:4])
print(aprendices[0::3])

#CONCATENAR O UNIR DOS LISTAS
programas_tecnicos = ["Sistemas Teleinformaticos","Redes"]
programas_tecnologos = ["ADSO","Topografia"]

programas_sena = programas_tecnicos + programas_tecnologos
print(programas_sena)

#Extender listas con .extend()
nuevos_programas_tecnicos = ["Inteligencia Artificial","Mineria de datos","Redes"]
programas_tecnicos.extend(nuevos_programas_tecnicos)
print(programas_tecnicos)

#Medir la longitud de una lista
print(len(programas_tecnicos))
print(len(programas_tecnologos))

#Contar elementos repetidos en una lista con la sentencia .count()
print(programas_tecnicos)
print(programas_tecnicos.count("Redes"))

#Obtener el indice de un elemento .index()
print(aprendices.index("Aleja"))
print(programas_tecnicos.index("Mineria de datos"))
print(programas_tecnologos.index("ADSO"))

#Copiar una lista nueva .copy()
nueva_lista_aprendices = aprendices.copy()
print(nueva_lista_aprendices)

#Agregar nuevos elementos con .append()
nueva_lista_aprendices.append("Sebastian")
nueva_lista_aprendices.append("Adriana")
print(nueva_lista_aprendices)

#Agregar un nuevo elemento en una posicion del indice .insert()
nueva_lista_aprendices.insert(1, "Oscar")
print(nueva_lista_aprendices)

#Eliminar un elemento de una lista .remove()
nueva_lista_aprendices.remove("Oscar")
print(nueva_lista_aprendices)

#Eliminar con elemento con pop este elimina segun su indice
nueva_lista_aprendices.pop(0)  # pyright: ignore[reportUnusedCallResult]
print(nueva_lista_aprendices)

"""#Limpia todos los elementos de la lista
nueva_lista_aprendices.clear()
print(nueva_lista_aprendices)"""

#Ordenar la lista

#De forma ascendente A-Z .sort()
nueva_lista_aprendices.sort()
print(nueva_lista_aprendices)

#De forma descendente Z-A .reverse()
nueva_lista_aprendices.reverse()
print(nueva_lista_aprendices)

#Buscar elementos de la lista con el operador IN
if "Sebastian" in nueva_lista_aprendices:
    print("Sebastian se encontro en la lista de aprendices")
else:
    print("No se encontro en la lista")

