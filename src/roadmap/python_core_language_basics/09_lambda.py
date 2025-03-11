""" 
¿Qué es una función lambda?
Una función lambda en Python permite crear funciones pequeñas de manera rápida y sencilla. La sintaxis básica es:

lambda argumentos: expresión

- lambda: la palabra clave que define una función anónima.
- argumentos: los parámetros que toma la función.
- expresión: lo que la función devuelve. Aquí no puedes tener múltiples sentencias, solo una expresión.

Caracteristicas
- Sólo puede contener expresiones y no debe incluir declaraciones en su cuerpo. return, pass, assert, o raise levantará un SyntaxError 

- Está escrito como una sola línea de ejecución.
- No admite anotaciones de tipo.
- Se puede invocar inmediatamente (IIFE).
"""

def identity(x):
  return x

lambda x:x

print((lambda x: x + 1)(10)) # IIFE

# nombrando una expresion lambda
suma = lambda x, y: x + y
suma(1,2)

full_name = lambda first, last: f"Full name: {first.title()} {last.title()}"

"""funciones de orden superior"""
high_ord_func = lambda x, func: x + func(x)
high_ord_func(5, lambda x: x * x)

"""
Closure

Características principales de una closure:
- Función anidada: La closure es una función que se define dentro de otra función.
- Acceso a variables del entorno: La función interna recuerda las variables del entorno de la función exterior (aunque la función exterior haya terminado su ejecución).
- Función devuelta: La función interna es devuelta por la función exterior o es utilizada fuera de su contexto original.
"""
# def outer_func(x):
#   y = 4
#   def inner_func(z):
#     print(f"x = {x}, y = {y}, z = {z}")
#     return x + y + z
#   return inner_func

def outer_func(x):
  y = 4
  return lambda z: x + y + z

for i in range(3):
  closure = outer_func(i)
  print(f"closure({i+5}) = {closure(i+5)}")
