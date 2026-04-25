fun main(){

    val t = Tecnico("530932042Z", "Daniel", "Espinosa", 1400.00,2)
    val c = Comercial("53096042Y", "Africa","Galindo",1500.00,200.00)

    val empresa = Plantilla()

    empresa.contratarEmpleado(t)
    empresa.contratarEmpleado(c)

    val lista = empresa.getEmpleadosPorNombre("a")

    if (lista.isNotEmpty()) {
        lista.forEach {println(it)}
    }
}