
abstract class Vehiculo(val id: Int, val modelo: String, bateria: Int): Comparable<Vehiculo> {

    var bateria: Int = bateria
    set(value) {
        if (value in 0..100) {
            field = value
        }
        else if (value > 100)
                field = 100
        else field = 0

    }

    init {
        println("Vehículo con Bateria $bateria, de modelo $modelo, id $id")
    }
    override fun compareTo(other: Vehiculo): Int {
        return this.bateria - other.bateria
    }
        abstract fun calcularAutonomia(): Int

}