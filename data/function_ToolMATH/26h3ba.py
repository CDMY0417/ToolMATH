def reduce_fraction_b(numerator: int, denominator: int):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    common_factor = gcd(numerator, denominator)
    return numerator // common_factor, denominator // common_factor
