from typing import List
from opp import Person

class Employee(Person):
  # aqui pueden ir los atributos de clase
  
  def __init__(self, job:str, salary:float) -> None:
    super().__init__(self)
    self.job = job # atributo de instancia
    self.salary = salary
    
  def __str__(self) -> str:
    return "Job:{}\nSalary:${:,.2f}".format(self.job, self.salary)

employees: List[Employee] = []
employees.append(Employee("software engineer", 3500))
employees.append(Employee("data scientist", 45000))

for employee in employees:
  print(employee)