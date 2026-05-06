def check_zero_matrix(A: list[list[int]]) -> bool:
    return all(all(a == 0 for a in row) for row in A)
