def ellipse_parameters_a(h: float, k: float, a_squared: float, b_squared: float):
    center = (h, k)
    semi_axes = (a_squared**0.5, b_squared**0.5)
    return center, semi_axes
