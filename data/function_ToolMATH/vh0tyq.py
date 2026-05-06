def probability_as_fraction_a(success_outcomes: int, total_outcomes: int):
    from fractions import Fraction
    return Fraction(success_outcomes, total_outcomes)
