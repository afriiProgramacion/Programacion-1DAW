
asignaturas = {'Matematicas': 6,
               'Física': 4,
               'Química': 5}
total = 0


for asignatura, credito in asignaturas.items():
    asignatura = input("Introduce una asígnatura para saber sus créditos: ")
    print(f"{asignatura} tiene {credito} créditos")
    total = total + credito

print("El total de créditos es: ", total)