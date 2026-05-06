def transform_hyperbola(x_squared_coeff: float, y_squared_coeff: float, constant: float):
    a_squared = x_squared_coeff / constant
    b_squared = y_squared_coeff / constant
    return a_squared, b_squared
