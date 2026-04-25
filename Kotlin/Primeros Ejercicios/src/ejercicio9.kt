fun main () {

    val ingredientes = "Tomate, Mozzarella"
        menu()
        println("Elige una opción: ")
        val option = readln().toInt()

        when (option) {
            1 -> {
                println("Has elegido vegetariana!!")
                vegetariana()
                val option = readln().toInt()

                when (option) {
                    1 -> println("Los ingredientes de tu pizza son ${ingredientes + ", Pimiento"}")
                    2 -> println("Los ingredientes de tu pizza son ${ingredientes + ", Tofu"}")
                    else -> println("Opción no válida")
                }
            }
            2 -> {
                println("Has elegido La pizza no vegetariana")
                no_vegetariana()
                val option = readln().toInt()
                print("Elige un solo ingrediente: ")
                when (option) {
                    1 -> println("Los ingredientes de tu pizza son ${ingredientes + ", Pepperoni"}")
                    2 -> println("Los ingredientes de tu pizza son ${ingredientes + ", Jamón"}")
                    3 -> println("Los ingredientes de tu pizza son ${ingredientes + ", Salmón"}")
                    else -> println("Opción no válida")

                }
            }
            else -> println("Opción no válida")
        }

}
fun menu() {
    println("ELIGE TU PIZZA")
    println("1. PIZZA VEGETARIANA")
    println("2. PIZZA NO VEGETARIANA")
}
fun vegetariana() {
    println("Elige un solo ingrediente: ")
    println("1. Pimiento")
    println("2. Tofu")
}

fun no_vegetariana() {
    println("Elige un solo ingrediente: ")
    println("1. Pepperoni")
    println("2. Jamón")
    println("3. Salmón")
}

/*
fun principal () {
    val option = readLine()!!.toInt()
    menu()
    print("INTRODUCE UNA OPCIÓN")
    val vegetariana = readLine()!!.toInt()

    when (option) {

        1 -> True
    }
}

 */