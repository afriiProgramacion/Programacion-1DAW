fun main () {
    val asignaturas: Map<String, Int> = mapOf(
        "Programación" to 6,
        "Entornos de desarrollo" to 4,
        "Digitaización" to 5
    )

    var TotalCreditos = 0
    for ((asignatura, creditos) in asignaturas) {
        println("$asignatura tiene $creditos créditos")
        TotalCreditos += creditos
    }
    TotalCreditos = 0

    asignaturas.forEach { (asignatura, notas) ->  println("$asignatura tiene $notas notas")}
    TotalCreditos = asignaturas.values.sum()
    println("El número total de créditos es $TotalCreditos")

}