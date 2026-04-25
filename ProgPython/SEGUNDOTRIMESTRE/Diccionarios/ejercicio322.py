
def pintaDiccionario (d):
    for item in d.items():
        print(item)

def pintaPersona (d, p):
    if (len(d)<1):
        raise NameError ("Diccionario vacío")
    else:
        try:
            valor = d[p]
            print(f"Tu nombre es: {valor[0]}, tu edad es: {valor[1]}, tu dirección {valor[2]} y tu telefono {clave}")
        except KeyError:
            print("Clave no encontrada")

nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")
direccion = input("Dime tu dirección: ")
telefono = input("Dime tu teléfono: ")

d = {}
clave = telefono 
valor = [nombre, edad, direccion]

try:
    d[clave] = valor
except KeyError:
    print("Clave incorrecta")

pintaPersona(d,clave)