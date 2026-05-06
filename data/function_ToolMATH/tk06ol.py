def probability_non_matching(non_matching_count: int, total_count: int):
    from fractions import Fraction
    return Fraction(non_matching_count, total_count)
