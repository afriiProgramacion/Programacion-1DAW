def pintaMenu():
    print("(1) Añadir cliente") 
    print("(2) Eliminar cliente") 
    print("(3) Mostrar cliente") 
    print("(4) Listar todos los clientes") 
    print("(5) Listar clientes preferentes") 
    print("(6) Terminar")


def añadir_cliente(clientes):
    nif = input("NIF DEL CLIENTE: ")
    if nif in clientes:
        print("Ya existe un cliente con ese NIF")
    else:
        nombre = input("Nombre: ")
        direccion = input("Dirección: ")
        telefono = input("Telefono: ")
        correo = input("Correo: ")
        preferente = input("¿Es cliente preferente (s/n?: ").lower()
        clientes[nif] = {
            'nombre': nombre,
            'direccion': direccion,
            'telefono': telefono,
            'correo': correo,
            'preferente': preferente
        }
        print("Cliente añadido correctamente")

def eliminar_cliente(clientes):
    nif = input("NIF del cliente a eliminar: ")
    if nif in clientes:
        del clientes[nif]
        print("Cliente eliminado")
    else:
        print("Cliente no encontrado")

def mostrar_cliente(clientes):
    nif = input("NIF del cliente: ")
    cliente = clientes.get(nif)

    if cliente:
        print(f"\Los datos del cliente {nif}")
        for clave, valor in cliente.items():
            print(f"{clave.capitalize()}: {valor}")
    else:
        print("Cliente no encontrado")

def listar_clientes(clientes):
    if not clientes:
        raise NameError ("No hay clientes registrados")
    
    print("\n Lista de todos los clientes: ")
    for nif, datos in clientes.items():
        if datos['preferente'] =='s':
            preferencia = 'SÍ'
        elif datos['preferente'] == 'n':
            preferencia = 'NO'
        else:
            raise NameError("Cuidado... hay dátos erróneos en el diccionario")
        
        print(f"{nif}: {datos['nombre']} {datos['direccion']} {datos['telefono']} {datos['correo']} Preferente: {preferencia}")

def listar_preferentes(clientes):
    contador = 0
    print("\n Clientes preferentes: ")

    for nif, datos in clientes.items():
        if datos['preferente'] == 's':
            print(f"{nif}: {datos['nombre']} {datos['direccion']} {datos['telefono']} {datos['correo']} Preferente{datos['preferente']}")
            contador +=1
        if contador == 0:
            print("NO HAY CLIENTES PREFERENTES")


opcion = "1"
clientes = {}
while opcion != "6":
    print(pintaMenu())
    opcion = input("Elige una opcion: ")
    match opcion:
        case "1":
            print(añadir_cliente(clientes))
        case "2":
            print(eliminar_cliente(clientes))
        case "3":
            print(mostrar_cliente(clientes))
        case "4":
            print(listar_clientes(clientes))
        case "5":
            print(listar_preferentes(clientes))
        case "6":
            print("Programa finalizado")