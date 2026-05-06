def multiply_same_base_exponents_a(base: int, exponents: list[int]) -> int:
    total_exponent = sum(exponents)
    return base ** total_exponent
