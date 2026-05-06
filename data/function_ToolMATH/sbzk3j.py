def reduce_fraction_j(numerator: int, denominator: int) -> tuple:
    def gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a
    gcd_value = gcd(numerator, denominator)
    return numerator // gcd_value, denominator // gcd_value
