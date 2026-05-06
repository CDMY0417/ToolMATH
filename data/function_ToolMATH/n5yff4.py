def probability_lowest_terms(successful_outcomes: int, total_outcomes: int) -> tuple:
    from fractions import Fraction
    fraction = Fraction(successful_outcomes, total_outcomes)
    return (fraction.numerator, fraction.denominator)
