import unittest
from typing import List

"""
	--------- Crear unittest ---------
	1.- Importar unittest de la biblioteca estándar
	2.- Crea una clase llamada TestSum eso hereda de la clase TestCase
	3.- Convierta las funciones de prueba en métodos agregando self como primer argumento
	4.- Cambia las afirmaciones para usar el método self.assertEqual() en la clase TestCase
	5.- Cambie el punto de entrada de la línea de comandos para llamar unittest.main()
"""


"""
    Given an array of integers nums and an integer target, return indices of the two numbers 
    such that they add up to target.
    You may assume that each input would have exactly one solution, and you may 
    not use the same element twice.
    You can return the answer in any order.

    Example 1:

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    Example 2:

    Input: nums = [3,2,4], target = 6
    Output: [1,2]
    Example 3:

    Input: nums = [3,3], target = 6
    Output: [0,1]
"""


def twoSum(nums: List[int], target: int) -> List[int]:
    num_map = {}  # {num:index}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]

        num_map[num] = i


def sumar(a, b):
    return a + b


def sumar_todos(*args):
    total_sum = 0
    for value in args:
        total_sum += value
    return total_sum


class TestSum(unittest.TestCase):
    """
    Mejorando los test con fixtures
    """

    def setUp(self):
        # Este código se ejecuta antes de cada prueba
        self.valor = 2
        self.valor = 3

    def tearDown(self):
        # Este código se ejecuta después de cada prueba
        pass

    def test_sumar_positivos(self):
        self.assertEqual(sumar(10, 5), 15, "should be 15")

    def test_sumar_negativos(self):
        self.asserEqual(sumar(-5, -2), -8, "should be -8")

    def test_sumar_cont_cero(self):
        self.assertEqual(sumar(10, 0), 10, "should be 10")

    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        integers = [4, 10, 20, 5, 8]
        result = sumar_todos(integers)
        self.assertEqual(result, 47)

    def test_bad_type(self):
        input = "hello"
        with self.assertRaises(TypeError):
            result = sumar_todos(input)


"""
	--------- Cómo Estructurar una Prueba Simple ---------
	
	1.- Primero hay que tomar un par de decisiones:
		- ¿Qué quieres probar?
		- ¿Estás escribiendo una prueba unitaria o una prueba de integración?
	
	2.- Entonces la estructura de una prueba debe seguir libremente este flujo de trabajo:
		- Crea tus entradas
		- Ejecute el código que se está probando, capturando la salida
		- Compare la salida con un resultado esperado
	
	Para esta aplicación, hay muchos comportamientos que podríamos verificar, como:
		- ¿Puede sumar una lista de números enteros (enteros)?
		- ¿Puede sumar una tupla o un conjunto?
		- ¿Puede sumar una lista de flotadores?
		- ¿Qué sucede cuando le proporciona un valor incorrecto, como un solo número entero o una cadena?
		- ¿Qué sucede cuando uno de los valores es negativo?
"""

# esto ayuda a ejecutar las pruebas que hemos creado
if __name__ == "__main__":
    unittest.main()

# EJECUTANDO PRUEBAS
# 1.- python -m unittest test: ejecuta todas las pruebas que tenga el modulo test
# 2.- python -m unittest -v test:
# Cuando usas -v, le estás diciendo a Python que te dé más detalles de las pruebas cuando las ejecute.
# Es decir, en lugar de mostrarte solo si pasaron o no, te mostrará más información, como qué prueba
# se ejecutó, si pasó o falló, y por qué.

# 3.- python -m unittest discover: Esto buscará en el directorio actual cualquier archivo nombrado test*.py
# 4.- ctrl + shift + p > python test > debug all unit test
