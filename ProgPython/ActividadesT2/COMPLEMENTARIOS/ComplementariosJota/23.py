#Diseña un algoritmo en el que, dadas tres personas, por ejemplo Pedro, Alicia y Carla,
# indique quiénes son de la misma quinta.

pedro = int(input("Introduce edad de Pedro: "))
alicia = int(input("Introduce edad de Alicia: "))
carla = int(input("Introduce edad de Carla: "))

if carla == pedro and pedro == alicia:
    print("Todos son de la misma quinta.")
else:
    if pedro == alicia and pedro != carla:
        print("Pedro y Alicia son de la misma quinta.")
    elif pedro == carla and pedro != alicia:
        print("Pedro y carla son de la misma quinta.")
    elif carla == alicia and carla != pedro:
        print("Carla y Alicia son de la misma quinta.")
    else:
        print("Cada uno tiene una edad.")