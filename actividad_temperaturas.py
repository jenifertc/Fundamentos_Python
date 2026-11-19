#ANALISIS DE TEMPERATURAS SEMANALES

temperaturas = [18,21,19,24,22,20,17,23,25,21,18,20,22,19]

#Indexacion
print("Primer dia: ", temperaturas[0])
print("Ultimo dia: ", temperaturas[-1])
print("Dia 7 mitad: ", temperaturas[6])
print("Penultimo dia: ", temperaturas[-2])

#Slicing
primera_semana = temperaturas[0:7]
segunda_semana = temperaturas[7:14]
dias_pares = temperaturas[1::2]
invertida = temperaturas[::-1]

print("Primera Semana: ", primera_semana)
print("Segunda Semana: ", segunda_semana)
print("Dias Pares: ", dias_pares)
print("Temperatura Invertida: ", invertida)

#Promedio de temperatura
prom_primer_semana = sum(primera_semana) / len(primera_semana)
print("Promedio Primera Semana:  ", prom_primer_semana)
prom_segunda_semana = sum(segunda_semana) / len(segunda_semana)
print("Promedio Segunda Semana: ", prom_segunda_semana)

#Cual semana tuvo mayor temperatura promedio
if prom_primer_semana > prom_segunda_semana:
    print("La primera semana tuvo mayor promedio")
elif prom_segunda_semana > prom_primer_semana:
    print("La segunda semana tuvo mayor promedio")
else:
    print("Las dos semanas tuvieron el mismo promedio")

