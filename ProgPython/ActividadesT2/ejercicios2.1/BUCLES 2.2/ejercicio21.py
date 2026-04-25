montos = 1
total = 0
while montos != 0:
    montos = int(input("Introduce los montos de tus compras (0 para finalizar): "))
    if montos > 0:
        total = total + montos
        

if total >= 100:
    total = total * 0.10
    print(f"El total con el descuento es: {total}$")

else:
    print(f"El total a pagar es: {total}$")