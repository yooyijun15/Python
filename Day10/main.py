from art import LOGO

print(LOGO)

def add(n1, n2):
  return n1 + n2
def subtract(n1, n2):
  return n1 - n2
def multiply(n1, n2):
  return n1 * n2
def divide(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

def calculable():
  first_num = float(input("What's the first number? "))
  for symbol in operations:
    print(symbol)
  shoud_continue = True

  while shoud_continue:
    operations_symbol = input("Pick an operation from the line above: ")
    next_num = float(input("What's the next number? "))
    calculation_function = operations[operations_symbol]
    result = calculation_function(first_num, next_num)
    print(f"{first_num} {operations_symbol} {next_num} = {result}")
    if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == "y":
      first_num = result
    else:
      shoud_continue = False
      calculable()

calculable()
