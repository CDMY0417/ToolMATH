def thirty_sixty_ninety_triangle_sides(hypotenuse: float):
    shorter_side = hypotenuse / 2
    longer_side = shorter_side * (3 ** 0.5)
    return shorter_side, longer_side
