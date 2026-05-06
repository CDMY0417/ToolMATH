def complete_the_square_aj(coeff_a: int, coeff_b: int, constant_c: int):
    vertex_x = -coeff_b / (2 * coeff_a)
    completed_square = coeff_a * (vertex_x ** 2) + coeff_b * vertex_x
    adjustment = completed_square - constant_c
    return (vertex_x, adjustment)
