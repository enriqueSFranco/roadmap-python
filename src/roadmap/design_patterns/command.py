"""
---------------------- Patrón Command ------------------------
- Es un patrón de diseño de comportamiento 
- Se usa para convertir una solicitud o acción en un objeto. 
- Permite separar al emisor de la acción de quien la recibe, lo que facilita el manejo de las solicitudes de manera flexible y extensible.


--------------------- ¿Qué hace el Patrón Command? -----------
Imagina que tienes un botón en una interfaz y, al presionar el botón, se realiza una acción 
(por ejemplo, encender una luz). El patrón Command convierte esa acción en un objeto que puede ser almacenado, ejecutado, 
deshecho o incluso revertido. Esto ayuda a encapsular la solicitud de la acción.


---------------------- ¿Cuándo usarlo? -----------------------
1.- Necesites desacoplar el emisor de la acción de la lógica que la ejecuta.
2.- Quieras tener comandos que puedan ser almacenados, cancelados o deshechos.
3.- Necesites enviar comandos a través de interfaces (como en sistemas distribuidos, o cuando un comando necesita ser transmitido por la red).
4.- Estés trabajando con listas de acciones que se ejecutan de manera secuencial o en ciertas condiciones, como en un deshacer/rehacer.

---------------------- Cómo Implementar -----------------------
1.- Declare la interfaz de comando con un único método de ejecución.
2.- Comience a extraer solicitudes en clases de comandos concretas que implementen la interfaz de comandos.
Cada clase debe tener un conjunto de campos para almacenar los argumentos de solicitud junto con una referencia al objeto receptor real.
Todos estos valores deben inicializarse a través del constructor de comandos.

3.- Identificar las clases que actuarán como remitentes. Agregue los campos para almacenar comandos en estas clases.
Los remitentes deben comunicarse con sus comandos solo a través de la interfaz de comandos. Los remitentes generalmente
no crean objetos de comando por su cuenta, sino que los obtienen del código del cliente.

4.- Cambie los remitentes para que ejecuten el comando en lugar de enviar una solicitud al receptor directamente.

5.- El cliente debe inicializar objetos en el siguiente orden:
    - Crear receptores.
    - Cree comandos y asociarlos con receptores si es necesario.
    - Cree remitentes y asociarlos con comandos específicos.


-------------------- Tips para implementar el patrón Command de forma elegante -----------------------
1.- Uso de parámetros en los comandos: Si el comando necesita parámetros, puedes pasarlos en el momento de la creación 
del comando, como lo hicimos con la luz en el ejemplo anterior.

2.- Comandos desechables o repetibles: Puedes almacenar los comandos en una lista o cola si necesitas realizar 
operaciones como deshacer o rehacer. Por ejemplo, un sistema de edición de texto puede almacenar los comandos 
de acción y deshacerlos cuando sea necesario.

3.- Comandos compuestos: Si tienes acciones complejas que deben realizarse secuencialmente, puedes componer comandos
(tener un comando que ejecute otros comandos). Esto se puede hacer agregando un comando "Composite" que ejecute otros comandos.

4.- Extensibilidad: El patrón Command es fácil de extender. Si necesitas agregar nuevas acciones, solo tienes que crear nuevos
comandos que implementen la interfaz Command, sin tener que modificar las clases existentes. Esto sigue el principio de 
abierto/cerrado (abierto para extensión, cerrado para modificación).
"""

from __future__ import annotations
from abc import ABC, abstractmethod


# Comando base para las acciones sobre las tareas
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Modelo de tarea
class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False

    def complete(self):
        self.completed = True
        print(f"Tarea '{self.name}' completada.")

    def delete(self):
        print(f"Tarea '{self.name}' eliminada.")

# Comandos para las acciones sobre las tareas
class CompleteTaskCommand(Command):
    def __init__(self, task):
        self.task = task

    def execute(self):
        self.task.complete()

    def undo(self):
        print(f"Deshaciendo la tarea '{self.task.name}' como completada.")

class DeleteTaskCommand(Command):
    def __init__(self, task):
        self.task = task

    def execute(self):
        self.task.delete()

    def undo(self):
        print(f"Deshaciendo la eliminación de la tarea '{self.task.name}'.")

# Invocador: El gestor de tareas
class TaskManager:
    def __init__(self):
        self.history = []

    def execute_command(self, command):
        command.execute()
        self.history.append(command)

    def undo_last_command(self):
        if self.history:
            command = self.history.pop()
            command.undo()

# Crear tareas
task1 = Task("Comprar leche")
task2 = Task("Hacer ejercicio")

# Crear comandos
complete_task1 = CompleteTaskCommand(task1)
delete_task2 = DeleteTaskCommand(task2)

# Crear el gestor de tareas
task_manager = TaskManager()

# Ejecutar comandos
task_manager.execute_command(complete_task1)  # Completa la tarea "Comprar leche"
task_manager.execute_command(delete_task2)    # Elimina la tarea "Hacer ejercicio"

# Deshacer las últimas acciones
task_manager.undo_last_command()  # Deshace la eliminación de la tarea
task_manager.undo_last_command()  # Deshace la tarea completada


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        ...

    @abstractmethod
    def undo(self) -> None:
        ...

class TextEditor:
    def __init__(self):
        self.text = ""
        self.history = []

    def write(self, text: str) -> None:
        self.text += text
        print(f"Texto actual: {self.text}")

    def delete(self) -> None:
        print(f"Texto antes de borrar: {self.text}")
        self.text = ""
        print(f"Texto actual: {self.text}")
    
    def format_text(self, style) -> None:
        print(f"Formateando texto con estilo: {style}")
        self.text = f"[{style}] {self.text}"
        print(f"Texto formateado: {self.text}")

    def save_state(self) -> None:
        self.history.append(self.text)
    
    def restore_state(self) -> None:
        if self.history:
            self.history.pop()
            print(f"Texto después de deshacer: {self.text}")
        else:
            print("No hay nada para deshacer.")


class WriteCommand(Command):
    def __init__(self, editor: TextEditor, text: str) -> None:
        self.editor = editor
        self.text = text

    def execute(self):
        self.editor.save_state()
        self.editor.write(self.text)

    def undo(self):
        self.editor.restore_state()


class DeleteCommand(Command):
    def __init__(self, editor: TextEditor) -> None:
        self.editor = editor

    def execute(self):
        self.editor.save_state()
        self.editor.delete()

    def undo(self):
        self.editor.restore_state()



class Button:
    def __init__(self, command: Command):
        self.command = command

    def press(self):
        self.command.execute()

    def undo(self):
        self.command.undo()


"""
1.- Crea una interfaz Command: Define una interfaz que todos los comandos deben implementar. 
Esta interfaz tiene un método execute(), que es donde se define la acción a ejecutar.
"""
class Command(ABC):
    """
    The Command interface declares a method for executing a command.
    """

    @abstractmethod
    def execute(self) -> None: ...


"""
2.- Crea clases concretas que implementen la interfaz Command: Cada clase concreta representará un comando específico.
En el método execute(), implementas lo que se debe hacer cuando se invoca el comando.
"""
class SimpleCommand(Command):
    """
    Some commands can implement simple operations on their own.
    """

    def __init__(self, payload: str) -> None:
        self.payload = payload

    def execute(self):
        print(
            f"SimpleCommand: See, I can do simple things like printing({self._payload})"
        )


class ComplexCommand(Command):
    """
    However, some commands can delegate more complex operations to other
    objects, called "receivers."
    """
    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        """
        Complex commands can accept one or several receiver objects along with
        any context data via the constructor.
        """
        self.receiver = receiver
        self._a = a
        self._b = b

    
    def execute(self) -> None:
        """
        Commands can delegate to any methods of a receiver.
        """
        print("ComplexCommand: Complex stuff should be done by a receiver object", end="")
        self.receiver.do_something(self._a)
        self.receiver.do_something_else(self._b)



"""
3.- Define el receptor (Receiver): El receptor es la clase que realiza la acción real.
El comando solo lo invoca, pero no sabe cómo se realiza la acción, esa responsabilidad la tiene el receptor.
"""
class Receiver():
    """
    The Receiver classes contain some important business logic. They know how to
    perform all kinds of operations, associated with carrying out a request. In
    fact, any class may serve as a Receiver.
    """
    def do_somethig(self, a: str) -> None:
        print(f"\nReceiver: Working on ({a}.)", end="")
    
    def do_something_else(self, b:str) -> None:
        print(f"\nReceiver: Also working on ({b}.)", end="")

"""
4.- Crea el objeto invocador (Invoker): El invocador es quien solicita la ejecución del comando.
No sabe qué comando específico está ejecutando, solo invoca el método execute().
"""
class Invoker:
    """
    The Invoker is associated with one or several commands. It sends a request
    to the command.
    """
    _on_start = None
    _on_finish = None

    """
    Initialize commands.
    """
    def set_on_start(self, command: Command) -> None:
        self._on_start = command

    def set_on_finish(self, command: Command) -> None:
        self._on_finish = command

    def do_something_important(self) -> None:
        """
        The Invoker does not depend on concrete command or receiver classes. The
        Invoker passes a request to a receiver indirectly, by executing a
        command.
        """
        print("Invoker: Does anybody want something done before I begin?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...doing something really important...")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


"""
5.- Usa los objetos en el cliente: En el cliente, se crea una instancia de los comandos y se pasa al invocador.
"""
if __name__ == "__main__":
    """
    The client code can parameterize an invoker with any commands.
    """
    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("say hi"))
    
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(receiver, "Send email", "Save report"))

    invoker.do_something_important()