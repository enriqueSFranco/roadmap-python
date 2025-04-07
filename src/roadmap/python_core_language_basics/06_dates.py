import logging
from datetime import datetime, date, timedelta
from typing import Dict

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('LoggerDate')

now = datetime.now()

# logger.info(now)
# logger.info(now.year)
# logger.info(now.month)
# logger.info(now.day)
# logger.info(now.hour)
# logger.info(now.minute)
# logger.info(now.second)


# diferencia entre fechas y tiempos
# Permite realizar operaciones como sumar o restar días, horas, minutos, y segundos de un objeto datetime.
timestamp = now.timestamp()
# logger.info(timestamp)