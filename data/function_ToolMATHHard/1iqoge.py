def solve_matrix_inverse_params_2x2(m12: float, m21: float, m22: float, n11: float, n12: float, n22: float):
    # Solve a and b so that [[a,m12],[m21,m22]] and [[n11,n12],[b,n22]] are inverses
    b = -(m21*n11) / m22
    a = (1 - m12*b) / n11
    return [a, b]
