fun main() {
    val numeros = (1..10).toSet()

    val pares = numeros.filter { it % 2 == 0 }.toSet()
    val multiplosDeTres = numeros.filter { it % 3 == 0 }.toSet()
    val paresYMultiplosDeTres = pares intersect multiplosDeTres

    println("numeros: $numeros")
    println("pares: $pares")
    println("multiplos_de_tres: $multiplosDeTres")
    println("pares_y_multiplos_de_tres: $paresYMultiplosDeTres")
}

