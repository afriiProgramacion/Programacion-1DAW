/* Escribir un programa que solicite el ingreso de una cantidad indeterminada de números
mayores que 1, finalizando cuando se reciba un cero. Imprimir la cantidad de números
primos ingresados */

fun esPrimo(n: Int): Boolean {
    if (n <= 1) return false
    for (i in 2 until n) {
        if (n % i == 0) {
            return false
        }
    }
    return true
}

fun main(){
    var primos = 0
    do {
        print("Introduce un numero mayor que 1: ")
        var num = readLine()?.toIntOrNull() ?: 1
        if(esPrimo(num)){
            primos++
        }
    } while(num != 1)
    println("Has introducido ${primos} números primos")
}