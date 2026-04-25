/* Escribir un programa que pregunte al usuario un entero del 1 al 100 y a continuación
muestre por pantalla la tabla de multiplicar de ese número.*/

fun main() {
    print("Introduce un número del 1 al 100: ")
    val n1 = readln().toInt()

    if (n1 in 0.. 100)
        for (i in 0..10){
            println("${i} x ${n1} = ${n1*i}")
        }
    else {
        print("El número introducido no es válido36")
    }
}