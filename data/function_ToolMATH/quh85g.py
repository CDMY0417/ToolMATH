def solve_linear_inequality_a(a: float, b: float) -> int:
    x = b / a
    return int(x) if x == int(x) else int(x) + 1
