def simplify_fraction_negation(numerator: int, denominator: int) -> float:
    if numerator == -denominator:
        return -1.0
    return numerator / denominator
