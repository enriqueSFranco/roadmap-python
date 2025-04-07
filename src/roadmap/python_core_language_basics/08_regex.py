""" Las expresiones regulares son una secuencia de caracteres que forman un patrón de búsqueda.
    Se utilizan para la búsqueda de cadenas de texto, validación de datos, etc. """

""" ¿Por qué aprender Regex?

- Búsqueda avanzada: Encontrar patrones específicos en textos grandes de forma rápida y precisa. (un editor de Markdown sólo usando Regex)

- Validación de datos: Asegurarte que los datos que ingresa un usuario como el email, teléfono, etc. son correctos.

- Manipulación del texto: Extraer, reemplazar y modificar partes de la cadena de texto fácilmente
"""
# 1.- importar el modulo de expresiones regulares "re"
import re

# 2.- crear un patron, que es una cadena de texto que describe lo que queremos buscar
pattern = "Hola"
# 3.- el texto donde queremos buscar
text = "Hola mundo"
# 4.- usar la funcion re
result = re.search(pattern, text)

if result:
    print(f"se ha encontrado el patron en el texto {text}")
else:
    print(f"no se encontro el patron en el texto {text}")

# devuelve la cadena que coincide con el pattern
result.group()
# devuelve la posicion incial de la coincidencia
result.start()
# devuelve la posicion final de la coincidencia
result.end()

# EJERCICIO 01
# Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto
# e indica en que posición empieza y termina la coincidencia.
text2 = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado"
pattern = "IA"
founf_ia = re.search(pattern, text)
start_index = founf_ia.start()
end_index = founf_ia.end()
print(f"start index: {start_index}, end index: {end_index}")

### encontrar todas las coincidencias de un patron
# .findall() devuelve una lista con todas las coincidencias
text3 = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
found_python = "Python"
matches = re.findall(pattern, text3)

# iter() devuelve un iterador que contiene todos los resultados de la búsqueda
matches_with_iter = re.finditer(pattern, text3)
for match in matches:
    print(match.group(), match.start(), match.end())

# EJERCICIO 02
# Encuentra todas las ocurrencias de la palabra "midu" en el siguiente texto e indica en que posición empieza y termina cada coincidencia y cuantas veces se encontró.
text = "Este es el curso de Python de midudev. ¡Suscríbete a midudev si te gusta este contenido! midu"
find_midu = "midu"
matches_of_midu = re.finditer(pattern, text)
for match in matches_of_midu:
    print(match.group(), match.start(), match.end())


### Modificadores

# Los modificadores son opciones que se pueden agregar a un patrón para cambiar su comportamiento

# re.IGNORECASE: Ignora las mayúsculas y minúsculas

text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero la ia no es tan mala. ¡Viva la Ia!"
pattern = "IA"
found_ia = re.findall(pattern, text, re.IGNORECASE)


### Reemplazar el texto

# .sub() reemplaza todas las coincidencias de un patrón en un texto
text = "Hola, mundo! Hola de nuevo. Hola otra vez."
pattern = "hola"
replacement = "Adiós"

new_text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
print(text)

###
# 02 - Meta caracteres
# Los metacaracteres son simbolos especiales con significados especificos en las expresiones regulares
###


# 1. El punto (.)
# Coincidir con cualquier caracter excepto una nueva linea

text = "Hola mundo, H0la de nuevo, H$la otra vez"
pattern = r"H.la"  # Hola, H0la, H$la

found = re.findall(pattern, text)

if found:
    print(found)
else:
    print("No se ha encontrado el patrón")


text = "casa caasa cosa cisa cesa causa"
pattern = r"c.sa"

matches = re.findall(pattern, text)
print(matches)

# Cómo usar la barra invertida para anular el significado especial de un símbolo
text = "Mi casa es balnca. El coche en negro."
pattern = r"\."
matches = re.findall(pattern, text)
print(matches)

# \d: coincide con cualquier dígito (0-9)
text = "El número de teléfono es 123456789"
pattern = r"\d{9}"  # busca un digito 9 veces, es decir, busca un numero de 9 digitos

# Ejercicio: Detectar si hay un número de México en el texto gracias al prefijo +52
text = "Mi número de teléfono es +52 1089999999 apúntalo vale?"
"""
Desglose de la expresión regular:
^\+: Asegura que el número comience con el signo +.
(\d{1,3}): Permite entre 1 y 3 dígitos para el código del país.
\s?: Permite un espacio opcional entre el código del país y el número de teléfono.
\d{8,15}: Permite entre 8 y 15 dígitos para el número de teléfono (esto cubre la longitud de los números en la mayoría de los países).
$: Indica que el número debe terminar allí.
"""
pattern = r"\+(\d{1,4})\s?(\d{1,15})"
found_number = re.search(pattern, text)

if found_number:
    print(f"encontre el numero {found_number.group()}")
else:
    print(f"no se encontro ningun numero de telefono en el texto {text}")


# \w: Coincide con cualquier caracter alfanumerico (a-z, A-Z, 0-9, _)
# \w es esencialmente abreviatura de [a-zA-Z0-9_]
text = "el_rubius_69"
pattern = r"\w"
found = re.findall(pattern, text)
print(found)

# Expresión regular: \s
# \s: El \s es un metacaracter que coincide con cualquier carácter de espacio en blanco. Esto incluye:
# Espacios (' ').
# Tabulaciones (\t).
# Saltos de línea (\n).
# Retornos de carro (\r).
# Otros caracteres relacionados con el espacio en blanco.
text = "Hola mundo\n¿Cómo estás?\t"
pattern = r"\s"
matches = re.findall(pattern, text)
print(matches)

# ^: Coincide con el principio de una cadena
username = "423_name%22"
pattern = r"^\w"  # valida que inicie con caracteres alfanumericos
valid = re.search(pattern, username)
if valid:
    print(f"el nombre de usuario '{username}' es valido")
else:
    print(f"el nombre de usuario '{username}' no es valido")


# $: Coincide con el final de una cadena
text = "Hola mundo."
pattern = r"mundo$"  # verifica si la cadena termina con 'mundo'

valid = re.search(pattern, text)

if valid:
    print("La cadena es válida")
else:
    print("La cadena no es válida")

# EJERCICIO:
# Tenemos una lista de archivos, necesitamos saber los nombres de los ficheros con extension .txt
files = "file1.txt file2.pdf midu-of.webp secret.txt"
pattern = r"\b\w+.txt\b"
matches = re.findall(pattern, files)
print(matches)


# \b: Coincide con el principio o final de una palabra
text = "casa casada cosa cosas casado casa"
pattern = r"\bc.sa\b"

found = re.findall(pattern, text)
print(found)

# |: Coincidr con una opción u otra
fruits = "platano, piña, manzana, aguacate, palta, pera, aguacate, aguacate"
pattern = r"palta|aguacate|p..a|\b\w{7}\b"

matches = re.findall(pattern, fruits)
print(matches)


###
# 03 - Quantifiers
# Los cuantificadores se utilizan para especificar cuántas ocurrencias de un carácter o grupo de caracteres se deben encontrar en una cadena.
###

# *: Puede aparecer 0 o más veces
text = "aaaba"
pattern = "a*"
matches = re.findall(pattern, text)
print(matches)

# Ejercicio 1:
# ¿Cuantas palabras tienen de 0 a más "a" y después una b? r"^a*b$"


# +: Una a más veces
text = "dddd aaa ccc a bb aa casa"
pattern = "a+"
matches = re.findall(pattern, text)
print(matches)

# ?: Cero o una vez
text = "aaabacb"
pattern = "a?b"
matches = re.findall(pattern, text)
print(matches)

# Ejercicio: Haz opcional que aparezca un +34 en el siguiente texto
phone = "+34 688999999"

# {n}: Exactamente n veces
text = "aaaaaa         aa   aaaa"
pattern = "a{3}"
matches = re.findall(pattern, text)

print(matches)

# {n, m}: De n a m veces
text = "u uu uuu u"
pattern = r"\w{2,3}"
matches = re.findall(pattern, text)
print(matches)

# Ejercicio:
# Encuentra las palabras de 4 a 6 letras en el siguiente texto
words = "ala casa árbol león cinco murcielago"
pattern = r"\b\w{4,6}\b"
matches = re.findall(pattern, words)
print(matches)

# Ejercicio
# Encuentra las palabras de más de 6 letras
words = "ala fantastico casa árbol león cinco murcielago"
pattern = r"\b\w{6,}\b"
matches = re.findall(pattern, words)
print(matches)


# [:] Coincide con cualquier caracter dentro de los corchetes

username = "rub.$ius_69+"
pattern = r"^[\w._%+-]+$"

match = re.search(pattern, username)
if match:
    print("El nombre de usuario es válido: ", match.group())
else:
    print("El nombre de usuario no es válido")


# Buscar todas las vocales de una palabra
text = "Hola mundo"
pattern = r"[aeiou]"
matches = re.findall(pattern, text)
print(matches)

# Una Regex para encontrar las palabras man, fan y ban
# pero ignora el resto
text = "man ran fan ñan ban"
pattern = r"[mfb]an"

matches = re.findall(pattern, text)
print(matches)

# Ejercicio:
# Nos han complicado el asunto, porque ahora hay palabras que encajan pero no empiezan por esas letras.
# Solo queremos las palabras man, fan y ban
text = "omniman fanatico man bandana"
# \b

text = "22"
pattern = r"[4-9]"

matches = re.findall(pattern, text)
print(matches)


# Ejercicio final con todo lo aprendido
# Mejorar esto: https://www.computerhope.com/jargon/r/regular-expression.png

## Buscar corner cases que no pasa y arreglarlo:
"lo.que+sea@shopping.online"
"michael@gov.co.uk"

# [^]: Coincide con cualquier caracter que no esté dentro de los corchetes
text = "Hola mundo"
pattern = r"[^aeiou]"
matches = re.findall(pattern, text)
print(matches)

# Expresión regular: [^0-9]

# El [] indica un conjunto de caracteres.
# El ^ al principio de los corchetes [] significa negación. En lugar de buscar los caracteres que están dentro del conjunto, buscará los caracteres que no están dentro de él.
# 0-9 es un rango que cubre todos los dígitos del 0 al 9.
# Entonces, la expresión regular [^0-9] busca cualquier carácter que no sea un dígito entre 0 y 9


# Expresión regular: "[#:^]"
# []: Los corchetes indican un conjunto de caracteres.
# #: El carácter # está dentro del conjunto, por lo que la regex busca el símbolo #.
#:: El carácter : también está dentro del conjunto, por lo que la regex busca el símbolo :.
# ^: El símbolo ^ también está dentro del conjunto. En este caso, como está dentro de los corchetes, no actúa como un operador de negación, sino que simplemente busca el carácter ^.
# En resumen, la expresión regular "[#:^]" buscará cualquiera de los tres caracteres: #, :, o ^.


# \W: es equivalente a [^a-zA-Z0-9_] -> re.search('\d', 'abc4def') -> 4
# \D es equivalente a [^0-9] -> re.search('\D', '234Q678') -> Q


# Expresión regular: \S
# \S: Este es el opuesto de \s, por lo que busca cualquier carácter que no sea un espacio en blanco. Es decir:
# Coincide con caracteres como letras, números, puntuación, etc.
# No coincidirá con espacios (' '), tabulaciones (\t), saltos de línea (\n), ni retornos de carro (\r).

# Coincidir un número de teléfono:
# Escribe una expresión regular para validar un número de teléfono que siga el siguiente formato: 123-456-7890. No deben aceptarse otros formatos como paréntesis o espacios.
patter_phone = r"^\d{3}-\d{3}-\d{4}$"

# Coincidir una dirección de correo electrónico:
# Crea una expresión regular para encontrar direcciones de correo electrónico que tengan el formato general usuario@dominio.com.
# Ejemplo válido: nombre@dominio.com
# Ejemplo no válido: nombre@dominio
pattern_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]\.[a-zA-Z]{2,}$"

# Coincidir un número entero (positivo o negativo):
# Escribe una expresión regular que coincida con números enteros que pueden ser negativos o positivos, con o sin signo.
# Ejemplo válido: 123, -123, +456
# Ejemplo no válido: 123.45, 123a
pattern_positive_number = r"^[+-]?\d+$"

text = "Ana es una buena amiga"
pattern_vowels = r"\b[aeiouAEIOU]+\w+\b"
# \b: Define un límite de palabra, asegurando que coincidamos con palabras completas.
# [aeiouAEIOU]: Coincide con cualquier vocal, mayúscula o minúscula.
# \w*: Coincide con cero o más caracteres alfanuméricos o guion bajo (es decir, el resto de la palabra).
# \b: Límite de palabra al final.
# Al usar los límites de palabra \b, se asegura de que coincida con palabras completas, no fragmentos.
matches = re.finditer(pattern_vowels, text)
for match in matches:
    print(match.group())


# Coincidir fechas en formato DD/MM/AAAA
pattern_date = r"^(0[1-9] | [12][0-9] | 3[01])/(0[1-9] | 1[0-2])/\d{4}$"

# Coincidir palabras con al menos una vocal
# \b para asegurarnos de que coincidamos con palabras completas y no fragmentos.
pattern_vowels2 = r"\b\w*[aeiouAEIOU]+\w*\b"
