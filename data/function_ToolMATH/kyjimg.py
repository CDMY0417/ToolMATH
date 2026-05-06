def reduce_fraction_f(numerator: int, denominator: int):
    def gcd(a: int, b: int):
        while b:
            a, b = b, a % b
        return a
    divisor = gcd(numerator, denominator)
    return numerator // divisor, denominator // divisor
