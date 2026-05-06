def factor_quadratic_y(b: int, c: int):
    p = (b + (b**2 - 4*c)**0.5) / 2
    q = (b - (b**2 - 4*c)**0.5) / 2
    return int(p), int(q)
