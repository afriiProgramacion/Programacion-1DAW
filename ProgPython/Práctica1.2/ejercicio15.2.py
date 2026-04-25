cantidad_depositada = int(input("¿Qué cantidad de dinero has depositado en la cuenta?"))
porcentaje_interes = 0.4

año1 = cantidad_depositada * (1 + 0.4)
año2 = año1 * (1 + 0.4)
año3 = año2 * (1 + 0.4)

print("El primer año la cantidad de ahorros fue:", año1)
print("El segundo año la cantidad fue de:", año2)
print("Y el tercero, la cantidad fue de:", año3)