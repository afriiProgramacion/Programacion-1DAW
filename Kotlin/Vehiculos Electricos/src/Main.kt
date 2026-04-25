fun main() {
    val flota = Flota()

    // Crear vehículos
    val p1 = Patinete(1, "Xiaomi", 80, 30)
    val p2 = Patinete(2, "Segway", 40, 20)
    val b1 = BicicletaElectrica(3, "Trek", 60, 3)

    // Agregar a la flota
    flota.agregar(p1)
    flota.agregar(p2)
    flota.agregar(b1)

    // Mostrar ordenados por batería
    println("\n--- Vehículos ordenados por batería ---")
    flota.listarOrdenadosPorBateria().forEach {
        println("${it.modelo} → batería: ${it.bateria}%")
    }

    // Modificar batería (prueba el setter)
    println("\n--- Modificando batería ---")
    p1.bateria = 150   // debería forzarse a 100
    p2.bateria = -10   // debería forzarse a 0
    println("p1 batería: ${p1.bateria}")  // 100
    println("p2 batería: ${p2.bateria}")  // 0

    // Eliminar un vehículo
    println("\n--- Eliminando vehículo con id 2 ---")
    flota.eliminarPorId(2)

    // Vehículos en activo y autonomía media
    println("\n--- Estado de la flota ---")
    val activos = flota.listarOrdenadosPorBateria()
    println("Vehículos en activo: ${activos.size}")
    println("Autonomía media: ${flota.autonomiaMedia()} km")
}