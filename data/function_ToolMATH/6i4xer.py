def tan_addition_formula(tan_a: float, tan_b: float, tan_c: float) -> float:
    return (tan_a + tan_b + tan_c - tan_a * tan_b * tan_c) / (1 - (tan_a * tan_b + tan_a * tan_c + tan_b * tan_c))
