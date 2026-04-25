fun main() {
    val diccionario = mutableMapOf<String, String>()

    println("Introduce pares palabra:traduccion separados por comas:")
    val entrada = readln().trim()

    entrada.split(",").forEach { par ->
        val partes = par.split(":")
        if (partes.size == 2) {
            val espanol = partes[0].trim().lowercase()
            val ingles = partes[1].trim()
            if (espanol.isNotEmpty() && ingles.isNotEmpty()) {
                diccionario[espanol] = ingles
            }
        }
    }

    println("Introduce una frase en espanol:")
    val frase = readln()

    val traducida = frase.split(" ").joinToString(" ") { palabra ->
        val clave = palabra.lowercase()
        diccionario[clave] ?: palabra
    }

    println("Frase traducida:")
    println(traducida)
}

