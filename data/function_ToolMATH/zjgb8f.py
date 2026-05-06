def simplify_fraction_ar(numerator: int, denominator: int):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    greatest_common_divisor = gcd(numerator, denominator)
    return (numerator // greatest_common_divisor, denominator // greatest_common_divisor)
