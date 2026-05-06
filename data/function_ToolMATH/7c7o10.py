def rationalize_denominator(numerator: float, denominator: float, factor: float):
    new_numerator = numerator * factor
    new_denominator = denominator * factor
    return (new_numerator, new_denominator)
