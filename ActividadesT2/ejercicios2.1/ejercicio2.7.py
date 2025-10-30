renta = int(input("Introduce tu renta anual: "))

if renta <= 10000:
    print("Te pertenece un tipo impositivo del 5%")
elif renta >=10000 and renta <= 20000:
    print("Te pertenece un tipo impositivo del 15%")
elif renta >= 20000 and renta <= 35000:
    print("Te pertenece un tipo impositivo del 20%")
elif renta >= 3500 and renta <= 60000:
    print("Te pertenece un tipo impositico del 30%")
else:
    print("Te pertenece un tipo impositivo del 45%")
