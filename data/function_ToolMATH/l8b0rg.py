def law_of_cosines_cos_angle(a: float, b: float, c: float) -> tuple:
    cos_C = (a**2 + b**2 - c**2) / (2 * a * b)
    cos_B = (a**2 + c**2 - b**2) / (2 * a * c)
    return cos_C, cos_B
