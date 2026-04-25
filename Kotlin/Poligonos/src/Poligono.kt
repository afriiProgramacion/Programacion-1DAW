abstract class Poligono {

    init {
        contadorPoligono++
    }


    companion object {
        var contadorPoligono: Int = 0
    }

    abstract fun area (): Int
    abstract fun perimetro() : Int
}