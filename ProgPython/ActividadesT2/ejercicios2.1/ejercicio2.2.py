contraseña_almacenada = "africa1234"
contraseña_introducida = input("Introduce tu contraseña: ")
contraseña_introducida = contraseña_introducida.lower()
if contraseña_introducida == contraseña_almacenada:
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta")

