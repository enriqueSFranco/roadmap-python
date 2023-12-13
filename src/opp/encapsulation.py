class Superhero:
  def __init__(self, name, power, secrete_indentity) -> None:
    self.name = name # Encapsulamiento público
    self._power = power # Encapsulamiento protegido
    self.__secret_identity = secrete_indentity # Encapsulamiento privado
    
  def show_detail(self):
    print("Name: {}\nPower: {}\nSecret identity: {}".format(self.name, self._power, self.__secret_identity))
    
  
batman = Superhero("Batman 🦇", "Intelligence", "Bruce Wayne")

batman.show_detail()