def least_common_multiple_n(a: int, b: int) -> int:
    def gcd(x: int, y: int) -> int:
        while y != 0:
            (x, y) = (y, x % y)
        return x
    return abs(a * b) // gcd(a, b)
