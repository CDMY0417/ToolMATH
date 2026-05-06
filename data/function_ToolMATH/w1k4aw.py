def solve_linear_inequality_c(c: int, a: int, b: int, d: int):
    lower_bound = (c - b) / a
    upper_bound = (d - b) / a
    return (lower_bound, upper_bound)
