public class Coche ( marca: String?, var color: String?, modelo: String?, val numeroCaballos: Int?, val numPuertas: Int?, val matricula: String?) {

    val marca: String? = marca
        get() = field?.replaceFirstChar { it.uppercase() }
    val modelo: String? = modelo
        get() = field?.replaceFirstChar { it.uppercase() }

    init {
        require(!marca.isNullOrBlank()) { "La marca no puede ser nula ni vacía" }
        require(!modelo.isNullOrBlank()) {"El modelo no puede ser nulo ni vacío"}
        require(numeroCaballos != null) { "Los caballos no pueden ser nulos" }
        require(numeroCaballos in 70..700) { "Los caballos deben estar entre 70 y 700" }
        require(numPuertas != null) { "Las puertas no puede ser nulos" }
        require(numPuertas in 3 .. 5)
        require(!matricula.isNullOrBlank()) {"La matricula no puede ser nulo"}
        require(matricula.length == 7) { "La matrícula debe tener 7 caracteres" }
        require(!color.isNullOrBlank()) {"El color no puede ser nulo"}


    }

    override fun toString(): String {
       var descripcion: String = "Coche de marca $marca, modelo $modelo, color $color, con $numPuertas, puertas,  $numeroCaballos caballos y  matricula $matricula"
        return descripcion
        
    }
}