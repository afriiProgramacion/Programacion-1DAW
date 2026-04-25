fun leerNombres(nivel: String): Set<String> {
    val nombres = mutableSetOf<String>()
    println("Introduce nombres de $nivel (x para terminar):")

    while (true) {
        val nombre = readln().trim()
        if (nombre.equals("x", ignoreCase = true)) break
        if (nombre.isNotEmpty()) nombres.add(nombre)
    }

    return nombres
}

fun main() {
    val primaria = leerNombres("primaria")
    val secundaria = leerNombres("secundaria")

    val todos = primaria union secundaria
    val repetidos = primaria intersect secundaria
    val soloPrimaria = primaria - secundaria
    val primariaIncluidaEnSecundaria = primaria.all { it in secundaria }

    println("\nNombres sin repeticiones:")
    println(todos)

    println("Nombres repetidos entre primaria y secundaria:")
    println(repetidos)

    println("Nombres de primaria que no se repiten en secundaria:")
    println(soloPrimaria)

    println("Todos los nombres de primaria estan incluidos en secundaria: $primariaIncluidaEnSecundaria")
}

