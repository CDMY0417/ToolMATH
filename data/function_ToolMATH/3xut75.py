def solve_quadratic_completed_square(h: float, k: float) -> tuple:
    import math
    root = math.sqrt(abs(k))
    solutions = (h + root, h - root) if k >= 0 else ()
    return solutions
