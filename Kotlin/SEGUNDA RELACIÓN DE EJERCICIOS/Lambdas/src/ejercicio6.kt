fun main() {
    print("Introduce una palabra: ")

    val palabra: String = readLine()?.trim() ?: ""
    val inversa: String = palabra.reversed()

    val esPalindromo = palabra.equals(inversa, ignoreCase = true)
    println("La palabra $palabra ${if (esPalindromo) "es" else "NO es"}")
}