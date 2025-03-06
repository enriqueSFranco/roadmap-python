from operator import mul, truediv

def calculate(operator, operand1, operand2):
  return operator(operand1, operand2)

def division(a, b):
  try:
    a = float(input("What is your first number? "))
    b = float(input("What is your second number? "))
    operation = input("Enter either * or /: ")
    
    if operation == "*":
      answer = calculate(mul, a, b)
    elif operation == "/":
      answer = calculate(truediv, a, b)
    else:
      raise RuntimeError(f"'{operation}' is an unsupported operation")
  except (RuntimeError, ValueError, ZeroDivisionError) as error: # asiganamos las excepciones a al variable error
    print("A {} has ocurred".format(type(error).__name__)) # para encontrar la clase de una Exception se uda type()
    match error:
      case RuntimeError():
        print(f"You have entered an invalid symbol: {error}")
      case ValueError():
        print(f"You have not entered a number: {error}")
      case ZeroDivisionError():
        print(f"You can't divide by zero: {error}")
  else:
    print("{} {} {} = {}".format(a, operation, b, answer))
    
division(10, "zero")