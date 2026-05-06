def modular_exponentiation_c(base: int, exponent: int, modulus: int) -> int:
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result
