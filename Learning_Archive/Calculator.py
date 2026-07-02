def calculate(a, operator, b):
  if operator == '+':
    return a + b
  elif operator == '-':
    return a - b
  elif operator == '*':
    return a * b
  elif operator == '/':
    if b == 0:
      return "Error: Division by zero"
    else:
      return a / b
  else:
    return "Invalid operator"

def recalc():
  global a  # Declared 'a' as global to modify it within the function
  operator = input("Enter the operator (+, -, *, /): ")
  b = float(input("Enter the second number: "))
  return operator, b

def startcalc():
  a = float(input("Enter the first number: "))
  while True:
    operator, b = recalc()  # Gets operator and b from recalc()
    result = calculate(a, operator, b)
    print("Result:", result)
    a = result  # Updates 'a' for subsequent calculations
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() != 'y':
      break

startcalc()
