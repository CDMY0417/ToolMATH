def solve_linear_equation_a(a: int, b: int, c: int) -> float:
    if a == b:
        if c == 0:
            return 'Infinite solutions'
        else:
            return 'No solution'
    return c / (a - b)
