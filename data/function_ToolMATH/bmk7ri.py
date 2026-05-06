def probability_of_event_h(favorable_outcomes: int, total_outcomes: int) -> str:
    from fractions import Fraction
    return str(Fraction(favorable_outcomes, total_outcomes))
