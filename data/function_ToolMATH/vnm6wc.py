def round_fraction(a: int, b: int, d: int):
    decimal_value = a / b
    rounded_numerator = round(decimal_value * d)
    return rounded_numerator / d
