def cuenta (palabra, letra):

    contador = 0
    for l in palabra:
        if l == letra:
            contador = contador + 1
    return (contador)

if __name__=='__main__':
    
    pal = input("Introduce una palabra: ")
    let = input("Introduce una letra: ")
    
    numeroletras = cuenta(pal,let)
    numerodeos = cuenta ("consuelo", "o")

    print(f"Hay {numeroletras} o en {pal} y {numerodeos} {let} en consuelo")