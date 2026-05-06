def solve_linear_equation_dq(a: int, b: int, c: int, d: int) -> float | str | None:
    if a == c:
        if b == d:
            return None  # Infinite solutions
        else:
            return 'No solution'
    else:
        return (d - b) / (a - c)
