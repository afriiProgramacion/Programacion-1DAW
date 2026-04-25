/*
En una determinada empresa, sus empleados son evaluados al final de cada año. Los
puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando,
traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados
pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas.
A continuación, se muestra una tabla con los niveles correspondientes a cada
puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada
por la puntuación del nivel.
Nivel Puntuación
Inaceptable 0.0
Aceptable 0.4
Meritorio 0.6 o más
 */




fun main () {
    print("Introduce tu puntuación: ")
    val puntos = readln().toFloat()
    println(puntuacion(puntos))
}

fun puntuacion (p:Float) {
    val resultado : String
    if (p in 0.0..<0.4) {
        println("Inaceptable ${((2400 * p) + 2400)}")
    } else if (p in 0.4..<0.6){
        println("Aceptable ${((2400 * p) + 2400)}")
    } else {
        println("Meritorio ${((2400 * p) + 2400)}")
    }
}