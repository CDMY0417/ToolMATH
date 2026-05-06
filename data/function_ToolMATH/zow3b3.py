def simplify_fraction_as(numerator: int, denominator: int):
    def gcd(a: int, b: int):
        while b != 0:
            a, b = b, a % b
        return a
    gcd_value = gcd(numerator, denominator)
    return numerator // gcd_value, denominator // gcd_value
