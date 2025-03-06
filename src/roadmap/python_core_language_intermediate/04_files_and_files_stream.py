"""
En esencia, un archivo es un conjunto contiguo de bytes utilizado para almacenar datos. 
Estos datos están organizados en un formato específico y pueden ser cualquier cosa tan simple como un archivo de texto o 
tan complicado como un programa ejecutable. 
Al final, estos archivos de bytes se traducen en binarios 1 y 0 para un procesamiento más fácil por la computadora.

---------- Un archivo se compone de 3 partes ----------
1.- encabezado(header): metadatos sobre el contenido del archivo (name_file, size, type. etc)
2.- datos (data or the contents of the file)
3.- fin del archivo (EOF): carcter especial que indica el final del archivo


---------- Finales de linea -----------
Un problema a menudo se encuentra cuando trabajando con datos de archivos es la representación de una nueva línea o final de línea
Ejemplo:
dogs.txt
Pug\r\n
Jack Russell Terrier\r\n
English Springer Spaniel\r\n

Output Unix:
Pug\r
\n
Jack Russell Terrier\r
\n
English Springer Spaniel\r
\n

NOTA: Esto puede hacer que la iteración sobre cada línea sea problemática
"""

# abrir un archivo
# reader = open("./dogs_breeds.txt")

# 1ra forma de cerrar un archvo
# try:
#    pass
# finally:
#    reader.close()

# 2da forma de cerrar un archivo <- forma recomendada
# with open("./dog_breeds.txt", "r") as reader:
#    print(reader.readline(5))

# iterando sobre cada line
# 1ra forma de iterar sobre las lineas del archivo
# with open("./dog_breeds.txt", "r") as reader:
#    # Read and print the entire file line by line
#    line = reader.readline()
#    while line != "":  # The EOF char is an empty string
#        print(line, end="")
#        line = reader.readline()

# 2da forma de iterar sobre las lineas del archivo
# with open("./dog_breeds.txt", "r") as reader:
# 	for line in reader.readlines():
# 		print(line, end='')

# 3ra forma de iterar sobre las lineas del archivo
# with open("./dog_breeds.txt", "r") as reader:  # enfoque pythonico ✅
#    for line in reader:
#        print(line, end="")


# Escritura de archivos
# with open("./dog_breeds.txt", "r") as reader:
# 	dog_breeds = reader.readlines()

# with open("./dog_breeds_reversed.txt", "w") as writer:
# 	for breed in reversed(dog_breeds):
# 		writer.write("breed")


# Escribir al final en un archivo poblado
# with open("./dog_breeds.txt", "a") as a_writer:
# 	a_writer.write("\nBeagle")

# Leer y escribir en dos archivos al mismo tiempo
d_path = "./dog_breeds.txt"
d_r_path = "./dog_breeds_reversed.txt"
with open(d_path, "r") as reader, open(d_r_path, "w") as writer:
    dog_breeds = reader.readlines()
    writer.writelines(reversed(dog_breeds))

"""
employees.csv
nombre,cargo,fecha_ingreso,salario,estado
Juan Pérez,Desarrollador,2019-06-01,3500,Activo
Ana Gómez,Gerente de Proyectos,2018-03-15,5500,Activo
Carlos Sánchez,Analista de Datos,2020-01-22,3200,Activo
María Rodríguez,Asistente Administrativo,2021-08-05,2400,Inactivo
Pedro Jiménez,Desarrollador,2017-11-30,4000,Activo
Lucía Fernández,Marketing,2019-09-10,3000,Activo
David López,Gerente de TI,2015-05-18,6000,Activo
Isabel García,Analista de Sistemas,2022-02-12,2900,Inactivo
Luis Martínez,Desarrollador,2020-11-25,3800,Activo
Marta Álvarez,Recursos Humanos,2018-07-10,2800,Activo

¿Qué puedes hacer con estos datos en Python?
Leer el archivo CSV: Usando pandas o el módulo csv.
Filtrar empleados activos.
Calcular el salario promedio.
Contar cuántos empleados hay por cargo.
Obtener el empleado con mayor salario.
"""
