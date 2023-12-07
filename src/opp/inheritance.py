from typing import List

class Person:
  # aqui pueden ir los atributos de clase
  
  def __init__(self, name: str, last_name: str, age: int) -> None:
    self.name = name
    self.last_name = last_name
    self.age = age
    
  def say(self) -> str:
    return "Hello, I am a person"
    
    
class Student(Person):
  def __init__(self, name: str, last_name: str, age: int, courses: List[str], subjects: List[int]) -> None:
    super().__init__(name, last_name, age)
    self.subjects = subjects
    self.courses = courses
    
  def add_note(self, note: int) -> None:
    self.subjects.append(note)
    
  def add_course(self, course: str):
    self.courses.append(course)
    
  def say(self) -> str:
    return "Hello, I am a student"
    
  def __str__(self) -> str:
    return "Name:{}\nLast Name:{}\nAge: {}\nSubjects: {}".format(self.name, self.last_name, self.age, self.courses, self.subjects)
    
student1 = Student("kike", "sfranco", 22, [], [])
print(student1)

class UniversityStudent(Student):
  def __init__(self, name: str, last_name: str, age: int, courses: List[str], subjects: List[int]) -> None:
    super().__init__(name, last_name, age, courses, subjects)
    
  def say(self):
    return "Hello, I am a university student"
  
  def __srt__(self) -> str:
    return "Name:{}\nLast Name:{}\nAge: {}\nCourses: {}\nSubjects: {}".format(self.name, self.last_name, self.age, self.courses, self.subjects)
    
"""
 Herencia Multiple: Clase que hereda de más de una clase base.
"""
class Vehicle:
  def __init__(self, brand: str, model: str, year: int) -> None:
    self.brand = brand
    self.model = model
    self.year = year
    self.mileage = 0
    self.is_running = False
  
  def start_engine(self):
    self.is_running = True
    print(f"The {self.year} {self.brand} {self.model}'s engine is now running.")
  
  def stop_engine(self):
    self.is_running = False
    print(f"The {self.year} {self.brand} {self.model}'s engine has been stopped.")
  
  def drive(self, distance: int):
    if self.is_running:
      self.mileage += distance
      print(f"The {self.year} {self.brand} {self.model} has been driven {distance} miles.")
    else:
      print("Start the engine first.")
      
  def vehicle_info(self) -> str:
    return "Brand: {}\nModel: {}\nYear: {}\nMileage: {}km\nRunning: {}".format(self.brand, self.model, self.year, self.mileage, self.is_running)
      
  def __str__(self) -> str:
    return "Brand: {}\nModel: {}\nYear: {}\nMileage: {}km\nRunning: {}".format(self.brand, self.model, self.year, self.mileage, self.is_running)
  
class Radio:
  def __init__(self, has_radio: bool) -> None:
    self.has_radio = has_radio
    
  def turn_on_radio(self) -> None:
    if self.has_radio:
      print("The radio is now on.")
    else:
      print("This vehicle doesn't have a radio.")
      
  def turn_off_radio(self) -> None:
    if self.has_radio:
      print("The radio is now off.")
    return
  
  def radio_info(self) -> str:
    return f"Radio: {'Yes' if self.has_radio else 'No'}"
  
  def __str__(self) -> str:
    return f"Radio: {'Yes' if self.has_radio else 'No'}"
  
class Car(Vehicle, Radio):
  def __init__(self, brand: str, model: str, year: int, has_radio:bool) -> None:
    Vehicle.__init__(self, brand, model, year)
    Radio.__init__(self, has_radio)
    
  def __str__(self) -> str:
    vehicle_info = self.vehicle_info()
    radio_info = self.radio_info()
    return "{}\n{}".format(vehicle_info, radio_info)
  
toyota = Car("toyota", "camry", 2022, True)
print(toyota)

"""
  Saber si una sub-clase hereda de una super clase
"""
herencia = issubclass(Car, Vehicle) # devolvera true si hereda de la clase Vehicle de lo contrario devolvera false