def isosceles_right_triangle_area(hypotenuse_length: float) -> float:
    leg_length = hypotenuse_length / 2 ** 0.5
    return 0.5 * leg_length * leg_length
