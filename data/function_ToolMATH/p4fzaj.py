def solve_for_height_in_cone(volume: float, radius: float) -> float:
    import math
    return volume / ((1/3) * math.pi * (radius ** 2))
