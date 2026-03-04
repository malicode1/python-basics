# 08_nested_loops.py
# Nested loops
print("Basic Nested Loop:")

for i in range(3):
    for j in range(3):
        print("i",i,"j",j)

print("\nMultiplication Table:")
for i in range(1,6):
    for j in range(1,6):
        print(i * j,end=" ")
print()