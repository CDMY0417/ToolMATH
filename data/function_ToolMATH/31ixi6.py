def smallest_exponent_mod(base: int, target: int, modulus: int) -> int:
    exponent = 1
    while pow(base, exponent, modulus) != target:
        exponent += 1
    return exponent
