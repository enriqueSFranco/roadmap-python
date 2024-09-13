# EJERCICIO:
# ¡La temporada 2 de "Los Anillos de Poder" está a punto de estrenarse!
# ¿Qué pasaría si tuvieras que encargarte de repartir los anillos
# entre las razas de la Tierra Media?
# Desarrolla un programa que se encargue de distribuirlos.
# Requisitos:
# 1. Los Elfos recibirán un número impar.
# 2. Los Enanos un número primo.
# 3. Los Hombres un número par.
# 4. Sauron siempre uno.
# Acciones:
# 1. Crea un programa que reciba el número total de anillos
#  y busque una posible combinación para repartirlos.
# 2. Muestra el reparto final o el error al realizarlo.

def es_primo(num: int) -> bool:
  if num <= 1:
    return False
  
  if num <= 3:
    return True
  
  if num % 2 == 0:
    return False
  
  if num % 2 == 0 or num % 3 == 0:
    return False
  
  i = 5
  while i * i <= num:
    if num % i == 0 or num % (i + 2) == 0:
      return False
    i += 6
    
  return True

print(es_primo(5))

# Un número primo es un número entero mayor que 1 que solo tiene dos divisores: 1 y él mismo. Por ejemplo, 2, 3, 5 y 7 son números primos.

# 1. **Verificaciones iniciales**:
#    if n <= 1:
#        return False
#    - Si `n` es menor o igual a 1, no es primo por definición.

#    if n <= 3:
#        return True
#    - Los números 2 y 3 son primos, por lo que si `n` es 2 o 3, la función retorna `True`.

# 2. **Divisibilidad por 2 o 3**:
#    if n % 2 == 0 or n % 3 == 0:
#        return False
#    - Los números divisibles por 2 o 3 (excepto 2 y 3 mismos) no son primos. Esto descarta rápidamente muchos números no primos.

# 3. **Prueba de divisibilidad usando un algoritmo eficiente**:
#    i = 5
#    while i * i <= n:
#        if n % i == 0 or n % (i + 2) == 0:
#            return False
#        i += 6
#    - Aquí se utiliza un método eficiente para verificar la primalidad. En lugar de probar todos los números menores que `n`, el código prueba solo los números que tienen una forma específica.

#    - La razón detrás de `i` comenzando en 5 y aumentando en pasos de 6 (`i += 6`) se basa en una observación sobre los números primos:
#      - Todos los números primos mayores que 3 pueden ser escritos en la forma de \(6k \pm 1\), donde `k` es un número entero. Esto se debe a que cualquier número que no es divisible por 2 ni por 3 debe ser de esta forma (por ejemplo, 5, 7, 11, 13, ...).

#    - **¿Por qué `i * i <= n`?**:
#      - Solo necesitamos comprobar hasta la raíz cuadrada de `n` porque si `n` es divisible por algún número mayor que su raíz cuadrada, entonces debe ser divisible también por algún número menor que su raíz cuadrada.

#    - **Pruebas de divisibilidad**:
#      if n % i == 0 or n % (i + 2) == 0:
#          return False
#      - Se verifica si `n` es divisible por `i` o `i + 2`. Si es divisible por cualquiera de estos, no es primo.

#    - **Incremento de `i`**:
#      i += 6
#      - Se incrementa `i` en 6 para probar los siguientes posibles factores primos en la forma \(6k \pm 1\).

# 4. **Resultado**:
#    return True
#    - Si ninguna de las pruebas anteriores ha encontrado un divisor, `n` es primo.

# ### Ejemplo

# Para ver cómo funciona con un número específico:

# - **Número 29**:
#   - `n <= 1`: No es aplicable, ya que 29 es mayor que 1.
#   - `n <= 3`: No es aplicable, ya que 29 es mayor que 3.
#   - `n % 2 == 0 or n % 3 == 0`: 29 no es divisible ni por 2 ni por 3.
#   - `i = 5`, `i * i <= 29` (25 ≤ 29):
#     - Verificamos 29 % 5 = 4 y 29 % 7 = 1, ninguno de ellos divide exactamente a 29.
#     - `i` se incrementa a 11, y `i * i > 29` (121 > 29), por lo que se termina el bucle.
#   - Como no se encontró ningún divisor, 29 es primo.
