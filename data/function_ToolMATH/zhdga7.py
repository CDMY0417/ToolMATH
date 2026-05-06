def least_common_multiple_ah(a: int, b: int) -> int:
    import math
    return abs(a * b) // math.gcd(a, b)
