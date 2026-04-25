class Flota {
    private val vehiculos = mutableListOf<Vehiculo>()

    fun agregar(v: Vehiculo) {
        vehiculos.add(v)
    }
    fun eliminarPorId (id:Int) {
        vehiculos.removeIf { it.id == id }
    }
    fun listarOrdenadosPorBateria (): List<Vehiculo> {
        return vehiculos.sortedBy(Vehiculo::bateria)
    }
    fun autonomiaMedia (): Double {
        return vehiculos.map { it.calcularAutonomia() }.average()
    }
}
