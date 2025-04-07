"""
+ ¿Qué es un Iterador en Python?

En Python, un iterador es un objeto que le permite iterar sobre colecciones de datos, como listas, tuplas, diccionarios, y conjuntos.

Los iteradores de Python implementan el patrón de diseño del iterador, que le permite atravesar un contenedor y acceder a sus elementos. El patrón del iterador desacopla la iteración algoritmos desde contenedor estructuras de datos.

Los Iteradores asumen la responsabilidad de dos acciones principales:

1.- Volviendo los datos de un flujo o contenedor un artículo a la vez
2.- Manteniendo el rastro de la actual y artículos visitados

Los iteradores de Python deben implementar una estructura interna bien establecida conocida como protocolo iterator

# La única responsabilidad de .__iter__() es devolver un objeto iterador.
´´´
def __iter__(self):
  return self
´´´

El método .__next__() será un poco más complejo dependiendo de lo que estés tratando de hacer con tu iterador. Este método debe devolver el siguiente elemento del flujo de datos. También debería plantear un StopIteration excepción cuando no hay más elementos disponibles en el flujo de datos.

+ Creando Diferentes Tipos de Iteradores

Usando los dos métodos que componen el protocolo del iterador en sus clases, puede escribir al menos tres tipos diferentes de iteradores personalizados. Puedes tener iteradores que:

1.- Tome un flujo de datos y produzca elementos de datos tal como aparecen en el datos originales
2.- Tome un flujo de datos, transformar cada artículo, y rendimiento artículos transformados
3.- No tome datos de entrada, generando nuevos datos como resultado de algún cálculo para finalmente producir el artículos generados
"""

from math import sqrt

class SequenceIterator:
  def __init__(self, sequence):
    self._sequence = sequence
    self._index = 0

  def __iter__(self):
    return self

  def __next__(self):
    if self._index < len(self._sequence):
      item = self._sequence[self._index]
      self._index += 1
      return item
    else:
      raise StopIteration

for item in SequenceIterator([1,2,3,4]):
  print(item)

# simulacion usando el metodo __next__()
sequence = SequenceIterator(["solo leveling", "hermana casera", "la vida despues del fin", "amo del tiempo"])
iterator = sequence.__iter__()

while True:
  try:
    item = iterator.__next__()
  except StopIteration:
    break
  else:
    print(item)

# transformando datos de entrada
class TransformIterator:
  def __init__(self, sequence):
    self._sequence = sequence
    self._index = 0

  def __iter__(self):
    return self

  def __next__(self):
    if self._index < len(self._sequence):
      item = self._sequence[self._index] ** 2 # Transformación: cuadrado del número
      self._index += 1
      return item
    else:
      raise StopIteration # Finaliza la iteración

for value in TransformIterator([1,2,3,4]):
  print(value)

# generando nuevos datos
class PrimeIterator:
  def __init__(self):
    self.current = 2 # Empezamos con el primer número primo
    self.generated_primes = []

  def __iter__(self):
    return self

  def __next__(self):
    while True:
      if self._is_prime(self.current):
        self.generated_primes.append(self.current)
        prime = self.current
        self.current += 1
        return prime
      self.current += 1

  def _is_prime(self, value: int) -> bool:
    if value <= 1: # los numeros menores o iguales a 1 no son primos
      return False
    if value <= 3: # 2 y 3 son primos
      return True
    if value % 2 == 0 and value % 3 == 0: # eliminamos todos los multimos de 2 y 3
      return False
    
    limit = int(sqrt(value)) + 1
    for i in range(5, limit, 6):
      if value % i == 0 or value % (i + 2) == 0:
        return False
    return True

primes_iter = PrimeIterator()

for _ in range(10):
  print(next(primes_iter))

class FibonacciIterator:
  def __init__(self, stop:int=10):
    self.stop = stop
    self.index = 0
    self.current = 0
    self.next = 1
  
  def __iter__(self):
    return self

  def __next__(self):
    if self.index < self.stop:
      self.index += 1
      fib_num = self.current
      self.current, self.next = (self.next, self.current + self.next)
      return fib_num
    else:
      raise StopIteration

for fib_number in FibonacciIterator():
  print(fib_number)

"""
Iteradores Generadores (Generator Iterators)

Un generador en Python es una función que se utiliza para producir una secuencia de valores de manera perezosa (lazy), es decir, solo genera un valor cuando se necesita. En lugar de devolver todos los valores de una vez (como en una lista), un generador produce un valor, lo "retorna" y luego guarda su estado para poder reanudar la ejecución cuando se necesite más valores. Este comportamiento lo hace muy eficiente, especialmente cuando se trata de grandes cantidades de datos o secuencias infinitas.


Cómo se crean los generadores:

1.- Uso de la palabra clave yield:
  Un generador es una función que utiliza la palabra clave yield para devolver un valor. Cada vez que se invoca el generador con next(), la ejecución de la función se reanuda justo después del yield.
  Diferencia clave con las funciones normales: Las funciones normales usan return para devolver un solo valor y terminan su ejecución, mientras que los generadores pueden usar yield múltiples veces, lo que permite que el generador produzca múltiples valores uno tras otro.
  
2.- Sintaxis simple: 
  Los generadores permiten crear iteradores sin necesidad de escribir clases adicionales, lo que simplifica la implementación.
"""

def infinity_count():
  count = 0
  while True:
    yield count
    count += 1

# Llamando a next en un generador creado en cada llamada
print(next(infinity_count()))  # Imprime 0
print(next(infinity_count()))  # Imprime 0
print(next(infinity_count()))  # Imprime 0

"""
¿Qué sucede aquí?

- Cada vez que llamas a contador_infinito(), se crea una nueva instancia del generador que comienza de cero (count = 0).

- Por lo tanto, cuando usas next() en el generador recién creado, el primer valor que devuelve es siempre 0, ya que el generador no recuerda su estado entre las llamadas.
"""