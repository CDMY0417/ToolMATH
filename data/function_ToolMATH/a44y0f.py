def solve_linear_equation_an(a: int, b: int):
    if a == 0:
        return None if b != 0 else 'Infinite solutions'
    return -b / a
