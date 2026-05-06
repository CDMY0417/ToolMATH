def side_of_30_60_90_triangle_given_short_side(short_side_length: float) -> tuple:
    longer_side = short_side_length * (3**0.5)
    hypotenuse = 2 * short_side_length
    return longer_side, hypotenuse
