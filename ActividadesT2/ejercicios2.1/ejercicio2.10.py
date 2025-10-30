pizza = input ("¿Qué pizza quieres vegetariana o no vegetariana?: ")
pizza_vegetariana = "Pimiento y Tofu"
pizza_no_vegetariana = "Pepperoni, Jamón y Salmón"

if pizza == "vegetariana":
    print(pizza_vegetariana)
    ingredientes = input("Qué ingrediente eliges?: ")
    print(f"La pizza es una pizza {pizza} y el ingrediente elegido es {ingredientes}")
else:
    print(pizza_no_vegetariana)
    ingredientes = input("Que ingrediente quieres?: ")
    print(f"La pizza es una pizza {pizza} y el ingrediente elegido es {ingredientes}")



