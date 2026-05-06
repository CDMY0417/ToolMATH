def cotangent_difference_a(x: float) -> float:
    from math import cos, sin
    return (cos(x) / sin(x)) - (cos(2 * x) / sin(2 * x))
