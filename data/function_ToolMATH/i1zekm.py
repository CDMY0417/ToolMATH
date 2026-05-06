def solve_quadratic_no_linear(a: int, c: int) -> list:
    discriminant = c / a
    if discriminant < 0:
        return []
    elif discriminant == 0:
        return [0]
    else:
        return [discriminant**0.5, -discriminant**0.5]
