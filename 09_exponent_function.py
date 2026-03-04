# 09_exponent_function.py
# Exponent function with power calculation

number = int(input("Enter a number: "))
power_value = int(input("Enter a power: "))

def powering(num,power):
    result = 1
    for i in range(power):
        result *= num
    return result

print(powering(number,power_value))