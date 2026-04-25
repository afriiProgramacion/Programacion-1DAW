import kotlin.math.sqrt

fun main() {
    println("Introduce una muestra de numeros separada por espacios o comas:")
    val entrada = readln().trim()

    val numeros = entrada
        .split(',', ' ')
        .map { it.trim() }
        .filter { it.isNotEmpty() }
        .mapNotNull { it.toDoubleOrNull() }

    if (numeros.isEmpty()) {
        println("No se han introducido numeros validos.")
        return
    }

    val media = numeros.average()
    val varianza = numeros.map { (it - media) * (it - media) }.average()
    val desviacionTipica = sqrt(varianza)

    println("Media: %.4f".format(media))
    println("Desviacion tipica: %.4f".format(desviacionTipica))
}

