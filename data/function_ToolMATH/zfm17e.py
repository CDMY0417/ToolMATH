def quadratic_inequality_solution_a(a: int, b: int, c: int, d: int):
    roots = sorted([(-b/a), (-d/c)])
    if a*c < 0:
        return (float('-inf'), roots[0]), (roots[1], float('inf'))
    else:
        return (roots[0], roots[1])
