from typing import List
import random

"""
  Construyendo Nuevas Listas Con Comprensiones
  sintaxis: new_list = [expression for member in iterable]
  Cada comprensión de lista en Python incluye tres elementos:

  1.- Expression es el propio miembro, una llamada a un método, o cualquier otra expresión válida que devuelva un valor. 
  2.- Member es el objeto o valor en la lista o iterable. En el ejemplo anterior, el valor del miembro es i.
  3.- Iterable es una lista, conjunto, secuencia, generador, o cualquier otro objeto que pueda devolver sus elementos uno a la vez. 
"""
numbers = ["1", "2", "3", "4"]
numbers = [int(num) for num in numbers]

"""
Genera una lista con los primeros 15 números pares usando comprensiones de lista.
"""
pares = [num for num in range(2, 11, 2)]
print(pares)

"""
Dada una lista de palabras, crea una nueva lista que contenga 
solo aquellas palabras que tengan más de tres letras.
"""
words = ["python", "java", "ruby", "c", "javascript"]
words = [word for word in words[:] if len(word) > 3]
print(words)

"""
Genera una lista con los primeros 20 números que son divisibles por 3 y 5.
"""
divisibles = [num for num in range(1,101) if num % 3 == 0 and num % 5 == 0] # [15, 30, 45, 60, 75, 90]
print(divisibles)

"""
Dada una lista de temperaturas en grados Celsius, convierte cada temperatura 
a Fahrenheit utilizando la fórmula (C * 9/5) + 32.
"""
temperaturas_celsius = [20, 25, 30, 35, 40]

temperaturas_fahrenheit = [(temp * 9 /5) + 32 for temp in temperaturas_celsius[:]]


"""
  Dada una lista de palabras, crea una nueva lista que contenga esas palabras en mayúsculas.
"""
palabras = ['hola', 'python', 'mundo', 'programacion']
mayusculas = [word.upper() for word in palabras[:]]

"""
Dada una lista de palabras, crea una lista que contenga la longitud de cada palabra.
"""
palabras = ['gato', 'perro', 'elefante', 'jirafa']
sizes = [len(word) for word in palabras[:]]

"""
Genera una lista con los primeros 15 números primos.
"""
def es_primo(num: int) -> bool:  
  return num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))

def is_prime_number(n) -> bool:
  count = 1
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      count += 1
    if count > 1: return False
  return count == 1

prime_list = [n for n in range(1, 100) if es_primo(n)][:15]
print(prime_list)

usernames = ["jhon smith", "cid", "shadow", "jack"]
print("cid" in usernames)

unique_items = list(set([1,2,1,2,3,4,5,5])) # opcion 1

def get_unique_items(list_object) -> List[int]: # opcion 2
  # [1,2,1,2,3,4,5,5]
  unique_items = []
  for item in list_object:
    if item not in unique_items:
      unique_items.append(item)
  return unique_items

matrix = [[0, 1, 2], [10, 11, 12], [20, 21, 22]]
def flat_list(list_object) -> List[int]:
  flattened_list = []
  for row in list_object:
    flattened_list.extend(row)
  
  return flattened_list

input = [1,2,3,4,5,6,7,8,9]
def split_list(list_object, chunk_size) -> List[int]:
  chunks = []
  for start in range(0, len(list_object), chunk_size):
    stop = start + chunk_size
    chunks.append(list_object[start:stop])
    
  return chunks

print(split_list(input, 4))

txns = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08

def get_price_with_tax(txn: float):
  return txn * (1 + TAX_RATE)

final_price = [get_price_with_tax(txn) for txn in txns]
print(final_price)


"""
  Usando logica condicional en list comprehension
  new_list = [expression for member in iterable (if conditional)]
"""
sentence = 'the rocket came back from mars'
vowels = [vowel for vowel in sentence if vowel in "aeiou"]
print(vowels)

def is_consonant(letter: str) -> list[str] :
  vowels = {'a', 'e', 'i', 'o', 'u'}
  return letter.isalpha() and letter.lower() not in vowels

consonants = [letter for letter in sentence if is_consonant(letter)]
print(consonants)

"""
  Usando Comprensiones de Conjunto y Diccionario
"""
quote = "life, uh, finds a way"
unique_vowels = {vowel for vowel in quote if vowel in "aeiou"}
print(unique_vowels)


"""
  Usando el Operador de Morsa
"""
def get_weather_data():
  return random.randrange(90, 150)
# recuperar las temperaturas >= 100
hot_temps = [temp for _ in range(20) if (temp := get_weather_data()) >= 100]
print(hot_temps)

"""
  Debe usar listas cuando necesite:
  - Mantenga sus datos ordenados: Las listas mantienen el orden de inserción de sus elementos.
  - Almacene una secuencia de valores: Las listas son una gran opción cuando necesita almacenar una secuencia de valores relacionados.
  - Muta tus datos: Las listas son tipos de datos mutables que admiten múltiples mutaciones.
  - Acceda a valores aleatorios por índice: Las listas permiten un acceso rápido y fácil a los elementos en función de su índice.
  
  
  Evite usar listas cuando necesite:
  - Almacenar datos inmutables: En este caso, debe usar una tupla. Son inmutables y más eficientes en memoria.
  - Representar registros de bases de datos: En este caso, considere usar una tupla o una clase de datos.
  - Almacene valores únicos y desordenados: En este escenario, considere usar un conjunto o diccionario. Los conjuntos no permiten valores duplicados, y los diccionarios pueden contener claves duplicadas.
  - Ejecute muchas pruebas de membresía donde el artículo no importa: En este caso, considere usar un set. Los conjuntos están optimizados para este tipo de operación.
  - Ejecute operaciones avanzadas de matriz y matriz: En estas situaciones, considere usar NumPyamis estructuras de datos especializadas.
  - Manipular sus datos como una pila o cola: En esos casos, considere usar deque de la collections módulo o Queue, LifoQueue, o PriorityQueue. Estos tipos de datos son seguros para roscas y están optimizados para una rápida inserción y eliminación en ambos extremos.
"""