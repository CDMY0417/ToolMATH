def subtract_angle(a: float, b: float) -> float:
    import math
    result = a - b
    while result < 0:
        result += 2 * math.pi
    while result >= 2 * math.pi:
        result -= 2 * math.pi
    return result
