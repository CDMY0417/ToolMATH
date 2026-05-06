def compute_probability_b(successful_outcomes: int, total_outcomes: int) -> str:
    from fractions import Fraction
    return str(Fraction(successful_outcomes, total_outcomes))
