import math
# Simple calculator Programme
# Function to add two numbers
def add(a, b):
  return a + b
# Function to subtract second number from first
def subtract (a, b):
  return a - b
# Function to multiply two number
def multiply (a, b):
  return a * b
# Function to divide first number by second
def divide (a, b):
  if b != 0:
    return a / b
  else:
    return "Error: Division by Zero"
  # Function for square root
def sqrt (a, b):
   if a < 0:
     return "Error: Cannot calculate sqare root of negative number"
   return math.sqrt(a)
# Function for exponential
def exponential(a, b):
   return a**b
 # Display Operation options to the user
print("Select Operation: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square Root")
print("6. Exponential")
print("7.: Exit")
  # Take input from the user for operation choice
choice = input("Enter choice (1/2/3/4/5/6): ")
  # Get two numbers as input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
  # Perform calculator based on the user's choice
if choice == '1':
    print("Result:", add (num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2)) 
elif choice == '4':
    print("Result:", divide(num1, num2))
elif choice == '5':
   print("Result:", sqrt(num1))
elif choice == '6':
   print("Result:", exponential(num1, num2))
elif choice == '7':
   print("Exiting the Calculator . Good bye")
else:
    print("Invalid choice")  


