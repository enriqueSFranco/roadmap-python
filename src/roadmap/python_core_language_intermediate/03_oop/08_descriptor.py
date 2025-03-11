"""
	¿Qué es un Descriptor en Python?
	Un descriptor en Python es cualquier objeto que implemente uno de los siguientes métodos especiales:

	__get__(self, instance, owner) -> obj :
		Este método se llama cuando accedemos a un atributo. En términos sencillos, este método se ejecuta cuando se obtiene el valor del atributo.
		- instance: Es la instancia del objeto que tiene el atributo.
		- owner: Es la clase de la instancia.

	__set__(self, instance, value):
	Este método se llama cuando asignamos un valor a un atributo. Es decir, se ejecuta cuando se establece el valor del atributo.

	- instance: La instancia del objeto que tiene el atributo.
	- value: El valor que se quiere asignar al atributo.

	__delete__(self, instance):
	Este método se llama cuando se elimina un atributo. Este método se ejecuta cuando usamos del sobre un atributo.

	__set_name__(self, owner, name)
    
	En pocas palabras, un descriptor es un objeto que controla cómo se accede, asigna o elimina un atributo de una clase

	¿Por qué usar Descriptores?
	Los descriptores permiten personalizar el comportamiento de los atributos en una clase, como:

	Validación de valores.
	Cálculo de valores al acceder a un atributo.
	Guardado de valores de manera controlada.
	Implementación de la lógica de acceso a los atributos de manera más flexible y reutilizable.


	¿Cuando usar un descritor?
	En general, si se encuentra copiando y pegando definiciones de propiedades a lo largo de su código 
	o si detecta código repetitivo, como en el ejemplo anterior, entonces debe considerar usar descriptores.
"""


class PositiveNumber:
    def __get__(self, instance, owner):
        return instance.__dict__.get(
            self.name, 0
        )  # Regresa el valor del atributo, o 0 si no está establecido

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("El valor debe ser un numero positivo") from None
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class MyClass:
    number = PositiveNumber()  # Usamos el descriptor aquí

    def __init__(self, number):
        self.number = number  # Al asignar a `number`, se usa el descriptor
