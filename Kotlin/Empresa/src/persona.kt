abstract class Persona (nombre: String,  edad: Int) {
    var nombre: String = nombre
    var edad: Int = edad

    init {
        contadorPersona++
    }

    companion object {
        var contadorPersona: Int = 0
    }

    abstract fun descripcion(): String

    override fun toString(): String {
        var descripcion = "Soy una persona con nombre $nombre y $edad años"
        return descripcion
    }
}