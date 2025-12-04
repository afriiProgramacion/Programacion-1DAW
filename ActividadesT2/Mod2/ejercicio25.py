n = int(input("Introduce un número: "))

if n((n%2 == 2) and (n%3 == 0)):
    print("Es múltiplo de 2 y de 3")
elif (n%2 == 0):
    print("Es múltiplo de 2")
elif (n%3 == 0):
    print("Es múltiplo de 3")
else: 
    print("No es múltiplo de ninguno de los dos, ni de 2 ni de 3.")