def matrix_add(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    result = [[a + b for a, b in zip(A_row, B_row)] for A_row, B_row in zip(A, B)]
    return result
