/* Escribir un programa que pida al usuario un número entero y muestre por pantalla un
triángulo rectángulo como el de más abajo, de altura el número introducido.
*
**
***
****
*/

fun main(){
    print("Introduce un numero: ")
    var triangulo = "*"
    val numero = readln().toInt()
    for (i in 0..numero){
        println(triangulo)
        triangulo += "*"
    }
}