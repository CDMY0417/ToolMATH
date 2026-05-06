def last_two_digits(base: int, exponent: int) -> int:
    result = 1
    base %= 100
    for _ in range(exponent):
        result = (result * base) % 100
    return result
