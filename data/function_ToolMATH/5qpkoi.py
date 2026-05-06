def simplify_fraction_bl(numerator: int, denominator: int) -> tuple:
    def gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a
    divisor = gcd(numerator, denominator)
    return numerator // divisor, denominator // divisor
