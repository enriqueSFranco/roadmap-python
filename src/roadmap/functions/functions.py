
# Funciones con numero variable de argumentos
def suma_variable(*numeros):
  total = 0
  for num in numeros:
    total += num
  return total

print(suma_variable(1,2,3,4,5))
print(suma_variable(4,7,8,10))