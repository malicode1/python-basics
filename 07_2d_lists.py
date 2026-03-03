# 07_2d_list.py
# 2d lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[1][1] = 999

print("Full Matrix:")
print(matrix)

print("\nAccess single element:")
print(matrix[0][2])

print("\nLoop through the matrix:")
for row in matrix:
    for number in row:
        print(number)
