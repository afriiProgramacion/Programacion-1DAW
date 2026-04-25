fun main() {
    val frutas1 = listOf("manzana", "pera", "naranja", "platano", "uva")
    val frutas2 = listOf("manzana", "pera", "durazno", "sandia", "uva")

    val setFrutas1 = frutas1.toSet()
    val setFrutas2 = frutas2.toSet()

    val frutasComunes = setFrutas1 intersect setFrutas2
    val frutasSoloEnFrutas1 = setFrutas1 - setFrutas2
    val frutasSoloEnFrutas2 = setFrutas2 - setFrutas1

    println("set_frutas1: $setFrutas1")
    println("set_frutas2: $setFrutas2")
    println("frutas_comunes: $frutasComunes")
    println("frutas_solo_en_frutas1: $frutasSoloEnFrutas1")
    println("frutas_solo_en_frutas2: $frutasSoloEnFrutas2")
}

