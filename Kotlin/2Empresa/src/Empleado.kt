abstract class Empleado(val dni: String, val nombre: String, val apellidos: String, sueldoB: Double): Comparable<Empleado> {

    companion object {
        const val SALARIO_MINIMO = 1200.00
    }

    var sueldoBase: Double = SALARIO_MINIMO
        set(value) {
            if (value > SALARIO_MINIMO)
                field = value
        }
    init {
        this.sueldoBase = sueldoB
    }

    abstract fun getSueldo(): Double

    override fun toString(): String {
        return "dni: $dni \n nombre: $nombre \n apellidos: $apellidos \n Sueldo base: $sueldoBase" + "\n NETO: " + this.getSueldo()
    }

    override fun compareTo(other: Empleado): Int{
        return (this.getSueldo()-other.getSueldo()).toInt()
    }
}