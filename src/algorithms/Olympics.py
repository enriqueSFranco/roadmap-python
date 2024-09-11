import logging
import random
from enum import Enum
from dataclasses import dataclass
from typing import Dict, List

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s:%(name)s:%(message)s")
logger = logging.getLogger('OlympicLogger')

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
MINUMUM_PARTICIPANTS = 3
MEDAL_EMOJIS = {
  "Gold": "🥇",
  "Silver": "🥈",
  "Bronze": "🥉"
}

class Medal(Enum):
  GOLD = "Gold"
  SILVER = "Silver"
  BRONZE = "Bronze"

@dataclass
class Participant:
  name: str
  country: str

class SportingEvent:
  def __init__(self, name: str) -> None:
    self.name = name
    self.participants: List[Participant] = []
    self.results: Dict[Medal: Participant] = {}

  def register_participant(self, participant: Participant):
    self.participants.append(participant)

  def simulate_sporting_event(self) -> None:
    if len(self.participants) < MINUMUM_PARTICIPANTS:
      logger.warning("No hay suficientes participantes para iniciar el evento.")
      return
    
    shuflee_participants = random.sample(self.participants, len(self.participants))

    self.results = {
      Medal.GOLD: shuflee_participants[0],
      Medal.SILVER: shuflee_participants[1],
      Medal.BRONZE: shuflee_participants[2]
    }

class SportingEventFactory:
  @staticmethod
  def create_event(name: str) -> SportingEvent:
    return SportingEvent(name)

class Olympic:
  def __init__(self) -> None:
    self.sporting_events: Dict[str: SportingEvent] = {} # {event1: SportingEvent(name, participants, results)}

  def create_sporting_event(self, name) -> None:
    self.sporting_events[name] = SportingEventFactory.create_event(name)

  def register_participant(self, event_name: str, participant: Participant) -> bool:
    event = self.sporting_events.get(event_name)
    if event:
      event.register_participant(participant)
      logger.debug(f"Added {participant} to {event_name}")
      return True
    else:
      logger.info(f"Evento '{event_name}' no encontrado")
      return False

  def run_all_events(self) -> None:
    for event in self.sporting_events.values():
      event.simulate_sporting_event()

  def generate_report(self) -> None:
    logger.info("🗒️ CREAR REPORTE")

    # TODO: Mostrar ganadores por cada evento
    logger.info("RESULTADOS POR EVENTO 💪")
    for event in self.sporting_events.values():
      logger.info(f"Evento: {event.name}")
      for medal, participant in event.results.items():
        logger.info(f"{MEDAL_EMOJIS[medal.value]} {participant.name} ({participant.country})")

    # TODO: Mostrar ranking de paises
    logger.info("RANKING POR PAISES 🌎")
    country_medals: Dict[str, Dict[str, int]] = self._calculate_medal_count()
    sorted_contries = sorted(country_medals.items(), key=lambda x: (-sum(x[1].values()), x[0]))

    for country, medals in sorted_contries:
      logger.info(f"{country}: Gold: {medals[Medal.GOLD]}, Silver: {medals[Medal.SILVER]}, Bronze: {medals[Medal.BRONZE]}")

  def _calculate_medal_count(self) -> Dict[str, Dict[str, int]]:
    medals_count: Dict[str, Dict[str, int]] = {}
    for event in self.sporting_events.values():
      for medal, participant in event.results.items():
        country = participant.country
        if country not in medals_count:
          medals_count[country] = {Medal.GOLD: 0, Medal.SILVER: 0, Medal.BRONZE: 0}
        medals_count[country][medal] += 1
    return medals_count

if __name__ == "__main__":
  olympics = Olympic()
  olympics.create_sporting_event("300mtr Atletismo"),
  olympics.create_sporting_event("Natacion 500mtr libres"),
  olympics.create_sporting_event("Tiro con arco")

  participants = {
    "Natacion 500mtr libres": [
      Participant("albert", "🇺🇸 Estados Unidos"), 
      Participant("pablo", "🇲🇽 Mexico"), 
      Participant("tony", "🇬🇧 Gran Bretaña"),
      Participant("john", "🇨🇦 Canada"), 
      Participant("lisa", "🇫🇷 Francia"), 
      Participant("hiro", "🇯🇵 Japon")
    ],
    "300mtr Atletismo": [
      Participant("morgan", "🇺🇸 Estados Unidos"), 
      Participant("ana", "🇲🇽 Mexico"), 
      Participant("ashley", "🇬🇧 Gran Bretaña"),
      Participant("maria", "🇩🇪 Alemania"), 
      Participant("amanda", "🇮🇹 italia")
    ],
    "Tiro con arco": [
      Participant("elizabeth", "🇺🇸 Estados Unidos"), 
      Participant("natalia", "🇲🇽 Mexico"), 
      Participant("sasha", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglaterra"),
      Participant("maria", "🇩🇪 Alemania"), 
      Participant("amanda", "🇵🇹 Portugal"),
      Participant("sofia", "🇲🇽 Mexico"), 
      Participant("olga", "🇨🇴 Colombia")
    ]
  }

  for evet_name, participants_list in participants.items():
    for participant in participants_list:
      olympics.register_participant(evet_name, participant)

  olympics.run_all_events()
  olympics.generate_report()
