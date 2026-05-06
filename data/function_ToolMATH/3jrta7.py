def solve_quadratic_equation_a(a: int, b: int, c: int) -> list:
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return []
    elif discriminant == 0:
        x = -b / (2 * a)
        return [int(x)] if x.is_integer() else []
    else:
        x1 = (-b + discriminant**0.5) / (2 * a)
        x2 = (-b - discriminant**0.5) / (2 * a)
        solutions = []
        if x1.is_integer():
            solutions.append(int(x1))
        if x2.is_integer():
            solutions.append(int(x2))
        return solutions
