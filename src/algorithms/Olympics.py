import logging
from dataclasses import dataclass
from typing import Dict, List

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s:%(name)s:%(message)s")
logger = logging.getLogger('Logger')

"""
  EJERCICIO:
  ¡Los JJOO de París 2024 han comenzado!
  Crea un programa que simule la celebración de los juegos.
  El programa debe permitir al usuario registrar eventos y participantes,
  realizar la simulación de los eventos asignando posiciones de manera aleatoria
  y generar un informe final. Todo ello por terminal.
  Requisitos:
  1. Registrar eventos deportivos.
  2. Registrar participantes por nombre y país.
  3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
  4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
  5. Mostrar los ganadores por cada evento.
  6. Mostrar el ranking de países según el número de medallas.
  Acciones:
  1. Registro de eventos.
  2. Registro de participantes.
  3. Simulación de eventos.
  4. Creación de informes.
  5. Salir del programa.

"""
@dataclass
class Participant:
  name: str
  country: str

class SportingEvent:
  def __init__(self, name: str) -> None:
    self.name = name
    self.participants: Dict[str: List[Participant]] = {} # {event1: [Participant(name, country), ...], event2: [Participant(name, country), ...], ...}
    self.results: Dict[str: List[Participant]] = {} # {event1: [{}, {}, {}], event2: [{}, {}, {}, {}]}

  def register_participant(self, participant: Participant):
    self.participants[self.name] = participant


class Olympic:
  def __init__(self) -> None:
    self.sportingEvents: Dict[str: SportingEvent] = {} # {event1: name}

  def create_sporting_event(self, name):
    newSportingEvent = SportingEvent(name)
    self.sportingEvents[name] = newSportingEvent

  def register_participant(self, event_name: str, participant: Participant) -> bool:
    event = self.sportingEvents.get(event_name)
    if event:
      event.register_participant(participant)
      logger.debug(f">>> ${event_name} - {participant}")
      return True
    else:
      logger.info(f"Evento {event} no encontrado")
      return False
      


olympics = Olympic()

sportingEvents = [
  olympics.create_sporting_event("300mtr Atletismo"),
  olympics.create_sporting_event("Natacion 500mtr libres"),
  olympics.create_sporting_event("Tiro con arco")
]

participants = {
  "Natacion 500mtr libres": [
    Participant("albert", "estados unidos"), 
    Participant("pablo", "mexico"), 
    Participant("tony", "inglaterra")
    ],
  "300mtr Atletismo": [
    Participant("morgan", "estados unidos"), 
    Participant("ana", "mexico"), 
    Participant("ashley", "inglaterra")
    ],
  "Tiro con arco": [
    Participant("elizabeth", "estados unidos"), 
    Participant("natalia", "mexico"), 
    Participant("sasha", "inglaterra")
    ]
}

for evet_name, participants_list in participants.items():
  for participant in participants_list:
    olympics.register_participant(evet_name, participant)

class OlympicUtils:
  def __init__(self) -> None:
    self.sportingEvents = {}
  
  def showSportingEvents(self) -> List[SportingEvent]:
    pass