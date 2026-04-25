class Patinete (id: Int, modelo: String, bateria: Int, autonomiaKm: Int): Vehiculo(id, modelo, bateria) {

    var autonomiaKm: Int = autonomiaKm

    override fun calcularAutonomia(): Int {
        return autonomiaKm
    }
}