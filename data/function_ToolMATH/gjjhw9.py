def sine_from_tangent(tan_angle: float) -> float:
    hypotenuse = (1 + tan_angle**2)**0.5
    return tan_angle / hypotenuse
