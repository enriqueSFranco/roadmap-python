# como hacer peticiones a APIs con Python

# sin dependencias
import json
from urllib.request import urlopen

api_users = "https://jsonplaceholder.typicode.com/todos/1"

with urlopen(api_users) as response:
    body = response.read()

todo_item = json.loads(body)
print(todo_item)
