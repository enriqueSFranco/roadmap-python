import sys
import os
import time
from enum import Enum
from typing import Dict, List, Optional

# Definición de constantes
MICKEY = "🐭"
EMPTY_CELL = "⬜️"
OBSTACLE = "⬛️"
EXIT = "🚪"

# Definición del laberinto
labyrinth = [
  [MICKEY, EMPTY_CELL, OBSTACLE, EMPTY_CELL, OBSTACLE],
  [EMPTY_CELL, EMPTY_CELL, OBSTACLE, EMPTY_CELL, OBSTACLE],
  [OBSTACLE, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, OBSTACLE],
  [EMPTY_CELL, OBSTACLE, OBSTACLE, EMPTY_CELL, OBSTACLE],
  [EMPTY_CELL, EMPTY_CELL, OBSTACLE, EMPTY_CELL, OBSTACLE],
  [OBSTACLE, EMPTY_CELL, OBSTACLE, EMPTY_CELL, EXIT],
]

# Posición inicial de Mickey
mickey_position = {"row": 0, "col": 0}

def print_labyrinth(labyrinth: List[List[str]]):
  os.system('cls' if os.name == 'nt' else 'clear')
  for row in labyrinth:
    print(" ".join(row))

def initialize_mickey_position() -> Optional[Dict[str, int]]:
  """Encuentra y retorna la posición inicial de Mickey en el laberinto."""
  for row_index, row in enumerate(labyrinth):
    if MICKEY in row:
      return { "row": row_index, "col": row.index(MICKEY)}
  return None

class Command(Enum):
  UP = "w",
  RIGHT = "d",
  DOWN = "s",
  LEFT = "a",
  EXIT = "e"

MENU_OPTIONS = [
  "[w] Move up",
  "[d] Move rigt",
  "[s] Move down",
  "[a] Move left",
  "[e] Exit"
]

def show_menu(options: List[str]) -> None:
  for option in options:
    print(option)

def is_move_valid(row: int, col: int) -> bool:
  """Verifica si el movimiento es válido dentro del laberinto y no choca con un obstáculo."""
  return row >= 0 and row < len(labyrinth) and col >= 0 and col < len(labyrinth) and labyrinth[row][col] != OBSTACLE

def move_mickey(command: Command) -> None:
  """Mueve a Mickey según el comando recibido y actualiza el laberinto."""
  global mickey_position
  row, col = mickey_position.values()
  new_row = row
  new_col = col

  if command == Command.UP.value[0]:
    new_row -= 1
  elif command == Command.RIGHT.value[0]:
    new_col += 1
  elif command == Command.DOWN.value[0]:
    new_row += 1
  elif command == Command.LEFT.value[0]:
    new_col -= 1
  else:
    print("Invalid move.")
    time.sleep(1)
    return

  if is_move_valid(new_row, new_col):
    # Update the labyrinth and Mickey's position
    labyrinth[row][col] = EMPTY_CELL
    new_mickey_coordinates = {"row": new_row, "col": new_col}
    mickey_position = new_mickey_coordinates
    if labyrinth[mickey_position["row"]][mickey_position["col"]] == EXIT:
      print_labyrinth(labyrinth)
      print("congratulations 🥳")
      sys.exit()
    labyrinth[new_row][new_col] = MICKEY
  else:
    print(f"Movimiento invalido row:{new_row}, col: {new_col}")
    time.sleep(1)

def start_game():
  """Inicia el juego y maneja la interacción con el usuario."""
  initialize_mickey_position()
  while True:
    print_labyrinth(labyrinth)
    show_menu(MENU_OPTIONS)
    choice = input("Enter an option:").strip().lower()

    if choice == Command.EXIT.value[0]:
      sys.exit()
      print("Invalid option, please try again.")
    move_mickey(choice)

if __name__ == "__main__":
  start_game()



# EJERCICIO:
# ¡Disney ha presentado un montón de novedades en su D23!
# Pero... ¿Dónde está Mickey?
# Mickey Mouse ha quedado atrapado en un laberinto mágico
# creado por Maléfica.
# Desarrolla un programa para ayudarlo a escapar.
# Requisitos:
# 1. El laberinto está formado por un cuadrado de 6x6 celdas.
# 2. Los valores de las celdas serán:
#    - ⬜️ Vacío
#    - ⬛️ Obstáculo
#    - 🐭 Mickey
#    - 🚪 Salida
# Acciones:
# 1. Crea una matriz que represente el laberinto (no hace falta
# que se genere de manera automática).
# 2. Interactúa con el usuario por consola para preguntarle hacia
# donde se tiene que desplazar (arriba, abajo, izquierda o derecha).
# 3. Muestra la actualización del laberinto tras cada desplazamiento.
# 4. Valida todos los movimientos, teniendo en cuenta los límites
# del laberinto y los obtáculos. Notifica al usuario.
# 5. Finaliza el programa cuando Mickey llegue a la salida.