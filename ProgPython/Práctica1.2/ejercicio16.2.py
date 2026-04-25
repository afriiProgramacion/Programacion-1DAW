PRECIO_BARRA = 3.49
no_fresco = 0.6
barras = int(input("¿Cuántas barras que no son del día has vendido?: "))
precio_habitual = barras * PRECIO_BARRA
precio_desc = precio_habitual * no_fresco


print ("El precio habitual de las barras que vas a comprar sería:", precio_habitual)
print ("Cómo has comprado barras que no son del día, el precio es:", precio_desc)
