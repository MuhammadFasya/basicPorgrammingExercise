def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions for addition")
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def subtract_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions for subtraction")
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result

def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix")
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            total = 0
            for k in range(len(matrix2)):
                total += matrix1[i][k] * matrix2[k][j]
            row.append(total)
        result.append(row)
    return result

def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def determinant_matrix(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Matrix must be square to calculate determinant")
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for i in range(len(matrix)):
        det += ((-1) ** i) * matrix[0][i] * determinant_matrix([row[:i] + row[i + 1:] for row in matrix[1:]])
    return det

def inverse_matrix(matrix):
    det = determinant_matrix(matrix)
    if det == 0:
        raise ValueError("Matrix is singular, it does not have an inverse")
    if len(matrix) == 1:
        return [[1 / det]]
    cofactors = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            minor = [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]
            row.append(((-1) ** (i + j)) * determinant_matrix(minor))
        cofactors.append(row)
    adjugate = transpose_matrix(cofactors)
    return [[adjugate[i][j] / det for j in range(len(adjugate))] for i in range(len(adjugate))]

# Example matrices
matrix_A = [[4, 5, 6],
            [1, 2, 8],
            [3, 7, 9]]

matrix_B = [[9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]]

# Addition
print("Matrix Addition:")
print(add_matrices(matrix_A, matrix_B))

# Subtraction
print("\nMatrix Subtraction:")
print(subtract_matrices(matrix_A, matrix_B))

# Multiplication
print("\nMatrix Multiplication:")
print(multiply_matrices(matrix_A, matrix_B))

# Transpose
print("\nMatrix Transpose:")
print(transpose_matrix(matrix_A))

# Determinant
print("\nMatrix Determinant:")
print(determinant_matrix(matrix_A))

# Inverse
print("\nMatrix Inverse:")
try:
    print(inverse_matrix(matrix_A))
except ValueError as e:
    print(e)