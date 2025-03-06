from string import ascii_letters

"""
sintaxis
{key: value for member in iterable [if condition]} -> dict
"""

power_of_two = {i: 2**i for i in range(1, 11)}
"""
power_of_two = {}
for i in range(1,11):
	power_of_two[i]: 2**i
"""

cities = ["mexico", "argentina", "italia", "alemania", "rusia", "estados unidos"]
{c: len(c) for c in cities}

matrix = [
    [9, 3, 8, 3],
    [4, 5, 2, 8],
    [6, 4, 3, 1],
    [1, 0, 4, 5],
]
# Las compresiones también pueden tener más de un for
{value: value**2 for row in matrix for value in row}

# creando un dict a partir de una lista
fruits = ["apple", "banana", "cherry"]
fruits_dict = {fruit.upper(): len(fruit) for fruit in fruits}

# genera un dict con letras minusculas como claves y su valor en ascii como value
{letter: ord(letter) for letter in ascii_letters}

parts = [
    "CPU",
    "GPU",
    "Motherboard",
    "RAM",
    "SSD",
    "Power Supply",
    "Case",
    "Cooling Fan",
]
part_costs = [250, 500, 150, 80, 100, 120, 70, 25]
stocks = [15, 8, 12, 30, 25, 10, 5, 20]
{part: stock * cost for part, stock, cost in zip(parts, stocks, part_costs)}
"""
# no hace ninguna transformacion a los datos
dict(zip(parts, stocks))

stock_map = {}
for i in range(0, len(parts)):
	stock_map[parts[i]] = stocks[i]
"""

parts_with_cost = {
    "CPU": 10021,
    "GPU": 10022,
    "Motherboard": 10023,
    "RAM": 10024,
    "SSD": 10025,
    "Power Supply": 10027,
    "Case": 10026,
    "Cooling Fan": 10025,
}

# transformando diccionarios existentes
{value: key for key, value in parts_with_cost.items()}

# se tiene un diccionario de frutas y sus precios, y necesita disminuir los precios en un 5%.
# Puedes hacer esto con una comprensión:
fruits = {
    "apple": 1.00,
    "banana": 0.50,
    "cherry": 2.00,
}
fruits_with_dicount = {fruit: round(cost * 0.95, 2) for fruit, cost in fruits.items()}

# filtra un diccionario de números por sus valores para crear un diccionario de números pares
numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
even_numbers = {key: value for key, value in numbers.items() if value % 2 == 0}

# filtrar un diccionario por teclas, diga que tiene un diccionario que asigna códigos postales a
# las ciudades, y necesita filtrar el diccionario para obtener las ciudades en un rango de códigos postales:
codes = {
    "1001": "Townsville",
    "1002": "Lakeview",
    "1003": "Mountainview",
    "1101": "Riverside",
    "1102": "Hilltop",
    "1201": "Greenfield",
    "1202": "Sunnydale",
    "1301": "Meadowbrook",
    "1302": "Creekwood",
}
filtered_codes = {
    code: town for code, town in codes.items() if "1100" <= code <= "1300"
}
