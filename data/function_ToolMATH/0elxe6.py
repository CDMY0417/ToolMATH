def least_positive_solution(b: int, n: int, min_value: int) -> int:
    k = (min_value - b + n - 1) // n
    return b + n * k
