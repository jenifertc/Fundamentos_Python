#ACTIVIDAD 2 CALCULADORA DE NOTAS

nota1 = float(input("Ingrese primer nota "))
nota2 = float(input("Ingrese segunda nota "))
nota3 = float(input("Ingrese tercera nota "))

prom = nota1 + nota2 + nota3
prom //= 3
print(prom)

if prom >= 3:
    print("Estudiante aprobo")
else:
    ("No aprobo")
