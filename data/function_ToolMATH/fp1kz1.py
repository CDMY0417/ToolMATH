def solve_quadratic_ba(a: int, b: int, c: int):
    from math import sqrt
    disc = b**2 - 4 * a * c
    if disc < 0:
        return []
    elif disc == 0:
        return [-b / (2 * a)]
    else:
        return [(-b + sqrt(disc)) / (2 * a), (-b - sqrt(disc)) / (2 * a)]
