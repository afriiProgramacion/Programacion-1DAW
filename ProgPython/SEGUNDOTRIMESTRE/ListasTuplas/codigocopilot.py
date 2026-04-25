Asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
recus = []

for asignatura in Asignaturas[:]:  # recorremos una copia
    nota = int(input(f"Introduce la nota que has sacado en {asignatura}: "))
    print(f"En {asignatura}, has sacado {nota}")

    if nota < 5:
        recus.append(asignatura)
    else:
        Asignaturas.remove(asignatura)  # eliminamos por valor, no por índice

print("Asignaturas que tienes que recuperar:", recus)
print("Asignaturas aprobadas:", Asignaturas)
