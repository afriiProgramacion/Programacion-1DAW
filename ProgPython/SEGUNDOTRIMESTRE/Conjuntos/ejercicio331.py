def direcciones_facturacion(compras):
    conjuntoDirecciones = set()

    for compra in compras:
        conjuntoDirecciones.add(compra[3])
    
    return conjuntoDirecciones


def diccionario_facturacion(compras):
    diccionarioClientes = {}

    for compra in compras:
        diccionarioClientes[compra[3]] = compra[0]

    return diccionarioClientes


# Ejemplo de datos (debes poner datos reales aquí)
compras = [
    ("Cliente1", "ProductoA", 10, "Calle A"),
    ("Cliente2", "ProductoB", 20, "Calle B"),
    ("Cliente3", "ProductoC", 30, "Calle A")
]

conjunto = direcciones_facturacion(compras)

for direccion in conjunto:
    print(direccion)

print('*' * 10)

diccionario = diccionario_facturacion(compras)

for cliente in diccionario.items():
    print(cliente)
