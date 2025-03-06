"""Single Responsibility Principle (SRP)"""

from pathlib import Path
from zipfile import ZipFile

""" 
sin usar SRP 

	En este ejemplo, tiene dos responsabilidades diferentes:
    Utiliza los métodos .read() y .write() para administrar el archivo. 
    También trata Archivos ZIP al proporcionar los métodos .compress() y .decompress().
"""
class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()
            

""" 
	usando SRP 

	La clase anterior viola el principio de responsabilidad única porque 
    tiene dos razones para cambiar su implementación interna. 
    
    Solución al problema:
    Dividir la clase en dos clases más pequeñas y enfocadas, cada una con su propia preocupación específica
    
"""
class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)

class ZipFileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()