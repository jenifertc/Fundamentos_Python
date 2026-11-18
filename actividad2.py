#ACTIVIDAD 2 CALCULADORA DE NOTAS

nota1 = float(input("Ingrese primer nota "))
nota2 = float(input("Ingrese segunda nota "))
nota3 = float(input("Ingrese tercera nota "))

#Punto 2 calcular promedio de notas
prom = (nota1 + nota2 + nota3) / 3
prom = round(prom, 2)
print("El promedio es: ", prom)


# punto 3 punto faltante para nota maxima (5.0)
puntos_faltan = 5.0 - prom
puntos_faltan = round(puntos_faltan, 2) 
print("Los puntos que faltan para alcanzar la nota máxima son: ", puntos_faltan) 

#punto 4 determinar si el estudiante aprobo o reprobo
aprobo = prom >= 3.0
print("El estudiante aprobo: ", aprobo)

reprobo = prom < 3.0
print("El estudiante reprobo: ", reprobo)

