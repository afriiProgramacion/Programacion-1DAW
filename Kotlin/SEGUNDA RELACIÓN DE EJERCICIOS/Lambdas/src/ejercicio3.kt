
fun main (){
    val cadenaLambda = {frase:String, p:Char -> frase.filter{it==p}.length}
    println(cadenaLambda("Consuelo", 'o'))
}