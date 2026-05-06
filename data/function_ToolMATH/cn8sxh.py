def trace_of_matrix(matrix: list[list[int]]) -> int:
    return sum(matrix[i][i] for i in range(len(matrix)))
