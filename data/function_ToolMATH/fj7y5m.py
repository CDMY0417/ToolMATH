def hyperbola_standard_form(x_coeff: float, y_coeff: float, rhs: float) -> str:
    a2 = rhs / x_coeff
    b2 = -rhs / y_coeff
    return f'x^2/{a2} - y^2/{b2} = 1'
