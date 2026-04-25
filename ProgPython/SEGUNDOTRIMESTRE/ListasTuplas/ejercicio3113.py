def CalculoMedia (n):
    suma = suma(n)
    cantidad = len(n)
    
    resultado = suma / cantidad

    return resultado 

def calculaDesviacionTipica (n):

    media = CalculoMedia(n)
    SumaCuadrados = 0
    cantidad = len(n)

    for numero in n:
        diferencia = numero - media
        SumaCuadrados += diferencia ** 2

    desviacionTipica = (SumaCuadrados / cantidad)

    return desviacionTipica**0.5

entrada = input("Introduce números separados por comas: ")
muestra = entrada.split(",")

secuencia = []

for valor in muestra:
    try:
        secuencia.append(int(valor))
    except ValueError:
        print("Ese valor no es numérico")
        muestra.remove(valor)

print(f"La media es: {CalculoMedia(secuencia)}")
print(f"La desviación típica es: {calculaDesviacionTipica(secuencia)}")