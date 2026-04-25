palabra = input("Introduceme una palabra: ")

try:
    for i in range (len(palabra)):
        print(f"letra {i}: {palabra[i]}")
except IndexError:
    print("ERROR. índice fuera de rángo")
