"""
  Logging

  Logging es un medio de rastrear los eventos que ocurren cuando se ejecuta algún software
  Un evento se describe mediante un mensaje descriptivo que puede contener opcionalmente datos variables (es decir, datos que son potencialmente diferentes para cada ocurrencia del evento).


"""

import logging
import time
from typing import Dict, Protocol

"""
  Por defecto la configuracion basica del logging solo muestra por consola
  los mensajes del nivel WARNING, ERROR y CRITICAL.

  Si queremos visualizar los mensajes por consola debemos agregar el nivel en la
  configuracion del loggin:
  Ejemplo:
  logging.basicConfig(level=logging.INFO) # Solo mostrar los mensaje desde el nivel
  INFO, WARNIGN, ERROR y CRITICAL
"""

# Configuración del logger
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s:%(name)s:%(message)s")
logger = logging.getLogger('Logger')

logger.debug("Esto es un mensaje DEBUG")
logger.info("Esto es un mensaje INFO")
logger.warning("Esto es un mensaje WARNIN")
logger.error("Esto es un mensaje ERROR")
logger.critical("Esto es un mensaje CRITICAL")

# Tipo de datos para las tareas
Tasks = Dict[str: str]

class Task:
  def __init__(self, name: str, description: str) -> None:
    self.name = name
    self.description = description

class TaskRepository(Protocol):
  def create_task(self, name:str, description: str) -> None:
    pass

  def remove_task(self, name:str) -> bool:
    pass

  def get_tasks(self) -> Tasks:
    pass


class InMemoryTaskRepository(TaskRepository):
  def __init__(self) -> None:
    self.tasks:Tasks = {}

  def create_task(self, name: str, description: str) -> None:
    self.tasks[name] = description

  def remove_task(self, name: str) -> bool:
    if name in self.tasks:
      del self.tasks[name]
      return True
    return False
  
  def get_tasks(self) -> Tasks:
    return self.tasks.copy()
    
class TaskManager:
  def __init__(self, respository: TaskRepository) -> None:
    self.respository = respository

  def create_task(self, name: str, description: str) -> None:
    start_time = time.time()
    self.respository.create_task(name, description)
    elapsed_time = (time.time() - start_time) * 1000
    logger.info(f"Tarea agregada: {name}: {description}. Timepo de ejecucion: {elapsed_time:.2f}ms")

  def remove_task(self, name: str) -> None:
    start_time = time.time()
    if self.respository.remove_task(name):
      elapsed_time = (time.time() - start_time) * 1000
      logger.info(f"Tarea eliminada: {name}. Tiempo de ejecucion {elapsed_time:.2f}ms")
    else:
      logger.warning(f"No se encontro la tarea: {name}")


class TaskUtils:
  def __init__(self, respository: TaskRepository) -> None:
    self.respository = respository

  def show(self) -> None:
    tasks = self.respository.get_tasks()
    if len(tasks) == 0:
      logger.warning("No hay tareas")
    for name, description in tasks.items():
      logger.info(f"Nombre: {name}, Descripcion: {description}")
