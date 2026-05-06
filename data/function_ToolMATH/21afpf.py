def percentage_to_fraction(percentage: int) -> tuple:
    from math import gcd
    numerator = percentage
    denominator = 100
    common_divisor = gcd(numerator, denominator)
    return (numerator // common_divisor, denominator // common_divisor)
