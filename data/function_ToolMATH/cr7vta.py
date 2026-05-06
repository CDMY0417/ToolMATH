def smallest_multiple_greater_than_a(m: int, n: int) -> int:
    quotient = n // m
    if n % m == 0:
        return n
    return (quotient + 1) * m
