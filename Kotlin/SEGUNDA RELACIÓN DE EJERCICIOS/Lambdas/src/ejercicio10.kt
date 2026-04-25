fun main() {
    val precios = listOf(50,75,46,22,80,65,8)
    val precios2 = intArrayOf(50,75,46,22,80,65,8)

    var menor = precios[0]
    var mayor = precios[0]

    for (precio in precios) {
        if (precio > mayor)
            mayor = precio
        if (precio < menor)
            menor = precio
    }

    println("El precio menor es: $menor")
    println("El precio mayor es: $mayor")

    println("El precio mayor es: ${precios2.max()}")
    println("El precio menor es: ${precios2.min()}")
}