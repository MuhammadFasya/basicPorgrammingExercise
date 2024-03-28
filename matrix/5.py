def input_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
    matrix = []
    print("Enter the elements row-wise:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Enter element at position ({i+1},{j+1}): "))
            row.append(element)
        matrix.append(row)
    return matrix

def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Cannot perform addition. Matrices should have the same dimensions.")
        return None
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def subtract_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Cannot perform subtraction. Matrices should have the same dimensions.")
        return None
    return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("Cannot perform multiplication. Number of columns of the first matrix should be equal to the number of rows of the second matrix.")
        return None
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix1[0])))
            row.append(element)
        result.append(row)
    return result

def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def determinant_matrix(matrix):
    if len(matrix) != len(matrix[0]):
        print("Determinant is defined only for square matrices.")
        return None
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for j in range(n):
        det += ((-1) ** j) * matrix[0][j] * determinant_matrix(minor(matrix, 0, j))
    return det

def minor(matrix, row, col):
    return [row[:col] + row[col+1:] for row in (matrix[:row] + matrix[row+1:])]

def inverse_matrix(matrix):
    det = determinant_matrix(matrix)
    if det == 0:
        print("The matrix is singular, it does not have an inverse.")
        return None
    adjoint = [[((-1) ** (i+j)) * determinant_matrix(minor(matrix, i, j)) for j in range(len(matrix))] for i in range(len(matrix))]
    adjoint = transpose_matrix(adjoint)
    return [[adjoint[i][j] / det for j in range(len(adjoint))] for i in range(len(adjoint))]

# Main code
print("Enter the first matrix:")
matrix_A = input_matrix()

print("\nEnter the second matrix:")
matrix_B = input_matrix()

print("\nMatrix Addition:")
add_result = add_matrices(matrix_A, matrix_B)
if add_result:
    for row in add_result:
        print(row)

print("\nMatrix Subtraction:")
sub_result = subtract_matrices(matrix_A, matrix_B)
if sub_result:
    for row in sub_result:
        print(row)

print("\nMatrix Multiplication:")
mul_result = multiply_matrices(matrix_A, matrix_B)
if mul_result:
    for row in mul_result:
        print(row)

print("\nMatrix Transpose:")
transpose_result = transpose_matrix(matrix_A)
for row in transpose_result:
    print(row)

print("\nMatrix Determinant:")
det_result = determinant_matrix(matrix_A)
if det_result is not None:
    print(det_result)

print("\nMatrix Inverse:")
inv_result = inverse_matrix(matrix_A)
if inv_result:
    for row in inv_result:
        print(row)
