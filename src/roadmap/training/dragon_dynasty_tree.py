# Python: dragon_dynasty_tree.py
# JavaScript: dragonDynastyTree.js
# Kotlin: DragonDynastyTree.kt
# Swift: DragonDynastyTree.swift

# EJERCICIO:
# ¡La Casa del Dragón ha finalizado y no volverá hasta 2026!
# ¿Alguien se entera de todas las relaciones de parentesco
# entre personajes que aparecen en la saga?
# Desarrolla un árbol genealógico para relacionarlos (o invéntalo).
# Requisitos:
# 1. Estará formado por personas con las siguientes propiedades:
#    - Identificador único (obligatorio)
#    - Nombre (obligatorio)
#    - Pareja (opcional)
#    - Hijos (opcional)
# 2. Una persona sólo puede tener una pareja (para simplificarlo).
# 3. Las relaciones deben validarse dentro de lo posible.
#    Ejemplo: Un hijo no puede tener tres padres.
# Acciones:
# 1. Crea un programa que permita crear y modificar el árbol.
#    - Añadir y eliminar personas
#    - Modificar pareja e hijo
# 2. Podrás imprimir el árbol (de la manera que consideres).

# NOTA: Ten en cuenta que la complejidad puede ser alta si
# se implementan todas las posibles relaciones. Intenta marcar
# tus propias reglas y límites para que te resulte asumible.

import logging
import os

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s:%(name)s:%(message)s")
logger = logging.getLogger("LoggerDragonDynastyTree")

class Person:
  def __init__(self, id: int, name: str) -> None:
    self.id = id
    self.name = name
    self.partner = None
    self.children = []

  def __repr__(self) -> str:
    return f"{self.name} (ID: {self.id})"

class FamilyTree:
  def __init__(self) -> None:
    self.family_tree = {}

  def add_person(self, id: int, name: str):
    if id in self.family_tree:
      raise ValueError(f"Ya existe una persona con el ID({id})")
    new_person = Person(id, name)
    self.family_tree[id] = new_person
    logger.info(f"Se agrego a {new_person} al arbol genealogico")

  def delete_person(self, id: int) -> None:
    if id not in self.family_tree:
      raise ValueError(f"No existe una persona con el ID {id}")
    person_eliminated = self.family_tree.pop(id, None)
    logger.debug(f"persona eliminada {person_eliminated.name}")

    # si tiene pareja, entonces se elimina
    if person_eliminated.partner:
      partner = person_eliminated.partner
      if not partner.children:
        self.family_tree.pop(partner.id, None)

    # si tiene hijos, entonces se eliminan
    if person_eliminated.children:
      for child in person_eliminated.children:
        child.partner = None

  def set_partner(self, id1, id2) -> None:
    if id1 not in self.family_tree or id2 not in self.family_tree:
      raise ValueError("Error: Uno de los IDs no existe en el arbol genealogico")
    
    person1 = self.family_tree[id1]
    person2 = self.family_tree[id2]
    
    # Validar si alguna de las dos personas ya tiene pareja
    if person1.partner or person2.partner:
      raise ValueError("Error: Una de las dos parejas ya tiene pareja")
    
    person1.partner = person2
    person2.partner = person1
    logger.info(f"Se asignó pareja: {person1} y {person2}")
  
  def set_child(self, father_id, child_id):
    if father_id not in self.family_tree or child_id not in self.family_tree:
      raise ValueError("Uno de los dos IDs no existe en el arbol")
    father = self.family_tree[father_id]
    child = self.family_tree[child_id]

    if child.partner:
      raise ValueError(f"{child} ya tiene pareja")

    father.children.append(child)
    logger.info(f"{child} ha sido asignado como hijo de {father}")


  def print_family_tree(self, id):
    if id not in self.family_tree:
      raise ValueError(f"Error: el ID: {id} no existe")
    person = self.family_tree[id]
    self._print_person(person)

  def _print_person(self, person: Person, level: int = 1):
    indent = "  " * level
    print(f"{indent}-{person}")
    if person.partner:
      print(f"{indent}-Partner: {person.partner}")
    if person.children:
      print(f"{indent}-Children: ")
      for child in person.children:
        self._print_person(child, level + 1)
        if child.children:
          print(f"{indent}-Grandchildren:")
          self._print_descendants(child, level + 2)

  
  def _print_descendants(self, person: Person, level):
    for descendant in person.children:
      self._print_person(descendant, level)
      if descendant.partner:
        print(f"{'  ' * level}  partner: {descendant.partner}")
      if descendant.children:
        print(f"{'  ' * level}  Great-grandchildren:")
        self._print_descendants(descendant, level + 1)

if __name__ == "__main__":
  os.system("cls" if os.name == "nt" else "clear")
  # Crear árbol genealógico
  tree = FamilyTree()
  # Agregar personas
  tree.add_person(1, "Jon Snow")
  tree.add_person(2, "Daenerys Targaryen")
  tree.add_person(3, "Arya Stark")
  tree.add_person(4, "Sansa Stark")
  
  # Asignar pareja
  tree.set_partner(1, 2)
  
  # Asignar hijos
  tree.set_child(1, 3)
  tree.set_child(1, 4)
  
  # Imprimir árbol genealógico
  print("Árbol genealógico:")
  tree.print_family_tree(1)
  
  # Eliminar persona
  print("\nEliminando a Sansa Stark:")
  tree.delete_person(4)
  
  # Imprimir árbol genealógico después de eliminar
  print("\nÁrbol genealógico después de eliminar a Sansa Stark:")
  tree.print_family_tree(1)
