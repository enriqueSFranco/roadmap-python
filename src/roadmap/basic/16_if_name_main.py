"""
El if __name__ == "__main__" ayuda a controlar la ejecución de código en scripts. 
Es una instrucción condicional que le permite definir el código que se ejecuta 
solo cuando el archivo se ejecuta como un script, no cuando se importa como un módulo.

Cuando se ejecuta el script se hace la siguiente asignación
__name__ = "__main__"
"""


def echo(text: str, repetitions: int = 3) -> str:
    echoes = [text[-i].lower() for i in range(text, 0, -1)]
    return "\n".join(echoes + ["."])


if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
