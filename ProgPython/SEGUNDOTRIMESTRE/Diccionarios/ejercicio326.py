def validacorreo (correo):

    if "@" not in correo:
        return False
    
    partes = correo.split("@")

    if len(partes) !=2:
        return False
    
    nombre, dominio = partes

    if not nombre or not dominio:
        return False
    
    if "." not in dominio:
        return False
    
    subdominio = dominio.split(".")

    if len(subdominio) > 2:
        return False
    
    extension = subdominio[-1]

    if len(extension) < 2:
        return False
    

d = {}
fin = False


while not fin:
    email = input("Introduce tu email: ")
    if validacorreo(email):
        nombre = input("Dime tu nombre: ")
        edad = int((input("Dime tu edad: ")))
        sexo = input("Género: (Hombre, Mujer, otro): ")
        telefono = input("Dime tu telefono: ")
        
        try:
            p = [nombre, edad, sexo, telefono]
            if email in d:
                raise KeyError 
            else:
                d[email] = p
        except KeyError:
            print("ERROR al añadir persona")
    else:
        print("Email no válido")

    for persona in d.items():
        print(persona)
    
    opcion = input("¿Otra persona? (s/n): ").lower()
    if opcion == 'n':
        fin = True
    
print("HEMOS TERMINADO")