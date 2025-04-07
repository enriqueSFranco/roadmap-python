# constante privada
_PI = 3.14


# funcion de uso interno
def _validate(value):
    if not isinstance(value, int | float) or value <= 0:
        raise ValueError("positive number expected")
    return value


class Circle:
    def __init__(self, radius):
        self._radius = _validate(radius)

    def calculate_area(self):
        return round(_PI * self._radius**2, 2)


circle = Circle(4)
circle._radius = 8

""" 
Nota: Aunque se puede acceder al atributo ._radius no es buena practica hacerlo,
ya que se esta indicando que es un atributo privado. Recordemos que el subrayado
es solo una convención de nombres. 
Python no restringe el acceso a este tipo de atributos.
Como desarrollador de Python, debemos respetar la convención y no acceder a atributos no públicos 
desde el exterior.
"""


class Square:
    def __init__(self, side):
        self.side = _validate(side)


"""
    Name Mangling
    El uso del doble guion bajo (__) delante de los métodos y atributos 
    en Python sirve principalmente para manglear el nombre del atributo o método, 
    lo cual tiene dos propósitos principales
"""


class SampleClass:
    def __init__(self, attribute):
        self.__attribute = attribute

    def __method(self):
        print(self.__attribute)


class_instance = SampleClass("Hello")
print(class_instance.__attribute)  # AttributeError
class_instance.__method()
# Si accedemos al atributo de la clase nos dara un AttributeError
# esto es porque estamos usando el guion doble __ y Python nombra a la clase de esta forma _SampleClass
"""
    Aunque Python permite el acceso a los atributos "privados" mediante el nombre mangling 
    (_SampleClass__attribute), no es recomendable hacerlo, ya que va en contra de la convención 
    de ocultar detalles internos de la clase. En su lugar, es mejor usar métodos públicos para 
    acceder a esos elementos si realmente es necesario.
"""
print(class_instance._SampleClass__attribute)
class_instance._SampleClass__method()
