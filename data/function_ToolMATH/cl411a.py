def is_terminating_decimal_b(n: int, d: int) -> bool:
    def remove_factors(x: int, factor: int) -> int:
        while x % factor == 0:
            x //= factor
        return x
    d = remove_factors(d, 2)
    d = remove_factors(d, 5)
    return d == 1
