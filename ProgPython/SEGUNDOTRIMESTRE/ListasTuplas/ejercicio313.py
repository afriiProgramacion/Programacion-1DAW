
Asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []

for asignatura in range (len(Asignaturas)):
    notaasignatura = int(input(f"Introduce la nota que has sacado en {Asignaturas[asignatura]}: "))
    notas.append(notaasignatura)       
    print(f"En {Asignaturas[asignatura]}, has sacado {notas[asignatura]}")