def expand_quadratic_a(a: int, b: int, c: int, d: int):
    ac = a * c
    bd = b * d
    ad_bc = a * d + b * c
    return ac, ad_bc, bd
