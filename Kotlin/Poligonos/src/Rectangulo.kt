open class Rectangulo (base: Int, var altura: Int) : Poligono(), Comparable<Rectangulo>, Dibujable {

    var base: Int = base

    init {
        if (base <1) {
            throw IllegalArgumentException("La base no puede ser menor a 1")
        }
        require(altura > 0) { "La altura no puede ser menor a 0" }
    }

    open override fun area(): Int {
        return base * altura
    }

    open override fun perimetro(): Int {
        return (base * 2 + altura * 2)
    }

    override fun toString(): String {
        var resultado: String = "Soy un rectángulo de $base x $altura"
        return (resultado)
    }

    override fun equals(other: Any?): Boolean {
        if (this === other)
            return true
        else
            return false
    }

    override fun compareTo(other: Rectangulo): Int {
        if (this.perimetro()==other.perimetro())
            return 0
        else
            return this.perimetro() - other.perimetro()
    }

    override fun dibuja() {
        for (i in 0 until this.altura) {
            for (j in 0 until this.base) {
                print("*")
            }
            println("")
        }
    }
}