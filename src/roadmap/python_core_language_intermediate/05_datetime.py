from datetime import date, datetime, time, timedelta, timezone

from dateutil import parser, tz  # descargar con python3 pip -m pyhton-dateutil

# El módulo datetime es el que se usa para trabajar con fechas y horas en Python.

"""
datetime: Para manejar fechas y horas (fecha + hora).
date: Para manejar solo fechas (año, mes, día).
time: Para manejar solo tiempos (hora, minuto, segundo, microsegundo).
timedelta: Para manejar diferencias de tiempo entre fechas u horas.
timezone: Para trabajar con zonas horarias.
"""

fecha_hora_actual = datetime(
    year=2025,
    month=2,
    day=28,
)
print(fecha_hora_actual.year)  # Año
print(fecha_hora_actual.month)  # Mes
print(fecha_hora_actual.day)  # Día
print(fecha_hora_actual.hour)  # Hora

# Solo la fecha
fecha = date(2025, 2, 28)
fecha_actual = date.today()
print(fecha_actual)

# solo la hora
hora = time(15, 45, 30)
# obtener la hora actual con datetime.now() y luego extraer solo la parte de la hora usando .time()
hora_actual = datetime.now().time()
print(hora_actual)

# timedelta: representar una diferencia entre dos fechas o tiempos
delta = timedelta(days=5, hours=3, minutes=30)
print(delta)

# operaciones con timedelta
fecha_hora = datetime.now()
# suma
nueva_fecha = fecha_hora + delta
print(nueva_fecha)

# resta
fecha_pasada = fecha_hora - delta
print(fecha_pasada)

diferencia = datetime(2025, 3, 5) - datetime(2025, 2, 28)
print(diferencia)  # Muestra la diferencia en días

# total de segundos
print(delta.total_seconds())  # Devuelve el total en segundos

# Formato de fecha y hora
# strftime() (para convertir un datetime en una cadena de texto)
fecha_hora_formateada = fecha_hora.strftime("%d/%m/%Y %H:%M:%S")
print(fecha_hora_formateada)  # Salida: 28/02/2025 15:45:30

# strptime() (para convertir una cadena en un objeto datetime)
cadena_fecha = "28/02/2025 15:45:30"
fecha_hora = datetime.strptime(cadena_fecha, "%d/%m/%Y %H:%M:%S")
print(fecha_hora)


# Zonas horarias con timezone
# Crear una zona horaria UTC-3
zona_horaria = timezone(timedelta(hours=-3))

# Crear un datetime con esa zona horaria
fecha_hora_con_zona = datetime(2025, 2, 28, 15, 45, 30, tzinfo=zona_horaria)
print(fecha_hora_con_zona)

London_tz = tz.gettz("Europe/London")
# now = datetime.now(tz=London_tz)
"""
Establecer la zona horaria de datetime.now() a la zona horaria UTC datetime.now(tz=tz.UTC)
Este método se recomienda sobre el uso utcnow()
"""
now = datetime.now(tz=tz.UTC)
print(now)

PYCON_DATE = parser.parser("May 12, 2025 8:00 AM")
PYCON_DATE = PYCON_DATE.replace(tzinfo=tz.gettz("America/New_York"))
now = datetime.now(tz=tz.tzlocal())

countdown = PYCON_DATE - now
print(countdown)
print(f"Countdown to PyCon US 2025: {countdown}")


# Haciendo Aritmética con Python datetime
"""
la instancia timedelta admiten suma y resta, así como enteros positivos y negativos para todos los argumentos.
"""
now = datetime.now()
tomorrow = timedelta(days=+1)
print(tomorrow + now)
# agrega tres días y resta cuatro horas
delta = timedelta(
    days=+3, hours=-4
)  # 2025-03-03 06:04:35.817000 | hora y fecha actual: fri 28 feb 10:05 am

"""
Calcular el final de un mes: Si quieres obtener el último día de un mes, puedes usar una combinación de timedelta y el siguiente mes, ajustando al primer día del mes siguiente.
Conversión entre diferentes tipos: Puedes convertir entre date, time y datetime usando los métodos .date(), .time() y .combine().
Trabajar con intervalos de fechas: Si necesitas crear fechas recurrentes, por ejemplo, para cada día o cada mes, puedes utilizar ciclos for junto con timedelta para crear rangos.
"""
