def normalize_vector(vector: list[int]) -> list[int]:
    from math import gcd
    a, b = vector
    divisor = gcd(abs(a), abs(b))
    return [a // divisor, b // divisor]
