def calculate_arcsin_sin_value(x: float) -> float:
    import math
    if -math.pi / 2 <= x <= math.pi / 2:
        return x
    elif math.pi / 2 < x <= 3 * math.pi / 2:
        return math.pi - x
    else:
        return x - 2 * math.pi
