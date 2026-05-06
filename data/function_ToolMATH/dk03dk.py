def factor_out_coefficient(coeff: int, b: int, c: int):
    new_b = b / coeff
    new_c = c / coeff
    return new_b, new_c
