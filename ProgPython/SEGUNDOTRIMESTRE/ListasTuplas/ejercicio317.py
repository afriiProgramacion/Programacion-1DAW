abecedario = list("abcdefghijklmnopqrstuvwxyz")
i = 0
while i < (len(abecedario)):
    if i % 3 == 0:
            abecedario = abecedario.pop(i)
    i += 1
print(abecedario)


