def scale_equation_a(coeff1: int, unit1: str, coeff2: int, unit2: str, scale_factor: int):
    scaled_coeff1 = coeff1 * scale_factor
    scaled_coeff2 = coeff2 * scale_factor
    return (scaled_coeff1, unit1, scaled_coeff2, unit2)
