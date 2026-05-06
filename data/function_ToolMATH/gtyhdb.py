def sum_of_squares_modulo(n: int, divisor: int) -> int:
    total = sum(i ** 2 for i in range(1, n + 1))
    return total % divisor
