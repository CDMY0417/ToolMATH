def simplify_fraction_ak(numerator: int, denominator: int) -> tuple:
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    gcd_value = gcd(numerator, denominator)
    return (numerator // gcd_value, denominator // gcd_value)
