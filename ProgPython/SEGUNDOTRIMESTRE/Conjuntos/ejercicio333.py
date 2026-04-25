
def conjunto_potencias(s):
    s = list(s)
    potencia = [set()]

    for elem in s:
        nuevos_subconjuntos = []

        for subconjunto in potencia:
            nuevos_subconjuntos.append(subconjunto | {elem})
        
        potencia.extend(nuevos_subconjuntos)
    
    potencia.remove(set())
    return potencia

resultado = conjunto_potencias({1,2,3})
print(resultado)