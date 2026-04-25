muñecas = 75
payasos = 112

nmuñecas = int(input("¿Cuántas muñecas has vendido en el último pedido?: "))
npayasos = int(input("¿Cuántos payasos has vendido en el último pedido?: "))

pmuñecas = muñecas * nmuñecas
ppayasos = payasos * npayasos

total = pmuñecas + ppayasos
print ("El paquete pesa:", total, "g")