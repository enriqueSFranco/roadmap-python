# Crear un conjunto
frutas = {"manzana", "pera", "sandia", "durazno"}
print(frutas)

numeros = set([1,2,3,4])
print(numeros)

# Operaciones entre conjuntos
conjuntoA = {1,2,3}
conjuntoB = {3,4,5}

union = conjuntoA | conjuntoB
print(union) # {1,2,3,4,5}

interseccion = conjuntoA & conjuntoB
print(interseccion) # {3}

diferencia = conjuntoA - conjuntoB
print(diferencia) # {1,2}

diferencia_simetrica = conjuntoA ^ conjuntoB
print(diferencia_simetrica) # {1,2,4,5}

# Metodos de conjuntos
frutas.add("uva") # {"manzana", "pera", "sandia", "durazno", "uva"}
print(frutas)

frutas.remove("pera") # {"manzana", "sandia", "durazno", "uva"}
print(frutas)

frutas.discard("manzana") # {"sandia", "durazno", "uva"}
print(frutas)

frutas.clear()
print(frutas)