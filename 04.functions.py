# 04.functions.py
# functions and basic calculator
print("---FUNCTIONS---")

num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))
operator = input("Enter operator: ")


def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Division by zero"
        else:
            return a / b
    else:
        return "Invalid operator"

result = calculator(num_1, num_2, operator)
print("Result: ",result)