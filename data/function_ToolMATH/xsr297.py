def gcdf(a: int, b: int, c: int) -> int:
    from math import gcd
    gcd_ab = gcd(abs(a), abs(b))
    gcd_abc = gcd(gcd_ab, abs(c))
    return gcd_abc
