def monic_quadratic_from_surd_shift(d: float, shift: float):
    # If x = sqrt(d) - shift, then (x+shift)^2 = d
    return [1, 2*shift, shift*shift - d]
