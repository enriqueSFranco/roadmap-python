# diccionarios

import timeit
from operator import itemgetter

"""
  Las claves pueden ser de cualquier tipo inmutable, como cadenas, números y tuplas. 
  Los valores pueden ser de cualquier tipo de datos, incluidos números, cadenas, listas, tuplas y hasta otros diccionarios.
"""
super_hero = {
    "name": "spider-man",
    "age": 15,
    "power": "Super strength",
    "secret-identity": "peter parker",
}
print(super_hero)

student = {"name": "kike", "age": 18, "notes": [10, 9, 8]}
print(student)

countries = {"Mexico": "CDMX", "Argentina": "Buenos Aires", "Colombia": "Bogotá"}
print(countries)

"""
  Modificar un Diccionario en Python
"""
scort_karely = {"name": "vendedora de caricias", "price": 1500}
print(scort_karely)
scort_karely["price"] = 300000
print(scort_karely)


"""
No se permiten duplicados en los diccionarios
Cada clave en un diccionario debe ser única. No se permite tener dos elementos con la misma clave en un diccionario. 
Sin embargo, los valores pueden ser duplicados.
"""
colors = {
    "rojo": "#FF0000",
    "verde": "#00FF00",
    "rojo": "#FF3333",  # La clave "rojo" ya existe, se reemplazará
}
print(colors)

"""Longitud del diccionario en Python"""
team = {"player_one": "alice", "player_two": "bob", "player_three": "carol"}

total_players = len(team)
print("Total de judadores: {}".format(total_players))

"""Elementos del diccionario - Tipos de datos"""
movie = {
    "title": "Avengers End Game",
    "year": "2019",
    "gender": ["science fiction", "action"],
    "actors": [
        "Robert Downey Jr",
        "Chris Evans",
        "Mark Ruffalo",
        "Chris Hemsworth",
        "Scarlett Johansson",
    ],
}

print(movie)
if type(movie) == dict:
    print("Los datos provienen de un diccionario")

# crear un diccionario con fromkeys
inventory = dict.fromkeys(["manzana", "platano", "sandia", "melon"], 0)
# crear un diccionario con compresion de diccionarios
squares = {integer: integer**2 for integer in range(1, 11)}

"""Funciones integradas en los dict: all, max, min, len, sort, sum"""
all(inventory.values())
inventory["pera"] = 0
all(inventory.values())

sum(inventory.values())

computer_parts = {
    "CPU": 299.99,
    "Motherboard": 149.99,
    "RAM": 89.99,
    "GPU": 499.99,
    "SSD": 129.99,
    "Power Supply": 79.99,
    "Case": 99.99,
    "Cooling System": 59.99,
}
min(computer_parts.values())
max(computer_parts.values())

students = {
    "Alice": 89.5,
    "Bob": 76.0,
    "Charlie": 92.3,
    "Diana": 84.7,
    "Ethan": 88.9,
    "Fiona": 95.6,
    "George": 73.4,
    "Hannah": 81.2,
}
# sorted devuelve una lista ordenada
sorted(students)
sorted(students.values())
dict(sorted(students.items(), key=lambda item: item[1]))
dict(sorted(students.items(), key=lambda item: item[1], reverse=True))

"""Recuperar elementos"""
manzana = inventory.get("manzana")
# si no existe devolvera None
pera = inventory.get("pera")
uva = inventory.get("uva", "No se encontro la key")

"""Recuperar todos los valores de las keys"""
inventory.values()
"""Recuperar todas las keys"""
inventory.keys()
"""Tuplas de clave-valor"""
inventory.items()
"""Verificar si una clave existe y sino entonces poner un valor por defecto"""
inventory.setdefault("manzana")
inventory.setdefault("mango", 0)

"""Usando setdefault"""
manhwas = {}
for category, name in [
    ("sistema", "solo leveling"),
    ("reencarnacion", "la vida despues del fin"),
    ("romance", "lagrimas en las flores marchitas"),
    ("sistema", "lector omniciente"),
]:
    manhwas.setdefault(category, []).append(name)

for category, name in [
    ("sistema", "solo leveling"),
    ("reencarnacion", "la vida despues del fin"),
    ("romance", "lagrimas en las flores marchitas"),
    ("sistema", "lector omniciente"),
]:
    if category not in manhwas:
        manhwas[category] = []
        manhwas[category].append(name)

"""Usando update"""
config = {"color": "green", "width": 42, "height": 100, "font": "Courier"}
user_config = {"path": "/home", "color": "red", "font": "Arial", "position": (200, 100)}
config.update(user_config)
# si la key no existe entonces la agrega junto con su valor
config.update([("width", 200), ("api_key", 1234)])
config.update(color="black", script="__main__.py")

"""Eliminando claves de un dict"""
inventory.pop("manzana")
inventory.pop("fresa")  # genera un keyerror
inventory.pop("fresa", 0)  # retorna el valor por defecto '0'

inventory.popitem()  # elimina en LIFO y lo devuelve como una tupla (key,value)

"""Saber si una key, value estan en el dict"""
MLB_teams = {
    "Colorado": "Rockies",
    "Chicago": "White Sox",
    "Boston": "Red Sox",
    "Minnesota": "Twins",
    "Milwaukee": "Brewers",
    "Seattle": "Mariners",
}

print("Colorado" in MLB_teams)
print("Bosto" in MLB_teams)
print("Red Sox" in MLB_teams.values())
print(("Boston", "Red Sox") in MLB_teams.items())

""" operadores de desigualdad == y != """
print([1, 2, 3] == [3, 2, 1])  # depende tanto del contenido como del orden
print(
    {"a": 1, "b": 2, "c": 3} == {"c": 3, "a": 1, "b": 2}
)  # si contiene la misma serie de key-value sin importar el orden seran iguales

"""
Union
El operador (|) crea un nuevo diccionario fusionando las claves y los valores de dos diccionarios iniciales. Los valores del diccionario a la derecha del operador tienen prioridad cuando ambos diccionarios comparten claves:
"""
default_config = {"color": "green", "width": 42, "height": 100, "font": "Courier"}

new_config = default_config | user_config

"""Iterando sobre dict"""
for student in students:
    print(student)

for student in students.keys():
    print(student, "->", students[student])

"""Ordenamiento"""

data = {
    193: {"name": "John", "age": 30, "skills": {"python": 8, "js": 7}},
    209: {"name": "Bill", "age": 15, "skills": {"python": 6}},
    746: {"name": "Jane", "age": 58, "skills": {"js": 2, "python": 5}},
    109: {"name": "Jill", "age": 83, "skills": {"java": 10}},
    984: {"name": "Jack", "age": 28, "skills": {"c": 8, "assembly": 7}},
    765: {"name": "Penelope", "age": 76, "skills": {"python": 8, "go": 5}},
    598: {"name": "Sylvia", "age": 62, "skills": {"bash": 8, "java": 7}},
    483: {"name": "Anna", "age": 24, "skills": {"js": 10}},
    277: {"name": "Beatriz", "age": 26, "skills": {"python": 2, "js": 4}},
}

sorted_people = sorted(
    data.items(),
    key=lambda item: (
        item[1]["skills"].get("python", 0) + item[1]["skills"].get("js", 0)
    ),
)

print(sorted_people)
dict(sorted_people)  # Opcion 1 para crear el dict ordenado
sorted_people_dict = {}  # Opcion 2
for key, value in sorted_people:
    sorted_people_dict[key] = value

"""Usando itemgetter"""
# (id, fecha, monto)
transacciones = [
    (1001, "2025-01-15", 350.50),
    (1002, "2025-01-14", 200.75),
    (1003, "2025-01-16", 450.25),
    (1004, "2025-01-14", 300.10),
]
# ordenar por fecha y monto
transacciones_ordenadas = sorted(transacciones, key=itemgetter(1, 2))
for t in transacciones_ordenadas:
    print(f"ID: {t[0]}, Fecha: {t[1]}, Monto: {t[2]}")

"""lambda vs itemgetter"""
dict_to_order = {
    1: "requests",
    2: "pip",
    3: "jinja",
    4: "setuptools",
    5: "pandas",
    6: "numpy",
    7: "black",
    8: "pillow",
    9: "pyparsing",
    10: "boto3",
    11: "botocore",
    12: "urllib3",
    13: "s3transfer",
    14: "six",
    15: "python-dateutil",
    16: "pyyaml",
    17: "idna",
    18: "certifi",
    19: "typing-extensions",
    20: "charset-normalizer",
    21: "awscli",
    22: "wheel",
    23: "rsa",
}

sorted_with_lambda = "sorted(dict_to_order.items(), key=lambda item: item[1])"
sorted_with_itemgetter = "sorted(dict_to_order.items(), key=itemgetter(1))"

sorted_with_lambda_time = timeit(stmt=sorted_with_lambda, globals=globals())

sorted_with_itemgetter_time = timeit(
    stmt=sorted_with_itemgetter,
    setup="from operator import itemgetter",
    globals=globals(),
)

print(
    f"""\
{sorted_with_lambda_time=:.2f} seconds
{sorted_with_itemgetter_time=:.2f} seconds
itemgetter is {(
    sorted_with_lambda_time / sorted_with_itemgetter_time
):.2f} times faster"""
)
