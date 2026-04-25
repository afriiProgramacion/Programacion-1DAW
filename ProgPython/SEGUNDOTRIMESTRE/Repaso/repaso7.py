l = ['naranja', 'manzana', 'mandarina']
l2 = ['naranja', 'pera', 'platano', 'mandarina']

c1 = set(l)
c2 = set(l2)

comunes = c1 & c2
print(comunes)