def factor_and_solve_quadratic(a: float, b: float, c: float):
    if a == 0:
        return None
    else:
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            return []
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        return [x1, x2]
