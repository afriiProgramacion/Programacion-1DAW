fun main () {
    val p1 = persona("Afri", 54.3, 1.57)
    val p2 = persona("Daniel", 60.00, 1.75)
    val p3 = persona("Gali", 55.00, 1.70)
    val p4 = persona("Selu", 65.00, 1.60)
    val p5 = persona("Laura", 80.0, 1.80)
    val p6 = persona("Juan", 75.0, 1.65)

    val personas = listOf(p1, p2, p3, p4, p5, p6)

    for (persona in personas) {
        println(persona.presentarse())
        println(persona.obtenerDesc())
        println("-".repeat(80)) 
    }
}