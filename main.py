#Calculator

def add (n1, n2):
  return n1 + n2
 
def subtract (n1, n2):
  return n1 - n2

def multiply (n1, n2):
  return n1 * n2

def divide (n1, n2):
  return n1 / n2

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

first_number = int(input("Enter your first number.\n"))
second_number = int(input("Enter your second number.\n"))

for key in operations:
  key = input("Select your operator between +, -, *, or /. \n")