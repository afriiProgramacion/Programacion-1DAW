import os

def pintaFacturas (d):
    for facturas in d.items():
        print(f"La factura número: {facturas[0]} tiene un importe de {facturas[1]}")

def pintaMenu():
    print("Elige una opción: ")
    print("1. Añadir Factura pendiente de pago")
    print("2. Pagar Factura pendiente")
    print("0. Salir")

os.system('cls')
d = {
    '1': 10.00,
    '2': 20.00,
    '3': 30.00
}
suma = 60
op = 1
while op != 0:
    pintaFacturas(d)
    pintaMenu()
    op = input("Opción: ")

    match op:
        case '1':
            numeroFactura = input("Introduce número de factura: ")
            importeFactura = float(input("Introduce Importe de la factura: "))
            if numeroFactura in d:
                print("CUIDADO!! SE VA A ACTUALIZAR EL IMPORTE DE UNA FACTURA")
                suma = suma-d[numeroFactura]
                d[numeroFactura] = importeFactura
                suma += importeFactura
            else:
                d[numeroFactura] = importeFactura
                suma += importeFactura

            print(f"Se debe {suma}")
        
        case '2':
            numeroFactura = input("Introduce un número de factura: ")

            try:
                suma -= d[numeroFactura]
                d.pop(numeroFactura)
            except KeyError:
                print("No existe esa factura")
            else:
                print("Se debe", suma)
        case '0':
            op =0
            print("Hasta Luego")
