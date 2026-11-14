#CONDICIONALES IF/ELIF/ELSE

#Estructura del condicional IF: ---si
if True:
    print("Se ejecuta la instruccion")

#Ejemplo del IF
edad = 12
if edad > 18:
    print("Eres un adulto")

else:
    print("Eres joven")

#Estructura del ELIF
if False:
    print("La primera condicion")
elif False:
    print("Segunda condicion")
elif False:
    print("Tercera Condicion")
else:
    print("Todas las condiciones son falsas")

#EJERCICIO CLASIFICACION DE EDAD

edad = 70

if edad < 18:
    print("Eres menor de edad")
elif edad >= 18 and edad < 65:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")

#IF ANIDADOS
if True:
    if True:
        print("se ejecuta la instruccion")
    elif True:
        print("Se ejecuta la instruccion")
    else:
        print("No se ejecuta la instruccion")
else:
    print("No se ejecuta la instruccion")

#EJERCICIO CLASIFICACION DE EDAD IF ANIDADO

edad = 24

if edad < 18:
    if edad > 12 and edad < 18:
        print("Adolescente")
    else:
        print("Ninio")
else:
    if edad >= 18 and edad < 60:
        print("Adulto")
    else:
        print("Adulto Mayor")

#EJERCICIO DEL PARTIDO CON IF

marcador_colombia = int(input("Ingrese el marcador de Colombia "))
marcador_chile = int(input("Ingrse marcador chile "))

if marcador_colombia > marcador_chile:
    print("Colombia es el ganador del partido ")

elif marcador_colombia == marcador_chile:
    print("Quedamos empatados")

else:
    print("Perdimos el partido ")


#OPERADOR TERNARIO

numero = 4

if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

#este es el mismo ejercicio solo que en operador ternario
print("El numero es par" if numero % 2 == 0 else "El numero es impar")