def matrix_difference_a(A: list[list[float]], x: float):
    size = len(A)
    I = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    return [[A[i][j] - x * I[i][j] for j in range(size)] for i in range(size)]
