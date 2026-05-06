def least_common_multiple_ao(a: int, b: int) -> int:
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return abs(a * b) // gcd(a, b)
