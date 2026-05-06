def solve_linear_equation_bs(a: int, b: int):
    if a == 0:
        if b == 0:
            return None  # Indeterminate
        else:
            return []   # No solution
    return [-b / a]
