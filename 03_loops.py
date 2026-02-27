# 03_loops.py
# Loop examples
print("---LOOPS---")

for i in range(1,11):
    print(i)

print()

for i in range(1,21):
    if i % 2 == 0:
        print(i)
print()

result = 0
while result != 5:
    result += 1
    print(result)

print()

num = int(input("Enter a number: "))
for i in range(1, num + 1):
    print(i)


