"""
FUNCTIONAL PROGRAMMING IN PYTHON: WHEN AND HOW TO USE IT

"""

# el objeto creado por la lambda es un ciudadano de primera clase
my_reverse = lambda s: s[::-1]
print(my_reverse("I am a string"))
lambda s: s[::-1]("I am a string")

animals = ["ferret", "vole", "dog", "gecko"]
sorted(animals, key=lambda s: -len(s))

# MAP
animals2 = animals = ["cat", "dog", "hedgehog", "gecko"]
iterator = map(lambda s: s[::-1], animals)
for animal in iterator:
    print(animal)

nums = 12345
# Esto daria un error por el 'float' ya que no es subscriptable, no se puede aplicar el slicing
iterator = map(lambda s: s[::-1], ["cat", "dog", 3.1416, "hedgehog", "gecko"])
result = list(
    map(
        lambda input: input if type(input) != "str" else None,
        ["cat", "dog", 3.1416, "hedgehog", "gecko"],
    )
)

numbers = [1, 2, 3, 4, 5, 6]
# la funcion str se aplica a cada objeto de la lista
map(str, numbers)
