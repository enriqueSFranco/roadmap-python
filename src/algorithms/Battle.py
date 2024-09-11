# EJERCICIO:
# ¡Deadpool y Wolverine se enfrentan en una batalla épica!
# Crea un programa que simule la pelea y determine un ganador.
# El programa simula un combate por turnos, donde cada protagonista posee unos
# puntos de vida iniciales, un daño de ataque variable y diferentes cualidades
# de regeneración y evasión de ataques.
# Requisitos:
# 1. El usuario debe determinar la vida inicial de cada protagonista.
# 2. Cada personaje puede impartir un daño aleatorio:
#    - Deadpool: Entre 10 y 100.
#    - Wolverine: Entre 10 y 120.
# 3. Si el daño es el máximo, el personaje que lo recibe no ataca en el
# siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
# 4. Cada personaje puede evitar el ataque contrario:
#    - Deadpool: 25% de posibilidades.
#    - Wolverine: 20% de posibilidades.
# 5. Un personaje pierde si sus puntos de vida llegan a cero o menos.
# Acciones:
# 1. Simula una batalla.
# 2. Muestra el número del turno (pausa de 1 segundo entre turnos).
# 3. Muestra qué pasa en cada turno.
# 4. Muestra la vida en cada turno.
# 5. Muestra el resultado final.

import logging
from random import random, randrange
import time 

# Configuracion de log
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s:%(name)s:%(message)s")
logger = logging.getLogger("BattleLogger")

class RandomUtils:
  @staticmethod
  def generate_random_int(min_damage: int, max_damage: int) -> int:
    return randrange(min_damage, max_damage + 1)
  
  @staticmethod
  def generate_boolean(probability) -> bool:
    return random() < probability

class Superhero:
  def __init__(self, name="deadpool", health=100, activate_regeneration=False, min_damage=10, max_damage=10, chance_to_evade=0.25) -> None:
    self.name = name
    self.health = health
    self.activate_regeneration = activate_regeneration
    self.min_damage = min_damage
    self.max_damage = max_damage
    self.chance_to_evade = chance_to_evade

  def attack(self) -> int:
    return RandomUtils.generate_random_int(self.min_damage, self.max_damage)

  def can_evade(self) -> bool:
    return RandomUtils.generate_boolean(self.chance_to_evade)

  def receive_damage(self, damage):
    if damage >= self.max_damage:
      self.health = 0
      self.activate_regeneration = True
      return
    self.health -= damage
    return self.health
  
  def is_alive(self) -> bool:
    return self.health > 0

  def display_status(self):
    return f"{self.name} tiene {self.health} de vida."

class Battle:
  def __init__(self, superhero_one: Superhero, superhero_two: Superhero) -> None:
    self.superhero_one = superhero_one
    self.superhero_two = superhero_two
    self.turn = 1

  # TODO: Implementar la concurrencia
  def simulate(self):
    while self.superhero_one.is_alive() and self.superhero_two.is_alive():
      logger.info(f"Turno: {self.turn}")
      time.sleep(1)

      # ataque superhero 1
      self.execute_turn(self.superhero_one, self.superhero_two)
      if self.superhero_two.is_alive():
        self.execute_turn(self.superhero_two, self.superhero_one)

      logger.info(self.superhero_one.display_status())
      logger.info(self.superhero_two.display_status())

      self.turn += 1

    logger.info(self.declare_winner())

  def execute_turn(self, attaker: Superhero, defender: Superhero):
    if attaker.is_alive():
      damage = attaker.attack()
      logger.info(f"the superhero {attaker.name} has inflicted {damage}")
      defender.receive_damage(damage)
      if damage >= defender.health:
        logger.info(f"{attaker.name} regeneration is active")

  def declare_winner(self) -> str:
    if self.superhero_one.is_alive():
      return f"El ganador es {self.superhero_one.name}"
    return f"El ganador es {self.superhero_two.name}"

if __name__ == "__main__":
  deadpool = Superhero("deadpool", health=100, activate_regeneration=False, min_damage=10, max_damage=100, chance_to_evade=0.25)
  wolverine = Superhero("wolverine", health=100, activate_regeneration=False, min_damage=10, max_damage=120, chance_to_evade=0.20)

  battle = Battle(deadpool, wolverine)
  battle.simulate()
