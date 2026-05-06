def multiply_fractions(frac1: tuple[int, int], frac2: tuple[int, int]) -> tuple[int, int]:
    num = frac1[0] * frac2[0]
    denom = frac1[1] * frac2[1]
    return num, denom
