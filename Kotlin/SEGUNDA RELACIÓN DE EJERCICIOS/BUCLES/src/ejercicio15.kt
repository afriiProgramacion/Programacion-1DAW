fun main () {
    var sumaPositivos = 0
    var numero: Int? = 0

    do {
        print("Ingresa un número (0 para terminar): ")
        val entrada = readLine()

        numero = entrada?.toInt()

        if (numero == null) {
            println("Entrada inválida. Por favor ingresa un número entero")
        } else if (numero > 0) {
            sumaPositivos += numero
        }
    } while (numero != 0)
    println("La sumatoria de los numeros es: $sumaPositivos")

    }