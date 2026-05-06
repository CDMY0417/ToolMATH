def probability_of_event_d(successful_outcomes: int, total_outcomes: int):
    from fractions import Fraction
    return Fraction(successful_outcomes, total_outcomes)
