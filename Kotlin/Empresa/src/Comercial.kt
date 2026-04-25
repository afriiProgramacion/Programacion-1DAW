class Comercial (nombre: String, edad: Int, salarioBase: Double, val ventasRealizadas: Int): Empleado(nombre, edad, salarioBase), Bonificable {

    override fun salarioTotal(): Double {
        return salarioBase + (ventasRealizadas *20)
    }

    override fun descripcion(): String {
        return "Comercial: $nombre, edad: $edad, salario base: $salarioBase, ventas realizadas: $ventasRealizadas"
    }

    override fun calculaBono(): Double {
        return salarioTotal() * 0.05
    }

}