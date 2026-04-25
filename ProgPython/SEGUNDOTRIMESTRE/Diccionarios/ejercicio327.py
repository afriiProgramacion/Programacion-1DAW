import os

def pintacesta (d):
    os.system("cls")
    print("Lista de la compra: ")
    for producto in d.items():
        print(f"{producto[0]} --- {producto[1]}")
        print("-" *10)

d = {}
fin = False
suma = 0.0

while not fin:
    nombre = input("Dime un producto: ")
    precio = float(input("Precio: "))

    if nombre in d:
        print(f"Se procederá a la actualización del producto existente: {nombre}.")
        print("Se reajustará el importe total")
        suma = suma-d[nombre]
        d[nombre] = precio
        suma = suma + precio
    else:
        d[nombre] = precio
        suma += precio
    
    pintacesta(d)
    print(f"La suma total es: {suma}")

    opcion = input("Otro producto? (s/n): ").lower()
    if opcion == 'n':
        fin = True