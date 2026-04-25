class Comercial(dni: String, nombre: String, apellidos: String, sueldoBase: Double, ventas: Double): Empleado(dni,nombre,apellidos,sueldoBase) {

    var ventas: Double = 0.0
        set(value){
            if (value > 120)
                field = value
            else
                field = (SALARIO_MINIMO / 10).toDouble()
        }
    init {
        this.ventas=ventas
    }

    override fun getSueldo(): Double{
        return(this.sueldoBase + 0.10 * this.ventas).toDouble()
    }
}