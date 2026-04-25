def CompruebaContraseña (contraseña_introducida):
    if contraseña_introducida == contraseña_almacenada:
        return True
    else:
        return False
    

#PROGRAMA PRINCIPAL

contraseña_almacenada = "qwerty123"
contraseña_introducida = input("Introduce la contraseña: ")
contraseña_introducida = contraseña_introducida.lower()
if CompruebaContraseña (contraseña_introducida):
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta")



