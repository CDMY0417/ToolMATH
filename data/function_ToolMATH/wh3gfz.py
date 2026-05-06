def power_with_fractional_exponent(base: float, numerator: float, denominator: float) -> float:
    radical_part = base ** (1/denominator)
    return radical_part ** numerator
