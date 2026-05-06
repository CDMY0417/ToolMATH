def least_common_multiple_t(c: int, d: int) -> int:
    def gcd(x: int, y: int) -> int:
        while y != 0:
            x, y = y, x % y
        return x
    return abs(c * d) // gcd(c, d)
