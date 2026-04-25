/* Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la
suma de los dígitos que lo componen. La condición de corte es que se ingrese el número
-1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron
números pares. */

fun main(){
    var numero: Int = 0
    var cantidadPares: Int = 0

    do{
        print("Introduce un numero entero positivo (-1 para salir): ")
        numero = readLine()?.toIntOrNull() ?: 0

        if (numero != -1){
            val sumaDigitos = sumaDigitos(numero)
            println("La suma de los digitos es $numero es: ${sumaDigitos}")

            if (numero%2 == 0){
                cantidadPares++
            }
        }
    } while(numero != -1)
    println("Cantidad de numeros pares ingresados: $cantidadPares")
}

fun sumaDigitos(n: Int): Int{
    var numero: Int = Math.abs(n)
    var suma: Int = 0
    var digito: Int = 0

    while (numero>0){
        digito=numero%10
        suma=suma+digito
        numero=numero/10
    }
    return suma
}