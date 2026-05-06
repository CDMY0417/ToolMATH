def solve_linear_factors(r1: float, r2: float) -> list:
    roots = []
    if r1 != 0:
        roots.append(r1)
    if r2 != 0 and r2 != r1:
        roots.append(r2)
    return roots
