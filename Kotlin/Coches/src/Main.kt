fun main(){
    val c1 = Coche(null, "azul", null, 100, 5, "6126KDK")
    val c2 = Coche("Citroen", "Gris", "Xsara", 800, 5, "CA9575BL")
    val c3 = Coche("Seat", "rojo", "Ronda", 75, 2, "9835CJW")
    val c5 = Coche(marca = "Seat", color = "Rojo", modelo = "Ibiza",
        numeroCaballos = 100, numPuertas = 4, matricula = "1234ABC")
    try {
        c5.color = null
    } catch (e: IllegalArgumentException) {
        println("Error al modificar: ${e.message}")
    }

}