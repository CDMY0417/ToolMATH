def factor_quadratic_b(a: int, b: int, c: int):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None  # No real roots, so no factorization into real binomials.
    
    sqrt_disc = discriminant**0.5
    root1 = (-b + sqrt_disc) / (2*a)
    root2 = (-b - sqrt_disc) / (2*a)
    if root1.is_integer() and root2.is_integer():
        return (int(root1), int(root2))
    return None
