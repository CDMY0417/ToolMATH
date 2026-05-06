def max_absolute_product(a_range: tuple, b_range: tuple) -> float:
    return max(abs(a_range[0] * b_range[0]), abs(a_range[0] * b_range[1]), abs(a_range[1] * b_range[0]), abs(a_range[1] * b_range[1]))
