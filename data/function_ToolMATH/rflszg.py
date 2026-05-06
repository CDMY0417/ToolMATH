def simplify_complex_expression(a: tuple[float, float], b: tuple[float, float]) -> tuple[float, float]:
    (a_re, a_im) = a
    (b_re, b_im) = b
    real_part = a_re * b_re - a_im * b_im
    imag_part = a_re * b_im + a_im * b_re
    return (real_part, imag_part)
