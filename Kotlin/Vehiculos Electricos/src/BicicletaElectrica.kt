class BicicletaElectrica (id: Int, modelo: String, bateria: Int, var asistenciaNiveles: Int): Vehiculo(id,modelo,bateria) {
    override fun calcularAutonomia(): Int {
        return bateria * asistenciaNiveles
    }
}