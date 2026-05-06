def equation_to_hyperbola_standard_form(x_squared_term: float, y_squared_term: float, constant: float):
    a_squared = x_squared_term / constant
    b_squared = y_squared_term / constant
    return (a_squared, b_squared)
