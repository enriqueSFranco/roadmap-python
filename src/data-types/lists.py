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

list((0,1,2,3,4,5,6,7,8,9))

list({"circle", "square", "triangle"})

list({"name": "kike", "age": 20, "city": "Mexico City"})

list("pythonista")

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