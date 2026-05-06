def compute_30_60_90_triangle_sides(hypotenuse: float):
    short_leg = hypotenuse / 2
    long_leg = hypotenuse / 2 * (3 ** 0.5)
    return short_leg, long_leg
