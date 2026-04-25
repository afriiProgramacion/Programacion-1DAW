/* Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-
finalizar programa. A continuación, el usuario debe poder seleccionar una opción (1, 2 ó
3). Si elige una opción incorrecta, informarle del error. El menú se debe volver a
mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las
opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión
del menú y el programa finalizará. */

fun menu(){
    println("1. Comenzar programa")
    println("2. Imprimir listado")
    println("3. Finalizar programa")
}

fun main(){
    do {
        menu()
        print("Introduce una opción: ")
        var opcion = readLine()?.toIntOrNull() ?: 3
        when(opcion){
            1 -> println("Has elegido comenzar el programa")
            2 -> println("Has elegido Imprimir listado")
            3 -> println("Has elegido finalizar programa")
            else -> println("Opcion incorrecta")
        }
    } while(opcion != 3)
    println("Programa finalizado")
}