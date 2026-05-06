def ellipse_parameters(a_squared: float, b_squared: float):
    a = max(a_squared, b_squared) ** 0.5
    b = min(a_squared, b_squared) ** 0.5
    c = (a_squared - b_squared) ** 0.5
    return a, b, c
