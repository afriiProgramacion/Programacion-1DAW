fun main() {
    val combinacion = (1..49).shuffled().take(6).sorted()
    println("Combinacion valida para La Primitiva:")
    println(combinacion.joinToString(" - "))
}

