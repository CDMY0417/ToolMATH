def simplify_fraction_r(numerator: int, denominator: int) -> tuple:
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    common_divisor = gcd(numerator, denominator)
    return (numerator // common_divisor, denominator // common_divisor)
