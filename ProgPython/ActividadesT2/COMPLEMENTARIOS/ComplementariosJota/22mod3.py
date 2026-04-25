#Observa atentamente el siguiente algoritmo e indica los errores que presenta. Corrígelo
# para que se ejecute correctamente.

num_intentos = 1
max_intentos = 5

valor_introducido = input("Cual es la capital de Francia?: ")

while valor_introducido != 'París' and max_intentos - num_intentos != 0:
    print("Respuesta incorrecta.")
    print(f"Sólo quedan {max_intentos - num_intentos} intentos.")
    valor_introducido = input("Cual es la capital de Francia?: ")
    num_intentos = num_intentos + 1

if max_intentos - num_intentos !=0:
    print("Bravo.")
else:
    print("Revise sus conocimientos de geografía.")