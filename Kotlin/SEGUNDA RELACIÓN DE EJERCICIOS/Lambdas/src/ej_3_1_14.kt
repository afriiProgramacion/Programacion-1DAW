fun main() {
    val letras = "TRWAGMYFPDXBNJZSQVHLCKE"

    println("Introduce el DNI (8 numeros y letra, por ejemplo 12345678Z):")
    val dni = readln().trim().uppercase()

    val patron = Regex("^(\\d{8})([A-Z])$")
    val coincidencia = patron.matchEntire(dni)

    if (coincidencia == null) {
        println("Formato de DNI no valido.")
        return
    }

    val numero = coincidencia.groupValues[1].toInt()
    val letraUsuario = coincidencia.groupValues[2][0]
    val letraCorrecta = letras[numero % 23]

    if (letraUsuario == letraCorrecta) {
        println("DNI valido.")
    } else {
        println("DNI no valido. La letra correcta para $numero es $letraCorrecta.")
    }
}

