def long_division_remainder(a: int, b: int) -> int:
    quotient = a // b
    remainder = a - quotient * b
    return remainder
