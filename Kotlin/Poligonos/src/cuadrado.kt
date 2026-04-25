class cuadrado (var lado: Int): Rectangulo(lado, lado) {

    override fun toString(): String {
        var resultado: String = "Soy un cuadrado de lado $lado"
        return (resultado)
    }

}