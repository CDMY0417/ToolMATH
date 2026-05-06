def subtract_scaled_equation_a(equation1: tuple, equation2: tuple, scale: int):
    a1, b1, c1 = equation1
    a2, b2, c2 = equation2
    return (a1 - scale * a2, b1 - scale * b2, c1 - scale * c2)
