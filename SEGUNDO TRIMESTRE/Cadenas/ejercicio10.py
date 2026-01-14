fruta = input("Dime una fruta: ")
copia = fruta[:-1]
print(copia)

print(fruta is copia)
print(fruta == copia)
print(f"{id(fruta)} -- {id(copia)}")