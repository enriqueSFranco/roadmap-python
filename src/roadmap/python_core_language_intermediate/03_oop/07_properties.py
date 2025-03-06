from time import sleep

"""
    Las propiedades son un mecanismo que te permite controlar el acceso y la manipulación de los atributos 
    de una clase de una manera más controlada y eficiente.

    En Python, property() es una función que te permite definir propiedades para un atributo de una clase
    Es como una forma especial de controlar el acceso (lectura y escritura) a un atributo sin tener que usar métodos comunes, pero con la flexibilidad de ejecutar código adicional si es necesario.
    
    La función property() se utiliza para definir getters, setters y deleters de una manera más limpia, sin tener que usar métodos explícitos como get_ o set_.
    
    property([fget=None, fset=None, fdel=None, doc=None])
"""


class Car:
    def __init__(self, color):
        self.color = color

    def _set_color(self, value):
        self.color = value

    def _get_color(self):
        return self.color

    color = property(_get_color, _set_color)


# usando una funcion lambda
class Circle:
    def __init__(self, radius):
        self._radius = radius

    radius = property(lambda self: self._radius)


circle = Circle(25)
Circle.radius.fget

"""
	Usando property() como Decorador
"""


class Person:
    def __init__(self, name) -> None:
        self.__name = name

    @property
    def get_name(self):
        return self.__name


"""
    Validando datos de entrada
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        try:
            self._x = float(value)
            print("Validated!")
        except ValueError:
            raise ValueError('"x" must be a number') from None

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        try:
            self._y = float(value)
            print("Validated!")
        except ValueError:
            raise ValueError('"y" must be a number') from None


point_a = Point(3, 5)

point_a.x = 10
print(point_a.x)

point_a.y = 5
print(point_a.y)

point_a.x = "one"
point_a.y = "5"

"""
    Hay un problema en la clase Point y es que el codigo que se usa para validar la entrada se repite.
    Para evitarlo vamos a abstraer la logica repetida usando un descriptor
"""


class Coordinate:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        try:
            instance.__dict__[self.name] = float(value)
            print("Validated!")
        except ValueError:
            raise ValueError(f"{self.name} must be a number") from None


class PointTwo:
    x = Coordinate()
    y = Coordinate()

    def __init__(self, x, y):
        self.x = x
        self.y = y


point_b = PointTwo(3, 8)
print(point_b.x)

point_b.x = 4
print(point_b.x)

point_b.y = 9
print(point_b.y)

"""
    Atributos computados
"""


"""
    Propiedades como cachés (Memoización)
"""


class CircleTwo:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._diameter = None
        self._radius = value

    @property
    def diameter(self):
        if self._diameter is None:
            sleep(0.5)
            self._diameter = self._radius * 2
        return self._diameter
