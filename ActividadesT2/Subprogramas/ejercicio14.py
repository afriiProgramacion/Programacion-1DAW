def primo(num):
    encontrado = False
    i = 2
    while (i <= num // 2) and (not encontrado):

        if (num%i==0):
            encontrado=True
        i=i+1

    if encontrado:
        print("NO ES PRIMO")
    else:
        print ("ES PRIMO")

def divisor (num):

    if primo(num):
        print(f"Es un número primo y no tiene divisores, el único es el mismo: {num}")  
    else:
        if (num < 4):
            print("Demasiado pequeño para descomponer, por favor, mayor que 4.")
        else:
            i = 2
            while (i <= num):
                if(num %i == 0):
                    print("{:3d} Es un divisor" .format(i))
                    num = num // i
                else:
                    i = i + 1
    

num = int(input("INTRODUCE UN NÚMERO PARA SABER SI ES PRIMO O NO: "))


divisor (num)
