/* Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los
años que ha cumplido (desde 1 hasta su edad). */

fun main() {
    print("¿Qué edad tienes?: ")
    val edad = readln().toInt()

    for (i in 1..edad) {
        println("$i ")
    }
}