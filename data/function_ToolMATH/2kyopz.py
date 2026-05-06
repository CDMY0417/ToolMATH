def calculate_triangle_sides(hypotenuse: float, sine_angle: float):
    vertical_side = sine_angle * hypotenuse
    horizontal_side = (1 - sine_angle**2)**0.5 * hypotenuse
    return vertical_side, horizontal_side
