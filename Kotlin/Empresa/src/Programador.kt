class Programador (nombre: String, edad: Int, salarioBase: Double, val lineasCodigoPorDia: Int, var lenguajeFavorito: String): Empleado(nombre, edad, salarioBase), Bonificable {

    override fun salarioTotal(): Double {
        return salarioBase + (lineasCodigoPorDia * 0.5)
    }

    override fun descripcion(): String {
        return "Programador: $nombre, edad: $edad, salario base: $salarioBase, lineas de código por día: $lineasCodigoPorDia, lenguaje favorito: $lenguajeFavorito"
    }
    override fun calculaBono(): Double {
        return salarioTotal() * 0.10
    }
}