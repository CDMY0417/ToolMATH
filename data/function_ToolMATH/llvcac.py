def sophie_germain_identity(a: int, b: int):
    term1 = a**2 + 2*(b**2) + 2*a*b
    term2 = a**2 + 2*(b**2) - 2*a*b
    return term1, term2
