def simplify_fraction_g(numerator: int, denominator: int) -> tuple:
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    greatest_common_divisor = gcd(numerator, denominator)
    return numerator // greatest_common_divisor, denominator // greatest_common_divisor
