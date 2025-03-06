"""
    Tuplas
  - permiten crear secuencias inmutables de valores
  - Los valores o elementos de una tupla pueden ser de cualquier tipo
"""

record = ("Jhon", 35, "Python Delveloper",) # tupla literal
print(record) # ('Jhon', 35, 'Python Delveloper')
print(record[0]) # Jhon

"""
  Construyendo tuplas de forma literal
"""
point = (2, 7,)
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday",)
print(days[::2]) # avanza en la tupla de 2 en 2

"""
  Construyendo tuplas con el constructor tuple()
  El tuple() constructor es útil cuando necesita crear una tupla de un iterador objeto
"""
pythonista = tuple("pythonista",)
vehicle = tuple({
  "manufacture": "Boeing",
  "model": "747",
  "passengers": 416,
}.values())

print(pythonista)

employee = (
  "Jhon",
  35,
  "Python Developer",
  ("Django", "Flask", "FastAPI", "CSS", "HTML"),
)

print(employee)

"""
Explorando la Inmutabilidad de Tuple
"""
jane = ("Jane Doe", 25, 1.75, "Canada",)
# jane[3] = "Mexico City" # TypeError: 'tuple' object does not support item assignment

student_info = ("Linda", 18, ["Math", "Physics", "History"])
student_info[2][2] = "Programming"
student_info[2].append("History")
print(student_info)

student_coruses = {
  ("Jhon", "Doe"): ["Physics", "Chemistry"],
  ("Linda", "Doe"): ["English", "History"],
}

print(student_coruses[("Jhon", "Doe")])

"""
  Desempaquetado Tuples
  En el desempaquetado regular, el número de variables debe coincidir con el número de valores a desempaquetar.
"""
point_z = (3,4,12)
x, y, z = point_z
print(x, y, z)

name, age, courses = student_info
print(name, age, courses)
first_day, *middle_days, last_day = days
print(first_day, middle_days, last_day)

name = ("Jhon", "Doe")
contact = ("john@example.com", "55-555-5555")
print((*name, *contact))