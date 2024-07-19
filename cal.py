def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return"Error:Division by zero!"
    return x/y
print("Simple Calculater")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.Divide")
choice = input("Choose an option: ")
print(choice)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == "1":
  print(num1, "+", num2, "=", add(num1, num2))
elif choice == "2":
  print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == "3":
  print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == "4":
  print(num1, "/", num2, "=", divide(num1, num2))
else:
  print("Invalid option")

