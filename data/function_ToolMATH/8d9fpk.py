def cubic_sine_expression(x: float, y: float, z: float) -> float:
    from math import sin
    return sin(x) * (sin(y)**2 - sin(z)**2)
