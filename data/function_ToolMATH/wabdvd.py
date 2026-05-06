def combine_equations(coeff1: int, equation1: tuple[int, int, int], coeff2: int, equation2: tuple[int, int, int]) -> tuple[int, int, int]:
    a1, b1, c1 = equation1
    a2, b2, c2 = equation2
    new_a = coeff1 * a1 + coeff2 * a2
    new_b = coeff1 * b1 + coeff2 * b2
    new_c = coeff1 * c1 + coeff2 * c2
    return (new_a, new_b, new_c)
