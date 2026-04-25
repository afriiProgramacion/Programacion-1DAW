data class Cliente(
    val nombre: String,
    val direccion: String,
    val telefono: String,
    val correo: String,
    val preferente: Boolean
)

fun main() {
    val clientes = mutableMapOf<String, Cliente>()

    while (true) {
        println("\nMenu:")
        println("1. Anadir cliente")
        println("2. Eliminar cliente")
        println("3. Mostrar cliente")
        println("4. Listar todos los clientes")
        println("5. Listar clientes preferentes")
        println("6. Terminar")
        print("Opcion: ")

        when (readln().trim()) {
            "1" -> {
                print("NIF: ")
                val nif = readln().trim()
                print("Nombre: ")
                val nombre = readln().trim()
                print("Direccion: ")
                val direccion = readln().trim()
                print("Telefono: ")
                val telefono = readln().trim()
                print("Correo: ")
                val correo = readln().trim()
                print("Preferente (s/n): ")
                val preferente = readln().trim().equals("s", ignoreCase = true)

                clientes[nif] = Cliente(nombre, direccion, telefono, correo, preferente)
                println("Cliente anadido correctamente.")
            }

            "2" -> {
                print("NIF del cliente a eliminar: ")
                val nif = readln().trim()
                if (clientes.remove(nif) != null) {
                    println("Cliente eliminado.")
                } else {
                    println("No existe un cliente con ese NIF.")
                }
            }

            "3" -> {
                print("NIF del cliente: ")
                val nif = readln().trim()
                val cliente = clientes[nif]
                if (cliente == null) {
                    println("Cliente no encontrado.")
                } else {
                    println("NIF: $nif")
                    println("Nombre: ${cliente.nombre}")
                    println("Direccion: ${cliente.direccion}")
                    println("Telefono: ${cliente.telefono}")
                    println("Correo: ${cliente.correo}")
                    println("Preferente: ${cliente.preferente}")
                }
            }

            "4" -> {
                if (clientes.isEmpty()) {
                    println("No hay clientes registrados.")
                } else {
                    println("Listado de clientes:")
                    for ((nif, cliente) in clientes) {
                        println("$nif - ${cliente.nombre}")
                    }
                }
            }

            "5" -> {
                val preferentes = clientes.filterValues { it.preferente }
                if (preferentes.isEmpty()) {
                    println("No hay clientes preferentes.")
                } else {
                    println("Clientes preferentes:")
                    for ((nif, cliente) in preferentes) {
                        println("$nif - ${cliente.nombre}")
                    }
                }
            }

            "6" -> {
                println("Programa finalizado.")
                return
            }

            else -> println("Opcion no valida.")
        }
    }
}

