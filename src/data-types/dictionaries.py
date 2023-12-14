# diccionarios

"""
  Las claves pueden ser de cualquier tipo inmutable, como cadenas, números y tuplas. 
  Los valores pueden ser de cualquier tipo de datos, incluidos números, cadenas, listas, tuplas y hasta otros diccionarios.
"""
super_hero = {
  "name": "spider-man",
  "age": 15,
  "power": "Super strength",
  "secret-identity": "peter parker"
}
print(super_hero)

student = {
  "name": "kike",
  "age": 18,
  "notes": [10, 9, 8]
}
print(student)

countries = {
  "Mexico": "CDMX",
  "Argentina": "Buenos Aires",
  "Colombia": "Bogotá"
}
print(countries)

"""
  Modificar un Diccionario en Python
"""
scort_karely = {
  "name": "vendedora de caricias",
  "price": 1500
}
print(scort_karely)
scort_karely["price"] = 300000
print(scort_karely)


"""
No se permiten duplicados en los diccionarios
Cada clave en un diccionario debe ser única. No se permite tener dos elementos con la misma clave en un diccionario. 
Sin embargo, los valores pueden ser duplicados.
"""
colors = {
  "rojo": "#FF0000",
  "verde": "#00FF00",
  "rojo": "#FF3333"  # La clave "rojo" ya existe, se reemplazará
}
print(colors)

"""Longitud del diccionario en Python"""
team = {
  "player_one": "alice",
  "player_two": "bob",
  "player_three": "carol"
}

total_players = len(team)
print("Total de judadores: {}".format(total_players))

"""Elementos del diccionario - Tipos de datos"""
movie = {
  "title": "Avengers End Game",
  "year": "2019",
  "gender": ["science fiction", "action"],
  "actors": ["Robert Downey Jr", "Chris Evans", "Mark Ruffalo", "Chris Hemsworth", "Scarlett Johansson"]
}

print(movie)
if type(movie) == dict:
  print("Los datos provienen de un diccionario")
