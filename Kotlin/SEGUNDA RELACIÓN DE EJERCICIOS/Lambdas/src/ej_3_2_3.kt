fun main() {
    val preciosFrutas = mapOf(
        "platano" to 1.35,
        "manzana" to 0.80,
        "pera" to 0.85,
        "naranja" to 0.70
    )

    println("Introduce una fruta:")
    val fruta = readln().trim().lowercase()

    println("Introduce el numero de kilos:")
    val kilos = readln().trim().toDoubleOrNull()

    if (kilos == null || kilos < 0) {
        println("Cantidad de kilos no valida.")
        return
    }

    val precioKilo = preciosFrutas[fruta]
    if (precioKilo == null) {
        println("La fruta '$fruta' no esta en el diccionario.")
    } else {
        val total = precioKilo * kilos
        println("$kilos kg de $fruta cuestan %.2f euros.".format(total))
    }
}

