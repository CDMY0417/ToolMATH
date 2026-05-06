def subtract_scaled_equation(equation1: tuple, equation2: tuple, scale: int):
    (a1, a2, b) = equation1
    (c1, c2, d) = equation2
    scaled_a1, scaled_a2, scaled_b = scale * a1, scale * a2, scale * b
    result_c1 = c1 - scaled_a1
    result_c2 = c2 - scaled_a2
    result_d = d - scaled_b
    return (result_c1, result_c2, result_d)
