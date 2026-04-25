def eliminaRepetidos(alumnos):
    if len(alumnos) == 0:
        raise NameError ("La lista está vacía")
    else:
        return set(alumnos)
    

def pideAlumnos(alumnos, eso):
    nombre = ""
    secundaria = ""
    while nombre != 'x':
        nombre = input("Introduce el nombre de los alumnos de primaria: ")
        if nombre.lower() != 'x':
            alumnos.append(nombre)

        else:
            while secundaria != 'x':
                secundaria = input("Introduce los nombres de los alumnos de secundaria: ")
                if secundaria.lower() != 'x':
                    eso.append(secundaria)


AlumnosPrimaria = []
AlumnosSecundaria = []

pideAlumnos(AlumnosPrimaria, AlumnosSecundaria)

repetidosPrimaria = eliminaRepetidos(AlumnosPrimaria)
repetidosSecundaria = eliminaRepetidos(AlumnosSecundaria)

print("Alumnos sin Repetir en cada lista: ")
print(repetidosPrimaria.union(repetidosSecundaria))

print("\nAlumnos Repetidos en cada lista: ")
print(repetidosPrimaria.intersection(repetidosSecundaria))

print("\nNombres que no se repiten en secundaria: ")
print(repetidosPrimaria.difference(repetidosSecundaria))

print("\nEstán todos los nombres de primaria incluidos en secundaria? : ")
print(repetidosPrimaria.issubset(repetidosSecundaria))

