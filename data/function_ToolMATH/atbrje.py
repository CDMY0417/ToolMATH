def is_invertible_modulo_a(x: int, n: int) -> bool:
    import math
    return math.gcd(x, n) == 1
