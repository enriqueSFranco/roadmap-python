from random import choice


class Point:
    # es responsable de crear y devolver un nuevo objeto vacío
    def __new__(cls, *args, **kwargs):
        print("1.- Create a new instance of Point")
        return super().__new__(cls)

    # El método .__init__() toma el nuevo objeto como su primer argumento self, junto con los argumentos constructors de clase.
    def __init__(self, x, y):
        print("2. Initialize the new instance of Point.")
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{type(self).__name__}(x={self.x}, y={self.y})"


point = Point(21, 42)


class A:
    def __init__(self, value_a):
        self.value_a = value_a


"""
    La clase B va a ser un objeto de clase A, esto es por que el metodo __new__
    crea y devuelve un objeto de A 
"""


class B:
    def __new__(cls, *args, **kwargs):
        print("Initialize the new instance of B.")
        return A(42)

    def __init__(self, value_b):
        self.value_b = value_b


a = A(1)
b = B(2)
print(isinstance(b, A))
print(isinstance(b, B))

# Validar entrada de argumentos en el init
# class Rectangle:
#    def __init__(self, width, height):
#        if not (isinstance(width, (int, float)) and width > 0):
#            raise ValueError(f"positive width expected, got {width}")
#        self.width = width
#        if not (isinstance(height, (int, float)) and height > 0):
#            raise ValueError(f"positive height expected, got {height}")
#        self.height = height


# Una forma mas pythonica es pasar los atributos a propiedades
class Rectangle:
    def __init__(self, width, height):
        self._width = None
        self._height = None
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not (isinstance(value, (int, float)) and value > 0):
            raise ValueError(f"positive width expected, got {value}")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not (isinstance(value, (int, float)) and value > 0):
            raise ValueError(f"positive height expected, got {value}")
        self._height = value


# Instancias de Devolución de una Clase Diferente
class Pet:
    def __new__(cls):
        other = choice([Dog, Cat, Python])
        instance = super().__new__(other)
        print(f"I'm a {type(instance).__name__}!")
        return instance


class Dog:
    def communicate(self):
        print("woof! woof!")


class Cat:
    def communicate(self):
        print("meow! meow!")


class Python:
    def communicate(self):
        print("hiss! hiss!")


"""
    A veces necesita implementar una clase que permita la creación de una sola instancia solamente. Este tipo de clase se conoce comúnmente como a clase singleton.
"""


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._isinstance
