class Triangulo (var l1: Int, var l2: Int, var l3: Int): Poligono() {

    init {
        require ((l1<l2+l3)&&(l2<l1+l3)&&(l3<l1+l2)){"ERROR NO ES TRIANGULO"}
        println("Triangulo creado correctamente")
    }




    override fun perimetro(): Int {
        return (l1 + l2 + l3)
    }

    override fun area(): Int {
        var sp: Double = 0.0
        var aHeron: Double = 0.0

        sp = (this.perimetro()/2).toDouble()
        aHeron = Math.sqrt(sp*(sp-l1)*(sp-l2)*(sp-l3))

        return aHeron.toInt()
    }

    override fun toString(): String {
        var resultado: String = "Soy un triángulo de lados $l1, $l2 y $l3"
        return (resultado)
    }
}