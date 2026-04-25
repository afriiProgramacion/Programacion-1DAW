class persona (var peso: Double, var altura: Double) {
    var nombre: String? = null

    val imc: Double
        get() {
            return (peso / (altura * altura))
        }
    constructor(nombre: String, p: Double, a: Double): this(p,a) {
        this.nombre = nombre
    }

    override fun toString(): String {
        var resultado: String = "Soy una persona, ${if(this.nombre != null) "Nombre: $nombre" else "in nombre"}, peso: $peso, altura: $altura, IMC: ${String.format("%.2f",imc)}"
        return resultado
    }

    fun presentarse(): String {
        var resultado: String = "HOLA SOY: " + this.toString() + "IES RAFAEL ALBERTI"
        return (resultado)
    }

    fun presentarse(edad: Int): String {
        var resultado: String = this.presentarse() + " y tengo $edad años"
        return resultado
    }

    fun alturaEncimaMedia(): Boolean {
        if (this.altura >= 1.75)
            return true
        else
            return false
    }

    fun pesoEncimaMedia(): Boolean {
        if (this.peso >= 70)
            return true
        else
            return false
    }

    fun obtenerDescImc(): String {
        return when {
            imc < 18.5 -> "Peso insuficiente"
            imc < 24.9 -> "Peso saludable"
            imc < 29.9 -> "Sobrepeso"
            else -> "Obesidad"
        }
    }

    fun obtenerDesc(): String {
        val nombrePersona = nombre ?: "Persona sin nombre"
        val alturaDesc = if (alturaEncimaMedia()) "Por encima de la media" else "Por debajo de la media"
        val pesoDesc = if (pesoEncimaMedia()) "Por encima de la media" else "Por debajo de la media"
        val imcDesc = obtenerDescImc()

        return "$nombrePersona con una altura de ${altura}m ($alturaDesc) y un peso de ${peso}kg ($pesoDesc) tiene un IMC de ${String.format("%.2f", imc)} ($imcDesc)."
    }

    override fun equals(other: Any?): Boolean {
        if (other !is persona)
            return false
        if (this === other)
            return true

        if ((this.nombre == other.nombre) && (this.imc == other.imc))
            return true
        else
            return false
    }
}