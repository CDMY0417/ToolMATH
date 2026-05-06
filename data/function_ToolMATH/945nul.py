def simplify_fraction_k(a: int, b: int) -> tuple:
    import math
    gcd = math.gcd(a, b)
    return (a // gcd, b // gcd)
