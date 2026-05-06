def triangle_inequality_constraints(a: int, b: int) -> tuple:
    min_n = abs(a - b) + 1
    max_n = a + b - 1
    return min_n, max_n
