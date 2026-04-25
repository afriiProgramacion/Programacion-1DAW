fun main () {
    var r: Rectangulo = Rectangulo(5, 2)
    var c: cuadrado = cuadrado (4)
    var t: Triangulo?= null
    
    try {
        t = Triangulo(5, 4, 6)
    } catch (e: Exception) {
        println(e.message)
        Poligono.contadorPoligono--
    }
    
    var lista: MutableList <Poligono> = mutableListOf(r,c,t)
    //lista.sort()

    for (poligono in  lista) {

            println(poligono)
            println("El perímetro es ${poligono.perimetro()}")
            println("El área es ${poligono.area()}")
            if (poligono is Rectangulo)
                poligono.dibuja()

    }

    println("El número total de polígonos es: ${Poligono.contadorPoligono}")

    if (t!= null) {
        println(t)
        println("El perímetro es ${t.perimetro()}")
        println("El área es ${t.area()}")
    }


}