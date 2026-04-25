mail = input("Dame tu correo: ")
pos_arroba = mail.find("@")
user = mail[:pos_arroba]
print (f"{user}@ceu.es")