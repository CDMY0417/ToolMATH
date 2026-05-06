def parametric_point_on_line(t: float, x_coeff: float, y_coeff: float, x_offset: float, y_offset: float):
    x = x_offset + x_coeff * t
    y = y_offset + y_coeff * t
    return (x, y)
