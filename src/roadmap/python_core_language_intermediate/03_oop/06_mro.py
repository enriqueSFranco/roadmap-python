class A:
	def saludar(self):
		print("Hola desde A")

class B(A):
	def saludar(self):
		print("Hola desde B")
		super().saludar()

class C(A):
	def saludar(self):
		print("Hola desde C")
		super().saludar()

class D(B, C):
	pass

print(D.mro()) # muestra como va el orden de llamada de los metodos

d = D()
B.saludar(d) # vamos a ejecutar el metodo saludar pero de la clase B, le pasamos un objeto al metodo saludar(self=d)

class Animal:
  def eat(self):
    print("Eating")

class Mammal(Animal):
  def breastfeed(self):
    print("Breastfeeding")

class Bird:  
  def fly(self):
    print("Flying")

class Murcielago(Mammal, Bird):
	pass
morbius = Murcielago()

morbius.eat()
morbius.breastfeed()
morbius.fly()


