def area_of_isosceles_right_triangle_c(hypotenuse: float) -> float:
    leg_length = hypotenuse / (2**0.5)
    return 0.5 * leg_length**2
