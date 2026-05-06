def cosine_law_angle(a: float, b: float, c: float) -> float:
    cos_angle = (a**2 + b**2 - c**2) / (2 * a * b)
    return cos_angle
