def simplify_fraction_l(numerator: int, denominator: int) -> (int, int):
    def gcd(x: int, y: int) -> int:
        while y:
            x, y = y, x % y
        return x
    common_divisor = gcd(numerator, denominator)
    return (numerator // common_divisor, denominator // common_divisor)
