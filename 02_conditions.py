# 02_conditions.py
# Conditions and basic calculator
print("---CONDITIONS---")

print("\n---CALCULATOR---")

num_1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num_2 = float(input("Enter second number: "))

if operator == "+":
    result = num_1 + num_2
elif operator == "-":
    result = num_1 - num_2
elif operator == "*":
    result = num_1 * num_2
elif operator == "/":
    if num_2 == 0:
        result = "Cannot divide by zero"
    else:
        result = num_1 / num_2
else:
    result = "Invalid operator!"
print("Result:",result)