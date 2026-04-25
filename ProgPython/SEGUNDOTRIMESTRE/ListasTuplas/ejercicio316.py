Asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
recus = []
n = 0
for asignatura in Asignaturas[:]:
    notaasignatura = int(input(f"Introduce la nota que has sacado en {asignatura}: "))
    notas.append(notaasignatura)       
    print(f"En {asignatura}, has sacado {notas[n]}")
    if notaasignatura < 5:
        recus.append(asignatura)
        print(f"Tienes que recuperar {recus}")
    elif notaasignatura >= 5:
        Asignaturas.remove(asignatura)
        print(Asignaturas)
        n += 1