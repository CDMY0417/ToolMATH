def solve_linear_equation_az(a: int, b: int) -> float:
    if a == 0:
        return None if b != 0 else 'Infinite solutions'
    return -b / a
