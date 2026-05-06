def solve_quadratic_for_zeros(a: int, b: int, c: int):
    discriminant = b**2 - 4*a*c
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    return sorted((root1, root2))
