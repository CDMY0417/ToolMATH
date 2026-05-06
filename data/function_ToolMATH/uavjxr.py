def cosine_addition_formula(a: float, b: float) -> float:
    import math
    return math.cos(math.radians(a)) * math.cos(math.radians(b)) - math.sin(math.radians(a)) * math.sin(math.radians(b))
