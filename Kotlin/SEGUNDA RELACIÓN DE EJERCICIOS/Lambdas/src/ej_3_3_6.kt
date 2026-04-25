fun main() {
    val vocales = setOf('a', 'e', 'i', 'o', 'u')
    val alfabeto = ('a'..'z').toSet()

    val consonantes = alfabeto - vocales
    val letrasComunes = vocales intersect consonantes

    println("vocales: $vocales")
    println("consonantes: $consonantes")
    println("letras_comunes: $letrasComunes")
}

