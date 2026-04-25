nombre = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo: ")
letra = nombre[:1]

sexobool=False

if sexo == "m":
    sexbool=False
else: 
    sexobool=True


if letra <= "m" and sexbool==True:
    print("Perteneces al grupo A")
elif letra >= "n" and sexbool==False:
    print("Perteneces al grupo A")
else:
    print("Pertneces al grupo B")


