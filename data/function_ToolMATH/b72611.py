def least_integer_multiple(factor: int, lower_bound: int) -> int:
    return ((lower_bound + factor - 1) // factor) * factor
