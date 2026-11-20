#ESTRUCTURA DE UN DICCIONARIO

from lista import aprendices


diccionario = {
    "clave_1": "valor_1",
    "clave_2": "valor_2",
    "clave_3": "valor_3"
}
print(diccionario)

#Diccionario vacio
diccionario_vacio = {}
print(type(diccionario_vacio))

#Diccionario con elementos 
diccionario_aprendiz = {
    "Nombre": "Jenifer",
    "Apellido": "Tibaduiza",
    "Programa": "ADSO",
    "Ficha": "3233140",
    "Edad": "31"
}
print(diccionario_aprendiz)

#Obtener un valor del diccionario por la clave
print(diccionario_aprendiz["Programa"])

#obtener
print(diccionario_aprendiz.get("Programa"))
print(diccionario_aprendiz.get("correo"))

#Obtener solamente las claves con .keys()
print(diccionario_aprendiz.keys())

#obtener solamente los valores con .values()
print(diccionario_aprendiz.values())

#obtener todo clave y valor con .items()
print(diccionario_aprendiz.items())

#Agregar un atributo al diccionario
diccionario_aprendiz["correo"] = "jenifer@gmail.com"
print(diccionario_aprendiz)

#Modificar un valor del diccionario
diccionario_aprendiz["Programa"] = "SST" #Lo busca si lo encuentra lo cambia y si no lo encuentra lo agrega
print(diccionario_aprendiz)

#Metodo UPDATE() para actualizar un valor
diccionario_aprendiz.update({"Nombre": "Luis"})
print(diccionario_aprendiz)

#Agregar un nuevo elemento con update()
diccionario_aprendiz.update({"Ciudad": "Sogamoso"})
print(diccionario_aprendiz)

#Eliminar un elemento del diccionario 

#Con .popitem() elimina el ultimo elemento
diccionario_aprendiz.popitem()
print(diccionario_aprendiz)

#Eliminar un elemento especifico usamos .pop()
diccionario_aprendiz.pop("Edad")
print(diccionario_aprendiz)

#Eliminar todos los elementos del diccionario con .clear()
"""diccionario_aprendiz.clear()
print(diccionario_aprendiz)"""

#Comprobar la pertenencia con In

print("Ficha" in diccionario_aprendiz)
print("Telefono" in diccionario_aprendiz)

if "Ficha" in diccionario_aprendiz:
    print("La clave ficha esta dentro del diccionario")
else:
    print("La clave ficha no esta dentro del diccionario")

#Recorrer un diccionario con el ciclo for

#Recorrer solo las claves del diccionario
for clave in diccionario_aprendiz.keys():
    print(clave)

#Recorrer los valores
for valores in diccionario_aprendiz.values():
    print(valores)

#Recorrer clave y valores del diccionario
for clave, valores in diccionario_aprendiz.items():
    print(f"{clave}:{valores}")

#Diccionarios Anidados

aprendices = {
    "aprendiz_1":{
        "Nombre": "James",
        "Apellido": "Rodriguez",
        "Programa": "ADSO"
    },
    "aprendiz_2":{
        "Nombre": "David",
        "Apellido": "Ospina",
        "Programa": "SST"
    },

    "aprendiz_3":{
        "Nombre": "Luis",
        "Apellido": "Diaz",
        "Programa": "Sistemas"
    }
}

#Acceder a un valor de un diccionario anidado
print(aprendices["aprendiz_2"][ "Programa"])

#Recorrer un diccionario anidado con ciclo For
for aprendiz,datos in aprendices.items():
    print(f"{aprendiz}")
    for clave,valores in datos.items():
        print(f"{clave}:{valores}")
    
