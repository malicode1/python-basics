# 10_try_except.py

try:
    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter second number: "))
    divide = num_1 / num_2
    print(divide)
except ValueError:
    print("Invalid input")
except ZeroDivisionError as err:
    print(err)

