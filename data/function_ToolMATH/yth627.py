def smallest_integer_greater_than_fraction(numerator: int, denominator: int) -> int:
    from math import ceil
    return ceil(numerator / denominator)
