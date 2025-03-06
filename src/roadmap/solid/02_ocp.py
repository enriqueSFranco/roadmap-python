"""
	Open-Closed Principle (OCP)
	Las entidades de software (clases, módulos, funciones, etc.) deben estar abiertas para la extensión, 
  	pero cerradas para su modificación.
    
    Esto significa que se deben poder agregar funcionalidades sin alterar el código existente.

    Fórmula para recordar:
    "Abierto para extensión, cerrado para modificación"
"""

from abc import ABC, abstractmethod
from math import pi


class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        if self.shape_type == "rectangle":
            self.width = kwargs["width"]
            self.height = kwargs["height"]
        elif self.shape_type == "circle":
            self.radius = kwargs["radius"]
        # el seguir modficando directamente la clase para dar soporte a una nueva figura viola el
        # principio de Open-Closed
        elif self.shape_type == "square":
            self.side = kwargs["side"]

    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.width * self.height
        elif self.shape_type == "circle":
            return pi * self.radius**2


rectangle = Shape("rectangle", width=10, height=5)
rectangle.calculate_area()

circle = Shape("circle", radius=2.5)

"""
	¿Cómo podemos arreglar la clase para que esté abierta a la extensión pero cerrada a la modificación?
    Convertimos a la clase ShapeWithOC Pen una clase abstracta
"""


class ShapeWithOCP(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(ShapeWithOCP):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * self.raduis**2


class Rectangle(Shape):
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


# 2do ejemplo
# Mal ejemplo: Se modifica la clase cada vez que se añade un nuevo tipo de notificación
class Notification:
    def __init__(self, method, message):
        if method == "email":
            print(f"Enviando email: {message}")
        elif method == "sms":
            print(f"Enviando SMS: {message}")


# Buen ejemplo: Se usa herencia para extender la funcionalidad
class NitificationWithOCP:
    def __init__(self, message):
        raise NotImplementedError


class EmailNotification(Notification):
    def send(self, message):
        print(f"Enviando email: {message}")


class SMSNotification(Notification):
    def send(self, message):
        print(f"Enviando SMS: {message}")


# Ahora, agregar otro tipo de notificación solo requiere crear una nueva clase sin tocar las existentes.
