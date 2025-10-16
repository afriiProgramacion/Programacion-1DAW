precio = input("Dime el precio de un producto en euros con dos decimales: ")
euros = precio.split(".")[0]
centimos = precio[-2:]
print (f"El precio que has introducido son {euros} euros y {centimos} céntimos")