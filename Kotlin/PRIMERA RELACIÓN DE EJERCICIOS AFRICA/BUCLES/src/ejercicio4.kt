/* Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla la cuenta atrás desde ese número hasta cero separados por comas.*/

fun main() {

    print("Introduce un número entero positivo: ")
    val num: Int = readln().toInt()

    if (num >= 0) {
        for (i in 1..num) {
            print("${num-i},")
        }
    }

}