"""
Los decoradores en Python son una forma de modificar o extender el comportamiento de funciones o métodos 
sin cambiar su código directamente. Puedes pensar en ellos como "envoltorios" que se colocan alrededor de una 
función para hacer algo extra, antes o después de que se ejecute la función original.




"""

import datetime
import functools
import time


def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper()


# Usando azucar sintactico para usar el decorador
# @decorator
# def say_whee():
#    print("whee!")

# Usando el decorador
# say_whee = decorator(say_whee) # se le pasa la referencia de la funcion say_whee a la funcion decorator y 'say_whee' ahora apunta al wrapper


# Reutilizando decoradores
def do_twice(func):
    @functools.wraps(func)  # finding yourself
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice


@do_twice
def say_whee():
    print("whee!")


@do_twice
def greet(name: str) -> str:
    print("creating greeting")
    return f"hello {name}"


hi_kirito = greet("kirito")
print(hi_kirito)

# Ejemplos del mundo real


# plantilla para contruir decoradores complejos
# archivo en decorators.py
def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # do something before
        value = func(*args, **kwargs)
        # do something after
        return value

    return wrapper_decorator


"""
Funciones de tiempo
Medirá el tiempo que tarda una función en ejecutarse y luego imprimirá la duración en la consola
"""


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        # do something before
        start_time = time.perf_counter()  # medicion de intervalos

        value = func(*args, **kwargs)

        # do something after
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__}() in {run_time:.4f}secs")
        return value

    return wrapper_timer


@timer
def was_some_time(num_times):
    for _ in range(num_times):
        sum([number**2 for number in range(10_000)])


was_some_time(1)

was_some_time(999)

"""
El siguiente decorador @debug imprimirá los argumentos de una función y su valor de retorno cada vez que llame a la función
"""


def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(args) for a in args]
        kwars_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwars_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__}() returned {repr(value)}")
        return value

    return wrapper_debug


@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you're growing up!"
