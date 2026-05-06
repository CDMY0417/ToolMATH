def least_common_multiple_aq(a: int, b: int) -> int:
    from math import gcd
    return (a * b) // gcd(a, b)
