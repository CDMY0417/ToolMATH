def triangle_inequality_range_c(a: int, b: int) -> tuple:
    lower_bound = abs(a - b) + 1
    upper_bound = a + b - 1
    return lower_bound, upper_bound
