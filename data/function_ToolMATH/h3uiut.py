def solve_linear_equation_gq(a: float, b: float, c: float) -> float:
    return (c - b) / a if a != 0 else float('inf')
