def quadratic_equation_solver(a: int, b: int, c: int):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return []  # No real solutions
    elif discriminant == 0:
        return [-b / (2*a)]  # One real solution
    else:
        sqrt_disc = discriminant**0.5
        x1 = (-b + sqrt_disc) / (2*a)
        x2 = (-b - sqrt_disc) / (2*a)
        return [x1, x2]
