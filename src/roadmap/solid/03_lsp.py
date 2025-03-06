from abc import ABC, abstractmethod

"""
  Liskov Substitution Principle (LSP)
  Concepto: Los objetos de una clase derivada deben ser intercambiables por objetos de la clase base sin alterar el comportamiento correcto del programa.

  Fórmula para recordar:
  "Un objeto derivado debe ser intercambiable por un objeto base"
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


"""
  Creamos un cuadrado a partir de un rectangulo
"""


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    """
        El método __setattr__ en Python es un "hook" que te permite interceptar cuando se asigna un valor a un atributo. Este método recibe dos parámetros:
        - key: El nombre del atributo (como una cadena de texto).
        - value: El valor que se desea asignar al atributo.
        
        Este método es llamado automáticamente cuando intentas asignar un valor a un atributo de un objeto.
    """

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in ("width", "height"):
            self.__dict__["width"] = (
                value  # Accede al diccionario interno __dict__ del objeto
            )
            self.__dict__["height"] = value


"""El codigo anterior no cumple el principio LSP"""


class Shape:
    @abstractmethod
    def calculate_area(self):
        pass


class Rectange(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side**2
