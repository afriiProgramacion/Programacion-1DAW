def dimensiones (n):
    if len(n) > 0:
        xm = len(n)
        ym = len(n[0])
        return xm, ym
    else:
        raise NameError("No es una matriz váida")

def multiplicable(a,b):
    x,y = dimensiones(a)
    z,t = dimensiones(b)

    if y == z:
         return True 
    else:
         return False
    

def multiplicar(a,b):
    
    x,y = dimensiones(a)
    z,t = dimensiones(b)
        
    if multiplicable (a,b):
            resultante = []

            for p in range (0,x):
                fila = [0] * t
                resultante.append(fila)

            
            for i in range (0,x):
                for j in range (0,t):
                    for k in range (0,y):
                        resultante [i][j]+=a[i][k]*b[k][j]
            return resultante
    else:
        raise NameError("MATRICES NO MULTIPLICABLES")


    
a = [[1,2,3],[4,5,6]]
b = [[-1,0],[0,1],[1,1]]

multiplicacion = multiplicable(a, b)
print(multiplicacion)

