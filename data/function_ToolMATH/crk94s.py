from fractions import Fraction

def fraction_in_lowest_terms(number: float):
    fraction = Fraction(number).limit_denominator()
    return fraction
