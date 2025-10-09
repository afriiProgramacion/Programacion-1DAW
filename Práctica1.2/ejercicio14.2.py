muñecas = 75
payasos = 112

nmuñecas = int(input("¿Cuántas muñecas has vendido en el último pedido?: "))
npayasos = int(input("¿Cuántos payasos has vendido en el último pedido?: "))

pmuñecas = muñecas * nmuñecas
ppayasos = payasos * npayasos

if (npayasos <= 0 and nmuñecas >=0):   
    print ("El peso del paquete es:", pmuñecas, "g")

elif (npayasos >=0 and nmuñecas <=0):
    print ("El peso del paquete es:", ppayasos, "g")

else: 
    pfinal = ppayasos + pmuñecas
    print("El peso total del paquete incluyendo", nmuñecas, "muñecas y", npayasos, "payasos es:", pfinal, "g")