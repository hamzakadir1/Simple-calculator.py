# simple calculator with basic functions
# define functions
def add(x, y):
   """This function adds two numbers"""

   return x + y

def subtract(x, y):
   """This function subtracts two numbers"""

   return x - y

def multiply(x, y):
   """This function multiplies two numbers"""

   return x * y

def divide(x, y):
   """This function divides two numbers"""

   return x / y

# take input from the user
print("Select operation.")
print("A.Add")
print("B.Subtract")
print("C.Multiply")
print("D.Divide")

choice = input("Enter choice(A/B/C/D):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == 'A':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == 'B':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == 'C':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == 'D':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")