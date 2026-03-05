# project calculator
def addition(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "division by zero"
    else:
        return a / b

print("---Simple Calculator---")
print("Operations:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

operation = input("Choose operation 1-4: ")

num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))

if operation == "1":
    print("Result:",addition(num_1, num_2))
elif operation == "2":
    print("Result:",subtract(num_1, num_2))
elif operation == "3":
    print("Result:",multiply(num_1, num_2))
elif operation == "4":
    print("Result:",divide(num_1, num_2))
else:
    print("Invalid operation")