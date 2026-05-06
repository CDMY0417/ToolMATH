def smallest_integer_modulo(start: int, remainder: int, modulus: int):
    k = (start - remainder + modulus - 1) // modulus
    return modulus * k + remainder
