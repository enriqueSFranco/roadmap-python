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