from abc import ABC, abstractmethod

"""
    Interface Segregation Principle (ISP)
    "Los clientes no deben verse obligados a depender de interfaces que no utilizan."

    Esto significa que en lugar de tener una interfaz grande y monolítica con un montón de métodos (algunos de los cuales una clase puede no necesitar), debes dividir esa interfaz en interfaces más pequeñas y específicas, de modo que las clases solo implementen los métodos que realmente necesitan.


    El Principio de Segregación de Interfaces (ISP) se basa en la idea de que las interfaces deben ser específicas y enfocadas. Esto evita que las clases estén obligadas a implementar métodos que no utilizan, lo que ayuda a:

    Reducir el acoplamiento entre las clases.
    Mejorar la mantenibilidad y la extensibilidad.
    Asegurar que las clases solo dependen de lo que realmente necesitan.
"""

"""
	Sin usar el principio ISP
	Si tienes una clase de notificación por correo electrónico, en realidad no necesitas los métodos de SMS y notificaciones push, pero tienes que implementarlos de todos modos. Esto viola ISP.
"""


class Notifier:
    def send_email(self, message):
        raise NotImplementedError()


def send_sms(self, message):
    raise NotImplementedError()


def send_push_notification(self, message):
    raise NotImplementedError()


"""
	Solución con ISP
	En lugar de una interfaz única, dividimos la interfaz en interfaces más pequeñas y específicas:
"""


class EmailNotifier(ABC):
    @abstractmethod
    def send_email(self, message):
        pass


class SMSNotifier(ABC):
    @abstractmethod
    def send_sms(self, message):
        pass


class PushNotifier(ABC):
    @abstractmethod
    def sed_push_notification(self, message):
        pass


class EmailNotificationService(EmailNotifier):
    def send_email(self, message):
        print(f"Sending email: {message}")


class SMSNotificationService(SMSNotifier):
    def send_sms(self, message):
        print(f"Sending SMS: {message}")


class PushNotificationService(PushNotifier):
    def send_push_notification(self, message):
        print(f"Sending push notification: {message}")
