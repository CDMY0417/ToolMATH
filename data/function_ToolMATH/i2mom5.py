def solve_linear_equation_gs(a: float, b: float):
    if a == 0:
        return None if b != 0 else 'Infinite solutions'
    return -b/a
