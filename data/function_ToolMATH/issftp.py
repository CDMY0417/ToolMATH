def apply_exponent_law(base_exponents: dict[str, list[int]]) -> dict[str, int]:
    new_base_exponents = {}
    for base, exponents in base_exponents.items():
        new_base_exponents[base] = sum(exponents)
    return new_base_exponents
