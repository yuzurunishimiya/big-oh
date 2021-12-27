
# square -> O(n^2)
def square(n):
    for i in range(n):
        for j in  range(n):
            print(i, j)

square(4)

print("\n------- ")
# get matrix instead
def matrix_square(n):
    matrix = [[x, y] for x in range(n) for y in range(n)]
    return matrix


# display matrix a with O(n)
def display_matrix_square(matrix: list, seq: int):
    for index, nested in enumerate(matrix, 1):
        if index % seq == 0:
            print(nested)
        else:
            print(nested, end=" ")

matrix = matrix_square(4)
display_matrix_square(matrix, seq=4)
