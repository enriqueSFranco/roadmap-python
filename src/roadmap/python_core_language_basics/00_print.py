import json
from pprint import pprint as pp

data = {"powers": [x**10 for x in range(10)]}
pp(data)  # pprint llama al metodo __repr__ en lugar de __srt__

# pprint()ordena automáticamente las teclas del diccionario antes de imprimir, lo que permite una comparación consistente.
cities = {"USA": {"Texas": {"Dallas": ["Irving"]}}}
pp(cities, depth=3)

"""
Nota: Los conjuntos de datos recursivos o muy grandes se pueden tratar usando el reprlib módulo también

import reprlib

reprlib.repr([x**10 for x in range(10)])
>>> '[0, 1, 1024, 59049, 1048576, 9765625, ...]'
"""

data = {"username": "jdoe", "password": "s3cret"}
ugly = json.dumps(data)  # serializa un string a json
# >>> {"username": "jdoe", "password": "s3cret"}
pretty = json.dumps(data, indent=4, sort_keys=True)
# >>> {"password": "s3cret","username": "jdoe"}

# ------------- variables --------------

# esta declaración realmente no crea una nueva variable
name: int
colors: dict[str, tuple[int, int, int]] = {
    "Red": (255, 0, 0),
    "Green": (0, 255, 0),
    "Blue": (0, 0, 255),
    "Yellow": (255, 255, 0),
    "Black": (0, 0, 0),
    "White": (255, 255, 255),
}
fruits: list[str] = []
rows: list[tuple[str, int, str]] = []

# asignacion paralela
is_authenticated = is_active = is_admin = False
print(is_authenticated, is_active, is_admin)

# tuple unpacking
person = ("Jane", 25, "Python Dev")
name = person[0]
age = person[1]
job = person[2]
print(name, age, job)

name2, age2, job2 = person

# swapa
a = 1
b = 2
a, b = b, a

# expresion de asignacion
line = input("type some text:")
while line != "stop":
    print(line)
    line = input("type some text:")

while line := input("type some text:") != "stop":  # usando una expresión de asignación
    print(line)

"""
Alcance de las variables

En Python, hay cuatro ámbitos diferentes, que se pueden presentar utilizando el acrónimo LEGB. 
Las letras en este acrónimo representan local, enclosing, global, and built-in scopes.
"""

# Global scope
global_variable = "global"


def outer_func():
    # Nonlocal scope
    nonlocal_variable = "nonlocal"

    def inner_func():
        # Local scope
        local_variable = "local"
        print(f"Hi from the '{local_variable}' scope!")
        print(f"Hi from the '{nonlocal_variable}' scope!")
        print(f"Hi from the '{global_variable}' scope!")

    inner_func()
