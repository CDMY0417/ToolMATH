def normalize_ellipse_equation(x2_coef: float, y2_coef: float, constant: float):
    a2 = x2_coef / constant
    b2 = y2_coef / constant
    return a2, b2
