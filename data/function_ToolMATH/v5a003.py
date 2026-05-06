def calculate_probability_s(successful_outcomes: int, total_outcomes: int):
    from fractions import Fraction
    return Fraction(successful_outcomes, total_outcomes)
