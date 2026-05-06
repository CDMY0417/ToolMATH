def difference_of_linear_function(f_x1_x2: float, x1: float, x2: float, a: float, b: float) -> float:
    slope = f_x1_x2 / (x1 - x2)
    return slope * (b - a)
