# como hacer peticiones a APIs con Python

# sin dependencias
import json
from pprint import pprint
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

api_todos = "https://jsonplaceholder.typicode.com/todos/1"

response = None
try:
    # hacer la solicutud
    response = urlopen("https://www.example.com")

    # leer la respuesta
    body = response.read()

    # decodificar la respuesta de bytes a texto
    data = body.decode("utf-8")  # data[:30]

    # si la respuesta es JSON intentamos parsearlo
    try:
        json_data = json.loads(data)
        print("Datos recibidos:", json_data)
    except json.JSONDecodeError:
        print("Respues no es JSON", data)
except URLError as e:
    print(f"Error URLError: {e.reason}")
except HTTPError as e:
    print(f"Error HTTP: {e.code} - {e.reason}")
except TimeoutError as e:
    print("Request timed out")
finally:
    if response is not None:
        response.close()

"""
NOTE: Una vez que se ha leido la respuesta ya no es posible volver a leerla
"""

with urlopen(api_todos) as response:
    body = response.read()

# explorando los headers
pprint(response.headers.items())

# recuperar un header
response.getheader("Server")
response.headers["Server"]

todo_item = json.loads(body)
print(todo_item)

"""
¿Qué pasa si quieres escribir el cuerpo de una respuesta en un archivo?, Tenemos 2 opciones:
1.- Escribe los bytes directamente en el archivo (sencillo)
2.- Decodificar los bytes en una cadena de Python y, a continuación, codificar la cadena de nuevo en un archivo (permite cambiar la codificacion)
"""
try:
    with urlopen(api_todos, timeout=10) as response:
        body = response.read()
except HTTPError as error:
    print(error.status, error.reason)
except URLError as error:
    print(error.reason)
except TimeoutError:
    print("Request timed out")

with open("example.html", "wb") as html_file:
    html_file.write(body)

# 2do ejemplo
with urlopen("https://www.google.com/") as response:
    body = response.read()

character_set = response.getheaders.get_content_charset()
print(character_set)  # 'ISO-8859-1'
content = body.decode(character_set)

with open("google.html", encoding="utf-8", mode="w") as file:
    file.write(content)
