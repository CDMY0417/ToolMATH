def modular_equivalence_e(value: int, modulus: int, lower_bound: int, upper_bound: int) -> int:
    equivalent_value = value % modulus
    if equivalent_value < lower_bound:
        equivalent_value += modulus
    elif equivalent_value > upper_bound:
        equivalent_value -= modulus
    return equivalent_value
