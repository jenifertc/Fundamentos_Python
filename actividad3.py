
# ACTIVIDAD 3: CLASIFICADOR DE IMC

# 1. Solicitar el peso y la estatura al usuario
peso = float(input("Ingrese su peso en kilogramos (kg): "))
estatura = float(input("Ingrese su estatura en metros: "))

# 2. Validar que el peso y la estatura sean positivos
if peso > 0 and estatura > 0:

    # 3. Calcular el indice de masa corporal (IMC)
    imc = peso / (estatura ** 2)

    # 4. Clasificar el resultado
    if imc < 18.5:
        clasificacion = "Bajo peso"

    elif imc <= 24.9:
        clasificacion = "Normal"

    elif imc <= 29.9:
        clasificacion = "Sobrepeso"

    else:
        clasificacion = "Obesidad"

    # 5. Mostrar los resultados
    print("\n----- RESULTADOS DEL IMC -----")
    print(f"Peso: {peso} kg")
    print(f"Estatura: {estatura} metros")
    print(f"Su IMC es: {round(imc, 2)}")
    print(f"Clasificacion: {clasificacion}")

else:
    print("Error: El peso y la estatura deben ser valores positivos.")
