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
  los mensajes del nivel DEBUG, INFO, WARNING, ERROR y CRITICAL.

  Si queremos visualizar los mensajes por consola debemos agregar el nivel en la
  configuracion del loggin:
  Ejemplo:
  logging.basicConfig(level=logging.INFO) # Solo mostrar los mensaje desde el nivel
  INFO, WARNIGN, ERROR y CRITICAL

  logger: Puede pensar en el registrador como un reportero en su código que decide qué grabar, 
  a qué nivel de detalle y dónde almacenar o enviar estos registros.

  Un logger que cree puede tener uno o más manejadores.
"""

# Configuración del logger y ajuste de nivel de registro
logger = logging.getLogger(
    __name__
)  # es buena practica pasar el __name__ como parametro de nombre

# creando un manejador
# nivel de registro NOTSET (Aún no está establecido)
console_handler = logging.StreamHandler()  # enviara los registros a la consola
file_handler = logging.FileHandler(
    "myapp.log", "a", "utf-8"
)  # escribira los registros en el archivo myapp.log

# format="%(levelname)s:%(name)s:%(message)s"
logging.basicConfig(
    filename="myapp.log",
    encoding="uft-8",
    filemode="a",  # append -> Agregar todos los registros al archivo y no sobrescribir los registros existentes.
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    style="%",
    datefmt="%Y-%m-%d %H:M",
)

# Agregar los handlers al logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# muestra en consola los handlers que usa el logger
print(logger.handlers)

# Asignando formato a los handlers
formartter = logging.Formatter(
    "{asctime} - {levelname} - {message}", style="{", datefmt="%Y-%m-%d %H:%M"
)
console_handler.setFormatter(formartter)
logger.warning("Stay calm!")

# Asignando un nivel de registro
console_handler.setLevel("DEBUG")
file_handler.setLevel("WARNING")

logger.debug("Esto es un mensaje DEBUG")
logger.info("Esto es un mensaje INFO")
logger.warning("Esto es un mensaje WARNIN")
logger.error("Esto es un mensaje ERROR")
logger.critical("Esto es un mensaje CRITICAL")

# Visializacion de datos variables
name = "Samara"
logger.debug(f"{name=}")  # iterpolacion de varialbe y su valor

donuts = 5
guests = 0

try:
    donuts_per_guest = donuts / guests
except ZeroDivisionError:
    # muestra un registro en el nivel de ERROR.
    logger.exception("DonutCalculationError")  # -> logging.error(exc_info=True)

# Tipo de datos para las tareas
Tasks = Dict[str:str]


class Task:
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description


class TaskRepository(Protocol):
    def create_task(self, name: str, description: str) -> None:
        pass

    def remove_task(self, name: str) -> bool:
        pass

    def get_tasks(self) -> Tasks:
        pass


class InMemoryTaskRepository(TaskRepository):
    def __init__(self) -> None:
        self.tasks: Tasks = {}

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
        logger.info(
            f"Tarea agregada: {name}: {description}. Timepo de ejecucion: {elapsed_time:.2f}ms"
        )

    def remove_task(self, name: str) -> None:
        start_time = time.time()
        if self.respository.remove_task(name):
            elapsed_time = (time.time() - start_time) * 1000
            logger.info(
                f"Tarea eliminada: {name}. Tiempo de ejecucion {elapsed_time:.2f}ms"
            )
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
