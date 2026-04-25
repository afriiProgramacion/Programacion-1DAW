def primo(numero):
    encontrado = False
    i = 2
    while (i <= numero // 2) and (not encontrado):

        if (numero%i==0):
            encontrado=True
        i=i+1

    if encontrado:
        print("NO ES PRIMO")
    else:
        print ("ES PRIMO")

if __name__=='__main__':
    
    numero = int(input("INTRODUCE UN NÚMERO PARA SABER SI ES PRIMO O NO: "))


    primo(numero)