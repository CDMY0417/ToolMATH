def sides_of_30_60_90_triangle(hypotenuse: float) -> tuple:
    shorter_side = hypotenuse / 2
    longer_leg = hypotenuse * (3 ** 0.5) / 2
    return shorter_side, longer_leg
