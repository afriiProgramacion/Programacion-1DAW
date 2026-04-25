fun main () {
    var r1: Rectangulo? = null

    try {
        r1 = Rectangulo(5, 4)
    } catch (e: Exception) {
        println(e)
    }
    if (r1 != null) {
        r1.base = -5
        println("Mi perímetro es ${r1.perimetro()}")
        println("Mi área es ${r1.area()}")
        println(r1)
    }

}
