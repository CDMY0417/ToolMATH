def calculate_probability_c(desired_outcome: int, total_outcomes: int):
    from fractions import Fraction
    return Fraction(desired_outcome, total_outcomes)
