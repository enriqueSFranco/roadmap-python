class Employee:
	num_instance = 0
	def __init__(self, name: str, age: int):
		"""
		Atributos de instancia
		- Propiedades que varían de una instancia a otra.
		"""
		self.name = name
		self.age = age
		type(self).num_instance += 1

Employee("employee1", 20)
Employee("employee1", 30)
Employee("employee1", 28)
print(Employee.num_instance) # 3

class Dog:
	""" 
	Atributo de clase
	- Tienen el mismo valor para todas las instancias de clase
	- Siempre debe asignarles un valor inicial
	- Para definir propiedades que deberían tener el mismo valor para cada instancia de clase
	"""
	species = "Canis familiaris"

	def __init__(self, name, age):
		self.name = name
		self.age = age

	# Instance method
	def description(self):
		return f"{self.name} is {self.age} years old"

	# Another instance method
	def speak(self, sound):
		return f"{self.name} says {sound}"

	"""
	Metodo __str__()
	Objetivo: devolver una cadena representativa, no realizar operaciones complejas

	- Definir cómo se representa en forma de cadena de texto una instancia 
	de esa clase cuando se imprime o se convierte a string

	- <__main__.Coche object at 0x7f9d9f7b0b20> === "{self.name} is {self.age} years old"

	- Evitar exceso de detalles
	- Evitar lógica compleja 
	"""  
	def __str__(self):
		return f"{self.name} is {self.age} years old"
  
"""
Creando instancias de clases
- Una instancia es un objeto creado a partir de una clase.
  Es como si la clase fuera un plano y la instancia, una construcción real basada en ese plano

"""
schnauzer = Dog("sebastian", 10)
schnauzer.speak("Woof Woof")
dog_list = [("Sebastian", 10), ("Maximo", 5), ("Scoobydoo", 3)]
for name, age in dog_list:
  dog = Dog(name, age)
  print(dog.description)

"""
  	Metodo __repr__()
	- Está destinado a proporcionar una representación precisa y descriptiva del objeto
	preferentemente con información suficiente para reconstruir el objeto

	Cuándo usar __repr__:
	- Para la depuración o cuando quieres obtener una representación precisa de un objeto 
	en el contexto de desarrollo. 
	Idealmente, el string devuelto por __repr__ debería ser detallado y útil para los desarrolladores.
	
	- Se utiliza en debuggers, logs, o cuando se evalúa la representación del objeto de manera detallada. 
	Cuando el objeto aparece en la consola o se visualiza en un entorno interactivo, 
	Python invoca __repr__ si __str__ no está definido.
"""
class Producto:
	def __init__(self, nombre, precio):
		self.nombre = nombre
		self.precio = precio

	# Representación amigable para el usuario
	def __str__(self):
		return f"Producto: {self.nombre}, Precio: ${self.precio}"

	# Representación para depuración
	def __repr__(self):
		return f"Producto(nombre='{self.nombre}', precio={self.precio})"


# Creando una instancia
producto = Producto("Camiseta", 25)

# Usando print() o str()
print(str(producto))  # Esto llama a __str__ y produce una salida legible
# Salida: Producto: Camiseta, Precio: $25

# Usando repr() o en el shell interactivo
print(repr(producto))  # Esto llama a __repr__ y produce una salida más detallada
# Salida: Producto(nombre='Camiseta', precio=25)

# También, si haces esto en el shell interactivo de Python:
producto
# Esto invoca __repr__ y produce:
# Producto(nombre='Camiseta', precio=25)


"""
	¿Qué es el "name mangling"?
	El name mangling es un proceso en Python que cambia el nombre de los atributos y 
	métodos privados (con __ al principio). El propósito de este proceso es evitar que 
	los atributos o métodos se sobrescriban accidentalmente, especialmente en clases heredadas.
"""


"""
	Atributos dinamicos de clase
"""

employee_dict = {
	"name": "John Doe",
	"position": "Python Developer",
	"department": "Engineering",
	"salary": 80000,
	"hire_date": "2020-01-01",
	"is_manager": False,
}

class EmployeeRecord:
	pass

employee_record = EmployeeRecord()

for field, value in employee_dict.items():
	setattr(employee_record, field, value)