def calculate_ellipse_equation(x: float, y: float, a_denom: float, b_denom: float):
    term1 = x**2 / a_denom**2
    term2 = y**2 / b_denom**2
    return term1 + term2
