def create_phone_number(n):
  if len(n) != 10 or any(not isinstance(num, int) or not 0 <= num <= 9 for num in n):
    raise ValueError("La matriz debe contener 10 enteros entre 0 y 9")
  
  return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))