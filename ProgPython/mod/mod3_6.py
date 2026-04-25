hay_negativos = False
for i in range (1,5):
    num = int(input("Introduce numero:"))
    if (num < 0):
        hay_negativos=True
if (hay_negativos):
    print("Existen números negativos Al menos uno")
else:
    print("Todos son positivos")



