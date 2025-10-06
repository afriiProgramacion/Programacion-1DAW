Importe = int(input("Introduce un precio sin IVA: "))
valorIva = float(input("Introduce el valor del IVA: "))
Iva = Importe + (Importe * valorIva / 100)
print ("El precio del artículo es: ", Iva)

