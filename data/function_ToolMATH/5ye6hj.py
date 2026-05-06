def conjugate_pair_polynomial(root_real: float, root_imag: float, leading_coefficient: float):
    a = leading_coefficient
    b = -2 * root_real
    c = root_real**2 + root_imag**2
    return a, a * b, a * c
