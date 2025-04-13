"""
---------------------- ¿Qué es el Patrón Strategy? ----------------------
El patrón Strategy permite definir una familia de algoritmos o comportamientos, encapsular cada uno de ellos 
y hacer que sean intercambiables. Así, un objeto puede elegir el algoritmo a utilizar en tiempo de ejecución sin 
tener que modificar su código base.


---------------------- ¿Cuándo usar el Patrón Strategy? ----------------------
El patrón Strategy es útil cuando:

1.- Tienes múltiples algoritmos o comportamientos para una operación y quieres poder elegir entre ellos en tiempo de ejecución.
2.- Necesitas cambiar el comportamiento de un objeto sin cambiar su clase.
3.- Cuando hay algoritmos similares que varían según los datos de entrada o las circunstancias, y deseas mantener 
el código limpio y fácil de extender.
4.- Estás buscando evitar condicionales complejos en el código, como if o switch, para decidir qué algoritmo usar.
"""

from abc import ABC, abstractmethod
from typing import Dict, List

"""
1.- Define una interfaz común para los algoritmos (Strategy): 
La interfaz común define el comportamiento que debe ser implementado por todas las estrategias posibles.
"""

"""
1.- Define una interfaz común para los algoritmos (Strategy): 
La interfaz común define el comportamiento que debe ser implementado por todas las estrategias posibles.
"""
class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self):
        pass

"""
2.- Implementa las clases concretas que representen cada estrategia: 
Cada clase concreta implementa un algoritmo específico, es decir, una forma diferente de realizar la tarea.
"""
class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List[int]) -> List[int]:
        return sorted(data)

class ConcreateStrategyB(Strategy):
    def do_algorithm(self, data: List[int]) -> List[int]:
        return sorted(data, reverse=True)
    

"""
3.- Crea el contexto (Context) que utiliza una estrategia: 
El contexto es la clase que usa el objeto Estrategia. 
El contexto no sabe cómo funciona el algoritmo, solo invoca el método ejecutar() de la estrategia.
"""
class Ctx:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self.strategy
    
    @strategy.setter
    def strategy(self, strategy: Strategy):
        self.strategy = strategy

    def do_some_bussiness_logic(self) -> Strategy:
        print("Context: Sorting data using the strategy (not sure how it'll do it)")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))


# strategy
class PayStrategy(ABC):
    @abstractmethod
    def procesar_pago(self, monto: float):
        pass

# estrategias concretas
class PayByCreditCard(PayStrategy):
    def procesar_pago(self, monto):
        print(f"Procesando pago con tarjeta de crédito por ${monto:.2f}.")

class PayByPayPal(PayStrategy):
    def __init__(self, password: str, email: str):
        self.password = password
        self.email = email
        self._signedIn = False  # Usamos _signedIn con "I" mayúscula
        self._data_base: Dict[str, str] = {
            "amanda1985": "amanda@ya.com",
            "qwerty": "jhon@amazon.mx"
        }

    def collect_payment_details(self):
        """Solicitar detalles de pago (email y contraseña) hasta que el usuario se loguee correctamente"""
        while not self._signedIn:  # Aquí usamos _signedIn con "I" mayúscula
            self.email = input("Enter the user's email: ")
            self.password = input("Enter your password: ")
            
            if self.is_verified():  # Llamamos al método correcto
                print("Data verification has been successful.")
            else:
                print("Wrong email or password!")

    @property
    def signed_in(self) -> bool:
        return self._signedIn  # Usamos _signedIn con "I" mayúscula

    @signed_in.setter
    def signed_in(self, value: bool):
        self._signedIn = value  # Usamos _signedIn con "I" mayúscula

    def procesar_pago(self, amount: float) -> bool:
        """Procesa el pago solo si el usuario está autenticado"""
        if self._signedIn:  # Usamos _signedIn con "I" mayúscula
            print(f"Paying {amount:.2f} using PayPal.")
            return True
        else:
            print("Unable to process payment. Please log in first.")
            return False

    def is_verified(self) -> bool:
        """Verificar si las credenciales son correctas"""
        if self._data_base.get(self.password) == self.email:  # Compara las credenciales
            self._signedIn = True  # Si es correcto, marcamos como autenticado
            return True
        return False


class PayByBankTransfer(PayStrategy):
    def procesar_pago(self, monto):
        print(f"Procesando pago con transferencia bancaria por ${monto:.2f}.")

# contexto
class ProcesadorPago:
    def __init__(self, strategy: PayStrategy):
        self.strategy = strategy

    @property
    def strategy(self) -> PayStrategy:
        return self.strategy
    
    @strategy.setter
    def strategy(self, strategy: PayStrategy):
        """Permite cambiar el método de pago dinámicamente."""
        self.strategy = strategy

    def procesar(self, monto: float):
        """Delegar el procesamiento del pago al método de pago actual."""
        self.metodo_pago.procesar_pago(monto)

if __name__ == "__main__":
    # Crear las estrategias de pago
    tarjeta_credito = PayByCreditCard()
    paypal = PayByPayPal()
    transferencia_bancaria = PayByBankTransfer()

    # Crear el procesador de pago con el método de pago inicial (tarjeta de crédito)
    procesador = ProcesadorPago(tarjeta_credito)
    # Procesar un pago con tarjeta de crédito
    procesador.procesar(100.0) # Procesando pago con tarjeta de crédito por $100.00.

    # Cambiar el método de pago a PayPal
    procesador.strategy(paypal)
    procesador.procesar(400.50)

    # cambiar el método de pago a transferencia bancaria
    procesador.strategy(transferencia_bancaria)
    procesador.procesar(3500.0)