"""
ENUMS
Una enumeración es un conjunto de nombres simbólicos ligados a valores únicos y constantes

Para crear enumeraciones se usa la clase Enum()

Las enumeraciones son útiles cuando necesitas definir un conjunto inmutable y discreto de valores
Ejemplos:
- Los días de la semana
- los meses
- las estaciones del año
- las direcciones cardinales
- los códigos de estado de los programas
- los códigos de estado HTTP
- los colores en un semáforo
- los planes de precios de un servicio web
Son excelentes ejemplos de enumeraciones en programación

En general, puede usar un enumer cada vez que tenga una variable que pueda tomar una de una conjunto limitado de valores posibles.
"""

import string
from enum import Enum, IntFlag, auto, unique
from typing import List

RED, GREEN, BLUE = range(3)
print(RED)  # 0


class Day(Enum):
    MONDAY = 1  # este valor debe ser constante, por lo que no permite reasignar el valor a los items de la enumeracion
    TUESDAY = 2
    WENSDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


list(Day)
print(Day.MONDAY)


class Season(Enum):
    WINTER, SPRING, SUMMER, FALL = range(1, 5)


class Size(Enum):
    S = "small"
    M = "medium"
    L = "large"
    XL = "extra large"


class SwitchPosition(Enum):
    ON = True
    OFF = False


class UserResponse(Enum):
    YES = True
    NO = False


class EstadoProceso(Enum):
    PENDIENTE = 1
    EN_PROCESO = 2
    TERMINADO = 3


# asignacion dinamica basada en una configuración externa
config = {"PENDIENTE": 100, "EN_PROCESO": 200, "TERMINADO": 300}

for status, value in config.items():
    setattr(EstadoProceso, status, value)


# Enumeracion vacia
class CodigoError(Enum): ...


class BaseTextEnum(Enum):
    def as_list(self):
        try:
            return list(self.value)
        except:
            return [str(self.value)]


class Alphabet(BaseTextEnum):
    LOWER = string.ascii_lowercase
    UPPER = string.ascii_uppercase


Alphabet.LOWER.as_list()


# Usando la api de Enum
class HTTPMethod(Enum):
    GET = 1
    POST = 2
    PUT = 3
    PATCH = 4
    DELETE = 5


names: List[str] = []
while True:
    name = input("Member name:")
    if name in {"q", "Q"}:
        break
    names.append(name.upper())

DynamicEnum = Enum("DynamicEnum", names)
list(DynamicEnum)


# auto asigna valores automaticos para cada miembro del enum
# el comportanimiento predeterminado es asignar valores enteros consecutivos
class Days(Enum):
    MONDAY = auto()  # 1
    TUESDAY = auto()  # 2
    WEDNESDAY = 3
    THURSDAY = auto()  # 4
    FRIDAY = auto()  # 5
    SATURDAY = auto()  # 6
    SUNDAY = 7


# cambiando el comportamiento predeterminado de la función auto()
class CardinalDirection(Enum):
    def _generate_next_value(
        self, name: str, start: int, count: int, last_values: List[str]
    ) -> str:
        return name[0]

    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()


# creando enums con alias y valores únicos
@unique
class OperatingSystem(Enum):
    UBUNTU = "linux"
    MACOS = "darwin"
    WINDOWS = "win"
    DEBIAN = "linux"


# al usar el decorador @unique se prohiben completamente los alias
print(
    OperatingSystem
)  # ValueError: duplicate values in <enum 'OperatingSystem'>: DEBIAN -> UBUNTU

# Aliases aren't listed
list(OperatingSystem)

# To access aliases, use __members__
list(OperatingSystem.__members__.items())


# iterando sobre enumeraciones
class Flavor(Enum):
    VANILLA = 1
    CHOCOLATE = 2
    MINT = 3


for flavor in Flavor:
    print(f"{flavor.name} -> {flavor.value}")

# iterando mediante el atributo .__members__, es undiccionario con los nombres de cada miembre de las enums
# y da acceso a todos los nombres y alias de la enum

for name in Flavor.__members__:
    print(name)

for name in Flavor.__members__.keys():
    print(name)

for value in Flavor.__members__.values():
    print(value)

for name, value in Flavor.__members__.items():
    print(f"{name} -> {value}")


# usando los enums con el patron match
class Semaphore(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3


red = Semaphore.RED
print(red == Semaphore.RED)  # true
print(Semaphore.RED == 1)  # false
print(Semaphore.RED in Semaphore)  # true
print(Semaphore.GREEN not in Semaphore)  # false


def handle_semaphore(light):
    match light:
        case Semaphore.RED:
            print("you must stop!")
        case Semaphore.YELLOW:
            print("light will change to red, be careful!")
        case Semaphore.GREEN:
            print("you can continue")


# agregando funcionalidades
class Mood(Enum):
    FUNKY = 1
    MAD = 2
    HAPPY = 3

    def describe_mood(self):
        return self.name, self.value

    def __str__(self):
        return f"I feel {self.name}"

    @classmethod
    def favorite_mood(cls):
        return cls.HAPPY


print(Mood.HAPPY.describe_mood())
Mood.HAPPY
Mood.favorite_mood()


class ESort(Enum):
    ASC = 1
    DESC = 2

    def __call__(self, values):
        return sorted(values, reverse=self is ESort.DESC)


nums = [5, 2, 7, 6, 3, 9, 8, 4]
print(ESort.ASC(nums))
print(ESort.DESC(nums))


# creacion de banderas IntFlag y Flag
# las flag debe tomar potencias de 2 (1,2,4,8)
class Role(IntFlag):
    OWNER = 8
    POWER_USER = 4
    USER = 2
    SUPERVISOR = 1
    ADMIN = OWNER | POWER_USER | USER | SUPERVISOR


jhon_roles = Role.USER | Role.SUPERVISOR
