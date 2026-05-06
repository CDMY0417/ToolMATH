def simplify_fraction_bf(numerator: int, denominator: int):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    gcd_value = gcd(numerator, denominator)
    return (numerator // gcd_value, denominator // gcd_value)
