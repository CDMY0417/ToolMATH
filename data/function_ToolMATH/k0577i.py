def parabola_x_intercepts(a: float, b: float, c: float):
    discriminant = b**2 - 4*a*c
    p = (-b + discriminant**0.5) / (2*a)
    q = (-b - discriminant**0.5) / (2*a)
    return p, q
