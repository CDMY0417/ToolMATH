def solve_linear_equation_ew(a: int, b: int, c: int, d: int) -> float:
    return (d - b) / (a - c) if a != c else None
