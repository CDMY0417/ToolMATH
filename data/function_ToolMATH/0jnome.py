def expand_binomial(a: int, b: int, c: int, d: int):
    a1 = a * c
    b1 = a * d + b * c
    c1 = b * d
    return a1, b1, c1
