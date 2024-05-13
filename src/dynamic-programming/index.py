def factorial_recursive(n: int) -> int:
  if n == 0:
    return 1
  return n * factorial_recursive(n - 1)

def factorial_iterative(n: int) -> int:
  if n == 0:
    return 1
  
  fact = 1
  while n > 0:
    fact *= n
    n -= 1
  
  return fact

def factorial__dp(n: int) -> int:
  pass

""" FIBONACCI """
def fibonacci_iteretive(n: int) -> int:
  if n == 1:
    return 0
  elif n == 2:
    return 1
  else:
    a, b = 0, 1
    for _ in range(2, n):
      fibo = a + b # 0 + 1 = 1
      a, b = b, fibo # 1
  return fibo

def fibonacci_recursive(n: int) -> int:
  if n == 1:
    return 0
  elif n == 2:
    return 1
  else:
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
  
  
def fibonacci_dp(n: int, memo = {}) -> int:
  if n in memo:
    return memo[n]
  
  if n <= 1:
    return n
  
  result = fibonacci_dp(n - 1, memo) + fibonacci_dp(n - 2, memo)
  memo[n] = result
  
  return result
  
print(fibonacci_dp(4))