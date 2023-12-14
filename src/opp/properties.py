class Person:
  def __init__(self, name) -> None:
    self.__name = name
    
  @property
  def get_name(self):
    return self.__name
  
