fun main() {
    val persona = mutableMapOf<String, String>()

    println("Introduce datos de una persona. Escribe 'fin' como campo para terminar.")

    while (true) {
        println("Campo:")
        val campo = readln().trim()
        if (campo.equals("fin", ignoreCase = true)) break
        if (campo.isEmpty()) {
            println("El campo no puede estar vacio.")
            continue
        }

        println("Valor de $campo:")
        val valor = readln().trim()
        persona[campo] = valor

        println("Contenido actual del diccionario:")
        println(persona)
    }

    println("Diccionario final:")
    println(persona)
}

