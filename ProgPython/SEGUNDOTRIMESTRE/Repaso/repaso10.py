def agregar_alumno(alumnos):
    nombre = input("Nombre del Alumno: ")
    notas = []

    for i in range(1,4):
        nota = float(input(f"Nota {i}: "))
        notas.append(nota)

    alumnos[nombre] = notas
    print(f"Alumno '{nombre}' añadido\n")

def media_alumno(notas):
    if len(notas) > 0:
        return sum(notas) / len(notas)
    else:
        return -1

def mostrar_medias(alumnos):
    print("\nMedias de los alumnos: ")
    for nombre, notas in alumnos.items():
        print(f"{nombre}: {media_alumno(notas):.2f}")

def mostrar_notas_distintas(alumnos):
    conjunto_notas = set()
    for notas in alumnos.values():
        conjunto_notas.update(notas)
    print(f"Notas distintas: {conjunto_notas}")