def translate_parabola_a(a: float, h: float, k: float, x_shift: float, y_shift: float):
    h_new = h + x_shift
    k_new = k + y_shift
    return a, h_new, k_new
