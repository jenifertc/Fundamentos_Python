print("Hola mundo")

#Tipo de escritura de las variables --------

#camelcase
aprendizSena = "SENA"

#PascalCase
AprendizSena = "sena"

#snake_case
aprendiz_sena = "sena"

#Reglas de las variables

# Al declarar una variable no se puede iniciar con un numero ej. 2026anio = "nuevo", tampoco se puede declarar con caracteres ni la letra ene
# No se puede usar palabras reservadas ej. def - if - while - break - else - print - input estan prohibidas

nombre_completo = "Jenifer Tibaduiza"

#Tipos de Datos Estructuras-------

nombre = "Jenifer"
print(type(nombre)) #str

edad = 31
print(type(edad)) #int

altura= 1.60
print(type(altura)) #float

activo = True
print(type(activo)) #bool

lista = ["python", "java"]
print(type(lista)) #list

conjunto = {"html", "css"}
print(type(conjunto)) #set

tupla= ("Java", "Css")
print(type(tupla))#tuple

diccionario = {"nombre": "Jenifer", "edad":31}
print(type(diccionario)) #dict

rango = range(5)
print(type(rango)) #range

complejo =  2 + 3j
print(type(complejo)) #complex
        
byte = b"hola"
print(type(byte)) #bytes

nulo = None
print(type(nulo)) #NoneType

#Conversion de tipo de datos o casteo

telefono = 3213582217 #int
print(type(telefono),telefono)

telefono_str = str(telefono) #string casteado
print(type(telefono_str), telefono_str) 

cedula = "1057585" #string
print(type(cedula),cedula)

cedula_int = int(cedula)#casteado
print(type(cedula_int), cedula_int) #el primer cedula_int muestra el tipo de dato y el segundo el resultado

matriculado = False
print(type(matriculado))

matriculado_int = int(matriculado) #casteado 
print(type(matriculado_int), matriculado_int)

#Casteo de decimal a entero
promedio = 4.13 #decimal
print(type(promedio),promedio)

promedio_int = int(promedio) #casteo
print(type(promedio_int), promedio_int)

#casteo de entero a decimal
activo = 1 #int
print(type(activo))

activo_bool = bool(activo) #casteo
print(type(activo_bool),activo_bool)

#Casteo de boleano a flotante
beneficio = True
print(type(beneficio))

beneficio_float = float(beneficio)
print(type(beneficio_float),beneficio_float)

#Casteo deimal a booleano
descuento = 10.5
print(type(descuento), descuento)

descuento_bool = bool(descuento)
print(type(descuento_bool),descuento_bool)

#COMENTARIO DE UNA SOLA LINEA

""" COMENTARIO DE UN BLOQUE """

#INDENTACION EN PYTHON

#Condicional If
if 5 > 2:
    print("5 es mayor que 2")
else:
    print("5 no es mayor que 2")

# input - entrada de datos
nombre_completo = input("Ingrese tu nombre completo:  ")
programa = input("Cual es tu programa de formacion ?")
# print salida de texto
#print(nombre_completo)
print("Hola  " , nombre_completo, "Bienvenido al curso de Python") #concatenado
print("Hola mi nombre es : ", nombre_completo, " y estoy en el programa de: ", programa )

#Impresion con formato F-String usar esta forma
print(f"Hola mi nombre es: {nombre_completo}, y estoy en el programa de: {programa}")