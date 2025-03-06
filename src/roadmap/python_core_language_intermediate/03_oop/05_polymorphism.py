class Animal:
  def __init__(self) -> None:
    pass
  
  def hacer_sonido(self):
    print("sonido generico de animal")
    
class Dog:
  def __init__(self) -> None:
    pass
  
  def hacer_sonido(self):
    print("guau guau")
    
class Cat:
  def __init__(self) -> None:
    pass
  
  def hacer_sonido(self):
    print("miau")
    
def probar_sonido(animal: Animal):
  animal.hacer_sonido()
    
dog = Dog()
cat = Cat()

probar_sonido(dog)
probar_sonido(cat)