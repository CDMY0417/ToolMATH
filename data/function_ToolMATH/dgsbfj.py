def solve_quadratic_aq(a: int, b: int, c: int):
    discriminant = b ** 2 - 4 * a * c
    sqrt_disc = discriminant ** 0.5
    root1 = (-b + sqrt_disc) / (2 * a)
    root2 = (-b - sqrt_disc) / (2 * a)
    return root1, root2
