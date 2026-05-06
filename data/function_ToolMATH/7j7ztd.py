def solve_quadratic_ar(a: float, b: float, c: float):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return []  # no real roots
    elif discriminant == 0:
        return [-b / (2*a)]  # one real root
    else:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return [root1, root2]
