def factor_quadratic_n(a: int, b: int, c: int):
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return (f'(x-{root1})', f'(x-{root2})')
    return None
