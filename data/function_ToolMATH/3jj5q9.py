def thirty_sixty_ninety_triangle_properties(short_side_length: float):
    long_side_length = short_side_length * (3 ** 0.5)
    hypotenuse_length = 2 * short_side_length
    return {'short_side_length': short_side_length, 'long_side_length': long_side_length, 'hypotenuse_length': hypotenuse_length}
