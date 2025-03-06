from typing import Dict, List


# Funciones con numero variable de argumentos
def suma_variable(*numeros):
    total = 0
    for num in numeros:
        total += num
    return total


print(suma_variable(1, 2, 3, 4, 5))
print(suma_variable(4, 7, 8, 10))


def f(qty: int, item: str, price: float) -> None:
    print(f"{qty} {item} cost ${price:.2f}")


"""Argumentos con palabras clave"""
f(qty=6, item="bananas", price=30.0)
"""Argumentos posicionales"""
f(price=30.0, qty=6, item="bananas")

"""Parametros pedeterminados"""


def g(qty=6, item="bananas", price=30.0) -> None:
    print(f"{qty} {item} cost ${price:.2f}")


g()
g(10)
g(item="apples")
g(price=50.35)

"""Parametros por valor y referencia"""
x = 5


def h(x):
    print("value x=", x)
    x = 10
    print("new value x=", x)


def b(x):
    x = "foo"
    print("x: ", x)


"""
1.- 4 (un número entero - inmutable):
El valor de x dentro de la función b(x) se asigna a "foo", pero el valor de i fuera de la función no se modifica porque los enteros son inmutables.
Salida de la función: x: foo

2.-dict(a=10, b=100) (un diccionario - mutable):
Se pasa la referencia del diccionario a la función b(x). Sin embargo, dentro de la función b, x se asigna a "foo". Esto no afecta al diccionario original, ya que estás creando una nueva asignación para x dentro de la función, no modificando el diccionario que fue pasado.
Salida de la función: x: foo

3.-{"name": "solo leveling", "status": "finalizado", "year": 2024} (otro diccionario - mutable):
Lo mismo que el caso anterior: el diccionario es mutable, pero dentro de la función x se le asigna el valor "foo", por lo que no se modifica el diccionario original fuera de la función.
Salida de la función: x: foo

4.-'bar' (una cadena - inmutable):
Las cadenas son objetos inmutables, por lo que al asignar "foo" a x dentro de la función, no cambia la cadena original 'bar' que se pasó como argumento.
Salida de la función: x: foo

5.- [200, 300, 400] (una lista - mutable):
Las listas son mutables, pero dentro de la función, x se asigna a "foo". Esto hace que la referencia a la lista original se pierda dentro de la función, y x apunte ahora a 

6.-"foo". La lista original no se modifica, ya que lo que realmente ocurrió fue que x fue reasignada a un nuevo valor.
Salida de la función: x: foo
"""
for i in (
    4,
    dict(a=10, b=100),
    {"name": "solo leveling", "status": "finalizado", "year": 2024},
    "bar",
    [200, 300, 400],
):
    b(i)

"""Argumento Tuple Packing"""


def c(*args):
    print(args)
    print(type(args), len(args))
    for i in args:
        print(i)


c(1, 2, 3)
c("foo", "bar", "baz", "qux", "quux")

l = ["foo", "bar", "baz", "qux"]
c(*l)

"""
dictionary packing

¿Qué hace **kwargs?
El **kwargs permite que una función reciba una cantidad variable de argumentos con nombre (es decir, clave-valor). Al usarse, Python empaqueta todos los argumentos adicionales en un diccionario.
"""


def register_employee(**kwargs):
    print(kwargs)


register_employee(name="Juan", age=20, position="Developer")


def register_task(**kwargs):
    print("tarea registrada:")
    for key, value in kwargs.items():
        print(f"{key}:{value}")


task = {
    "nombre": "Desarrollar API",
    "responsable": "Juan",
    "fecha_limite": "2025-03-01",
    "prioridad": "Alta",
}
register_task(
    **dict(
        nombre="Desarrollar API",
        responsable="Juan",
        fecha_limite="2025-03-01",
        prioridad="Alta",
    )
)
register_task(**task)


def insertar_registro(**kwargs):
    # Simulación de inserción en base de datos
    print("Insertando registro en base de datos:")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")


# Llamada con diferentes campos para un registro de empleado
insertar_registro(
    nombre="Ana", puesto="Gerente", salario=50000, fecha_ingreso="2024-01-15"
)


def j(*args):
    for i in args:
        print(i)


l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9]
l3 = [10, 11]

j(*l1, *l2, *l3)


def k(**kwargs):
    for k, v in kwargs.items():
        print(k, "->", v)


d1 = {"a": 1, "b": 2}
d2 = {"x": 3, "y": 4}

k(**d1, **d2)

"""
keyword arguments
En Python, el asterisco (*) dentro de la firma de una función tiene un propósito especial: obliga a que todos los argumentos a partir de ese punto se pasen como argumentos nombrados (keyword arguments).
"""


def oper(x, y, *, op="+"):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    else:
        return x / y


oper(10, 2, op="*")  # ✅
# oper(5, 3, '-') ❌

"""
Anotacion de una funcion: característica que permite añadir metadatos a las funciones.
"""


def process_data(data: List[int], mappings: Dict[str, int]) -> int:
    return sum(data) + sum(mappings.values())


process_data.__annotations__


# Funciones internas
def parent():
    print("Printing from parent()")

    def first_child():
        print("Printing from first_child()")

    def second_child():
        print("Printing from second_child()")

    # El orden en que se definen las funciones internas no importa
    first_child()
    second_child()


# Funciones como valores de devolucion
def parent2(num):
    def first_child():
        return "Hi, I'm Kirito"

    def second_child():
        return "Call me Ester"

    if num == 1:
        return first_child  # devolviendo la referencia de la funcion 'first_child'
    else:
        return second_child


first = parent2(1)
second = parent2(2)
first()
second()
