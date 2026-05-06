def partial_fractions_coefficients(a: float, r: float, s: float):
    A_plus_B = 0
    As_Plus_Br = -1/a
    A = (As_Plus_Br + A_plus_B * s) / (r - s)
    B = A_plus_B - A
    return A, B
