def solve_quadratic_t(a: float, b: float, c: float):
    discriminant = b**2 - 4*a*c
    root1 = (-b + complex(0, discriminant**0.5)) / (2*a)
    root2 = (-b - complex(0, discriminant**0.5)) / (2*a)
    return (root1, root2)
