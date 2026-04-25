abstract class Empleado( nombre: String, edad: Int, var salarioBase: Double) : Persona(nombre, edad) {

    override fun descripcion(): String {
        return "Empleado: $nombre, edad: $edad, salario base: $salarioBase"
    }


    abstract fun salarioTotal(): Double
}
