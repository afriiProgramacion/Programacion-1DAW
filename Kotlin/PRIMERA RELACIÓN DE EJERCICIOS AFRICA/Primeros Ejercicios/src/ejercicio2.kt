/* Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña
introducida por el usuario coincide con la guardada en la variable sin tener en cuenta
mayúsculas y minúsculas. */
fun main() {
    val contrasenaG = "manteca1234"
    print("Introduce la contrasena: ")
    val contrasena = readLine()?.lowercase()

    if (contrasena != null && contrasena == contrasenaG) {
        println("La contrasena es correcta")
    } else {
        println("La contrasena es incorrecta")
    }
}