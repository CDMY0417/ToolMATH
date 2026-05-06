def multiply_powers_with_same_base(coeff1: int, coeff2: int, base: int, exponent1: int, exponent2: int) -> int:
    return coeff1 * coeff2 * (base ** (exponent1 + exponent2))
