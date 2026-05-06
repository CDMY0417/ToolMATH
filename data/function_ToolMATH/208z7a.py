def horizontal_asymptote_of_rational_function(numerator_degree: int, denominator_degree: int) -> float:
    if numerator_degree < denominator_degree:
        return 0.0
    elif numerator_degree == denominator_degree:
        return 1.0
    else:
        return None
