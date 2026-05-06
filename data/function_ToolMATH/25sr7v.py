from cmath import sqrt

def solve_quadratic_d(a: int, b: int, c: int):
    discriminant = b**2 - 4*a*c
    root1 = (-b + sqrt(discriminant)) / (2*a)
    root2 = (-b - sqrt(discriminant)) / (2*a)
    return root1, root2
