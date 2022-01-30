#Calculator

def add (n1, n2):
  return n1 + n2
 
def subtract (n1, n2):
  return n1 - n2

def multiply (n1, n2):
  return n1 * n2

def divide (n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  }

first_number = int(input("Enter your first number.\n"))
for symbol in operations:
  print(symbol)
operations_symbol = input("Select your operator from the four choices displayed above. \n")
second_number = int(input("Enter your second number.\n"))

calculate = operations[operations_symbol]
#by using the variable "calculate", we are accessing the VALUE, not the key of the operations symbol that the user selected.
answer = calculate(first_number, second_number)

#we've turned the variable into one of the already defined functions as a result. calculate() = add(first_number, second_number), subtract(first_number, second_number), etc, etc.

print(f"{first_number} {operations_symbol} {second_number} = {answer}")