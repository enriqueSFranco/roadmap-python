from random import randint
from timeit import repeat
from typing import List

ARRAY_LENGTH = 10000
# def bubble_sort(data: List[int]):
#    n = len(data)

#    for i in range(n):
#        for j in range(n - i - 1):
#            if data[j + 1] > data[i]:
#                data[j], data[j + 1] = data[j + 1], data[j]

#    return data

"""
    Mejora 1: Optimización con bandera
    Una de las mejoras más comunes al algoritmo de burbuja es la optimización con una bandera. La idea es que si en una pasada no se realizan intercambios, esto significa que la lista ya está ordenada, y por lo tanto, no es necesario hacer más pasadas. Esto evita comparaciones innecesarias una vez que el arreglo ya está ordenado.

    Cómo funciona:

    En cada pasada, después de comparar y, si es necesario, intercambiar los elementos adyacentes, se pone una bandera (un valor booleano, por ejemplo) que indica si hubo algún intercambio en esa pasada.
    Si no hubo intercambios en una pasada completa, significa que la lista ya está ordenada, por lo que se detiene el algoritmo.
    Esto reduce las comparaciones en algunos casos, especialmente si el arreglo ya está casi ordenado. La complejidad en el mejor de los casos se reduce a O(n) si el arreglo ya está ordenado.

    Bandera de intercambio: Si no se hacen intercambios en una pasada, el arreglo ya está ordenado, por lo que se detiene.
"""


def bubble_sort(data: List[int]):
    n = len(data)
    alredy_sorted = True

    for i in range(n):
        alredy_sorted = True
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                alredy_sorted = False

        if alredy_sorted:
            break
    return data


"""
    Mejora 2: Optimización con el límite del último intercambio
    Otra mejora común es recordar la última posición donde se hizo un intercambio. Esto es útil porque después de esa posición, los elementos ya están correctamente ordenados. Así que en cada pasada, podemos reducir el rango de comparación.

    Cómo funciona:

    Cada vez que se hace un intercambio, guardamos la posición del último intercambio realizado.
    En la siguiente pasada, solo se comparan los elementos hasta la última posición donde se hizo un intercambio, ya que después de esa posición los elementos ya están ordenados.
    Esto también ayuda a reducir el número de comparaciones y mejora el rendimiento en algunos casos, aunque no cambia la complejidad temporal en el peor de los casos.

    Límite del último intercambio: Después de cada pasada, se reduce el rango de elementos a comparar porque los últimos elementos ya están ordenados.
"""


def run_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from __main__ import {algorithm}" if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


if __name__ == "main":
    data = [randint(0, 1000) for _ in range(ARRAY_LENGTH)]
