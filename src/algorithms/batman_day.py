# EJERCICIO:
# Cada año se celebra el Batman Day durante la tercera semana de septiembre...
# ¡Y este año cumple 85 años! Te propongo un reto doble:
#
# RETO 1:
# Crea un programa que calcule cuándo se va a celebrar el Batman Day hasta
# su 100 aniversario.
#

from datetime import date, timedelta
from typing import Dict

def third_saturday_september(year: int):
  first_day = date(year, 9, 1) # primer dia de septiembre
  first_saturday = first_day + timedelta(days=(5 - first_day.weekday()) % 7)
  third_saturday = first_saturday + timedelta(days=14)
  return third_saturday

def batman_day(start_year: int, end_year) -> Dict[int, str]:
  dates: Dict[int, str] = {}
  for year in range(start_year, end_year + 1):
    batman_date = third_saturday_september(year)
    dates[year] = batman_date.strftime("%d/%m/%Y")
  return dates

def batman_anniversary(anniversary: int = 1):
  base_year = 1939
  year = base_year + anniversary
  batman_date = third_saturday_september(year)
  return batman_date.strftime("%d/%m/%Y")

start_year = 2024  # 85th anniversary
end_year = 2029    # 90th anniversary (100 years of Batman)
batman_day_dates = batman_day(start_year, end_year)

for year, date_str in batman_day_dates.items():
  print(f"Batman Day on {date_str} ({year})")

anniversary = 100  # Change this number for the desired anniversary
anniversary_date = batman_anniversary(anniversary)
print(f"The {anniversary}th anniversary of Batman will be on: {anniversary_date}")

# RETO 2:
# Crea un programa que implemente el sistema de seguridad de la Batcueva.
# Este sistema está diseñado para monitorear múltiples sensores distribuidos
# por Gotham, detectar intrusos y activar respuestas automatizadas.
# Cada sensor reporta su estado en tiempo real, y Batman necesita un programa
# que procese estos datos para tomar decisiones estratégicas.
# Requisitos:
# - El mapa de Gotham y los sensores se representa con una cuadrícula 20x20.
# - Cada sensor se identifica con una coordenada (x, y) y un nivel
#  de amenaza entre 0 a 10 (número entero).
# - Batman debe concentrar recursos en el área más crítica de Gotham.
# - Input: El programa recibe un listado de tuplas representando coordenadas de los
#  sensores y su nivel de amenaza. El umbral de activación del protocolo de
#  seguridad es 20 (sumatorio de amenazas en una cuadrícula 3x3).
# Acciones:
# - Identifica el área con mayor concentración de amenazas
#  (sumatorio de amenazas en una cuadrícula 3x3).
# - Si el sumatorio de amenazas es mayor al umbral, activa el
#  protocolo de seguridad.
# - Calcula la distancia desde la Batcueva, situada en (0, 0). La distancia es
#  la suma absoluta de las coordenadas al centro de la cuadrícula amenazada.
# - Muestra la coordenada al centro de la cuadrícula más amenazada, la suma de
#  sus amenazas, la distancia a la Batcueva y si se debe activar el
#  protocolo de seguridad.