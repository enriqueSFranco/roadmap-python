from typing import List
from copy import deepcopy # copia profunda

colors = [
  "red",
  "orange",
  "yellow",
  "green",
  "blue",
  "indigo",
  "violet"
]
# imprime la lista
print(colors)

# recupera el 1er elemento
red = colors[0]
print(red)

"""
  LIST
  - Son tipos de datos mutables implica que las listas son hashable
  - Pueden contener diferentes tipos de datos como son << int, strings, booleans, dictionary, tuples and lists >>
  - Almacenan datos homogéneos.
  
"""
userInfo = [42, "apple", True, {"name": "John Doe"}, (1, 2, 3), [3.14, 2.78]]

print(userInfo[3]) # {"name": "John Doe"}


"""
  Construyendo Listas en Python
  1.- Creando listas a través de literales
  2.- Creando listas con el constructor list()
  3.- Creando una list comprehension
"""

"""
Creando listas a través de literales
"""
cities = [
  "New York",
  "Los Angeles",
  "Chicago",
  "Houston",
  "Philadelphia"
]

matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

inventory = [
  {"product": "phone", "price": 30000, "quantity": 100},
  {"product": "laptop", "price": 37800, "quantity": 30},
  {"product": "PlayStation 5", "price": 16000, "quantity": 10},
]

functions = [print, len, range, type, enumerate]

list_empty = []

"""
Usando el Constructor list()
"""

numbers = list((0,1,2,3,4,5,6,7,8,9))

figures = list({"circle", "square", "triangle"})

user_data = list({"name": "kike", "age": 20, "city": "Mexico City"})

pythonista = list("pythonista")

"""
  Usando el constructor del objeto list()
  Ejercicio: Crear una función que genere los digitos de la serie de fibonacci dado un limite
  firma: fibonacci_generator(stop: int)
"""
def fibonacci_generator(stop: int) -> None:
  current_fib, next_fib = 0, 1
  
  for _ in range(0, stop):
    fib_num = current_fib
    current_fib, next_fib = next_fib, current_fib + next_fib
    yield fib_num
    
fibonacci = list(fibonacci_generator(10))
print(list(fibonacci))
#print([*fibonacci_generator(10)])

"""
  Construyendo listas con comprensiones de listas
  sintaxis: [expression(item) for item in iterable]
"""

digits_squared = [number ** 2 for number in range(1, 11)]
print(digits_squared)

"""
  Acceso a elementos en una lista: indexación
"""

languages = ["pyhton", "java", "c++", "javascript", "dart", "kotlin", "swift"]
language_python = languages[0] # recupera el string python
first_language = languages[-6] # recupera el string python 
language_kotlin = languages[5] # recupera el string kotlin
last_language = languages[-1] # recupera el string swift
language_swift = languages[6] # recupera el string swift

employees = [
  {"name": "jhon", "age": 22, "job": "Software Engineer"},
  {"name": "Alice", "age": 24, "job": "Web Developer"},
  {"name": "Bob", "age": 32, "job": "Data Analyst"},
  {"name": "Mark", "age": 22, "job": "Intern"},
  {"name": "Samantha", "age": 36, "job": "Project Manager"}
]

print(employees[0]["job"])

"""
  Recuperar Múltiples Artículos de una Lista: Slice
  sitaxis: list_object[start:stop:step]
  
  - start: Especifica el índice en el que desea iniciar el corte. El segmento resultante incluye el elemento en este índice. (valor predeterminado 0)
  - stop: Especifica el índice en el que desea que el corte deje de extraer elementos. El segmento resultante no incluye el elemento en este índice. (valor predeterminado len(list_object))
  - step: Proporciona un valor entero que representa cuántos elementos omitirá el corte en cada paso. (valor predeterminado 1)
"""

letters = ["A", "a", "B", "b", "C", "c", "D", "d"]
print("letters {}".format(letters))
upper_letters = letters[0::2] # or letters[::2]
print("upper letters {}".format(upper_letters))

lower_letters = letters[1::2] # comienza en el indice 1, recorreco toda la lista y va de 2 en 2
print("lower letters {}".format(lower_letters))

last_three_letters = letters[-3::]
print("last three {}".format(last_three_letters))


"""
  Creación de Copias de una Lista
  
  1.- Copia superficial
  2.- Copia profunda
"""

# copia superficial con el método copy
countries = ["United States", "Canada", "Poland", "Germany", "Austria"]
nations = countries.copy() # or nations = copy(countries) -> from copy import copy

id(nations) == id(countries) # identidad diferente

# copia profunda
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix_copy = deepcopy(matrix)

id(matrix) == id(matrix_copy) # identidad diferente

"""
  Actualizando elementos de la lista
"""

digits = [1,2,3,4]
digits_copy = digits.copy()
digits[0] = "one"
digits[1] = "two"
digits[2] = "three"

print(digits)

# si conocemos el valor de un item pero no su index
digits[digits.index(4)] = "four"
print(digits)

digits[::] = digits_copy
print(digits)

digits[1:1] = [100, 200, 300] # agreandamos la lista [1, 100, 200, 300,, 2, 3, 4]
print(digits)

digits[1:4] = [] # acortamos la lista [1,2,3,4]
print(digits)

digits.extend([5,6,7,8,9])
print(digits)

digits.insert(0, 0)
digits.insert(len(digits), 10) # digits[len(digits):] = [10]
print(digits)

# eliminando elementos de la lista
to_visit = [
  "https://realpython.com",
  "https://python.org",
  "https://stackoverflow.com",
]

visited_stackoverflow = to_visit.pop() # elimina el ultimo elemento de la lista
visited_realpython = to_visit.pop(0) # elimina el primer elemento de la lista otra forma seria to_visit.pop(-3)
print(list([visited_stackoverflow, visited_realpython]))

cache = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
cache_copy = cache.copy() # creando copia superficial

cache.clear() # otra forma seria cache[:]
print("cache {}".format(cache))

"""
  Concatenar listas
"""

super_heroes_dc = ["batman", "super man"]
super_heroes_marvel = ["iron man", "captain america"]
super_heroes_marvel_vs_dc = super_heroes_marvel + super_heroes_dc
print("marvel vs dc {}".format(super_heroes_marvel_vs_dc))

"""
  Repetir contenido
"""

horoscopos = ["aries", "tauro", "geminis"] * 2
print(horoscopos)


# ordenando una lista con sorted
sorted_cache_copy = sorted(cache_copy, reverse=True) # sorted no afecta a la lista original
print("sorted cache {}".format(sorted_cache_copy))

"""
  Recorrer una lista
"""
usernames = ["kirito", "naruto", "goku"]

print("\niterando lista")
for username in usernames:
  print(username)
  
# iterando de forma inversa
print("\niterando lista con la funcion reversed()")
for username in reversed(usernames):
  print(username)

print("\niterando lista con la funcion enumerate()")
for i, username in enumerate(usernames):
  print("{} is the index of {}".format(i, username))
  
# iterar varias listas en paralelo
print("\niterando varias listas con la funcion zip()")
integers = [1,2,3,4,5]
letters = ["a", "b", "c", "d", "e"]
floats = [10.0, 11,0, 12.0, 13.0, 14.0, 15.0]
for i, l, f in zip(integers, letters, floats):
  print(i, l, f)

def remove_odds(list:List[int]) -> List[int]:
  for num in list[:]:
    if num % 2:
      list.remove(num)
  return list

print(remove_odds([1,2,3,4,5,6,7,8,9,10]))

"""
  Construyendo Nuevas Listas Con Comprensiones
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
