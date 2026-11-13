#Operadores Aritmeticos 

a = 10
b = 3

suma = a + b
print(f"La suma de: {a} y {b} es: {suma}")

resta = a - b
print(f"La resta de: {a} y {b} es: {resta}")

multiplicacion = a * b
print(f"La multiplicacion de: {a} y {b} es: {multiplicacion}")

division = a / b
print(f"La division de: {a} y {b} es: {division}")

division = a // b
print(f"La division de: {a} y {b} es: {division}")

#Modulo o Residuo
modulo = a % b
print(f"El modulo de: {a} entre {b} es: {modulo}")

#potencia o exponenciacion
potencia = a ** b
print(f"La potencia de : {a} elevado  a {b} es: {potencia}")

#PRECEDENCIA DE OPERADORES

resultado = 10 + 3 * 2
print(f"El resultado de la operacion 10 + 3 * 2 es: {resultado}")

resultado_2 = (a + b) * 2
print(f"El resultado de la operacion es: {resultado_2}")

resultado_3 = 10 * 3 // 3
print(f"El resultado de la operacion es: {resultado_3}")

ejercicio = ((a + b) * (a - b) / (a * b)) - ((a ** b) % 3)
print(f"El resultado es: {ejercicio}")

#LIBRERIAS DE PYTHON - EN PYP https://pypi.org/

import math
print(math.pi)
print(math.e)
print(math.sqrt(16))

import random
print(random.random())