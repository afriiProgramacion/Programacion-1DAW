peso = float(input("Introduce tu peso en Kg: "))
altura = float(input("Introduce también tu estatura en metros: "))
imc = peso / altura **2
imc_redond = round(imc, 2)
print ("Tu indice de masa corporal es:", imc_redond)