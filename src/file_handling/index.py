from os import listdir, scandir, path
from datetime import datetime
# file = open("dc_comics.txt") # accediendo al archivo

# print(file.read()) # lee todo el fichero
# print(file.readline()) # lee la primer linea

""" leer el archivo caracter por caracter con readLine() """
# character = file.readline(1)

# while character != "":
#   print(character)
#   character = file.readline(1)

""" usando readLines() """
# lines = file.readlines()
# print(lines)

# file.close()

""" usando whit() para abrir el archivo """
# al hacer esto se vacia el archivo antes de escribir, esto significa que si el archivo ya tenía contenido, 
# ese contenido se eliminará y se reemplazará por el nuevo contenido que estamos escribiendo.
# NOTE: abrimos el fichero en modo escritura
# with open('nombre_fichero', 'w') as f:
#   content = "Superman"
#   f.write(content)

""" abrimos el fichero en modo lectura """
# with open('nombre_fichero', 'r') as f:
#   for line in f:
#     print(line, end='')
    
""" usando el modulo os """
# MÉTODO listdir()
script_dir = path.dirname(path.abspath(__file__))
# if path.exists(shoping_dir):
#   # Listar los archivos en el directorio 'shoping'
#   entries = listdir(shoping_dir)
#   print("Archivos en el directorio 'shoping':", entries)
# else:
#   print("El directorio 'shoping' no existe en la ruta proporcionada:", shoping_dir)

def convert_data(timestamp):
  d = datetime.utcfromtimestamp(timestamp)
  formated_date = d.strftime("%d %b %Y")
  return formated_date

def get_files():
  dir_entries = scandir(script_dir)
  for entry in dir_entries:
    if entry.is_file():
      print("- {0} ultima modificacion: {1}".format(entry.name, convert_data(entry.stat().st_mtime)))
  
""" listar solamente archivos en un directorio"""    
print("ficheros dentro de la carpeta my_files")
with scandir(script_dir) as entries:
  for entry in entries:
    if entry.is_file():
      print("- {0} ultima modificacion: {1}".format(entry.name, convert_data(entry.stat().st_mtime)))

""" listar solamente directorios """
print("\ndirectorios dentro de la carpeta my_files")
for entry in listdir(script_dir):
  if path.isdir(path.join(script_dir, entry)):
    print("[+]",entry)
