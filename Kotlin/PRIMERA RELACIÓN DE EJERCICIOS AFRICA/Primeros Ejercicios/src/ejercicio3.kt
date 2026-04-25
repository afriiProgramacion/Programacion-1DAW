fun main(){
    print("Introduce Dividendo: ")
    val a = readln().toIntOrNull() ?: 0

    print("Introduce Divisor: ")
    val b = readln().toIntOrNull() ?: 0

    try{
        val resultado: Float = divide(a.toFloat(), b.toFloat())
        println("El resultado es: $resultado")
    }catch (e: Exception){
        println(e.message)
    }
}



fun divide (a: Float, b: Float): Float{

    if (b==0.0f){
        throw IllegalArgumentException("ERROR: Division por cero")
    }else{
        return (a/b)
    }
}