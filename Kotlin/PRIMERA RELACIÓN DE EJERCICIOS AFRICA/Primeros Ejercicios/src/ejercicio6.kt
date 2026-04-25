/* Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el
nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y los
hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa
que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le
corresponde */

fun main(){
    print("Cual es tu nombre: ")
    val nombre = readln()
    print("Cual es tu sexo: ")
    val sexo = readln()
    println(comprobar(nombre,sexo))
}

fun comprobar(n: String, s: String){

    if (s == "F" && n[0].uppercaseChar() < 'M'){
        println("Perteneces al Grupo A")
    } else if (s == "M" && n[0].uppercaseChar() > 'N' ) {
        println("Perteneces al Grupo A")
    } else {
        println("Perteneces al Grupo B")
    }
}