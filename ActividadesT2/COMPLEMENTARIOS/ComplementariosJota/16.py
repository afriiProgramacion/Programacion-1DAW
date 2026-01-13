#Muestra los números del 320 al 160, contando de 20 en 20 hacia atrás utilizando los tres
# bucles, al igual que el ejercicio anterior.

inicio = 320
fin = 160

for i in range (inicio,fin-1,-20):
    print(i)

while inicio >= fin:
    print(inicio)
    inicio = inicio - 20