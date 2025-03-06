class ParkingSystem:  
  
  def __init__(self, big: int, medium: int, small: int):
    self.slots = [big, medium, small]

  def addCar(self, carType: int) -> bool:
    pass
  
parking_system = ParkingSystem(1, 1, 0)
print(parking_system.addCar(1))
print(parking_system.addCar(2))
print(parking_system.addCar(3))