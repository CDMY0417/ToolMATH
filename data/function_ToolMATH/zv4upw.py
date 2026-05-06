def combine_fractions_c(a: int, b: int, c: int, d: int):
    numerator = a * d + b * c
    denominator = b * d
    return numerator, denominator
