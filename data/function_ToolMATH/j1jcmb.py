def solve_quadratic_equation_at(a: int, b: int, c: int):
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        real_part = -b / (2 * a)
        imaginary_part = (-discriminant)**0.5 / (2 * a)
        return [complex(real_part, imaginary_part), complex(real_part, -imaginary_part)]
    elif discriminant == 0:
        return [-b / (2 * a)]
    else:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        return [root1, root2]
