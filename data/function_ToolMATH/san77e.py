def fraction_to_common_fraction(floating_number: float):
    from fractions import Fraction
    common_fraction = Fraction(floating_number).limit_denominator()
    return (common_fraction.numerator, common_fraction.denominator)
