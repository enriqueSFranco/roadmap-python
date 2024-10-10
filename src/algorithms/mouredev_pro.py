# EJERCICIO:
# He presentado mi proyecto más importante del año: mouredev pro.
# Un campus para la comunidad, que lanzaré en octubre, donde estudiar
# programación de una manera diferente.
# Cualquier persona suscrita a la newsletter de https://mouredev.pro
# accederá a sorteos mensuales de suscripciones, regalos y descuentos.
#  Desarrolla un programa que lea los registros de un fichero .csv y
# seleccione de manera aleatoria diferentes ganadores.
# Requisitos:
# 1. Crea un .csv con 3 columnas: id, email y status con valor "activo"
  #  o "inactivo" (y datos ficticios).
  #  Ejemplo: 1 | test@test.com | activo
            # 2 | test2@test.com | inactivo
  #  (El .csv no debe subirse como parte de la corrección)
# 2. Recupera los datos desde el programa y selecciona email aleatorios.
# Acciones:
# 1. Accede al fichero .csv y selecciona de manera aleatoria un email
  #  ganador de una suscripción, otro ganador de un descuento y un último
  #  ganador de un libro (sólo si tiene status "activo" y no está repetido).
# 2. Muestra los emails ganadores y su id.
# 3. Ten en cuenta que la primera fila (con el nombre de las columnas)
  #  no debe tenerse en cuenta.

import logging
import csv
import os
from random import choice, sample
from uuid import uuid4
from typing import Dict, List

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s:%(name)s:%(message)s")
logger = logging.getLogger("LoggerMouredev")

HEADERS = ["id", "email", "status"]
TOTAL_RECORDS = 10
TOTAL_WINNERS = 3
statuses = ["activo", "inactivo"]

def generate_email(id: str, domain: str):
  """Genera un correo electrónico basado en un ID y un dominio."""
  return f"test{id}@{domain}"

def generate_data(total_records: int) -> List[Dict[str, str]]:
  """Genera una lista de diccionarios con datos aleatorios.

    Args:
      total_records (int): Número total de registros a generar.

    Returns:
      List[Dict[str, str]]: Lista de registros generados.
    """
  
  data = []
  for _ in range(1, total_records + 1):
    staus = choice(statuses)
    id = str(uuid4())
    data.append({"id": id, "email": generate_email(id, "test.com"), "status": staus})
  return data


def create_csv_file(file_name: str, total_records: int, headers: List[str]):
  data = generate_data(total_records)

  with open(file_name, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)
  
def read_csv_file(file_name):
  if not os.path.exists(file_name):
    return []
  
  with open(file_name, "r", newline="") as file:
    reader = csv.DictReader(file)
    return [row for row in reader]

def get_random_winner(subscribers: List[Dict[str, str]]):
  if len(subscribers) < TOTAL_WINNERS:
    raise ValueError("No hay suficientes suscriptores para realizar el sorteo")
  
  active_subscribers = [s for s in subscribers if s['status'] == "activo"]

  if len(active_subscribers) < TOTAL_WINNERS:
    raise ValueError("No hay suficientes suscriptores 'activos' para realizar el sorteo")

  return sample(active_subscribers, TOTAL_WINNERS)

def select_winners(file_name):
  subscribers = read_csv_file(file_name)
  winners = get_random_winner(subscribers)
  prizes = ["Subscription", "Dicount", "Book"]

  if winners:
    for i, winner in enumerate(winners, start=0):
      print(f"{prizes[i]}: {winner['email']}")


if __name__ == "__main__":
  file_name = "data.csv"
  if not os.path.exists(file_name):
    create_csv_file(file_name, TOTAL_RECORDS, HEADERS)
  select_winners(file_name)