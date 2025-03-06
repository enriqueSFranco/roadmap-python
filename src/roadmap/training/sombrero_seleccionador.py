# EL SOMBRERO SELECCIONADOR
# EJERCICIO:
# Cada 1 de septiembre, el Hogwarts Express parte hacia la escuela
# de programación de Hogwarts para magos y brujas del código.
# En ella, su famoso sombrero seleccionador ayuda a los programadores
# a encontrar su camino...
# Desarrolla un programa que simule el comportamiento del sombrero.
# Requisitos:
# 1. El sombrero realizará 10 preguntas para determinar la casa del alumno.
# 2. Deben existir 4 casas. Por ejemplo: Frontend, Backend, Mobile y Data.
  #  (Puedes elegir las que quieras)
# Acciones:
# 1. Crea un programa que solicite el nombre del alumno y realice 10
  #  preguntas, con cuatro posibles respuestas cada una.
# 2. Cada respuesta asigna puntos a cada una de las casas (a tu elección).
# 3. Una vez finalizado, el sombrero indica el nombre del alumno 
  #  y a qué casa pertenecerá (resuelve el posible empate de manera aleatoria,
  #  pero indicándole al alumno que la decisión ha sido complicada).

import random
from typing import Dict

houses = ["Frontend", "Backend", "Mobile", "Data"]

questions = [
  {
    "question": "¿Cuál es tu lenguaje de programación favorito?",
    "options": {
      "A": ("JavaScript", {'Frontend': 3, 'Backend': 1, 'Mobile': 2, 'Data': 1}),
      "B": ("Python", {'Frontend': 1, 'Backend': 3, 'Mobile': 2, 'Data': 2}),
      "C": ("Java", {'Frontend': 1, 'Backend': 2, 'Mobile': 3, 'Data': 1}),
      "D": ("SQL", {'Frontend': 1, 'Backend': 1, 'Mobile': 1, 'Data': 4}),
    }
  },
  {
    "question": "¿Cuál es tu herramienta de desarrollo favorita?",
    "options": {
      "A": ("VS Code", {'Frontend': 3, 'Backend': 1, 'Mobile': 1, 'Data': 2}),
      "B": ("IntelliJ", {'Frontend': 1, 'Backend': 3, 'Mobile': 1, 'Data': 1}),
      "C": ("Android Studio", {'Frontend': 1, 'Backend': 2, 'Mobile': 3, 'Data': 1}),
      "D": ("Jupyter", {'Frontend': 1, 'Backend': 1, 'Mobile': 1, 'Data': 4}),
    }
  },
  {
    "question": "¿Qué tipo de proyecto te gustaría desarrollar?",
    "options": {
      "A": ("Una web interactiva", {'Frontend': 4, 'Backend': 1, 'Mobile': 2, 'Data': 1}),
      "B": ("Una API", {'Frontend': 1, 'Backend': 4, 'Mobile': 1, 'Data': 1}),
      "C": ("Una app móvil", {'Frontend': 1, 'Backend': 2, 'Mobile': 4, 'Data': 1}),
      "D": ("Un análisis de datos", {'Frontend': 1, 'Backend': 1, 'Mobile': 1, 'Data': 4}),
    }
  },
  {
    "question": "¿Cómo prefieres trabajar?",
    "options": {
      "A": ("En equipo", {'Frontend': 2, 'Backend': 2, 'Mobile': 2, 'Data': 2}),
      "B": ("Solo", {'Frontend': 1, 'Backend': 1, 'Mobile': 1, 'Data': 1}),
      "C": ("En pair programming", {'Frontend': 2, 'Backend': 2, 'Mobile': 2, 'Data': 2}),
      "D": ("Con mentoría", {'Frontend': 2, 'Backend': 2, 'Mobile': 2, 'Data': 2}),
    }
  },
  {
    "question": "¿Qué te motiva a programar?",
    "options": {
      "A": ("Crear soluciones", {'Frontend': 2, 'Backend': 3, 'Mobile': 2, 'Data': 2}),
      "B": ("Aprender nuevas tecnologías", {'Frontend': 2, 'Backend': 2, 'Mobile': 2, 'Data': 3}),
      "C": ("Desarrollar habilidades", {'Frontend': 2, 'Backend': 2, 'Mobile': 3, 'Data': 2}),
      "D": ("Analizar información", {'Frontend': 1, 'Backend': 1, 'Mobile': 1, 'Data': 4}),
    }
  },
  {
    "question": "¿Qué es lo que más valoras en un proyecto?",
    "options": {
      "A": ("La estética", {'Frontend': 4, 'Backend': 1, 'Mobile': 2, 'Data': 1}),
      "B": ("La funcionalidad", {'Frontend': 1, 'Backend': 4, 'Mobile': 1, 'Data': 2}),
      "C": ("La usabilidad", {'Frontend': 3, 'Backend': 2, 'Mobile': 2, 'Data': 1}),
      "D": ("La eficiencia", {'Frontend': 1, 'Backend': 2, 'Mobile': 1, 'Data': 4}),
    }
  },
  {
    "question": "¿Cómo prefieres aprender?",
    "options": {
      "A": ("A través de tutoriales", {'Frontend': 2, 'Backend': 2, 'Mobile': 2, 'Data': 2}),
      "B": ("Con proyectos prácticos", {'Frontend': 3, 'Backend': 3, 'Mobile': 3, 'Data': 1}),
      "C": ("Leyendo documentación", {'Frontend': 1, 'Backend': 2, 'Mobile': 1, 'Data': 4}),
      "D": ("Asistiendo a conferencias", {'Frontend': 2, 'Backend': 1, 'Mobile': 1, 'Data': 2}),
    }
  },
  {
    "question": "¿Cuál es tu estilo de programación?",
    "options": {
      "A": ("Ágil", {'Frontend': 2, 'Backend': 3, 'Mobile': 1, 'Data': 2}),
      "B": ("Waterfall", {'Frontend': 1, 'Backend': 2, 'Mobile': 2, 'Data': 1}),
      "C": ("Prototipado rápido", {'Frontend': 3, 'Backend': 1, 'Mobile': 2, 'Data': 1}),
      "D": ("Iterativo", {'Frontend': 2, 'Backend': 2, 'Mobile': 2, 'Data': 2}),
    }
  },
  {
    "question": "¿Qué tipo de usuario te gustaría impactar?",
    "options": {
      "A": ("Desarrolladores", {'Frontend': 2, 'Backend': 3, 'Mobile': 1, 'Data': 2}),
      "B": ("Usuarios finales", {'Frontend': 3, 'Backend': 1, 'Mobile': 2, 'Data': 1}),
      "C": ("Negocios", {'Frontend': 1, 'Backend': 4, 'Mobile': 1, 'Data': 1}),
      "D": ("Investigadores", {'Frontend': 1, 'Backend': 1, 'Mobile': 1, 'Data': 4}),
    }
  },
  {
    "question": "¿Cuál es tu desafío favorito en la programación?",
    "options": {
      "A": ("Resolver bugs", {'Frontend': 1, 'Backend': 3, 'Mobile': 1, 'Data': 2}),
      "B": ("Optimizar el rendimiento", {'Frontend': 1, 'Backend': 4, 'Mobile': 2, 'Data': 1}),
      "C": ("Crear interfaces atractivas", {'Frontend': 4, 'Backend': 1, 'Mobile': 2, 'Data': 1}),
      "D": ("Analizar grandes datos", {'Frontend': 1, 'Backend': 1, 'Mobile': 1, 'Data': 4}),
    }
  },
]

def ask_question() -> Dict[str, int]:
  scores = {house: 0 for house in houses}

  for i, q in enumerate(questions):
    print(f"\n{i + 1}.{q['question']}")
    for letter, (answer, points) in q["options"].items():
      print(f"{letter}. {answer}")

    while True:
      try:
        response = input("Elige una opción (A, B, C, D): ").strip().upper()
      except KeyboardInterrupt:
        print("\nPrograma interrumpido. Saliendo...")
        return scores
      if response in q["options"]:
        # sumar los puntos a las casas
        for house, points in q["options"][response][1].items():
          scores[house] += points
        break
      else:
        print("Opcion invalida. Intentelo de nuevo.")
  return scores

# type Score = Dict[str, int] requiere python 3.12 o superior para usar type alias

# {'Frontend': 8, 'Backend': 5, 'Mobile': 5, 'Data': 3}
def determine_house(scores: Dict[str, int]):
  max_score = max(scores.values())
  winners = [house for house, score in scores.items() if score >= max_score]

  if len(winners) > 1:
    chosen_house = random.choice(winners)
    print(f"La decisión ha sido complicada, pero has sido seleccionado para la casa {chosen_house}.")
  else:
    chosen_house = winners[0]
    print(f"Has sido seleccionado para la casa {chosen_house}.")
  
def main():
  name = input("¿Cual es tu nombre? ")
  print(f"Bienvenido, {name}!")
  
  scores = ask_question()
  determine_house(scores)

if __name__ == "__main__":
  main()