def multiply_and_adjust_fraction(numerator: int, denominator_five_power: int, extra_two_power: int):
    adjusted_numerator = numerator * (2 ** extra_two_power)
    adjusted_denominator = 10 ** denominator_five_power
    return adjusted_numerator, adjusted_denominator
