def decimal_to_fraction_a(decimal_number: float, denominator: int):
    numerator = round(decimal_number * denominator)
    return numerator, denominator
