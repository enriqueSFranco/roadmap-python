from abc import ABC, abstractmethod

"""
  	Dependency Inversión Principle (DIP)
  	Las abstracciones no deben depender de los detalles. Los detalles deben depender de las abstracciones.

  	"Los módulos de alto nivel no deben depender de los módulos de bajo nivel. Ambos deben depender de abstracciones (interfaces o clases abstractas). Las abstracciones no deben depender de los detalles. Los detalles deben depender de las abstracciones."

	En palabras más simples:

	Módulos de alto nivel: Son las partes del sistema que contienen la lógica de negocio importante, la que implementa el propósito principal de la aplicación.
	Módulos de bajo nivel: Son los componentes que gestionan detalles más específicos, como la base de datos, el sistema de archivos o servicios externos (por ejemplo, APIs o servicios de correo electrónico).
	El principio sugiere que los módulos de alto nivel no deberían depender directamente de los módulos de bajo nivel. En su lugar, ambos deben depender de abstracciones, como interfaces o clases abstractas.
"""


class FrontEnd:
    def __init__(self, back_end):
        self.back_end = back_end

    def display_data(self):
        data = self.back_end.get_data_from_database()
        print("Display data:", data)


class BackEnd:
    def get_data_from_database(self):
        return "Data from the database"


"""
	El problema de las clases Frontend y Backend es que la clase Fronted esta dependiendo de
    la clase Backend.
    Este acoplamiento puede conducir a problemas de escalabilidad. Por ejemplo, si la aplicación crece rápidamente y queremos que la aplicación pueda leer datos de un API REST. ¿Cómo hacemos eso?
"""


# Una propuesta es usar inversion de dependencia
class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass


class Database(DataSource):
    def get_data(self):
        return "Data from database"


class API(DataSource):
    def get_data(self):
        return "Data from API"


db_front_end = FrontEnd(Database())
db_front_end.display_data()

api_front_end = FrontEnd(API())
db_front_end.display_data()
