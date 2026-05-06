def distance_between_planes(a1: int, b1: int, c1: int, d1: int, d2: int) -> float:
    import math
    numerator = abs(d1 - d2)
    denominator = math.sqrt(a1 ** 2 + b1 ** 2 + c1 ** 2)
    return numerator / denominator
