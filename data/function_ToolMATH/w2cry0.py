def multiply_fractions_u(frac1: tuple[int, int], frac2: tuple[int, int]) -> tuple[int, int]:
    numerator = frac1[0] * frac2[0]
    denominator = frac1[1] * frac2[1]
    return (numerator, denominator)
