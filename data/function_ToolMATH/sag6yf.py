def side_length_30_60_90_triangle_a(longer_leg: float):
    shorter_leg = longer_leg / (3**0.5)
    hypotenuse = 2 * shorter_leg
    return shorter_leg, hypotenuse
