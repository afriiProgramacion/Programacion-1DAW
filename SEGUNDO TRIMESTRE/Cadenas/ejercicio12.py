palabra = "banana"
num_a = palabra.count("a")
print (num_a)

i = palabra.find("a")
contador = 0

while (i!=-1):
    palabra = palabra [i+1:]
    contador += 1
    i = palabra.find("a")

print(contador)