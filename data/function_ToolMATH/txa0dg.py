def sin_and_csc_squared(angle: float) -> float:
    from math import sin
    return (sin(angle) + 1/sin(angle))**2
