def subtract_equations_f(equation1: tuple[float, float], equation2: tuple[float, float]) -> tuple[float, float]:
    y_coeff1, constant1 = equation1
    y_coeff2, constant2 = equation2
    return (y_coeff1 - y_coeff2, constant1 - constant2)
