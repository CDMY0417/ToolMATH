def cotangent_difference(x: float, y: float) -> float:
    from math import sin, cos
    return (cos(x) * sin(y) - sin(x) * cos(y)) / (sin(x) * sin(y))
