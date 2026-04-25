data class Venta(
    val cliente: String,
    val dia: Int,
    val monto: Double,
    val domicilio: String
)

fun domiciliosParaFacturas(ventas: List<Venta>): Set<String> {
    return ventas.map { it.domicilio }.toSet()
}

fun main() {
    val ventas = listOf(
        Venta("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"),
        Venta("Jorge Russo", 7, 699.0, "Mirasol 218"),
        Venta("Nuria Costa", 7, 532.90, "Calle Las Flores 355"),
        Venta("Julian Rodriguez", 12, 5715.99, "La Mancha 761"),
        Venta("Jorge Russo", 15, 958.0, "Mirasol 218")
    )

    val domicilios = domiciliosParaFacturas(ventas)
    println("Domicilios a los que enviar factura:")
    domicilios.forEach { println(it) }
}

