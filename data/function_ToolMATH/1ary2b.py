def calculate_probability(numerator: int, denominator: int) -> str:
    from math import gcd
    gcd_value = gcd(numerator, denominator)
    return f"{numerator // gcd_value}/{denominator // gcd_value}"
