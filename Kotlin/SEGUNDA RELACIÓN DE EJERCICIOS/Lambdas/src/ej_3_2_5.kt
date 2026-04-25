fun main() {
    val asignaturas = mapOf(
        "Matematicas" to 6,
        "Fisica" to 4,
        "Quimica" to 5
    )

    var totalCreditos = 0

    for ((asignatura, creditos) in asignaturas) {
        println("$asignatura tiene $creditos creditos")
        totalCreditos += creditos
    }

    println("El numero total de creditos del curso es $totalCreditos")
}

