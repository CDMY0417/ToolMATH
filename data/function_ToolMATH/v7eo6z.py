def sqrt_fraction(numerator: int, denominator: int) -> tuple[int, int]:
    from math import isqrt
    num_sqrt, denom_sqrt = isqrt(numerator), isqrt(denominator)
    return num_sqrt, denom_sqrt
