def right_triangle_sides_given_hypotenuse(hypotenuse: float, side_ratio: tuple):
    factor = hypotenuse / side_ratio[2]
    return (side_ratio[0] * factor, side_ratio[1] * factor, hypotenuse)
